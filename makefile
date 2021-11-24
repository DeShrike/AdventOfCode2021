CC=gcc
AR=ar

all: dayX

rmbin:
	rm dayX

###################################00

dayX: dayX.o
	$(CC) -o dayX dayX.o

dayX.o: dayX.c
	$(CC) -c -O3 dayX.c

###################################00

clean:
	rm *.o
