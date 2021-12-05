#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "aoc.h"

#define DAY 1

#define MAX_LINES 3000
#define MAX_LINE_LENGTH 10

void part_a();
void part_b();

char** lines;
int line_count = 0;
int* numbers;

void main()
{
	start_day(DAY);

	lines = read_input(DAY, "../", MAX_LINES, MAX_LINE_LENGTH, &line_count);
	if (lines == NULL)
	{
		perror("read_input()");
		return;
	}

    numbers = convert_input_to_numbers(lines, line_count);

    part_a();
    part_b();

    free(numbers);
	free_input(lines, line_count);
}

void part_a()
{
	start_part_a();

	int increase_count = 0;
	for (int ix = 1; ix < line_count; ix++)
	{
		if (numbers[ix] > numbers[ix - 1])
		{
			increase_count++;
		}
	}

	show_answer(increase_count);
}

void part_b()
{
	start_part_b();

	int increase_count = 0;
	int prev_sum = -1;
	for (int ix = 0; ix < line_count - 2; ix++)
	{
		int sum = numbers[ix] + numbers[ix + 1] + numbers[ix + 2];
		if (sum > prev_sum && prev_sum != -1)
		{
			increase_count++;
		}

		prev_sum = sum;
	}

	show_answer(increase_count);
}
