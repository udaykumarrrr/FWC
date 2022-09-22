#include <avr/io.h>
#include <stdbool.h>
#include <util/delay.h>
int main(void)
{
	bool a=1,c=0;
	bool A, C, F;


	DDRD=0b00000100;
	DDRB=0b11111100;

	F=(A&&!C) || (!A&&C);
	PORTD=(F<<2);
	return 0;
}
