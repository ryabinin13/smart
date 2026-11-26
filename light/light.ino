const int LED = 2;
const int SENSE_PIN = A0;

void setup() {
  Serial.begin(9600);
  pinMode(LED, OUTPUT);
  pinMode(SENSE_PIN, INPUT);
}

void loop() {
  if (Serial.available()) {
    byte a = Serial.read();
    if (a == 49) digitalWrite(LED, HIGH);
    else         digitalWrite(LED, LOW);
    while (Serial.available()) Serial.read();
  }

  int cmd = digitalRead(LED);
  int raw = analogRead(SENSE_PIN);

  Serial.print("LED=");
  Serial.print(cmd);
  Serial.print(" RAW=");
  Serial.print(raw);
  Serial.print(" V=");
  Serial.println(raw * 5.0 / 1023.0, 2);

  delay(200);
}
