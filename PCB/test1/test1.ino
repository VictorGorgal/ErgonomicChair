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

#define ANALOG_IN A0  // Analog input
// Sensors
#define CONTROL D8
#define SEAT1 D7
#define SEAT2 D6
#define SEAT3 D5
#define SEAT4 D0
#define COASTER1 D4
#define COASTER2 D3
#define COASTER3 D2
#define COASTER4 D1

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

  pinMode(ANALOG_IN, INPUT);
  pinMode(CONTROL, OUTPUT);
  pinMode(SEAT1, OUTPUT);
  pinMode(SEAT2, OUTPUT);
  pinMode(SEAT3, OUTPUT);
  pinMode(SEAT4, OUTPUT);
  pinMode(COASTER1, OUTPUT);
  pinMode(COASTER2, OUTPUT);
  pinMode(COASTER3, OUTPUT);
  pinMode(COASTER4, OUTPUT);
  
//  connectWifi();
  
//  setMqtt();
//  connectMqtt();
}

void loop() {
//  client.loop();

//  if (!client.connected()) {
//    connectMqtt();
//  }

//  if (millis() - delta > 60000) {
//    Serial.println("Sending...");
    
    // Don't send if all sensors are 0
//    publish_MQTT("1;1;1;1;1;1;1;1");

  digitalWrite(CONTROL, HIGH);
  digitalWrite(SEAT1, LOW);
  digitalWrite(SEAT2, LOW);
  digitalWrite(SEAT3, LOW);
  digitalWrite(SEAT4, LOW);
  digitalWrite(COASTER1, LOW);
  digitalWrite(COASTER2, LOW);
  digitalWrite(COASTER3, LOW);
  digitalWrite(COASTER4, LOW);
  delay(5);

  Serial.print(analogRead(ANALOG_IN));

  digitalWrite(CONTROL, LOW);
  digitalWrite(SEAT1, HIGH);
  digitalWrite(SEAT2, LOW);
  digitalWrite(SEAT3, LOW);
  digitalWrite(SEAT4, LOW);
  digitalWrite(COASTER1, LOW);
  digitalWrite(COASTER2, LOW);
  digitalWrite(COASTER3, LOW);
  digitalWrite(COASTER4, LOW);
  delay(5);

  Serial.print(", ");
  Serial.print(analogRead(ANALOG_IN));

  digitalWrite(CONTROL, LOW);
  digitalWrite(SEAT1, LOW);
  digitalWrite(SEAT2, HIGH);
  digitalWrite(SEAT3, LOW);
  digitalWrite(SEAT4, LOW);
  digitalWrite(COASTER1, LOW);
  digitalWrite(COASTER2, LOW);
  digitalWrite(COASTER3, LOW);
  digitalWrite(COASTER4, LOW);
  delay(5);

  Serial.print(", ");
  Serial.print(analogRead(ANALOG_IN));

  digitalWrite(CONTROL, LOW);
  digitalWrite(SEAT1, LOW);
  digitalWrite(SEAT2, LOW);
  digitalWrite(SEAT3, HIGH);
  digitalWrite(SEAT4, LOW);
  digitalWrite(COASTER1, LOW);
  digitalWrite(COASTER2, LOW);
  digitalWrite(COASTER3, LOW);
  digitalWrite(COASTER4, LOW);
  delay(5);

  Serial.print(", ");
  Serial.print(analogRead(ANALOG_IN));

  digitalWrite(CONTROL, LOW);
  digitalWrite(SEAT1, LOW);
  digitalWrite(SEAT2, LOW);
  digitalWrite(SEAT3, LOW);
  digitalWrite(SEAT4, HIGH);
  digitalWrite(COASTER1, LOW);
  digitalWrite(COASTER2, LOW);
  digitalWrite(COASTER3, LOW);
  digitalWrite(COASTER4, LOW);
  delay(5);

  Serial.print(", ");
  Serial.print(analogRead(ANALOG_IN));

  digitalWrite(CONTROL, LOW);
  digitalWrite(SEAT1, LOW);
  digitalWrite(SEAT2, LOW);
  digitalWrite(SEAT3, LOW);
  digitalWrite(SEAT4, LOW);
  digitalWrite(COASTER1, HIGH);
  digitalWrite(COASTER2, LOW);
  digitalWrite(COASTER3, LOW);
  digitalWrite(COASTER4, LOW);
  delay(5);

  Serial.print(", ");
  Serial.print(analogRead(ANALOG_IN));

  digitalWrite(CONTROL, LOW);
  digitalWrite(SEAT1, LOW);
  digitalWrite(SEAT2, LOW);
  digitalWrite(SEAT3, LOW);
  digitalWrite(SEAT4, LOW);
  digitalWrite(COASTER1, LOW);
  digitalWrite(COASTER2, HIGH);
  digitalWrite(COASTER3, LOW);
  digitalWrite(COASTER4, LOW);
  delay(5);

  Serial.print(", ");
  Serial.print(analogRead(ANALOG_IN));

  digitalWrite(CONTROL, LOW);
  digitalWrite(SEAT1, LOW);
  digitalWrite(SEAT2, LOW);
  digitalWrite(SEAT3, LOW);
  digitalWrite(SEAT4, LOW);
  digitalWrite(COASTER1, LOW);
  digitalWrite(COASTER2, LOW);
  digitalWrite(COASTER3, HIGH);
  digitalWrite(COASTER4, LOW);
  delay(5);

  Serial.print(", ");
  Serial.print(analogRead(ANALOG_IN));

  digitalWrite(CONTROL, LOW);
  digitalWrite(SEAT1, LOW);
  digitalWrite(SEAT2, LOW);
  digitalWrite(SEAT3, LOW);
  digitalWrite(SEAT4, LOW);
  digitalWrite(COASTER1, LOW);
  digitalWrite(COASTER2, LOW);
  digitalWrite(COASTER3, LOW);
  digitalWrite(COASTER4, HIGH);
  delay(5);

  Serial.print(", ");
  Serial.println(analogRead(ANALOG_IN));

//    delta = millis();
//  }
}
