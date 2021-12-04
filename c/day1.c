#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "aoc.h"

#define DAY 1


#define MAX_LINES 3000
#define MAX_LINE_LENGTH 10

char** lines;
int line_count = 0;

void main()
{
	start_day(DAY);

	lines = read_input(DAY, MAX_LINES, MAX_LINE_LENGTH, &line_count);
	if (lines == NULL)
	{
		perror("read_input()");
		return;
	}

	/***********************/

	start_part_a();

	show_answer(123);

	/***********************/

	start_part_b();

	show_answer(456123);

	/***********************/

	free_input(lines, line_count);
}
