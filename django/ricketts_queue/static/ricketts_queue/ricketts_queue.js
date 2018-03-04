var app = new Vue({
  el: '#app',
  data: {
    message: 'Hello Vue!',
    queryString: '',
    queryResults: [{
      id: '_-6cSUHJ9IU',
      timeString: '00:03:41',
      snippet: {
        publishedAt: '2016-03-21T23:19:40.000Z',
        channelId: 'UCq7VAQmXDurV-9VN2bSFXvw',
        title: 'Hellifornia',
        description: 'Provided to YouTube by Warner Music Group Hellifornia · Gesaffelstein Aleph ℗ 2013 Parlophone / Warner Music France, a Warner Music Group Company All Instruments, Producer: Mike Levy...',
        thumbnails: {
          default: {
            url: 'https://i.ytimg.com/vi/_-6cSUHJ9IU/default.jpg',
            width: 120,
            height: 90
          },
          medium: {
            url: 'https://i.ytimg.com/vi/_-6cSUHJ9IU/mqdefault.jpg',
            width: 320,
            height: 180
          },
          high: {
            url: 'https://i.ytimg.com/vi/_-6cSUHJ9IU/hqdefault.jpg',
            width: 480,
            height: 360
          }
        },
        channelTitle: 'Gesaffelstein - Topic',
        liveBroadcastContent: 'none'
      },
      contentDetails: {
        duration: 'PT3M41S',
        dimension: '2d',
        definition: 'hd',
        caption: 'false',
        licensedContent: true,
        regionRestriction: {
          allowed: ['CA', 'US']
        },
        projection: 'rectangular'
      }
    }],
  },

  methods: {
    submitSearch() {
      // send a search request to the server
      this.$http.get('http://127.0.0.1:8000/search/', {
        params: { q: this.queryString }
      }).then(response => {  // if successful
        this.queryResults = response.body.items;  // save the results
        this.queryString = '';  // reset the input to blank
      }, response => {  // if unsuccessful
      });
    },
  }
})
