#include <SoftwareSerial.h>
SoftwareSerial btSerial(3, 4);
char bt_read;
void setup() {
  Serial.begin(9600);
  Serial.println("connected");
}

void loop() {
  if (btSerial.available()){
    bt_read = btSerial.read();
    // 작동 코드
  }
}
