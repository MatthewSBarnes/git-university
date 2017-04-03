////
/// Seyedyashar Morabbiheravi 
/// 0547952
/// COIS 4470 Assignment 2 Q 2 
/// 



using System;
using System.Collections.Generic;

namespace A2Q2
{
	class MainClass
	{
		//public static double mod(double a, double b)
		//{
		//	return a - (b * Math.Floor(a / b));
		//}
		public static void Main(string[] args)
		{
			//Console.WriteLine("Hello World!");


			double m1, m2, x1, x2,xFinal, a1, a2;
			int count = 100;

			// manually entering the input 
			//x1 = 7;//Given By part 2 
			//x2 = 8;//Given By part 2
			//a1 = 11;//Given By part 2
			//m1 = 16;//Given By part 2
			//a2 = 3;//Given By part 2
			//m2 = 32;//Given By part 2



			Console.WriteLine("Please Enter x1(Greater than zero)?)");
			x1 = Convert.ToDouble(Console.ReadLine());

			Console.WriteLine("Please Enter a1(Greater than zero)?)");
			a1 = Convert.ToDouble(Console.ReadLine());

			Console.WriteLine("Please Enter M1(Greater than zero)?)");
			m1 = Convert.ToDouble(Console.ReadLine());

			Console.WriteLine("Please Enter x2(Greater than zero)?)");
			x2 = Convert.ToDouble(Console.ReadLine());

			Console.WriteLine("Please Enter a2(Greater than zero)?)");
			a2 = Convert.ToDouble(Console.ReadLine());

			Console.WriteLine("Please Enter M2(Greater than zero)?)");
			m2 = Convert.ToDouble(Console.ReadLine());



		
			// Hold all the numbers 
			List<double> holder = new List<double>();




			for (int i = 0; i < count; i++)
			{
				/////////
				/// Calculate X1 and X2
				///
				x1 =  (a1 * x1)% m1;
				x2 = (a2 * x2) % m2;
				/// Calcuating X final, Using ABSOLUTE VALUE 

				if (x1 > x2)
				{
					xFinal = (x1 - x2) % m1;

				}

				else
				{
					xFinal = (x2 - x1) % m1;
				}

				/// 
				/// Calculation the Random number and adding it to LIST HOLDER

				if (xFinal > 0)
				{
					Console.WriteLine("x1={0}, x2={1} xfinal={2}", x1, x2, xFinal); 
					Console.WriteLine("\n Just added {0} as the new random calculated number", xFinal / m1);
					holder.Add(xFinal / m1);

				}
				else //if (xFinal == 0.00)
				{
					Console.WriteLine("x1={0}, x2={1} xfinal={2}", x1, x2, xFinal);
					Console.WriteLine("\n Just ggg added {0} as the new random calculated number", (m1 - 1) / m1);
					holder.Add((m1 - 1) / m1);


				}






			}












		}
	}
}
