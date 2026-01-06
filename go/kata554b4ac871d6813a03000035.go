package kata

import (
	"fmt"
	"strconv"
	"strings"
)

func HighAndLow(in string) string {
	numbers := strings.Split(in, " ")
	first_number, err := strconv.ParseInt(numbers[0], 10, 32)

	if err != nil {
		return ""
	}

	first_number_in_int := int(first_number)
	max := first_number_in_int
	min := first_number_in_int

	for _, number := range numbers {
		number_serialized, err := strconv.ParseInt(number, 10, 32)

		if err != nil {
			return ""
		}

		number_in_int := int(number_serialized)

		if number_in_int > max {
			max = number_in_int
		}

		if number_in_int < min {
			min = number_in_int
		}
	}

	result := fmt.Sprintf("%d %d", max, min)

	return result
}
