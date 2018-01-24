#include <Servo.h>

Servo ankle;
Servo knee;

void setup() {
  ankle.attach(2);
  knee.attach(3);
}

void loop() {
  ankle.write(0);
  knee.write
  ankle.write(30);
  knee.write(30);
  delay(100)
}
