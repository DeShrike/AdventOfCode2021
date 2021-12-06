CC=gcc
AR=ar

all: day1 day6

rmbin:
	rm day1
	rm day6

###################################00

day1: day1.o aoc.o
	$(CC) -o day1 day1.o aoc.o

day1.o: day1.c aoc.h
	$(CC) -c -O3 day1.c

###################################00

day6: day6.o aoc.o
	$(CC) -o day6 day6.o aoc.o

day6.o: day6.c aoc.h
	$(CC) -c -O3 day6.c

###################################00

aoc.o: aoc.c aoc.h
	$(CC) -c -O3 aoc.c

###################################00

clean:
	rm *.o
