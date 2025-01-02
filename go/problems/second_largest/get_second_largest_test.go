package get_second_largest

import "testing"

func TestGetSecondLargest(t *testing.T) {
	cases := []struct {
		input       []int
		expected    int
		expectError bool
	}{
		{[]int{1}, 0, true},
		{[]int{1, 2}, 1, false},
		{[]int{2, 2}, 2, false},
		{[]int{1, 2, 3}, 2, false},
		{[]int{4, 1, 2, 3}, 3, false},
		{[]int{-1, 4, 1, 2, 3}, 3, false},
		{[]int{-6, -1, 4, 1, 2, 3}, 3, false},
	}
	for _, c := range cases {
		result, err := GetSecondLargest(c.input)
		if c.expectError {
			if err == nil {
				t.Errorf("Expected an error for input %v but got none", c.input)
			}
			continue
		}
		if err != nil {
			t.Errorf("Unexpected error for input %v: %v", c.input, err)
		}
		if result != c.expected {
			t.Errorf("For input %v, expected: %v, got: %v", c.input, c.expected, result)
		}
	}
}
