// codewars https://www.codewars.com/kata/5a00e05cc374cb34d100000d/train/go problem

package kata

import (
    "math"
)

func SquareSum(numbers []int) int {
    result := 0

	for _, v := range numbers {
        result += int(math.Pow(float64(v), 2))
    }

    return result
}