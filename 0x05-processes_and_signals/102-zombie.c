#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>

/**
 * infinite_while - Run an infinite while loop.
 *
 * Return: Always 0.
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
 * main - Creates five zombie processes.
 *
 * Return: 0 on success, 1 on failure.
 */
int main(void)
{
	pid_t child_pid;
	int i = 0;

	for (i = 0; i < 5; i++)
	{
		child_pid = fork();
		if (child_pid == -1)
		{
			perror("fork");
			return (1);
		}
		else if (child_pid > 0)
		{
			printf("Zombie process created, PID: %d\n", child_pid);
			sleep(1);
		}
		else
			exit(0);
	}

	infinite_while();

	return (0);
}
