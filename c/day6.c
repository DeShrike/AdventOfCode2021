#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "aoc.h"

#define DAY 6

#define MAX_STAGES 9
#define MAX_INITIAL_NUMBERS 1000
#define MAX_LINE_LENGTH 1000
#define MAX_LINES 2

void part_a();
void part_b();

char** lines;
int line_count = 0;
int numbers[MAX_INITIAL_NUMBERS];
long long stages[MAX_STAGES];

void main()
{
	start_day(DAY);

	lines = read_input(DAY, "../", MAX_LINES, MAX_LINE_LENGTH, &line_count);
	if (lines == NULL)
	{
		perror("read_input()");
		return;
	}

    rtrim(lines[0]);

    for (int ix = 0; ix < MAX_INITIAL_NUMBERS; ix++)
    {
        numbers[ix] = -1;
    }

    char delim[] = ",";
    char *ptr = strtok(lines[0], delim);
    int ix = 0;
    while (ptr != NULL)
    {
        numbers[ix++] = atoi(ptr);
        ptr = strtok(NULL, delim);
    }

    part_a();
    part_b();

	free_input(lines, line_count);
}

long long breed(int days)
{
    for (int s = 0; s < MAX_STAGES; s++)
    {
        stages[s] = 0;
    }

    for (int ix = 0; ix < MAX_INITIAL_NUMBERS; ix++)
    {
        if (numbers[ix] < 0)
        {
            continue;
        }

        stages[numbers[ix]]++;
    }

    for (int i = 0; i < days; i++)
    {
        long long pregnant = stages[0];
        for (int s = 1; s < MAX_STAGES; s++)
        {
            stages[s - 1] = stages[s];
            stages[s] = 0;
        }

        stages[6] += pregnant;
        stages[8] += pregnant;
    }

    long long sum = 0;
    for (int s = 0; s < MAX_STAGES; s++)
    {
        sum += stages[s];
    }

    return sum;
}

void part_a()
{
	start_part_a();

    long long result = breed(80);

	show_answer(result);
}

void part_b()
{
	start_part_b();

    long long result = breed(256);

	show_answer(result);
}
