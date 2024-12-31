package reverse_array_in_place

import (
	"reflect"
	"testing"
)

func TestReverseArray(t *testing.T) {
	cases := []struct {
		input    []int
		expected []int
	}{
		{[]int{1}, []int{1}},
		{[]int{1, 2}, []int{2, 1}},
		{[]int{1, 2, 3}, []int{3, 2, 1}},
	}
	for _, c := range cases {
		result := ReverseArray(c.input)
		if !reflect.DeepEqual(result, c.expected) {
			t.Errorf(
				"For input %v, expected: %v, got: %v",
				c.input,
				c.expected,
				result,
			)
		}
	}
}
