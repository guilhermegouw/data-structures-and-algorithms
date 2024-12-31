package remove_duplicates

import (
	"reflect"
	"testing"
)

func TestRemoveDuplicates(t *testing.T) {
	cases := []struct {
		input    []int
		expected []int
	}{
		{[]int{1}, []int{1}},
		{[]int{1, 2}, []int{1, 2}},
		{[]int{1, 2, 2}, []int{1, 2}},
		{[]int{1, 2, 2, 3}, []int{1, 2, 3}},
		{[]int{1, 2, 2, 3, 3}, []int{1, 2, 3}},
		{[]int{1, 2, 2, 3, 3, 4}, []int{1, 2, 3, 4}},
	}
	for _, c := range cases {
		result := RemoveDuplicates(c.input)
		if !reflect.DeepEqual(result, c.expected) {
			t.Errorf(
				"For input %v, expected: %v, got %v",
				c.input, c.expected, result,
			)
		}
	}
}
