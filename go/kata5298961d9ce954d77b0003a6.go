package kata

func Range(start int, end int, step int) []int {
	result := []int{}

	if start == 0 {

	}
	if end < start {
		return result
	}

	for i := start; i < end; i = i + step {
		result = append(result, i)
	}
	return result
}
