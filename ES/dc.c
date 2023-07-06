#include <lpc17xx.h>
void delay_ms(unsigned int ms)// delay routine
{
unsigned int i,j;
for(i=0;i<ms;i++)
for(j=0;j<60000;j++);
}
#define SBIT_CNTEN 0 //counter enable
#define SBIT_PWMEN 2 //pwm 2 block enable
#define SBIT_PWMMR0R 1 //This bit is used to Reset PWMTC whenever it Matches PWMRx(x:0-6)
#define SBIT_PWMENA3 11 //This bit is used to enable/disable the PWM output for PWMx(x:1-6)
#define PWM_3 4 //P2_2 (0-1 Bits of PINSEL4)
int main(void)
{
int dutyCycle;
SystemInit();
/* Cofigure pins(P2_2 ) for PWM mode. */
LPC_PINCON->PINSEL4 = (1<<PWM_3) ;
/* Enable Counters,PWM module */
LPC_PWM1->TCR = (1<<SBIT_CNTEN) | (1<<SBIT_PWMEN);
LPC_PWM1->PR = 0x00; /* No Prescalar */
LPC_PWM1->MCR = (1<<SBIT_PWMMR0R); /*Reset on PWMMR0, reset TC if it
matches MR0 */
LPC_PWM1->MR0 = 100; /* set PWM cycle(Ton+Toff)=100) */
/* Enable the PWM output pins for PWM_1-PWM_4(P2_0 - P2_3) */
LPC_PWM1->PCR = (1<<SBIT_PWMENA3);
while(1)
{
{
LPC_PWM1->MR3 = dutyCycle; /* Increase the dutyCycle from 0-100 */
delay_ms(5);
}
if(!(LPC_GPIO2->FIOPIN & 0x00000800))//if sw 23 pressed
{
while(!(LPC_GPIO2->FIOPIN & 0x00000800));
dutyCycle-=10; //decrement duty cycle 10%
if(dutyCycle<0)
{
dutyCycle=0;
}
}
else if(!(LPC_GPIO2->FIOPIN & 0x00001000)) //if SW 22 pressed
{
while(!(LPC_GPIO2->FIOPIN & 0x00001000));
dutyCycle+=10; //increment duty cycle 10%
if(dutyCycle>100)
{
dutyCycle=99;
}
}
}
}