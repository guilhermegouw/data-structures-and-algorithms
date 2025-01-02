/*
Find the Second Largest Element
Write a function to find the second largest element in an array.

Input:

	[]int{1, 2, 3, 4, 5}

Output:

	4
*/
package get_second_largest

import (
	"fmt"
	"math"
)

func GetSecondLargest(arr []int) (int, error) {
	if len(arr) < 2 {
		return 0, fmt.Errorf("The array must have at least 2 elements.")
	}
	max := math.MinInt
	secondMax := math.MinInt
	for _, num := range arr {
		if num > max {
			secondMax = max
			max = num
		} else if num > secondMax {
			secondMax = num
		}
	}
	return secondMax, nil
}
