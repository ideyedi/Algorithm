package main

import (
	"fmt"
)

func mergeAlternately(word1 string, word2 string) string {
	var answer string = ""
	var index int = 0

	for {
		if len(word1) == index {
			answer += string(word2[index:])
			break
		} else if len(word2) == index {
			answer += string(word1[index:])
			break
		} else {
			fmt.Println(word1[index] + word2[index])
			answer += string(word1[index]) + string(word2[index])
		}
		index += 1
	}
	return answer
}

func main() {
	fmt.Println(mergeAlternately("ab", "qwe"))
}
