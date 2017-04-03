using System;

namespace COIS4470A2Q1PD
{
	class MainClass
	{
		public struct count 
		{                                 /* sum of ...              */

			public double setup;                          /*   setup instances       */
			public double holding;                        /*   inventory held (+)    */
			public double shortage;                       /*   inventory short (-)   */
			public double order;                          /*   orders                */
			public double demand;                         /*   demands               */

		}

		/// <summary>
		/// Uniform the specified rand. This class is used for Question 1 part e and d 
		/// Uniform Dist to calculate the data 
		/// <returns>The uniform returns an int that represent the number of item sold on that day.</returns>
		/// <param name="rand">Rand.</param>
		public static int uniform (Random rand)
		{
			double high = 48; //Taken from sis.dat
			double low = 17; //Taken from sis.dat

			return Convert.ToInt32(Math.Ceiling( (low + ((high - low) * rand.NextDouble()))));


		}

		public static int Geometric(Random random ) /* use 0.0 < p < 1.0 */
		{
			double average = 29.29; // taken from sis.dat 
			double p = 1/average; 
			return Convert.ToInt32((long)(Math.Log(1.0 - random.NextDouble()) / Math.Log(p)));
		}

	
		public static void Main(string[] args)
		{
			Console.WriteLine("Hello World!");
			int MAXIMUM = 80;
			int MINIMUM = 25; 
			int index = 0;                      /* time interval index     */
			int inventory = MAXIMUM;                /* current inventory level */
			int demand;                             /* amount of demand        */
			int order;                              /* amount of order         */
			Random random= new Random();

			count sum;
			sum.setup = 0;
			sum.holding = 0;
			sum.shortage = 0;
			sum.order = 0;
			sum.order = 0;
			sum.demand = 0;

			for (int i = 0; i < 100;i++) 
			{
			    index++;
			    if (inventory<MINIMUM) {             /* place an order          */
			      order         = MAXIMUM - inventory;
			      sum.setup++;
			      sum.order    += order;
			    }
			    else                                   /* no order                 */
			      order         = 0;                   
			    inventory      += order;               /* there is no delivery lag */
				demand          = Geometric(random);
			sum.demand     += demand;
			    if (inventory > demand) 
			      sum.holding  += (inventory - 0.5 * demand);
			    else {
					sum.holding  += Math.Pow(inventory,2) / (2.0 * demand);
			      sum.shortage += Math.Pow(demand - inventory,2) / (2.0 * demand);
    		}
			    inventory -= demand;
			  }

			  if (inventory<MAXIMUM) {               /* force the final inventory to */
			    order           = MAXIMUM - inventory; /* match the initial inventory  */
			    sum.setup++;
			    sum.order      += order;
			    inventory      += order;
			  }

  Console.WriteLine("\nfor {0} time intervals ", index);
  Console.WriteLine("with an average demand of {0}\n", sum.demand / index);
  Console.WriteLine("and policy parameters (s, S) = ({0}, {1})\n\n", MINIMUM, MAXIMUM);
  Console.WriteLine("   average order ............ = {0}\n", sum.order / index);
  
  Console.WriteLine("   average holding level .... = {0}\n", sum.holding*25 / index);
  Console.WriteLine("   average shortage level ... = {0}\n", sum.shortage*700 / index);
			Console.WriteLine("   setup frequency .......... = {0}\n", sum.setup * 1000 / index);
  Console.WriteLine("   SUM OF COSY ... = {0}\n", ((sum.shortage*700)+ (sum.holding*25)+(sum.setup*1000)) / index);

  
		}
	}
}
