import unittest


class MultiSet:
    """ A multiset (or bag) generalizes a set by allowing multiple instances of the multiset's elements. 

    The multiplicity of an element is the number of instances of the element in a specific multiset.


    For example:

        The multiset "a, b"  contains only elements 'a' and 'b', each having multiplicity 1
        In multiset "a, a, b",  'a' has multiplicity 2 and 'b' has multiplicity 1
        In multiset "a, a, a, b, b, b", 'a' and 'b' both have multiplicity 3
    
    Notice order of insertion does not matter, so "a, a, b" and "a, b, a" are the same multiset,
    where 'a' has multiplicity 2 and 'b' has multiplicity 1.
    
    """
    
    def __init__(self):
        """ Initializes the MultiSet as empty."""
        raise Exception("TODO IMPLEMENT ME !")
        
    
    def add(self, el):
        """ Adds one instance of element el to the multiset 

            NOTE: MUST work in O(1)        
        """
        raise Exception("TODO IMPLEMENT ME !")
        
    def get(self, el):
        """ Returns the multiplicity of element el in the multiset. 
            
            If no instance of el is present, return 0.

            NOTE: MUST work in O(1)        
        """
        raise Exception("TODO IMPLEMENT ME !")
    
    def removen(self, el, n):
        """ Removes n instances of element el from the multiset (that is, reduces el multiplicity by n)
            
            If n is negative, raises ValueError.            
            If n represents a multiplicity bigger than el current multiplicity, raises LookupError
            
            NOTE: multiset multiplicities are never negative
            NOTE: MUST work in O(1)
        """
        raise Exception("TODO IMPLEMENT ME !")
        
        
def is_env_working():
    """ Don't modify this function"""
    return "yes"

  
class EnvWorkingTest(unittest.TestCase):
    """ Just to test you can run tests.  """
    
    def test_env_working(self):
        """ This sest should always pass."""
        
        self.assertEqual(is_env_working(), "yes")
 
class AddGetTest(unittest.TestCase):
    
    def test_get_non_existing(self):
        m = MultiSet()
        self.assertEqual(m.get('a'),0)
        self.assertEqual(m.get(666),0)
        
    
    def test_aa(self):
        
        m = MultiSet()        
        self.assertEqual(m.get('a'),0)
        m.add('a')
        self.assertEqual(m.get('a'),1)
        m.add('a')
        self.assertEqual(m.get('a'),2)
        
    def test_aabb(self):
        
        m = MultiSet()        
        self.assertEqual(m.get('a'),0)
        self.assertEqual(m.get('b'),0)        
        m.add('a')
        self.assertEqual(m.get('a'),1)
        self.assertEqual(m.get('b'),0)        
        m.add('a')
        self.assertEqual(m.get('a'),2)
        self.assertEqual(m.get('b'),0)        
        m.add('b')
        self.assertEqual(m.get('a'),2)        
        self.assertEqual(m.get('b'),1)
        m.add('b')
        self.assertEqual(m.get('a'),2)        
        self.assertEqual(m.get('b'),2)
    
class RemovenTest(unittest.TestCase):

    def test_removen_nothing(self):
        m = MultiSet()
        m.add('a')
        m.removen('a', 0)
        self.assertEqual(m.get('a'), 1)
        m.removen('b', 0)
        self.assertEqual(m.get('b'), 0)
        
    
    def test_removen_aa_non_existing(self):
        m = MultiSet()
        m.add('a')
        m.add('a')
        
        with self.assertRaises(LookupError):
            m.removen('a',3)  # too many

        with self.assertRaises(LookupError):            
            m.removen('b',1) # never inserted                
    
    def test_aa(self):
        
        m = MultiSet()        
        m.add('a')
        m.add('a')
        self.assertEqual(m.get('a'),2)
        m.removen('a', 1)
        self.assertEqual(m.get('a'),1)        
        m.removen('a', 1)
        self.assertEqual(m.get('a'),0)
        m.removen('a', 0)
        self.assertEqual(m.get('a'),0)
      
    def test_aab(self):
        
        m = MultiSet()        
        m.add('a')
        m.add('a')
        m.add('b')
        self.assertEqual(m.get('a'),2)
        self.assertEqual(m.get('b'),1)
        m.removen('a', 2)
        self.assertEqual(m.get('a'),0)
        self.assertEqual(m.get('b'),1)
        self.assertEqual(m.get('b'),1)
        m.removen('a',0)
        self.assertEqual(m.get('a'),0)
        self.assertEqual(m.get('b'),1)      
        m.removen('b', 1)
        self.assertEqual(m.get('a'),0)
        self.assertEqual(m.get('b'),0)      
        m.removen('b', 0)
        self.assertEqual(m.get('a'),0)
        self.assertEqual(m.get('b'),0)      

