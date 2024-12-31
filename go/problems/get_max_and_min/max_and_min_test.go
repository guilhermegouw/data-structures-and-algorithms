package get_max_and_min

import (
	"testing"
)

func TestFindEquilibriumIndexes(t *testing.T) {
	cases := []struct {
		input       []int
		expectedMax int
		expectedMin int
	}{
		{[]int{-7, 1, 5, 2, -4, 3, 0}, 5, -7},
	}
	for _, c := range cases {
		resultMax, resultMin := GetMaxAndMin(c.input)
		if resultMax != c.expectedMax || resultMin != c.expectedMin {
			t.Errorf(
				"For input %v, expected (max, min): (%v, %v), got: (%v, %v)",
				c.input,
				c.expectedMax,
				c.expectedMin,
				resultMax,
				resultMin,
			)
		}
	}
}
