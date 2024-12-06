// kata 5168bb5dfe9a00b126000018 codewars -> https://www.codewars.com/kata/5168bb5dfe9a00b126000018/train/csharp

using System;

public static class Kata
{
	public static string Solution(string str)
	{
		return ReverseString(str);
	}

	public static string ReverseString(string input)
	{
		string reversedString = "";
		char[] inputString = input.ToCharArray();

		for (int count = input.Length - 1; count >= 0; count--)
		{
			Console.WriteLine(count);
			reversedString = reversedString + inputString[count];
		}

		return reversedString;
	}
}