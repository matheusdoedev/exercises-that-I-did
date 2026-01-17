package kata

import "strings"

func Solution(str string) []string {
	caracters := strings.Split(str, "") // split string
	result := []string{}                // declare result array to append all two caracters combination
	current_combination := ""           // declare combination array (or string to append)
	last_caracter_index := len(caracters) - 1

	// iterate over characters
	for i, char := range caracters {
		current_combination = current_combination + char
		// if is the last character in array, look if combination is empty
		if i == last_caracter_index && len(current_combination) == 1 {
			// if is, add the caracter to combination plus the _
			current_combination = current_combination + "_"
			result = append(result, current_combination)
			current_combination = ""
			continue
		}
		// if index is odd
		if i%2 != 0 {
			// append to result array and then reset combination array
			result = append(result, current_combination)
			current_combination = ""
		}
	}
	return result
}
