const MqttConnection = require('flespi-io-js')
let connector = new MqttConnection({
    token: 'FlespiToken HbNyj8NP9ZhQOskjA3uu0dr3PTF7jayOc9cl5PY4D6JhmRoMIH7yKmqn4VjdVHPV',
    server: `ws://server.io`,
    mqttSettings: {
      reschedulePings: true,
      keepalive: 3600,
      resubscribe: false,
      reconnectPeriod: 5000,
      connectTimeout: 3600000
    }
  })

let token = connector.token
connector.token = 'FlespiToken HbNyj8NP9ZhQOskjA3uu0dr3PTF7jayOc9cl5PY4D6JhmRoMIH7yKmqn4VjdVHPV'

let socketConfig = connector.config
connector.config = {
  server: `ws://server.io`,
  mqttSettings: {
    reschedulePings: true,
    keepalive: 3600,
    resubscribe: false,
    reconnectPeriod: 5000,
    connectTimeout: 3600000
  }
}

/* region structure */
region = {
  "cdn": "https://ru-cdn.flespi.io",
  "default": false,
  "gw": "ru-gw.flespi.io",
  "mqtt": "ru-mqtt.flespi.io:8883",
  "mqtt-ws": "ru-mqtt.flespi.io:443",
  "region": "ru",
  "rest": "https://ru.flespi.io"
}
connector.setRegion(region)

connector.http.mqtt.logs.get(query)
// or
connector.mqtt.getLogs(query)