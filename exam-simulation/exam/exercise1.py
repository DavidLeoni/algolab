import unittest

def insertion_sort(A):
    """ Sorts in-place list A with insertion sort.  """
                                         
    for i in range(1, len(A)):                
        temp = A[i]                       
        j = i                             
        while j > 1 and A[j-1] > temp:    
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
            
    def test_elements(self):
        v = [1,3,2]
        insertion_sort(v)
        self.assertEqual(v,[1,2,3])