/*
Write a function that reverses an array in place.

Input:
[]int{1, 2, 3, 4, 5}

Output:
[]int{5, 4, 3, 2, 1}
*/
package reverse_array_in_place

func ReverseArray(arr []int) []int {
	left := 0
	right := len(arr) - 1
	for left < right {
		arr[left], arr[right] = arr[right], arr[left]
		left += 1
		right -= 1
	}
	return arr
}
