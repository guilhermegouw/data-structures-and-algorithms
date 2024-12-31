/*
Remove Duplicates from Sorted Array
Return a new array with duplicates removed, preserving order.

Input:
[]{1, 2, 2, 3, 3, 3, 4, 4, 4}

Output:
[]{1, 2, 3, 4}
*/

package remove_duplicates

// in-place
// func RemoveDuplicates(arr []int) []int {
// 	writeIndex := 1
// 	for i := 1; i < len(arr); i++ {
// 		if arr[i] != arr[writeIndex-1] {
// 			arr[writeIndex] = arr[i]
// 			writeIndex += 1
// 		}
// 	}
// 	return arr[:writeIndex]
// }

func RemoveDuplicates(arr []int) []int {
	seen := make(map[int]bool)
	result := []int{}

	for _, val := range arr {
		if !seen[val] {
			seen[val] = true
			result = append(result, val)
		}
	}
	return result
}
