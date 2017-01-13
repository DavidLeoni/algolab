import unittest

def insertion_sort(A):
    """ Sorts in-place list A with insertion sort.  """
                                         
    for i in range(1, len(A)):                
        temp = A[i]                       
        j = i                             
        while j > 0 and A[j-1] > temp:    
            A[j] = A[j-1]                  
            j -= 1                         
        A[j] = temp                           
    

class InsertionSortTest(unittest.TestCase):
   
    def test_zero_elements(self):
        v = []
        insertion_sort(v)
        self.assertEqual(v,[])     
        
    def test_return_none(self):    
        self.assertEquals(None, insertion_sort([2]))        
        
    def test_one_element(self):
        v = ["a"]
        insertion_sort(v)
        self.assertEqual(v,["a"])     
                
    def test_three_elements(self):
        v = [1,3,2]
        insertion_sort(v)
        self.assertEqual(v,[1,2,3])

    def test_two_elements(self):
        v = [2,1]
        insertion_sort(v)
        self.assertEqual(v,[1,2])  
        
    def test_piccinno_list(self):        
        v = [23, 34, 55, 32, 7777, 98, 3, 2, 1]        
        insertion_sort(v)
        vcopy = v[:]
        vcopy.sort()
        self.assertEqual(v, vcopy) 