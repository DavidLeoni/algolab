import unittest

class SortedStack:
    """ A stack that only accepts integers, which must be pushed already sorted in 
        either ascending or descending order.
    """

    def __init__(self, ascending):
        """ Creates a SortedStack. Expects a boolean value to determine in which 
            sorting order the integers are going to be pushed. 
        
        Example:
        
        Ascending:       Descending
           
           8                 3
           5                 5
           3                 8
        
        """        
        self._elements = []
        self._ascending = ascending
        
    def size(self):
        return len(self._elements)
        
    def is_empty(self):
        return len(self._elements) == 0
        
    def pop(self):
        """ Removes the element at the top of the stack and returns it.
            
            If the stack is empty, raises an IndexError
        """
        if (len(self._elements) == 0):
            raise IndexError("Stack is empty!")
              
        return self._elements.pop()                
        
    def push(self, item):        
        """ Inserts an integer item in the stack
            
            If item is not an integer, or does not respect sorting order, raises a ValueError
        """
        
        if (type(item) is not int):
            raise ValueError("Invalid object! Expected an integer, found instead "  
            + str(item) + " of type " + str(type(item)))
       
        if len(self._elements) > 0:
            if self._ascending:
                if item < self._elements[-1]:
                    raise ValueError("Invalid object! Stack is with ascending order, but received number "
                    + str(item) + " which is less than last number: " + str(self._elements[-1])) 
            else:
                if item > self._elements[-1]:
                    raise ValueError("Invalid object! Stack is with descending order, but received number "  
                    + str(item) + " which is greater than last number: " + str(self._elements[-1]))         
        
        self._elements.append(item)
            
    def peek(self):
        """
            Returns the first element in the stack, without modifying the stack.        
        
            If stack is empty, raises an IndexError.
        """        
        
        if (len(self._elements) == 0):
            raise IndexError("Stack is empty!")            
        else:
            return self._elements[-1]

    def __str__(self):
        if    self._ascending :    
            asc = 'ascending'
        else:
            asc = 'descending'
        return "SortedStack (" + asc + "):  " + " elements=" + str(self._elements) 

    def ascending(self):
        """ Returns true if stack is ascending, false otherwise. """
        
        return self._ascending

def transfer(s):
    """ Takes as input a SortedStack s (either ascending or descending) and 
        returns a new SortedStack with the same elements of s, but in reverse order. 
        At the end of the call s will be empty.
        
        Example:
        
            s       result
            
            2         5
            3         3
            5         2
    """
    
    ret = SortedStack(not s.ascending())
    
    while s.size() > 0:
        num = s.pop()
        ret.push(num)
            
    return ret


def merge(s1,s2):
    """ Takes as input two SortedStacks having both ascending order, 
       and returns a new SortedStack sorted in descending order, which will be the sorted merge 
       of the two input stacks. MUST run in O(n1 + n2) time, where n1 and n2 are s1 and s2 sizes.
       
       If input stacks are not both ascending, raises ValueError.
       At the end of the call the input stacks will be empty.       
       
       Example:
       
       s1 (asc)   s2 (asc)      result (desc)
       
          5          7             2
          4          3             3
          2                        4
                                   5
                                   7
    
    """       
    
    if not (s1.ascending() and s2.ascending()):
        raise ValueError("Input stacks must be either both ascending! "
                         + "Found instead: s1: " + str(s1.ascending) + " and s2: " + str(s2.ascending) )

    ret = SortedStack(False)

    while s1.size() > 0 or s2.size() > 0:
        
        if s1.size() > 0:
            if s2.size() > 0:
                if s1.peek() > s2.peek():
                    e = s1.pop()
                else:
                    e = s2.pop()           
            else:
                e = s1.pop()
        else:
            e = s2.pop()
                
        ret.push(e)                         

    return ret    


class MergeTest(unittest.TestCase):
    
    def test_empty(self):
        s1 = SortedStack(True)
        s2 = SortedStack(True)

        m = merge(s1,s2)
        self.assertEqual(m.size(), 0)        
        
    def test_input_asc(self):
        """ Inputs must be ascending """
        
        with self.assertRaises(ValueError):
            merge(SortedStack(False),SortedStack(True))

        with self.assertRaises(ValueError):
            merge(SortedStack(True),SortedStack(False))

        with self.assertRaises(ValueError):
            merge(SortedStack(False),SortedStack(False))
            
        
    def test_1_empty(self):
        s1 = SortedStack(True)
        s2 = SortedStack(True)
        
        s1.push(1)
        m = merge(s1,s2)

        self.assertEqual(m.size(), 1)
        self.assertEqual(s1.size(), 0)
        self.assertEqual(s2.size(), 0)
        self.assertEqual(m.peek(), 1)

    def test_empty_1(self):
        s1 = SortedStack(True)
        s2 = SortedStack(True)
        
        s2.push(1)
        m = merge(s1,s2)
        self.assertEqual(m.size(), 1)
        self.assertEqual(s1.size(), 0)
        self.assertEqual(s2.size(), 0)
        self.assertEqual(m.peek(), 1)

    def test_1_2(self):
        s1 = SortedStack(True)
        s2 = SortedStack(True)
        
        s1.push(1)
        s2.push(2)
        m = merge(s1,s2)
        
        self.assertEqual(m.size(), 2)
        self.assertEqual(s1.size(), 0)
        self.assertEqual(s2.size(), 0)
        self.assertEqual(m.pop(), 1)
        self.assertEqual(m.pop(), 2)

    def test_2_1(self):
        s1 = SortedStack(True)
        s2 = SortedStack(True)
        
        s1.push(2)
        s2.push(1)
        m = merge(s1,s2)
        
        self.assertEqual(m.size(), 2)
        self.assertEqual(s1.size(), 0)
        self.assertEqual(s2.size(), 0)        
        self.assertEqual(m.pop(), 1)
        self.assertEqual(m.pop(), 2)


    def test_12_3(self):
        s1 = SortedStack(True)
        s2 = SortedStack(True)

        s1.push(1)
        s1.push(2)        
        s2.push(3)
        m = merge(s1,s2)
        self.assertEqual(m.size(), 3)
        self.assertEqual(s1.size(), 0)
        self.assertEqual(s2.size(), 0)
        self.assertEqual(m.pop(), 1)
        self.assertEqual(m.pop(), 2)
        self.assertEqual(m.pop(), 3)


    def test_3_12(self):
        s1 = SortedStack(True)
        s2 = SortedStack(True)

        s1.push(3)
        s2.push(1)        
        s2.push(2)
        m = merge(s1,s2)
        self.assertEqual(m.size(), 3)
        self.assertEqual(s1.size(), 0)
        self.assertEqual(s2.size(), 0)
        self.assertEqual(m.pop(), 1)
        self.assertEqual(m.pop(), 2)
        self.assertEqual(m.pop(), 3)
        
        
