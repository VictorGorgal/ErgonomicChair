#include <ESP8266WiFi.h>
#include <PubSubClient.h>

#define WIFI_SSID "Victor"
#define WIFI_PASSWORD  "morenamorenas"

#define MQTT_BROKER "192.168.10.8"
#define MQTT_PORT 1883
#define MQTT_PUB_TOPIC "chairs/1"
#define MQTT_USER "victor"
#define MQTT_PASSWD "morenamorenas"
#define MQTT_CLIENT_ID "node_test_1"

long delta;

WiFiClient espClient;
PubSubClient client(espClient);

void connectWifi() {
  Serial.print("Connecting to: ");
  Serial.println(WIFI_SSID);

  WiFi.mode(WIFI_STA);
  WiFi.begin(WIFI_SSID, WIFI_PASSWORD);

  while (WiFi.status() != WL_CONNECTED) {
    delay(250);
    Serial.print(".");
  }

  Serial.println();
  Serial.println("------ WI-FI ------");
  Serial.println(WIFI_SSID);
  Serial.print("IP obtido: ");
  Serial.println(WiFi.localIP());
}

void setMqtt() {
  client.setServer(MQTT_BROKER, MQTT_PORT);
}

void connectMqtt () {
  Serial.println("------ MQTT Broker ------");
  
  while (!client.connected()) {
    if (client.connect(MQTT_CLIENT_ID, MQTT_USER, MQTT_PASSWD)) {
      Serial.println("Connected");
    } else {
      Serial.print("Failed: ");
      Serial.println(client.state());
    }
  }
  Serial.println("-------------------------");
}

void publish_MQTT(String message){
  client.publish(MQTT_PUB_TOPIC, message.c_str());
}

void setup() {
  Serial.begin(115200);
  
  delta = millis();
  
  connectWifi();
  
  setMqtt();
  connectMqtt();
}

void loop() {
  client.loop();

  if (!client.connected()) {
    connectMqtt();
  }

  if (millis() - delta > 5000) {
    Serial.println("Sending...");
    publish_MQTT("1;1;1;1;0;0;0;0");

    delta = millis();
  }
}
