#include <Arduino.h>
int A=0,B=0,C=0;
int F;
void setup()
{
	pinMode(2,INPUT);
	pinMode(3,INPUT);
	pinMode(4,INPUT);
	pinMode(13,OUTPUT);
}
void loop()
{
	A=digitalRead(2);
	B=digitalRead(3);
    C =digitalRead(4);
	F=(A&&!C)||(!A&&C);
	digitalWrite(13,F);
}