class TransferTest(unittest.TestCase):
    
    def test_empty(self):
        s1 = SortedStack(True)        
        s2 = transfer(s1)
        self.assertEquals(s2.size(), 0)                
            
    def test_one(self):
        s1 = SortedStack(True)
        s1.push(5)        
        s2 = transfer(s1)
        self.assertEquals(s2.size(), 1)
        self.assertEquals(s2.peek(), 5)
                

    def test_two_ascending(self):
        s1 = SortedStack(True)
        s1.push(5)        
        s1.push(6)        
        s2 = transfer(s1)
        self.assertEquals(s2.size(), 2)
        self.assertEquals(s2.ascending(), False)        
        self.assertEquals(s2.pop(), 5)
        self.assertEquals(s2.pop(), 6)


    def test_two_descending(self):
        s1 = SortedStack(False)
        s1.push(6)        
        s1.push(5)        
        s2 = transfer(s1)
        self.assertEquals(s2.size(), 2)
        self.assertEquals(s2.ascending(), True)        
        self.assertEquals(s2.pop(), 6)
        self.assertEquals(s2.pop(), 5)


class SortedStackTest(unittest.TestCase):
               
    def test_size(self):
        s = SortedStack(True)
        self.assertEqual(s.size(), 0)
        s.push(5)
        self.assertEqual(s.size(), 1)
        s.pop()
        self.assertEqual(s.size(), 0)

    
    def test_is_empty(self):
        s = SortedStack(True)
        self.assertTrue(s.is_empty())
        s.push(5)
        self.assertFalse(s.is_empty())

    def test_peek_empty(self):
        s = SortedStack(True)
        with self.assertRaises(IndexError):
            s.peek()

    def test_peek_one(self):
        s = SortedStack(True)        
        s.push(5)
        self.assertEqual(s.peek(), 5)
        self.assertEqual(s.peek(), 5)  # testing peek is not changing the stack
        self.assertEqual(s.size(), 1)     
        
    def test_pop_empty(self):
        s = SortedStack(True) 
        with self.assertRaises(IndexError):
            s.pop()
            
    def test_pop_one(self):
        s = SortedStack(True) 
        with self.assertRaises(IndexError):
            s.pop()
        s.push(5)        
        self.assertEqual(s.pop(), 5)
        self.assertEqual(s.size(), 0)
        
    def test_pop_two(self):
        s = SortedStack(True)     
        with self.assertRaises(IndexError):
            s.pop()
        s.push(5)
        s.push(6)        
        self.assertEqual(s.pop(), 6)
        self.assertEqual(s.size(), 1)
        self.assertEqual(s.pop(), 5)
        self.assertEqual(s.size(), 0)
        with self.assertRaises(IndexError):
            s.pop()
                        
    def test_push_non_integer(self):
        s = SortedStack(True)        
        with self.assertRaises(ValueError):
            s.push("evil string")
    
    def test_push(self):
        s = SortedStack(True)        
        self.assertEqual(s.size(), 0)
        s.push(5)
        self.assertEqual(s.size(), 1)
        self.assertEqual(s.peek(), 5)
        s.push(6)
        self.assertEqual(s.size(), 2)
        self.assertEqual(s.peek(), 6)
        s.push(6) 
        self.assertEqual(s.size(), 3)
        self.assertEqual(s.peek(), 6)
        with self.assertRaises(ValueError):
            s.push(5)
    

    def test_descending(self):
        s = SortedStack(False)        
        self.assertEqual(s.size(), 0)
        s.push(8)
        self.assertEqual(s.size(), 1)
        self.assertEqual(s.peek(), 8)
        s.push(6)
        self.assertEqual(s.size(), 2)
        self.assertEqual(s.peek(), 6)
        s.push(6) 
        self.assertEqual(s.size(), 3)
        self.assertEqual(s.peek(), 6)
        with self.assertRaises(ValueError):
            s.push(7)

    def test_str(self):
        s = SortedStack(True)
        s.push(5)
        s.push(6)        
        self.assertTrue( 'ascending' in str(s))
        self.assertTrue( '5' in str(s))
        self.assertTrue( '6' in str(s))
        self.assertTrue( 'SortedStack' in str(s))

        s2 = SortedStack(False)
        self.assertTrue( 'descending' in str(s2))
    
    