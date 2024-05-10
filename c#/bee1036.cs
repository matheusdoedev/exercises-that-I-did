using System;

class URI
{

	static void Main(string[] args)
	{

		string[] numbers = Console.ReadLine().Split(' ');
		float A = float.Parse(numbers[0]);
		float B = float.Parse(numbers[1]);
		float C = float.Parse(numbers[2]);

		float AMultipleByTwo = 2 * A;

		if (AMultipleByTwo == 0)
		{
			Console.WriteLine("Impossivel calcular");
		}

		float Delta = CalculateBaskhara(A, B, C);

		if (Delta < 0)
		{
			Console.WriteLine("Impossivel calcular");
		}

		float DeltaSqrtRoots = (float)Math.Sqrt(Delta);
		float r1 = (-B + DeltaSqrtRoots) / AMultipleByTwo;
		float r2 = (-B - DeltaSqrtRoots) / AMultipleByTwo;

		Console.WriteLine("R1 = " + r1.ToString("0.00000"));
		Console.WriteLine("R2 = " + r2.ToString("0.00000"));

	}

	static float CalculateBaskhara(float A, float B, float C)
	{
		return (B * B) - 4 * A * C;
	}

}