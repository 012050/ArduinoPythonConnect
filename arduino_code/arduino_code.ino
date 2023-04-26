
char s_read;
void setup() {
  Serial.begin(9600);
  Serial.println("connected");
}

void loop() {
  if (Serial.available()){
    s_read = Serial.read();
    Serial.println(s_read);
  }
}
