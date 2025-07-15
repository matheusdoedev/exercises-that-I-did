package kata

import (
	"strconv"
	"strings"
)

func High(s string) string {
	highest_char := ""
	highest_score := 0

	for _, char := range strings.Split(s, "") {
		char_int, err := strconv.Atoi(char)

		if err != nil {
			panic(err)
		}

		char_score := char_int - 65 + 1

		if char_score > highest_score {
			highest_char = char
		}
	}

	return highest_char
}
