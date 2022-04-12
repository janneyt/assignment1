import unittest
import assignment1 as sa1
import big_o
from static_array import StaticArray

class MyTestCase ( unittest.TestCase ):
    def test_min_max(self):
        arr = StaticArray ( 5 )
        for i, value in enumerate ( [7, 8, 6, -5, 4] ):
            arr[i] = value

        arr1 = StaticArray(2)
        for i, value in enumerate ([1,2]):
            arr1[i] = value

        arr_single_value = StaticArray(1)
        for i, value in enumerate([1]):
            arr_single_value[i] = value
        self.assertEqual(sa1.min_max(arr1),tuple((1,2)))
        self.assertEqual(sa1.min_max(arr_single_value), tuple((1,1)))
        self.assertEqual(sa1.min_max(arr), tuple((-5,8)))

    def test_fizz_buzz(self):
        self.assertEqual(sa1.fizz_buzz([3,5,15,1]),["fizz","buzz","fizzbuzz",1])

if __name__ == '__main__':
    unittest.main ()
