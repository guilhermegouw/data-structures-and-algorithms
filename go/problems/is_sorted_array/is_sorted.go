/*
Write a function that determines if the array is sorted
in ascending order.

input:
[]int{1, 3, 5, 6, 7}
output:
True

input:
[]int{1, 2, 5, 4, 6}
output:
False
*/
package is_sorted_array

func IsSorted(arr []int) bool {
	for i := 0; i < len(arr)-1; i++ {
		current := arr[i]
		next := arr[i+1]
		if current > next {
			return false
		}
	}
	return true
}
