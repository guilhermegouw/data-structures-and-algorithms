package is_sorted_array

import "testing"

func TestIsSorted(t *testing.T) {
	cases := []struct {
		input    []int
		expected bool
	}{
		{[]int{1}, true},
		{[]int{1, 2}, true},
		{[]int{3, 2}, false},
		{[]int{1, 3, 2}, false},
	}
	for _, c := range cases {
		result := IsSorted(c.input)
		if result != c.expected {
			t.Errorf(
				"For input %v, expected: %v, got: %v",
				c.input, c.expected, result,
			)
		}
	}
}
