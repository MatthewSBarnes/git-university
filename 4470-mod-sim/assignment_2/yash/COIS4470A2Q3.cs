using System;

namespace COIS4470A2Q3
{
	class MainClass
	{
		public static void Main(string[] args)
		{
			Console.WriteLine("Hello World!");

			Random random = new Random();

			double q = 7;

			for (int i = 0; i < 1000; i++)
			{
				Console.WriteLine("{0} ", Exponential(q, random)); 


			}


		}
		public static double Exponential(double q, Random random)
		{
			return (-q * Math.Log(1.0 - random.NextDouble()));
		}
	}
}
