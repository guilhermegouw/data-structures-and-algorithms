import 'package:test/test.dart';
import '../../lib/problems/three_cups.dart';

void main() {
  group('Three cups function', () {
    test('One swap type A', () {
      expect(threeCups('A'), equals('middle'));
    });
    test('One swap type B', () {
      expect(threeCups('B'), equals('left'));
    });
    test('One swap type C', () {
      expect(threeCups('C'), equals('right'));
    });
    test('Two swaps AA', () {
      expect(threeCups('AA'), equals('left'));
    });
    test('Two swaps AB', () {
      expect(threeCups('AB'), equals('right'));
    });
    test('Two swaps AC', () {
      expect(threeCups('AC'), equals('middle'));
    });
    test('Two swaps BA', () {
      expect(threeCups('BA'), equals('middle'));
    });
    test('Two swaps BB', () {
      expect(threeCups('BB'), equals('left'));
    });
    test('Two swaps BC', () {
      expect(threeCups('BC'), equals('right'));
    });
    test('Two swaps CA', () {
      expect(threeCups('CA'), equals('right'));
    });
    test('Two swaps CB', () {
      expect(threeCups('CB'), equals('middle'));
    });
    test('Two swaps CC', () {
      expect(threeCups('CC'), equals('left'));
    });
  });
}

