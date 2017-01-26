import unittest


class SwapArray:
    """ A sequence of elements that can only be modified by swapping one element 
        with the successisarre one.
    """
    
    def __init__(self, python_list):
        """ Initializes the SwapArray with the elements found in python_list. """
        
        self._arr = python_list[:]  # we store a _copy_ of the array
        
    def swap_next(self, i):
        """ Swaps the elements at indeces i and i + 1
        
            If index is negative or greater or equal of the last index, raises 
            an IndexError
        
        """
        if i < 0 or i >= len(self._arr) - 1:
            raise IndexError("Wrong index: " + str(i) )

        tmp = self._arr[i]
        self._arr[i] = self._arr[i + 1]
        self._arr[i + 1] = tmp

    def size(self):
        """ Returns the size of the SwapArray """
        return len(self._arr)
        
    def get(self, i):
        """ Returns the element at index i.
        
            If index is outside the bounds of the array, raises an IndexError        
        """
        return self._arr[i]
        
    def get_last(self):
        """ Returns the last element of the array
                    
            If array is empty, raises an IndexError                            
        """
        
        return self._arr[-1]
    
    def __str__(self):
        return "SwapArray: " + str(self._arr)
        
def is_sorted(sarr):  
    """ Returns True if the provided SwapArray sarr is sorted, False otherwise
    
        NOTE: Here you are a user of SwapArray, so you *MUST NOT* access
              directly the field _arr.
    """
    raise Exception("TODO IMPLEMENT ME !")
        
def max_to_right(sarr):
    """ Modifies the provided SwapArray sarr so that its biggest element is
        moved to the last index. The order in which the other elements will be
        after a call to this function is left unspecified (so it could be any).
        
        NOTE: Here you are a user of SwapArray, so you *MUST NOT* access
              directly the field _arr. To do changes, you can only use 
              the method swap(self, i).   
        NOTE: does *not* return anything!               
    """
    raise Exception("TODO IMPLEMENT ME !")

class SwapTest(unittest.TestCase):

    def test_zero_element(self):
        sarr = SwapArray([]);
        with self.assertRaises(IndexError):
            sarr.swap_next( 0)
        with self.assertRaises(IndexError):
            sarr.swap_next(1)
        with self.assertRaises(IndexError):
            sarr.swap_next(-1)

    
    def test_one_element(self):
        sarr = SwapArray(['a']);
        with self.assertRaises(IndexError):
            sarr.swap_next(0)
        

    def test_two_elements(self):
        sarr = SwapArray(['a','b']);
        sarr.swap_next(0)
        self.assertEqual(sarr._arr, ['b','a'])
        
    def test_return_none(self):
        sarr = SwapArray(['a','b', 'c', 'd']);
        self.assertEquals(None, sarr.swap_next(1))
                
    def test_long_list(self):
        sarr = SwapArray(['a','b', 'c', 'd']);
        sarr.swap_next(1)
        self.assertEqual(sarr._arr, ['a', 'c','b', 'd'])
        

class IsSortedTest(unittest.TestCase):
    
    def test_is_sorted_empty(self):
        self.assertTrue(is_sorted(SwapArray([])))

    def test_is_sorted_one(self):
        self.assertTrue(is_sorted(SwapArray([6])))

    def test_is_sorted_two(self):
        self.assertTrue(is_sorted(SwapArray([7,7])))
        self.assertTrue(is_sorted(SwapArray([6,7])))
        self.assertFalse(is_sorted(SwapArray([7,6])))    

    def test_is_sorted_three(self):
        self.assertTrue(is_sorted(SwapArray([6,7,8])))
        self.assertFalse(is_sorted(SwapArray([8,8,7])))


class MaxToRightTest(unittest.TestCase):
    
    def test_max_to_right_empty(self):        
        sarr = SwapArray([])
        max_to_right(sarr)
        self.assertEqual(sarr._arr, [])

    def test_max_to_right_return_none(self):        
        sarr = SwapArray([])
        self.assertEqual(None, max_to_right(sarr))


    def test_right_max_to_right_1(self):        
        
        sarr = SwapArray([5])
        max_to_right(sarr)
        self.assertEqual(5, sarr.get(0))

    def test_right_max_to_right_2_first(self):        
        sarr = SwapArray([7, 6])
        max_to_right(sarr)
        self.assertEqual(sarr.get(0), 6)
        self.assertEqual(sarr.get(1), 7)

    def test_right_max_to_right_2_last(self):        
        sarr = SwapArray([6,7])
        max_to_right(sarr)
        self.assertEqual(sarr.get_last(), 7)
        
    def test_right_max_to_right_3_first(self):        
        sarr = SwapArray([8,6, 7])
        max_to_right(sarr)
        self.assertEqual(sarr.get(2), 8)

    def test_right_max_to_right_3_middle(self):        
        sarr = SwapArray([7, 8, 6])
        max_to_right(sarr)
        self.assertEqual(sarr.get(2), 8)

    def test_right_max_to_right_3_last(self):        
        sarr = SwapArray([7, 6, 8])
        max_to_right(sarr)
        self.assertEqual(sarr.get(2), 8)
        

#unittest.main()            