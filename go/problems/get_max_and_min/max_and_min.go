/*
Write a function to find the largest and smallest elements
in an array.

input:
[]{1, 2, 3, 4, 5}

output:
{5, 1}
*/
package get_max_and_min

func GetMaxAndMin(arr []int) (int, int) {
	if len(arr) == 0 {
		return 0, 0
	}
	highest := arr[0]
	lowest := arr[0]

	for _, item := range arr {
		if item > highest {
			highest = item
		}
		if item < lowest {
			lowest = item
		}
	}
	return highest, lowest
}
