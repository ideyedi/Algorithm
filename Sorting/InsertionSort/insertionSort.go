package main

import (
	"fmt"
)

func insertion(arr []int) {
	for j := 1; j < len(arr); j++ {
		key := arr[j]
		i := j - 1

		for i >= 0 && arr[i] > key {
			arr[i+1] = arr[i]
			i--
		}
		arr[i+1] = key
	}
}

func main() {
	arr := []int{5, 2, 4, 6, 1, 3}
	fmt.Println("Before arr : ", arr)

	insertion(arr)
	fmt.Println("result : ", arr)
}
