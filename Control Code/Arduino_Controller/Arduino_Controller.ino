#include<Servo.h>

Servo leftAnkleM;
Servo leftKneeM;
Servo leftHipM;
Servo rightAnkleM;
Servo rightKneeM;
Servo rightHipM;

int leftAnkle = 90;
int leftKnee = 0;
int leftHip = 90;
int rightAnkle = 90;
int rightKnee = 0;
int rightHip = 90;

String values;

void setup() {
  leftAnkleM.attach(2);
  leftKneeM.attach(3);
  leftHipM.attach(4);
  rightAnkleM.attach(5);
  rightKneeM.attach(6);
  rightHipM.attach(7);
  
  Serial.begin(9600);
}

void loop() {
  if (Serial.available()>0){
    values = Serial.readStringUntil('x');
    leftAnkle = values.substring(0,3).toInt();
    leftKnee = values.substring(3,6).toInt();
    leftHip = values.substring(6,9).toInt();
    rightAnkle = values.substring(9,12).toInt();
    rightKnee = values.substring(12,15).toInt();
    rightHip = values.substring(15,18).toInt();
  }

  leftLeg(leftAnkle, leftKnee, leftHip);
  delay(100);
  rightLeg(rightAnkle, rightKnee, rightHip);
  delay(100);
}

void leftLeg(int ankle,int knee,int hip){
  leftAnkleM.write(180-ankle);
  leftKneeM.write(90-knee);
  leftHipM.write(160-hip);
}

void rightLeg(int ankle,int knee,int hip){
  rightAnkleM.write(ankle);
  rightKneeM.write(90+knee);
  rightHipM.write(hip);
}

