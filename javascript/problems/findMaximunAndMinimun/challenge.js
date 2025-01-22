/**
Write a function to find the largest and smallest elements in an array.

input:
[1, 2, 3, 4, 5]

output:
(5, 1)
*/
function getLargestAndSmallest(arr) {
  let smallest = Number.MAX_SAFE_INTEGER
  let largest = Number.MIN_SAFE_INTEGER
  for (let i = 0; i < arr.length; i++) {
    if (arr[i] > largest) {
      largest = arr[i];
    } if (arr[i] < smallest) {
      smallest = arr[i]
    }
  }
  return [largest, smallest]
}

module.exports = getLargestAndSmallest;
