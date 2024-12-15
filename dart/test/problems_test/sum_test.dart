import 'package:test/test.dart';
import '../../lib/problems/sum.dart';

void main() {
  group('Sum function', () {
    test('should return 3 when adding 1 and 2', () {
      expect(sum(1, 2), equals(3));
    });
    test('should return 0 when adding 0 and 0', () {
      expect(sum(0, 0), equals(0));
    });
  });
}
