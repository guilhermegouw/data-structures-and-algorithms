const getLargestAndSmallest = require('./challenge');

test('smallest and largest are the same when array lenght equals 1', () => {
  expect(getLargestAndSmallest([1])).toBe([1, 1]);
});
