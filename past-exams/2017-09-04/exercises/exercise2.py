import unittest

class Node:
    """ A Node of an UnorderedList. Holds data provided by the user. """
    
    def __init__(self,initdata):
        self._data = initdata
        self._next = None

    def get_data(self):
        return self._data

    def get_next(self):
        return self._next

    def set_data(self,newdata):
        self._data = newdata

    def set_next(self,newnext):
        self._next = newnext


class UnorderedList:
    """
        This is a stripped down version of the UnorderedList seen in the lab
        
    """
        
    def __init__(self):
        self._head = None

    def to_python(self):
        """ Returns this UnorderedList as a regular Python list. This method 
            is very handy for testing.
        """
        python_list = []
        current = self._head        
        
        while (current != None):
            python_list.append(current.get_data())
            current = current.get_next()                       
        return python_list        
        
    def __str__(self):
        current = self._head
        strings = []
        
        while (current != None):
            strings.append(str(current.get_data()))            
            current = current.get_next()            
        
        return "UnorderedList: " + ",".join(strings)
        
        
    def add(self,item):    
        """ Adds item at the beginning of the list """
        
        new_head = Node(item)
        new_head.set_next(self._head)
        self._head = new_head


    def find_couple(self,a,b):
        """ Search the list for the first two consecutive elements having data equal to 
            provided a and b, respectively. If such elements are found, the position
            of the first one is returned, otherwise raises LookupError.
            
            - MUST run in O(n), where n is the size of the list.
            - Returned index start from 0 included
            
        """                
        
        raise Exception("TODO IMPLEMENT ME !")

    def swap (self, i, j):
        """
            Swap the data of nodes at index i and j. Indeces start from 0 included.
            If any of the indeces is out of bounds, rises IndexError.
            
            NOTE: You MUST implement this function with a single scan of the list.
            
        """
        
        raise Exception("TODO IMPLEMENT ME !")

class UnorderedListTest(unittest.TestCase):
    """ Test cases for UnorderedList

    """    
    
    def test_init(self):
        ul = UnorderedList()
    
    def test_str(self):
        ul = UnorderedList()
        self.assertTrue('UnorderedList' in str(ul))
        ul.add('z')
        self.assertTrue('z' in str(ul))
        ul.add('w')
        self.assertTrue('z' in str(ul))
        self.assertTrue('w' in str(ul))
              
        
    def test_add(self):
        """ Remember 'add' adds stuff at the beginning of the list ! """
        
        ul = UnorderedList()
        self.assertEquals(ul.to_python(), [])
        ul.add('b')
        self.assertEquals(ul.to_python(), ['b'])
        ul.add('a')
        self.assertEquals(ul.to_python(), ['a', 'b'])



class FindCoupleTest(unittest.TestCase):
    
    def test_empty(self):
        ul = UnorderedList()
        with self.assertRaises(LookupError):
            ul.find_couple('a','b')
        
    def test_a(self):
        ul = UnorderedList()
        ul.add('a')
        with self.assertRaises(LookupError):
            ul.find_couple('a','b')

    def test_ab(self):
        ul = UnorderedList()
        ul.add('b')        
        ul.add('a')

        self.assertEquals(ul.find_couple('a','b'), 0)
        
        with self.assertRaises(LookupError):
            ul.find_couple('b','a')
    
    def test_abc(self):
        ul = UnorderedList()
        ul.add('c')        
        ul.add('b')        
        ul.add('a')

        self.assertEquals(ul.find_couple('a','b'), 0)
        self.assertEquals(ul.find_couple('b','c'), 1)
        
        with self.assertRaises(LookupError):
            ul.find_couple('a','c')

    def test_aab(self):
        ul = UnorderedList()
        ul.add('b')........
        ul.add('a')........
        ul.add('a')

        self.assertEquals(ul.find_couple('a','b'), 1)


    def test_abbb(self):
        ul = UnorderedList()
        ul.add('b')        
        ul.add('b')        
        ul.add('b')        
        ul.add('a')

        self.assertEquals(ul.find_couple('a','b'), 0)
        self.assertEquals(ul.find_couple('b','b'), 1)
        
        with self.assertRaises(LookupError):
            ul.find_couple('a','a')

class SwapTest(unittest.TestCase):
    
    def test_empty(self):
        ul = UnorderedList()
        with self.assertRaises(IndexError):
            ul.swap(0,3) 
        with self.assertRaises(IndexError):
            ul.swap(2,0)            

    def test_one(self):
        ul = UnorderedList()
        ul.add('a')
        ul.swap(0,0)
        self.assertEqual(ul.to_python(), ['a'])

    def test_one_wrong_indeces(self):
        ul = UnorderedList()
        ul.add('a')
        with self.assertRaises(IndexError):
            ul.swap(-1,0)            
        with self.assertRaises(IndexError):
            ul.swap(0,-1)            
        with self.assertRaises(IndexError):
            ul.swap(0,2)            

    def test_two(self):
        ul = UnorderedList()
        ul.add('b')
        ul.add('a')
        
        ul.swap(0,1)
        self.assertEqual(ul.to_python(), ['b','a'])
        ul.swap(0,1)
        self.assertEqual(ul.to_python(), ['a', 'b'])

    def test_three(self):
        ul = UnorderedList()
        ul.add('c')        
        ul.add('b')
        ul.add('a')
        
        ul.swap(0,1)
        self.assertEqual(ul.to_python(), ['b','a','c'])
        ul.swap(1,2)
        self.assertEqual(ul.to_python(), ['b', 'c','a'])
