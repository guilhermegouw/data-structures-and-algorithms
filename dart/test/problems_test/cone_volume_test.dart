import 'package:test/test.dart';
import '../../lib/problems/cone_volume.dart';

void main() {
  group('Tests for getConeVolume', () {
    test('should return aprox: 12.57 when r = 2 and h = 3', () {
      expect(getConeVolume(2, 3), closeTo(12.57, 0.01));
    });
  });
}
