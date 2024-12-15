import 'package:test/test.dart';
import '../../lib/problems/winning_team.dart';

void main() {
  group('Winning team Group', () {
    test('None of the teams score, output should be "T"', () {
      expect(getWinningTeam([0, 0, 0], [0, 0, 0]), equals("T"));
    });
    test('Apples win with one three-point shot, output should be "A"', () {
      expect(getWinningTeam([0, 0, 0], [1, 0, 0]), equals("A"));
    });

    test('Bananas win with one two-point shot, output should be "B"', () {
      expect(getWinningTeam([0, 1, 0], [0, 0, 0]), equals("B"));
    });

    test('Apples win with combined scores, output should be "A"', () {
      expect(getWinningTeam([1, 2, 3], [3, 2, 1]), equals("A"));
    });

    test('Bananas win with combined scores, output should be "B"', () {
      expect(getWinningTeam([3, 2, 1], [1, 2, 3]), equals("B"));
    });
  });
}
