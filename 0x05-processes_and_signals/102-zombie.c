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
		sleep(1);
	return (0);
}
/**
 * main - entry point
 * Return: never returns
 */
int main(void)
{
	int i = 0, pid;

	while (i++ < 5)
	{
		pid = fork();
		if (pid > 0)
			sleep(1);
		else
		{
			printf("Zombie process created PID: %d\n", getpid());
			exit(0);
		}
	}

	infinite_while();

	return (0);
}
