/*
The equilibrium index in an array is an index where the sum of the elements
to the left of the index is equal to the sum of the elements to the right of the index.
If there is no such index, return []

Example:
Input: A = [-7, 1, 5, 2, -4, 3, 0]
Output: [3, 6]
Explanation:

At index 3, left sum is (-7 + 1 + 5) = -1 and right sum is (-4 + 3 + 0) = -1.
At index 6, left sum is (-7 + 1 + 5 + 2 - 4 + 3) = 0 and right sum is 0.
Input: A = [1, 2, 3]
Output: -1 (no equilibrium index)
*/
package equilibrium_indexes_array

func Sum(arr []int) int {
	sum := 0
	for _, num := range arr {
		sum += num
	}
	return sum
}

func FindEquilibriumIndexes(arr []int) []int {
	equilibrium_indexes_array := []int{}
	totalSum := Sum(arr)
	leftSum := 0
	for i, num := range arr {
		rightSum := totalSum - leftSum - num
		if leftSum == rightSum {
			equilibrium_indexes_array = append(equilibrium_indexes_array, i)
		}
		leftSum += num
	}
	return equilibrium_indexes_array
}
