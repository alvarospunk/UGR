#include <stdio.h>
#include <time.h>
#include <stdlib.h>
#include <unistd.h>
#include <errno.h>

#define NUM_CORES 4
#define TOPE 100000

/* función que calcula números primos */
void calcular_primos()
{
    unsigned long i, num, primos = 0;
    for (num = 1; num <= TOPE; ++num) {
        for (i = 2; (i <= num) && (num % i != 0); ++i);
        if (i == num)
            ++primos;
    }
    printf("Calculados %d primos por un core\n", primos);
}

int main(int argc, char ** argv)
{
    time_t start, end;
    time_t run_time;
    unsigned long i;
    pid_t pids[NUM_CORES]; // array con los pids de los futuros procesos hijos

    time(&start);
		/* se hace un fork por cada core del procesador */
    for (i = 0; i < NUM_CORES; ++i) {
        if (!(pids[i] = fork())) {
            calcular_primos();
            exit(0);
        }
        if (pids[i] < 0) {
            perror("Fork");
            exit(1);
        }
    }
		/* esperar a que terminen todos los procesos hijos */
    for (i = 0; i < NUM_CORES; ++i) {
        waitpid(pids[i], NULL, 0);
    }
    time(&end);
    run_time = difftime(end, start);
    printf("Esta máquina con %d cores ha calculado los números primos dentro del tope %d "
           "en %d segundos\n", NUM_CORES, TOPE, run_time);
    return 0;
}
