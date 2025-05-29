// codewars https://www.codewars.com/kata/54b42f9314d9229fd6000d9c/train/go problem

package kata

import "strings"

func DuplicateEncode(word string) string {
	stringParts := strings.Split(strings.ToUpper(word), "")
	stringResult := ""

	for i := 0; i < len(stringParts); i++ {
		counter := 0

		for j := 0; j < len(stringParts); j++ {
			if stringParts[i] == stringParts[j] {
				counter += 1
			}
			if counter >= 2 {
				break
			}
		}
		if counter > 1 {
			stringResult += ")"
		} else {
			stringResult += "("
		}
	}
	return stringResult
}
