import 'package:test/test.dart';
import '../../lib/problems/data_plan.dart';


void main() {
    group('Get data available for next month', () {
    test('Zero months with no usage', () {
       expect(getAvailableData(10, 0, []), 10) ;
      }); 
     test('One month no usage', () {
       expect(getAvailableData(10, 1, [0]), 20) ;
      }); 
     test('One month with usage', () {
       expect(getAvailableData(10, 1, [5]), 15) ;
      }); 
     test('Two months with usage', () {
       expect(getAvailableData(10, 2, [5, 5]), 20) ;
      }); 
     test('Throws error for negative plan.', () {
       expect(() => getAvailableData(-10, 2, [5, 5]), throwsA(isA<ArgumentError>())) ;
      }); 
     test('Throws error for negative months.', () {
       expect(() => getAvailableData(10, -2, [5, 5]), throwsA(isA<ArgumentError>())) ;
      }); 
     test('Throws error for mismatch usage list length and months.', () {
       expect(() => getAvailableData(10, 2, [5, 5, 5]), throwsA(isA<ArgumentError>())) ;
      }); 
     test('Throws error for any negative value inside usage list.', () {
       expect(() => getAvailableData(10, 2, [-5, 5]), throwsA(isA<ArgumentError>())) ;
      }); 
    });
  }
