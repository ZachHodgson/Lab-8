#include <Servo.h>

Servo s1; // servo object
Servo s2; // servo object

//servo 1
int pot1 = 0; //pot pin
int angle1; // variable to adjust angle 

int pot2 = 1; //pot pin
int angle2; // variable to adjust angle 

void setup() {
  // put your setup code here, to run once:
  s1.attach(9); // servo attached to pin 9
  s2.attach(8); // servo attached to pin 8
}

void loop() {
  //put your main code here, to run repeatedly:
  angle1 = analogRead(pot1); // assigns the value of the pot to the variable angle
  angle1 = map(angle1, 0, 1023, 0, 180); // allows the servo to move between 0 and 180
  s1.write(angle1); // sets the position to the scaled value of angle
  angle2 = analogRead(pot2); // assigns the value of the pot to the variable angle
  angle2 = map(angle2, 0, 1023, 0, 180); // allows the servo to move between 0 and 180
  s2.write(angle2); // sets the position to the scaled value of angle
  delay(15);
}
