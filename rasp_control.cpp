#include <stdlib.h>
#include <iostream>
#include <string>
#include <string.h>
#include <wiringPiI2C.h>
#include <wiringPi.h>
#include <unistd.h>
#include <mutex>
using namespace std;

#define PinInterrupt 15

pthread_mutex_t mutex1 = PTHREAD_MUTEX_INITIALIZER;
int fd;
//
//void LigarLed()
//{
//	for (int i = 1; i < 7; i++)
//	{
//		wiringPiI2CWrite(fd, 0);
//		delay(10); // Esperar o I2C do MSP
//	}
//	
//	wiringPiI2CWrite(fd, 1);
//	delay(10); 
//}

bool finish = false;

void Interrupt()
{
	printf("Interrompido\n");
	pthread_mutex_unlock(&mutex1);
}

int main(int argc, char *argv[])
{
	wiringPiSetup();
	pinMode(PinInterrupt, INPUT);
	if (argc < 2)
		return 0;
	
	fd = wiringPiI2CSetup(0x34);
//	if ((atoi(argv[7]) & 1) == 1)
//		LigarLed();
	
	for (int i = 1; i < argc; i++)
	{
		wiringPiI2CWrite(fd, atoi(argv[i]));
		delay(10); // Esperar o I2C do MSP
	}

	pthread_mutex_lock(&mutex1);
	wiringPiISR(PinInterrupt, INT_EDGE_RISING, Interrupt);	
	pthread_mutex_lock(&mutex1);
	int retorno = wiringPiI2CRead(fd);
	delay(10);
	printf("%d\n",retorno);
	return retorno;

}
