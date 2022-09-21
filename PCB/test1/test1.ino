//#include <ESP8266WiFi.h>
//#include <PubSubClient.h>

#define WIFI_SSID "Victor"
#define WIFI_PASSWORD  "morenamorenas"

#define MQTT_BROKER "192.168.10.8"
#define MQTT_PORT 1883
#define MQTT_PUB_TOPIC "chairs/1"
#define MQTT_USER "victor"
#define MQTT_PASSWD "morenamorenas"
#define MQTT_CLIENT_ID "node_test_1"

#define ANALOG_IN A0  // Analog input
#define VIBRACAL 10
#define CALIBRATION D9
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

// Raw sensor reading
uint16_t control;
uint16_t seat1;
uint16_t seat2;
uint16_t seat3;
uint16_t seat4;
uint16_t coaster1;
uint16_t coaster2;
uint16_t coaster3;
uint16_t coaster4;

// Sensor calibrations
uint16_t control_calibration;
uint16_t seat1_calibration;
uint16_t seat2_calibration;
uint16_t seat3_calibration;
uint16_t seat4_calibration;
uint16_t coaster1_calibration;
uint16_t coaster2_calibration;
uint16_t coaster3_calibration;
uint16_t coaster4_calibration;

// Sensors On-Off state
bool control_active;
bool seat1_active;
bool seat2_active;
bool seat3_active;
bool seat4_active;
bool coaster1_active;
bool coaster2_active;
bool coaster3_active;
bool coaster4_active;

uint16_t THRESHOLD = 18;
uint8_t DELAY = 2;

long serverTimer;
long motorTimer;
long serialTimer;

bool motorCounting;

/*
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
*/

/**
 * Checks if the motor should turn on
 */
void vibrate_motor() {
  if (!(todos() || nenhum())) {
    if (millis() - motorTimer > 6000) {
      digitalWrite(VIBRACAL, HIGH);
    }
  } else {
    motorTimer = millis();
    digitalWrite(VIBRACAL, LOW);
  }
}

String getPayload() {
  String payload;

  payload += boolToChar(seat1_active);
  payload += ";";
  payload += boolToChar(seat2_active);
  payload += ";";
  payload += boolToChar(seat3_active);
  payload += ";";
  payload += boolToChar(seat4_active);
  payload += ";";
  payload += boolToChar(coaster1_active);
  payload += ";";
  payload += boolToChar(coaster2_active);
  payload += ";";
  payload += boolToChar(coaster3_active);
  payload += ";";
  payload += boolToChar(coaster4_active);

  return payload;
}

/**
 * Gets raw sensor data with the calibration and checks which ones are being activated
 */
void checkSensors() {
  control_active = readingToBool(control, control_calibration);
  seat1_active = true;
  seat2_active = readingToBool(seat2, seat2_calibration);
  seat3_active = readingToBool(seat3, seat3_calibration);
  seat4_active = readingToBool(seat4, seat4_calibration);
  coaster1_active = readingToBool(coaster1, coaster1_calibration);
  coaster2_active = readingToBool(coaster2, coaster2_calibration);
  coaster3_active = readingToBool(coaster3, coaster3_calibration);
  coaster4_active = readingToBool(coaster4, coaster4_calibration);
}

/**
 * Transforms a sensor reading into a on-off output based on the calibration
 */
bool readingToBool(uint16_t reading, uint16_t sensor_calibration) {
  int difference = reading - sensor_calibration;

  if (difference > THRESHOLD || (difference * -1) > THRESHOLD) {
    return true;
  }

  return false;
}

void readSensors() {
  digitalWrite(COASTER4, LOW);
  digitalWrite(CONTROL, HIGH);
  delay(DELAY);

  control = analogRead(ANALOG_IN);

  digitalWrite(CONTROL, LOW);
  digitalWrite(SEAT1, HIGH);
  delay(DELAY);

  seat1 = analogRead(ANALOG_IN);

  digitalWrite(SEAT1, LOW);
  digitalWrite(SEAT2, HIGH);
  delay(DELAY);

  seat2 = analogRead(ANALOG_IN);

  digitalWrite(SEAT2, LOW);
  digitalWrite(SEAT3, HIGH);
  delay(DELAY);

  seat3 = analogRead(ANALOG_IN);

  digitalWrite(SEAT3, LOW);
  digitalWrite(SEAT4, HIGH);
  delay(DELAY);

  seat4 = analogRead(ANALOG_IN);

  digitalWrite(SEAT4, LOW);
  digitalWrite(COASTER1, HIGH);
  delay(DELAY);

  coaster1 = analogRead(ANALOG_IN);

  digitalWrite(COASTER1, LOW);
  digitalWrite(COASTER2, HIGH);
  delay(DELAY);

  coaster2 = analogRead(ANALOG_IN);

  digitalWrite(COASTER2, LOW);
  digitalWrite(COASTER3, HIGH);
  delay(DELAY);

  coaster3 = analogRead(ANALOG_IN);

  digitalWrite(COASTER3, LOW);
  digitalWrite(COASTER4, HIGH);
  delay(DELAY);

  coaster4 = analogRead(ANALOG_IN);
}

void calibrate() {
  control_calibration = control;
  seat1_calibration = seat1;
  seat2_calibration = seat2;
  seat3_calibration = seat3;
  seat4_calibration = seat4;
  coaster1_calibration = coaster1;
  coaster2_calibration = coaster2;
  coaster3_calibration = coaster3;
  coaster4_calibration = coaster4;
}

bool todos() {
  return seat2_active && seat3_active && seat4_active
   && coaster1_active && coaster2_active && coaster3_active && coaster4_active;
}

bool nenhum() {
  return !(seat2_active || seat3_active || seat4_active
   || coaster1_active || coaster2_active || coaster3_active || coaster4_active);
}

char boolToChar(bool b) {
  if (b) {
    return '1';
  } else {
    return '0';
  }
}

void setup() {
  Serial.begin(115200);

  pinMode(ANALOG_IN, INPUT);
  pinMode(CALIBRATION, INPUT_PULLUP);
  pinMode(VIBRACAL, OUTPUT);
  pinMode(CONTROL, OUTPUT);
  pinMode(SEAT1, OUTPUT);
  pinMode(SEAT2, OUTPUT);
  pinMode(SEAT3, OUTPUT);
  pinMode(SEAT4, OUTPUT);
  pinMode(COASTER1, OUTPUT);
  pinMode(COASTER2, OUTPUT);
  pinMode(COASTER3, OUTPUT);
  pinMode(COASTER4, OUTPUT);

  digitalWrite(VIBRACAL, LOW);
  digitalWrite(CONTROL, LOW);
  digitalWrite(SEAT1, LOW);
  digitalWrite(SEAT2, LOW);
  digitalWrite(SEAT3, LOW);
  digitalWrite(SEAT4, LOW);
  digitalWrite(COASTER1, LOW);
  digitalWrite(COASTER2, LOW);
  digitalWrite(COASTER3, LOW);
  digitalWrite(COASTER4, LOW);
}

void loop() {
  if (millis() - serialTimer > 500) {
    readSensors();
    checkSensors();

    if (digitalRead(CALIBRATION) == LOW) {
      calibrate();
    }

    vibrate_motor();

    Serial.println(getPayload() += "   ");

    serialTimer = millis();
  }
}
