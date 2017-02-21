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


    def dup_first(self):
        """ Modifies this list by adding a duplicate of first node right after it. 
        
            For example, the list 'a','b','c' should become 'a','a','b','c'.            
            An empty list remains unmodified.            

            ** DOES NOT RETURN ANYTHING !!! **          

        """

        raise Exception("TODO IMPLEMENT ME !")

            
    def dup_all(self):
        """ Modifies this list by adding a duplicate of each node right after it.
        
            For example, the list 'a','b','c' should become 'a','a','b','b','c','c'.
            An empty list remains unmodified.      
            
            ** MUST PERFORM IN O(n) WHERE n is the length of the list. **
            
            ** DOES NOT RETURN ANYTHING !!! **
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
        

class DupFirstTest(unittest.TestCase):

    def test_dup_first_return_none(self):
        ul = UnorderedList()        
        self.assertEqual(ul.dup_first(), None)

    def test_dup_first_empty(self):
        ul = UnorderedList()        
        ul.dup_first()
        self.assertEqual(ul.to_python(), [])

    def test_dup_first_one(self):
        ul = UnorderedList()        
        ul.add('a')
        ul.dup_first()
        self.assertEqual(ul.to_python(), ['a', 'a'])

    def test_dup_first_two(self):
        ul = UnorderedList()        
        ul.add('b')
        ul.add('a')
        ul.dup_first()
        self.assertEqual(ul.to_python(), ['a', 'a', 'b'])

    def test_dup_first_two_dups(self):
        ul = UnorderedList()        
        ul.add('a')
        ul.add('a')
        ul.dup_first()
        self.assertEqual(ul.to_python(), ['a', 'a', 'a'])

    def test_dup_first_three(self):
        ul = UnorderedList()        
        ul.add('c')
        ul.add('b')
        ul.add('a')
        ul.dup_first()
        self.assertEqual(ul.to_python(), ['a', 'a', 'b', 'c'])


class DupAllTest(unittest.TestCase):

    def test_dup_all_return_none(self):
        ul = UnorderedList()        
        self.assertEqual(ul.dup_all(), None)

    def test_dup_all_empty(self):
        ul = UnorderedList()        
        ul.dup_all()
        self.assertEqual(ul.to_python(), [])

    def test_dup_all_one(self):
        ul = UnorderedList()        
        ul.add('a')
        ul.dup_all()
        self.assertEqual(ul.to_python(), ['a', 'a'])

    def test_dup_all_two(self):
        ul = UnorderedList()        
        ul.add('b')
        ul.add('a')
        ul.dup_all()
        self.assertEqual(ul.to_python(), ['a', 'a', 'b', 'b'])

    def test_dup_all_two_dups(self):
        ul = UnorderedList()        
        ul.add('a')
        ul.add('a')
        ul.dup_all()
        self.assertEqual(ul.to_python(), ['a', 'a', 'a', 'a'])

    def test_dup_all_three(self):
        ul = UnorderedList()        
        ul.add('c')
        ul.add('b')
        ul.add('a')
        ul.dup_all()
        self.assertEqual(ul.to_python(), ['a', 'a', 'b', 'b', 'c', 'c'])
