const axios = require('axios')

axios.get('http://jso123123nplaceholder.typicode.com/posts')
  .then(response => {
    console.log(response)
  })
  .catch(err => {
    console.log(err)
  })