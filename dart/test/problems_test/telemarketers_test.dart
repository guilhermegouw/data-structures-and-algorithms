import 'package:test/test.dart';
import '../../lib/problems/telemarketers.dart';

void main() {
  group('Is telemarketers tests', () {
    test('First digit not 8 or 9', () {
      expect(isTelemarketer(1, 2, 3, 4), equals("answer"));
    });
    test('First digit is 8 but second and third are not equal', () {
      expect(isTelemarketer(8, 2, 3, 4), equals("answer"));
    });
    test('First digit is 8 second and third are equal but fourth not 8 or 9',
        () {
      expect(isTelemarketer(8, 2, 2, 4), equals("answer"));
    });
    test('First digit is 8 second and third are equal and fourth is 8', () {
      expect(isTelemarketer(8, 2, 2, 8), equals("ignore"));
    });
  });
  group('Exception tests', () {
    test('Digit out of range throws ArgumentError', () {
      expect(() => isTelemarketer(10, 2, 3, 4), throwsA(isA<ArgumentError>()));
    });
    test('Negative digit throws ArgumentError', () {
      expect(() => isTelemarketer(-1, 2, 3, 4), throwsA(isA<ArgumentError>()));
    });
  });
}
