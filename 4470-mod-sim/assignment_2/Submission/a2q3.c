
/* -------------------------------------------------------------------------
 * A random variate generator for exponential distribution.
 * MEW = 7, MEW = 170.
 * generate 1000 random variates for each.
 * Histograms in other file.
 *
 * Name              : a2q3.c 
 * Author            : Matthew Barnes 
 * Language          : ANSI C 
 * Compile with      : gcc a2q3.c
 * ------------------------------------------------------------------------- 
*/

#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <math.h>

#define MAX_LEN 1000

/* ============== */
   int main(void)
/* ============== */
{
  long rand_count = 1000;
  double mean = 7;

  double random;
  double rand_num;

  double rand_store[MAX_LEN];
  srand(time(NULL));
  
  FILE *fp;

  fp = fopen("a2q3.csv", "w");
  if (fp == NULL) {
    printf("Couldn't open file\n");
    return (1);
  }

  for (int i = 0; i < rand_count; i++)
  {
      rand_num = (-1) * (mean * log(1 - ((double) rand() / RAND_MAX)));
      fprintf(fp, "%6.6f\n", rand_num);
      rand_store[i] = rand_num;
  }

  for (int j = 0; j < (sizeof(rand_store)/sizeof(rand_store[0])); j++) {
    printf("  %d:    %6.6f\n", j, rand_store[j]);
  }
  fclose(fp);
  return (0);
}
