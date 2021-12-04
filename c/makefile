CC=gcc
AR=ar

all: day1

rmbin:
	rm day1

###################################00

day1: day1.o aoc.o
	$(CC) -o day1 day1.o aoc.o

day1.o: day1.c aoc.h
	$(CC) -c -O3 day1.c

aoc.o: aoc.c aoc.h
	$(CC) -c -O3 aoc.c

###################################00

clean:
	rm *.o
