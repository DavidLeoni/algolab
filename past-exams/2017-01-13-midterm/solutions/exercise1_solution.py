import unittest


def swap(A, x, y):
    """
        In the array A, swaps the elements at indeces x and y.
    """
    tmp = A[x]
    A[x] = A[y]
    A[y] = tmp

def pivot(A, first, last):
    """ Modifies in-place the slice of the array A with indeces between first included
        and last included. Returns the new pivot index.
        
    """
    p = A[first]
    j = first
    for i in range(first + 1, last + 1):
        if A[i] < p:
            j += 1
            swap(A, i, j)
    A[first] = A[j]
    A[j] = p
    return j
    
def quicksort(A, first, last):
    """
        Sorts in-place the slice of the array A with indeces between first included
        and last included.
    """
    if first < last:
        j = pivot(A, first, last)
        quicksort(A, first, j - 1)
        quicksort(A, j + 1, last)


def qs(A):
    """
        Sorts in-place the array A by calling quicksort function on the full array.
    """
    if len(A) > 0:
        quicksort(A, 0, len(A) - 1)

class SwapTest(unittest.TestCase):
   
    def test_one_element(self):
        v = ['a'];
        swap(v,0,0)
        self.assertEqual(v, ['a'])

    def test_two_elements(self):
        v = ['a','b'];
        swap(v,0,1)
        self.assertEqual(v, ['b','a'])
        
    def test_return_none(self):
        v = ['a','b', 'c', 'd'];
        self.assertEquals(None, swap(v,1,3))        
        
    def test_long_list(self):
        v = ['a','b', 'c', 'd'];
        swap(v,1,3)
        self.assertEqual(v, ['a', 'd','c', 'b'])
        
        
    def test_swap_property(self):
        v = ['a','b','c','d'];
        w = ['a','b','c','d'];
        swap(v,1,3)
        swap(w,3,1)
        self.assertEqual(v, w)

    def test_double_swap(self):
        v = ['a','b','c','d'];        
        swap(v,1,3)
        swap(v,1,3)
        self.assertEqual(v, ['a','b','c','d'])

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