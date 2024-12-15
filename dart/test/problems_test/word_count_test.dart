import 'package:test/test.dart';
import '../../lib/problems/word_count.dart';

void main() {
  group('Word count function', () {
    test('should return 0 when sentence equals ""', () {
      expect(wordCount(""), equals(0));
    });
    test('should return 1 when sentence has one word no spaces "Dart"', () {
      expect(wordCount("Dart"), equals(1));
    });
  });
}
