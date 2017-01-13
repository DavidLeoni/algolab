import unittest

class CappedStack:

    def __init__(self, cap):
        """ Creates a CappedStack capped at cap. 
        
            Cap must be > 0, otherwise an IndexError is thrown
        """        
        if cap < 1:
            raise IndexError("Cap must be >= 0, found instead " + str(cap))
        # notice we assign to variables with underscore to respect Python conventions        
        self._cap = cap
        # notice with use _elements instead of the A in the pseudocode, because it is
        # clearer, starts with underscore, and capital letters are usual reserved 
        # for classes or constants
        self._elements = []         
        
    def size(self):
        return len(self._elements)
        
    def is_empty(self):
        return len(self._elements) == 0
        
    def pop(self):
        if (len(self._elements) > 0):
            return self._elements.pop()        
        # else: implicitly, Python will return None
    
    def peek(self):
        if (len(self._elements) > 0):
            return self._elements[-1]
        # else: implicitly, Python will return None        
        
    def push(self, item):
        if (len(self._elements) < self._cap):
            self._elements.append(item)
        # else fail silently

    def cap(self):
        """ Returns the cap of the stack 
        """
        return self._cap
        
    def peekn(self, n):
        """
            Returns a list with the n top elements, in the order in which they
            were pushed. For example, if the stack is the following: 
            
                e
                d
                c
                b
                a
                
            peekn(3) will return the list ['c','d','e']

            If there aren't enough element to peek, raises IndexError
            If n is negative, raises an IndexError

        """
        raise Exception("TODO IMPLEMENT ME!")
        
    def popn(self, n):
        """ Pops the top n elements, and return them as a list, in the order in 
            which they where pushed. For example, with the following stack:
            
                e
                d
                c
                b
                a
            
            popn(3)
            
            will give back ['c','d','e'], and stack will become:
            
                b
                a
            
            If there aren't enough element to pop, raises an IndexError
            If n is negative, raises an IndexError
        """
        
        raise Exception("TODO IMPLEMENT ME!")
        
    def set_cap(self, cap):
        """ Sets the cap value to the provided cap. 
        
            If the cap is less then the stack size, all the elements above 
            the cap are removed from the stack.
            
            If cap < 1, raises an IndexError
            Does *not* return anything!
        
            For example, with the following stack, and cap at position 7:
            
            cap ->  7
                    6
                    5  e
                    4  d
                    3  c
                    2  b
                    1  a
                    
            
            calling method set_cap(3) will change the stack to this:
            
            cap ->  3  c
                    2  b
                    1  a                                
            
        """
        
        raise Exception("TODO IMPLEMENT ME!")
    
    def __str__(self):
        return "CappedStack: cap=" + str(self._cap) + " elements=" + str(self._elements) 
        
        
class CappedStackTest(unittest.TestCase):

    """ Test cases for CappedStackTest

         Note this is a *completely* separated class from CappedStack and
         we declare it here just for testing purposes!
         The 'self' you see here have nothing to do with the selfs from the
         CappedStack methods!        
    """

    def test_init_wrong_cap(self): 
        """ 
            We use the special construct 'self.assertRaises(IndexError)' to state
            we are expecting the calls to CappedStack(0) and CappedStack(-1) to raise
            an IndexError.
        """
        with self.assertRaises(IndexError):
            CappedStack(0)
        with self.assertRaises(IndexError):
            CappedStack(-1)
    
    
    def test_cap(self):        
        self.assertEqual(CappedStack(1).cap(), 1) 
        self.assertEqual(CappedStack(2).cap(), 2) 
    
        
    def test_size(self):
        s = CappedStack(5)        
        self.assertEqual(s.size(), 0)
        s.push("a")
        self.assertEqual(s.size(), 1)
        s.pop()
        self.assertEqual(s.size(), 0)
    
    def test_is_empty(self):
        s = CappedStack(5)
        self.assertTrue(s.is_empty())
        s.push("a")
        self.assertFalse(s.is_empty())
        
    
    def test_pop(self):
        s = CappedStack(5) 
        self.assertEqual(s.pop(), None)        
        s.push("a")        
        self.assertEqual(s.pop(), "a")        
        self.assertEqual(s.pop(), None)
        
    def test_peek(self):
        s = CappedStack(5)
        self.assertEqual(s.peek(), None)         
        s.push("a")
        self.assertEqual(s.peek(), "a")
        self.assertEqual(s.peek(), "a")  # testing peek is not changing the stack
        self.assertEqual(s.size(), 1)
                        
    def test_push(self):
        s = CappedStack(2)        
        self.assertEqual(s.size(), 0)
        s.push("a")
        self.assertEqual(s.size(), 1)
        s.push("b")
        self.assertEqual(s.size(), 2)
        self.assertEqual(s.peek(), "b")
        s.push("c")  # capped, pushing should do nothing now!
        self.assertEqual(s.size(), 2)
        self.assertEqual(s.peek(), "b")

    def test_str(self):
        s = CappedStack(4)
        s.push("a")
        s.push("b")        
        self.assertTrue("cap" in str(s))
        self.assertTrue("elements" in str(s))
        
    def test_peekn(self):
        s = CappedStack(10)
        s.push("a")
        s.push("b")
        s.push("c")
        s.push("d")
        s.push("e")
        self.assertEquals(s.peekn(3), ['c','d','e'])
        #self.assertEquals(s.size(), 2)
        #self.assertEqual(s.peek(), "b")
        

    def test_peekn_wrong_n(self):
        s = CappedStack(10)
        s.push("a")
        s.push("b")
        with self.assertRaises(IndexError):
            s.peekn(3)

        with self.assertRaises(IndexError):
            s.peekn(-1)


    def test_peekn_five(self):
        s = CappedStack(10)
        s.push("a")
        s.push("b")
        s.push("c")
        s.push("d")
        s.push("e")
        self.assertEquals(s.peekn(3), ['c','d','e'])
        self.assertEquals(s.size(), 5)
        self.assertEquals(s.peekn(3), ['c','d','e'])  # testing peek is not changing the stack

        
    def test_popn_five(self):
        s = CappedStack(10)
        s.push("a")
        s.push("b")
        s.push("c")
        s.push("d")
        s.push("e")
        self.assertEquals(s.popn(3), ['c','d','e'])
        self.assertEquals(s.size(), 2)
        self.assertEqual(s.peek(), "b")
        
    def test_set_cap_return_none(self):        
        s = CappedStack(10)
        self.assertEqual(s.set_cap(10), None)
        
    def test_set_cap_too_low(self):
        s = CappedStack(10)
        with self.assertRaises(IndexError):
            s.set_cap(-1)
            
        with self.assertRaises(IndexError):
            s.set_cap(0)
            
        
    def test_set_cap_high(self):
        """ Will set a cap high, stack should be preserved """        
        s = CappedStack(10)
        s.push('a')
        s.push('b')
        s.push('c')
        
        s.set_cap(5)
        
        self.assertEqual(s.cap(), 5)
        self.assertEqual(s.size(), 3)
        self.assertEqual(s.peek(), 'c')        


    def test_set_cap_low(self):
        """ Will set a cap low, some element will be removed """
        s = CappedStack(10)
        s.push('a')
        s.push('b')
        s.push('c')
        s.push('d')
        s.push('e')
        
        s.set_cap(3)
        
        self.assertEqual(s.cap(), 3)
        self.assertEqual(s.size(), 3)
        self.assertEqual(s.peek(), 'c')        
        
#unittest.main()        