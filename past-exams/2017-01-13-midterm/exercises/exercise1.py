import unittest


def swap(A, x, y):
    """
        In the array A, swaps the elements at indeces x and y.
    """
    raise Exception("TODO IMPLEMENT ME!")

def pivot(A, first, last):
    """ Modifies in-place the slice of the array A with indeces between first included
        and last included. Returns the new pivot index.
        
    """
    raise Exception("TODO IMPLEMENT ME!")
    
def quicksort(A, first, last):
    """
        Sorts in-place the slice of the array A with indeces between first included
        and last included.
    """
    raise Exception("TODO IMPLEMENT ME!")


def qs(A):
    """
        Sorts in-place the array A by calling quicksort function on the full array.
    """
    raise Exception("TODO IMPLEMENT ME!")


class PivotTest(unittest.TestCase):
    """ Test cases only for pivot function

    """    


    def test_pivot_zero(self):
        with self.assertRaises(Exception):
            pivot([],0,0)

    def test_pivot_one(self):        
        self.assertEqual(0, pivot([3],0,0))

    def test_pivot_two_already_ordered(self):
        self.assertEqual(0, pivot([6, 7],0,1))

    def test_pivot_two_not_ordered(self):
        self.assertEqual(1, pivot([7, 6],0,1))

    def test_pivot_three_not_ordered(self):
        self.assertEqual(1, pivot([7, 6,8],0,1))
        

class QuicksortTest(unittest.TestCase):
    """ Test cases for qs function

    """    
            
    def test_zero_elements(self):
        v = []
        qs(v)
        self.assertEqual(v,[])     
        
    def test_return_none(self):    
        self.assertEquals(None, qs([2]))        
        
    def test_one_element(self):
        v = ["a"]
        qs(v)
        self.assertEqual(v,["a"])     
        

    def test_two_elements(self):
        v = [2,1]
        qs(v)
        self.assertEqual(v,[1,2])  
        
    def test_three_elements(self):
        v = [2,1,3]
        qs(v)
        self.assertEqual(v,[1,2,3])
    
    def test_piccinno_list(self):        
        v = [23, 34, 55, 32, 7777, 98, 3, 2, 1]        
        qs(v)
        vcopy = v[:]
        vcopy.sort()
        self.assertEqual(v, vcopy)      
    
#unittest.main()    