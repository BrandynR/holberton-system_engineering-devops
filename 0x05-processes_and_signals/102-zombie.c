#include <stdio.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <stdlib.h>

/**
 * infinite_while - infinite loop
 * Return: returns 0
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 * zombie - creates 5 zombie processes
 * Return: 0 on success
 */
int zombie(void)
{
	pid_t p;
	int i;

	for (i = 0; i < 5; i++)
	{
		p = fork();
		if (p > 0)
		{
			sleep(2);
		}
		else
		{
		printf("Zombie process created, PID: %u\n", p);
		sleep(2);
		}
	}

	return (0);
}

/**
 * main - creates 5 zombie processes, infinitely loops a wait after
 *
 * Return: 0 on success
 */
int main(void)
{
	zombie();
	infite_while();
	return (0);
}
