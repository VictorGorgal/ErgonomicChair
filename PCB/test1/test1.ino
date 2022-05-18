void setup() {
  Serial.begin(115200);

  pinMode(D8, OUTPUT);
  pinMode(A0, INPUT);

  digitalWrite(D8, HIGH);
}

void loop() {
  Serial.println(analogRead(A0));
}
