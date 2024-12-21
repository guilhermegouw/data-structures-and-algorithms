package equilibrium_indexes_array

import (
	"reflect"
	"testing"
)

func TestFindEquilibriumIndexes(t *testing.T) {
	cases := []struct {
		input    []int
		expected []int
	}{
		{[]int{-7, 1, 5, 2, -4, 3, 0}, []int{3, 6}},
		{[]int{1, 2, 3}, []int{}},
	}
	for _, c := range cases {
		result := FindEquilibriumIndexes(c.input)
		if !reflect.DeepEqual(result, c.expected) {
			t.Errorf("Expected: %v Got: %v", result, c.expected)
		}
	}
}
