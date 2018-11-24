#include <stdlib.h>
#include <iostream>
#include <string>
#include <string.h>
#include <wiringPiI2C.h>
#include <wiringPi.h>
#include <unistd.h>
using namespace std;

#define PinInterrupt 2

int fd;

void LigarLed()
{
	for (int i = 1; i < 7; i++)
	{
		wiringPiI2CWrite(fd, 0);
		delay(10); // Esperar o I2C do MSP
	}
	
	wiringPiI2CWrite(fd, 1);
	delay(10); 
}

int main(int argc, char *argv[])
{
	if (argc < 2)
		return 0;
	
	fd = wiringPiI2CSetup(0x34);
	if ((atoi(argv[7]) & 1) == 1)
		LigarLed();
	
	else
	{
		for (int i = 1; i < argc; i++)
		{
			wiringPiI2CWrite(fd, atoi(argv[i]));
			delay(10); // Esperar o I2C do MSP
		}

		while (wiringPiI2CRead(fd) != 7)
			delay(100);
	}
	
	waitForInterrupt(PinInterrupt, INT_EDGE_RISING);
	
	int retorno = wiringPiI2CRead(fd);
	delay(10);
	
	return retorno;

}
