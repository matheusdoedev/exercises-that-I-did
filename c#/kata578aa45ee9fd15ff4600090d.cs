// kata 578aa45ee9fd15ff4600090d codewars -> https://www.codewars.com/kata/578aa45ee9fd15ff4600090d/train/csharp

using System;

public class Kata
{
	public static int[] SortArray(int[] array)
	{
		return BubbleSort(array);
	}

	public static int[] BubbleSort(int[] numbers)
	{
		int x = 0;
		int y = 1;

		while (x < numbers.Length)
		{
			while (y < numbers.Length)
			{
				bool isNumbersOdd = IsOdd(numbers[x]) && IsOdd(numbers[y]);
				bool isFirstNumberBiggerThanSecond = numbers[x] > numbers[y];

				if (isNumbersOdd && isFirstNumberBiggerThanSecond)
				{
					(numbers[x], numbers[y]) = (numbers[y], numbers[x]);
				}
        y += 1;
			}
      
			x += 1;
      y = x + 1;
		}
    
    

		return numbers;
	}

	public static bool IsOdd(int number)
	{
		return number % 2 != 0;
	}
}