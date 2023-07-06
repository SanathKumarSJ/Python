Main code:- Step Angle Rotation




#include <lpc17xx.h>
void delay(unsigned int ms)
{
unsigned int i,j;
for(i=0;i<ms;i++)
for(j=0;j<20000;j++); //delay subroutine
}
/* start the main program */
int main()
{
int cycle;
SystemInit(); //Clock and PLL configuration
LPC_GPIO0->FIODIR |= 0x00078000; //Configure the PORT0 pins as OUTPUT;
for(cycle=0; cycle<13; cycle++)// for loop condition for number of rotation. It gives approx 90
degree rotation
{
LPC_GPIO0->FIOPIN = 0x00008000 ; // p0.15 pin
delay(100);
LPC_GPIO0->FIOPIN = 0x00010000 ;// p0.16 pin
delay(100);
LPC_GPIO0->FIOPIN = 0x00020000 ; // p0.17 pin
delay(100);
LPC_GPIO0->FIOPIN = 0x00040000 ;// p0.18 pin
delay(100);
}
}



Stepper motor rotation clockwise and anticlockwise.


#include "lpc17xx.h"
void delay();
void delay()
{
int i,j;
for(i=0;i<0xff;i++)
for(j=0;j<0x400;j++);
}
int main (void)
{
char rotate=0;
SystemInit();
LPC_GPIO0
->FIODIR |= 0x00078000;
while(1) {
if(rotate==1) {
LPC_GPIO0
->FIOPIN
= 0x00008000
;
delay();
LPC_GPIO0
->FIOPIN = 0x00010000
;
delay();
LPC_GPIO0
->FIOPIN
= 0x00020000
;
delay();
LPC_GPIO0
->FIOPIN
= 0x00040000
;
delay();
}
else {
LPC_GPIO0
->FIOPIN
= 0x00040000
;
delay();
LPC_GPIO0
->FIOPIN
= 0x00020000
;
delay();
LPC_GPIO0
->FIOPIN
= 0x00010000
;
delay();
LPC_GPIO0
->FIOPIN
= 0x00008000
;
delay();
}
if(!(LPC_GPIO2
->FIOPIN
& 0x00000800))
{
while(!(LPC_GPIO2
->FIOPIN
& 0x00000800));
rotate=1;
}
else if(!(LPC_GPIO2
->FIOPIN
& 0x00001000))
{
while(!(LPC_GPIO2
->FIOPIN
& 0x00001000));
rotate=0;
}}
}




