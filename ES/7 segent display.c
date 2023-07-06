#include <lpc17xx.h>
void delay_ms(unsigned int ms)
{
unsigned int i,j;
for(i=0;i<ms;i++)
for(j=0;j<40000;j++);
}
/* start the main program */
int main()
{
SystemInit(); //Clock and PLL configuration
LPC_GPIO0->FIODIR = 0x0000001f7; //Configure the PORT0 pins as OUTPUT;
while(1)
{
LPC_GPIO0->FIOSET = 0x00000004; // Make all the Port pins as high
LPC_GPIO0->FIOCLR = 0x000001f3;//clear all segments
LPC_GPIO0->FIOSET = 0x00000100;// set g to make 0
delay_ms(200);
LPC_GPIO0->FIOCLR = 0x000001f3;//clear all segments
LPC_GPIO0->FIOSET = 0x000001e1;//set a,d,e,f,g to make 1
delay_ms(200);
LPC_GPIO0->FIOCLR = 0x000001f3;//clear all segments
LPC_GPIO0->FIOSET = 0x00000090;//set c,f to make 2
delay_ms(200);
LPC_GPIO0->FIOCLR = 0x000001f3;//clear all segments
LPC_GPIO0->FIOSET = 0x000000c0;//set e and f to make 3
delay_ms(200);
LPC_GPIO0->FIOCLR = 0x000001f3;//clear all segments
LPC_GPIO0->FIOSET = 0x00000061;//set a,d,e to make 4
delay_ms(200);
LPC_GPIO0->FIOCLR = 0x000001f3;//clear all segments
LPC_GPIO0->FIOSET = 0x00000042;//set b,e to make 5
delay_ms(200);
LPC_GPIO0->FIOCLR = 0x00004713;//clear all segments
LPC_GPIO0->FIOSET = 0x00000002;//set b to make 6
delay_ms(200);
LPC_GPIO0->FIOCLR = 0x000001f3;//clear all segments
LPC_GPIO0->FIOSET = 0x000001e0;//set d,e,f,g to make 7
delay_ms(200);
LPC_GPIO0->FIOCLR = 0x000001f3;//clear all segments
LPC_GPIO0->FIOSET = 0x00000000;//set all 0 to make 8
delay_ms(200);
LPC_GPIO0->FIOCLR = 0x000001f3;//clear all segments
LPC_GPIO0->FIOSET = 0x00000040;//set e to make 9
delay_ms(200);
LPC_GPIO0->FIOCLR = 0x000001f3;//clear all segments
LPC_GPIO0->FIOSET = 0x00000020;//set d to make A
delay_ms(200);
LPC_GPIO0->FIOCLR = 0x000001f3;//clear all segments
LPC_GPIO0->FIOSET = 0x00000003;//set a,b to make b
delay_ms(200);
LPC_GPIO0->FIOCLR = 0x000001f3;//clear all segments
LPC_GPIO0->FIOSET = 0x00000112;//set set b,c,g to make C
delay_ms(200);
LPC_GPIO0->FIOCLR = 0x000001f3;//clear all segments
LPC_GPIO0->FIOSET = 0x00000081;//set a,f to make d
delay_ms(200);
LPC_GPIO0->FIOCLR = 0x000001f3;//clear all segments
LPC_GPIO0->FIOSET = 0x00000012;//set b,c to make E
delay_ms(200);
LPC_GPIO0->FIOCLR = 0x000001f3;//clear all segments
LPC_GPIO0->FIOSET = 0x00000032;//set b,c,d to make F
}
}