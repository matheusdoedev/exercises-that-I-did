package kata

import "strings"

func DNAStrand(dna string) string {
	dna_parts := strings.Split(dna, "")
	result := ""

	for _, part := range dna_parts {
		if part == "T" {
			result = result + "A"
		} else if part == "A" {
			result = result + "T"
		} else if part == "G" {
			result = result + "C"
		} else if part == "C" {
			result = result + "G"
		}
	}

	return result
}
