import 'package:test/test.dart';
import '../../lib/problems/hello_world.dart';

void main() {
  group('Hello function', () {
    test('should return "Hello, World!"', () {
      expect(hello(), equals("Hello, World!"));
    });
  });
}
