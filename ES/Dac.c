#triangular

#include "LPC17xx.h"
uint32_t val;
int main()
{
SystemInit();
LPC_PINCON->PINSEL1 |= 0x02<<20; //p0.26 pinsel bits 20 and 21
while(1)
{
while(1)
{
val++;// increment values by 6
LPC_DAC->DACR=(val<<6);//send values to dac
if(val>=0x3ff)// if value exceeds 1024
{
break;
}
}
while(1)
{
val--; // decrement value by 6
LPC_DAC->DACR=(val<<6);// send value to dac
if(val<=0x000)// if value come down by 0
{
break;
}
}
}
}




Square Wave generation:-


#include "LPC17xx.h"
void delay(unsigned int ms)// delay subroutine
{
unsigned int i,j;
for(i=0;i<ms;i++)
for(j=0;j<2000;j++);
}
int main()
{
SystemInit();
LPC_PINCON->PINSEL1 |= 0x02<<20;//p0.26 pinsel bits 20 and 21
while(1)
{
LPC_DAC->DACR=0xffff;// send maximum values to dac
delay(20); // delay
LPC_DAC->DACR=0x0000;// send min values to dac
delay(20);
}
}

