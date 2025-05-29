// codewars https://www.codewars.com/kata/5a00e05cc374cb34d100000d/train/go problem

package kata

func ReverseSeq(n int) []int {
	numbers := make([]int, n)

	for i := n; i > 0; i-- {
		numbers[n - i] = i
	}

	return numbers
}
