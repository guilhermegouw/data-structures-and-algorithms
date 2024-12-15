import 'package:test/test.dart';
import '../../lib/problems/occupied_spaces.dart';

void main() {
  group('Get Occupied Spaces Both Days', () {
    test('No spaces occupied today or yesterday', () {
      expect(get_occupied_spaces_both_days(1, '.', '.'), 0);
    });
    test('One space occupied yesterday none today', () {
      expect(get_occupied_spaces_both_days(1, 'C', '.'), 0);
    });
    test('One space occupied yesterday one today', () {
      expect(get_occupied_spaces_both_days(1, 'C', 'C'), 1);
    });
    test('Two spaces one space occupied yesterday one today', () {
      expect(get_occupied_spaces_both_days(1, 'C.', 'C.'), 1);
    });
    test(
        'Two spaces one space occupied yesterday one today different positions',
        () {
      expect(get_occupied_spaces_both_days(1, '.C', 'C.'), 0);
    });
    test('Two spaces occupied yesterday and today', () {
      expect(get_occupied_spaces_both_days(2, 'CC', 'CC'), 2);
    });
  });
}
