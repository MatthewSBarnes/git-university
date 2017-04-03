
/* -------------------------------------------------------------------------
 * Demonstrates how a random number generator can be developed by
 * combining two Linear Congruential Generators using the following 
 * algorithm.
 *
 * The first generator has multiplier a_1, and modulus m_1,
 * The second generator has multiplier a_2, and modulus m_2,
 *
 * NOTE: use 0 <= MINIMUM < MAXIMUM, i.e., 0 <= s < S.
 *
 * Name              : a1q2.c 
 * Author            : Matthew Barnes 
 * Language          : ANSI C 
 * Compile with      : gcc a1q2.c
 * ------------------------------------------------------------------------- 
*/

#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <math.h>

#define MAX_LEN 100

/* ============== */
   int main(void)
/* ============== */
{
  int m_1 = 16;
  int m_2 = 32;
  long a_1 = 11;
  long a_2 = 3;
  long x_1 = 7;                  /* must be [1, (m_1 - 1)] */
  long x_2 = 8;                  /* must be [1, (m_2 - 1)] */
  double temp;

  double max_range = 0.5;
  double min_range = 0.2;
  int gap_size = 0;

  long num_rand = 100;              /* number of random numbers ot be generated */
  long index = 0;

  double rand_store[MAX_LEN];
  int gap_store[MAX_LEN];
  int start_gap_flag = 0;
  int total_samples = 0;

  for (int j = 0; j < MAX_LEN; j++) {
    gap_store[j] = 0;
  }

  // printf ("Enter a seed for m_1: ");
  // scanf ("%d", &m_1);
  // printf ("Enter a seed for m_2: ");
  // scanf ("%d", &m_2);
  // printf ("Enter a value for a_1: ");
  // scanf ("%ld", &a_1);
  // printf ("Enter a value for a_2: ");
  // scanf ("%ld", &a_2);
  // printf ("Enter a value for x_1: ");
  // scanf ("%ld", &x_1);
  // printf ("Enter a value for x_2: ");
  // scanf ("%ld", &x_2);
  // printf ("Enter how many numbers to generate: ");
  // scanf ("%ld", &num_rand);
  // printf ("You entered: %d\n", m_1);
  // printf ("You entered: %d\n", m_2);
  
  while (index < num_rand) {
    index++;

    x_1 = (a_1 * x_1) % m_1;
    x_2 = (a_2 * x_2) % m_2;

    temp = (fabs((x_1 - x_2) % m_1));

    if (temp > 0) {
      temp = temp / m_1;
    } else {
      temp = (m_1 - 1) / m_1;
    }
    /* formatting output */
    if (index % 5 == 0) {
      printf("%.3ld  Generated random number: %6.4f\n", index, temp);
      printf("%.3ld  x_1: %ld,       x_2: %ld\n", index, x_1, x_2);
      if ( min_range < temp && temp < max_range ) {
        total_samples++;
        if (start_gap_flag) {
          gap_store[gap_size] = gap_store[gap_size] + 1;
        }
        //printf("gap_store[%d]: %d", gap_size, gap_store[gap_size]);
        gap_size = -1;
        start_gap_flag = 1;
        //printf("\n==%.3ld==\n", index);
      }
    } else {
      printf("     Generated random number: %6.4f\n", temp);
      printf("     x_1: %ld,       x_2: %ld\n", x_1, x_2);
      if ( min_range < temp && temp < max_range ) {
        total_samples++;
        if (start_gap_flag) {
          gap_store[gap_size] = gap_store[gap_size] + 1;
        }
        //printf("gap_store[%d]: %d", gap_size, gap_store[gap_size]);
        gap_size = -1;
        start_gap_flag = 1;
        //printf("\n==%.3ld==\n", index);
      }
    }
    rand_store[index] = temp;
    gap_size++;
  }

  printf("\n%ld numbers have been generated\n\n", index);

  for(int i = 0; i < (sizeof(gap_store)/sizeof(gap_store[0])); i++) {
    if (gap_store[i] != 0) {
      printf("\n Gap Length of %d, observed count is %d\n", i, gap_store[i] );
      printf(" Gap Length of %d, expected count is %6.6f\n\n", i, ((max_range - min_range) * pow((1 - (max_range - min_range)), i) * total_samples));
    }
    printf(" Gap Length of %d, expected count is %6.6f\n", i, ((max_range - min_range) * pow((1 - (max_range - min_range)), i) * total_samples));
    //printf("\n%d ", gap_store[i]);
  }

  return (0);
}