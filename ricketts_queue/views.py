from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.contrib.auth import models

from isodate import parse_duration, strftime
import requests


from .settings import YOUTUBE_DATA_API_KEY

def index(request):
    context = {
        'users': models.User.objects.all(),
    }
    return render(request, 'ricketts_queue/index.html', context=context)

    # return HttpResponse("Hello, world. You're at the Ricketts Queue index.")

def search(request):
    # get the query string from the GET parameters
    q = request.GET.get('q', None)

    # if there is no query string, return empty result
    if q is None:
        return JsonResponse({})

    # search for the query string on youtube
    # docs: https://developers.google.com/youtube/v3/docs/search/list
    search_page = requests.get('https://www.googleapis.com/youtube/v3/search', params={
        'part': 'snippet',  # resource type being requested [required]
        'key': YOUTUBE_DATA_API_KEY,  # authenticate with api key
        'q': q,  # query term to search for
        'safeSearch': 'none',  # don't filter search results
        'type': 'video',  # resource types, e.g. 'video,playlist,channel'
    })

    # get the list of video ids of the search results
    videoIds = []
    for item in search_page.json()['items']:
        videoIds.append(item['id']['videoId'])

    # get details about each of the search results
    details_page = requests.get('https://www.googleapis.com/youtube/v3/videos', params={
        'part': 'contentDetails',  # resource type being requested [required]
        'key': YOUTUBE_DATA_API_KEY,  # authenticate with api key
        'id': ','.join(map(str, videoIds)),  # search result ids as comma separated list
    })

    # combine search items, detail items, computed time strings into one list
    items = []
    for search_item, detail_item in zip(search_page.json()['items'], details_page.json()['items']) :
        iso_duration = detail_item['contentDetails']['duration']
        time_delta = parse_duration(iso_duration)
        time_string = strftime(time_delta, '%H:%M:%S')
        items.append({
            'id': search_item['id']['videoId'],
            'timeString': time_string,
            'snippet': search_item['snippet'],
            'contentDetails': detail_item['contentDetails'],
        })

    # return combined search results as JSON
    return JsonResponse({
        'items': items,
    })
