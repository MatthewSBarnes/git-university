
/* -------------------------------------------------------------------------
 * This program simulates a simple (s,S) inventory system using demand read  
 * from a text file.  Backlogging is permitted and there is no delivery lag.
 * The output statistics are the average demand and order per time interval
 * (they should be equal), the relative frequency of setup and the time
 * averaged held (+) and short (-) inventory levels.
 *
 * NOTE: use 0 <= MINIMUM < MAXIMUM, i.e., 0 <= s < S.
 *
 * Name              : sis1.c  (Simple Inventory System, version 1)
 * Authors           : Steve Park & Dave Geyer 
 * Language          : ANSI C 
 * Compile with      : gcc sis1.c
 * ------------------------------------------------------------------------- 
*/

#include <stdio.h>                        
#include <stdlib.h>
#include <time.h>
#include <math.h>

#define FILENAME  "sis1.dat"            /* input data file                */
#define MINIMUM   40                    /* 's' inventory policy parameter */
#define MAXIMUM   80                    /* 'S' inventory policy parameter */
#define sqr(x)    ((x) * (x))

/* ======================== */
   long GetDemand(FILE *fp)
/* ======================== */
{
  long d;
  fscanf(fp, "%ld\n", &d);
  
  return (d);
}


/* ======================== */
   long GenDemand()
/* ======================== */
{
  long d;
  long max = 49;
  long min = 17;

  d = (rand() % (max - min)) + min;   /* generate demand between min and max of sis1.dat*/
  return (d);
}


/* ======================== */
   long GeoDemand()
/* ======================== */
{
  long d;                   /*           mean = 29.29;       */
  double p = 1/29.29;       /* i guess this equals 1 / 29.29 */
  double random = ((double) rand() / RAND_MAX);
  d = (fabs((long) (((double) log(1.0 - random) / (double) log(1-p)))));
  return (d);
}


/* ============== */
   int main(void)
/* ============== */
{
  FILE *fp;                                /* input data file         */
  long index     = 0;                      /* time interval index     */
  long inventory = MAXIMUM;                /* current inventory level */
  long demand;                             /* amount of demand        */
  long order;                              /* amount of order         */
  long C_holding = 25;                     /* cost per car per week   */
  long C_shortage = 700;                   /* cost per car per week   */
  long C_setUp = 1000;                     /* cost per order          */
  long C_unit = 8000;                      /* each car ordered        */

  srand(time(NULL));
  /* used for calculating min and max values in sis1.data
    long max = 0;
    long min = 9999;
    long temp = 0;
  */ 

  struct {                                 /* sum of ...              */
    double setup;                          /*   setup instances       */
    double holding;                        /*   inventory held (+)    */
    double shortage;                       /*   inventory short (-)   */
    double order;                          /*   orders                */
    double demand;                         /*   demands               */
  } sum = { 0.0, 0.0, 0.0, 0.0, 0.0 };

  fp = fopen(FILENAME, "r");
  if (fp == NULL) {
    fprintf(stderr, "Cannot open input file %s\n", FILENAME);
    return (1);
  }

  
  /* used for calculating min and max values in sis1.dat 
    while (!feof(fp)) {
      temp = GetDemand(fp);
      if (max < temp)
        max = temp;
      if (min > temp)
        min = temp;
    }
  
    printf("max: %ld\n", max);
    printf("min: %ld\n", min);

    fclose(fp);
    return(0);
  */


  while (index < 100) {               /*!feof(fp)) {*/
    index++;
    if (inventory < MINIMUM) {             /* place an order          */
      order         = MAXIMUM - inventory;
      sum.setup++;
      sum.order    += order;
    }
    else                                   /* no order                 */
      order         = 0;                   
    inventory      += order;               /* there is no delivery lag */
    demand          = GeoDemand();             /*GetDemand(fp);*/
    sum.demand     += demand;
    if (inventory > demand) 
      sum.holding  += (inventory - 0.5 * demand);
    else {
      sum.holding  += sqr(inventory) / (2.0 * demand);
      sum.shortage += sqr(demand - inventory) / (2.0 * demand);
    }
    inventory      -= demand;
  }

  if (inventory < MAXIMUM) {               /* force the final inventory to */
    order           = MAXIMUM - inventory; /* match the initial inventory  */
    sum.setup++;
    sum.order      += order;
    inventory      += order;
  }

  printf("\nfor %ld time intervals ", index);
  printf("with an average demand of %6.2f\n", sum.demand / index);
  printf("and policy parameters (s, S) = (%d, %d)\n\n", MINIMUM, MAXIMUM);
  printf("   average order ............ = %6.2f\n", sum.order / index);
  printf("   setup frequency .......... = %6.2f\n", sum.setup / index);
  printf("   setup cost ............... = %6.2f\n", sum.setup * C_setUp / index);
  printf("   average holding level .... = %6.2f\n", sum.holding / index);
  printf("   average holding cost ..... = %6.2f\n", sum.holding * C_holding / index);
  printf("   average shortage level ... = %6.2f\n", sum.shortage / index);
  printf("   average shortage cost .... = %6.2f\n", sum.shortage * C_shortage / index);
  printf("   sum of the three costs ... = %6.2f\n", (sum.shortage * C_shortage / index) + (sum.holding * C_holding / index) + (sum.setup * C_setUp / index));

  fclose(fp);
  return (0);
}
