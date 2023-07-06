#include "lpc17xx.h"
#define Switch 11 //p2.11
#define Led1 19 //p1.19
#define Led2 20 //p1.20
#define Led3 21 //p1.21
#define Led4 22 //p1.22
#define Led5 23 //p1.23
#define Led6 24 //p1.24
#define Led7 25 //p1.25
#define Led8 26 //p1.26
int main (void)
{
uint32_t switchStatus;
LPC_GPIO1->FIODIR = 0x07f80000; /* P1.xx defined as Outputs */
LPC_GPIO1->FIOCLR = 0x07f80000; /* turn off all the LEDs */
LPC_GPIO2->FIODIR = 0x00000000; /* P2.xx defined as Outputs */
while(1)
{
/* Turn On all the leds and wait for one second */
switchStatus = (LPC_GPIO2->FIOPIN>>Switch) & 0x01 ; // Read the switch status
if(switchStatus == 1) //Turn ON/OFF LEDs depending on switch status
{
LPC_GPIO1->FIOPIN = (1<<Led1)|(1<<Led2)|(1<<Led3)|(1<<Led4);//turn on 1st 4 leds (normal
condition)
}
else
{
LPC_GPIO1->FIOPIN = (1<<Led5)|(1<<Led6)|(1<<Led7)|(1<<Led8);//turn on next 4 leds(switch pressed)
}
}
}
