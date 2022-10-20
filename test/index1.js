const mqtt = require('mqtt')
let token = "FlespiToken HbNyj8NP9ZhQOskjA3uu0dr3PTF7jayOc9cl5PY4D6JhmRoMIH7yKmqn4VjdVHPV", // flespi.io access token
clientId = "1601533", // client id
_client = mqtt.connect("wss://mqtt.flespi.io", { // creating client
   username: token,
   clientId: clientId
})
 
_client.on('message', (topic, message) => { // processing messages as they appear
    console.log(JSON.parse(message.toString('utf-8')))
})

_client.subscribe("#") // subscribing
//    .then(cred => {
//       let { err, granted } = cred
//       if (err) {
//          console.log(err)
//          return false
//       }
// })