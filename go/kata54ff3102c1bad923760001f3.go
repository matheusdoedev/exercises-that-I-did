package kata

import (
    "strings"
)

func GetCount(str string) (count int) {
	count = 0

	for _, c := range strings.Split(str, "") {
		if c == "a" || c == "e"|| c == "i" || c == "o" || c == "u" {
			count += 1
		}
	}

  return count
}