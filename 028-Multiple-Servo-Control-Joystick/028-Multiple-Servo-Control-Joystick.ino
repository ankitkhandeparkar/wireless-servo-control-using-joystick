#include <Servo.h>

int joyX = 0;
int joyY = 1;
  
int x;
int y;

int servox;
int servoy;

//String sss = "o";
//String ss = "p";

//String s1;
//String s2;

void setup() 
{
  Serial.begin(1200);
}
  
void loop()
{
  
  servox = analogRead(joyX);
  x = map(servox, 0, 1023, 0, 180);
  //s1 = sss + x;
  Serial.print(x);

  Serial.print(" ");  
  servoy = analogRead(joyY);
  y = map(servoy, 0, 1023, 0, 180);
  //s2 = ss + y;
  Serial.println(y);


  

  

  delay(500);  
}
