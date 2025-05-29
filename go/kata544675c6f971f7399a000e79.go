// codewars https://www.codewars.com/kata/544675c6f971f7399a000e79/train/go problem
package kata

import (
	"strconv"
)

func StringToNumber(str string) int {
	result, err := strconv.ParseInt(str, 10, 32)

	if (err != nil) {
		return 0
	}

	number := int(result)

	return number
}