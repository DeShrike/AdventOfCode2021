#ifndef _AOC_H
#define _AOC_H

void start_day(int day);
void free_input(char** lines, int line_count);
char** read_input(int day, int max_lines, int max_line_length, int* line_count);
void start_part_a();
void start_part_b();
void show_answer(long long answer);
long long get_answer_a();
long long get_answer_b();

#endif
