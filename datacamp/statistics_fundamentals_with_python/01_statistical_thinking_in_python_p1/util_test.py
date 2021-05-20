import unittest   # The test framework
import util
import numpy as np
from numpy.testing.utils import assert_array_equal

class Test_Util(unittest.TestCase): 
    def test_return_input_as_x(self): 
        a = [1, 1, 2, 2, 3, 3, 7, 8, 9, 10]
        x, y = util.ecdf(a)
        assert_array_equal(x, np.array(a))

    def test_return_length_of_x(self): 
        a = [1, 1, 2, 2, 3, 3, 7, 8, 9, 10]
        x, y = util.ecdf(a)
        self.assertEqual(len(y), len(a))

    def test_return_10_y_values(self): 
        a = [1, 1, 2, 2, 3, 3, 7, 8, 9, 10]
        x, y = util.ecdf(a)
        assert_array_equal(y, np.array([0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]))

    def test_return_3_y_values(self): 
        a = [1, 1, 2]
        x, y = util.ecdf(a)
        expected_y = np.array([0.333, 0.666, 0.999])
        for i in range(len(a)): 
            self.assertAlmostEqual(y[i], expected_y[i], places=2)

if __name__ == '__main__':
    unittest.main()
