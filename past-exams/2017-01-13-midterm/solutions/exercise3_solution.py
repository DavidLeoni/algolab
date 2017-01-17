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

    def remove(self, item):
        """ Removes first occurrence of item from the list
        
            If item is not found, raises an Exception.
        """
        current = self._head        
        prev = None
        
        while (current != None):
            if (current.get_data() == item):
                if prev == None:  # we need to remove the head 
                    self._head = current.get_next()
                else:  
                    prev.set_next(current.get_next())
                    current = current.get_next()                    
                return  # Found, exits the function
            else:
                prev = current
                current = current.get_next() 
        
        raise Exception("Tried to remove a non existing item! Item was: " + str(item))

                        
    def occurrences(self, item):
        """ 
            Returns the number of occurrences of item in the list.
        """

        current = self._head            
        
        i = 0        
        
        while current != None:            
            if current.get_data() == item:            
                i += 1
            current = current.get_next()
                
        return i
        
    def shrink(self):
        """ 
            Removes from this UnorderedList all nodes at odd indeces (1, 3, 5, ...), 
            supposing that the first node has index zero, the second node 
            has index one, and so on. 
            
            So if the UnorderedList is 
                'a','b','c','d','e' 
            a call to shrink() will transform the UnorderedList into 
                'a','c','e'
            
            Must execute in O(n) where 'n' is the length of the list.
            Does *not* return anything.
        """

        current = self._head            
                
        while current != None:                                    
            if current.get_next() != None:
                    current.set_next(current.get_next().get_next())
            current = current.get_next()

                        
class UnorderedListTest(unittest.TestCase):
    """ Test cases for UnorderedList

    """    
    
    def test_init(self):
        UnorderedList()
    
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
        
    def test_remove_empty_list(self):
        ul = UnorderedList()
        with self.assertRaises(Exception):
            ul.remove('a')
        
    def test_remove_one_element(self):
        ul = UnorderedList()
        ul.add('a')
        with self.assertRaises(Exception):
            ul.remove('b')
        ul.remove('a')
        self.assertEquals(ul.to_python(), [])
        
    def test_remove_two_element(self):
        ul = UnorderedList()
        ul.add('b')
        ul.add('a')
        with self.assertRaises(Exception):
            ul.remove('c')
        ul.remove('b')
        self.assertEquals(ul.to_python(), ['a'])        
        ul.remove('a')
        self.assertEquals(ul.to_python(), [])        


    def test_occurrences_zero(self):
        self.assertEqual(UnorderedList().occurrences('a') , 0)
        self.assertEqual(UnorderedList().occurrences(7) , 0 )
        
    def test_occurrences_one(self):
        
        ul = UnorderedList()
        ul.add('a')
        self.assertEqual(ul.occurrences('a') , 1)
        self.assertEqual(ul.occurrences('b') , 0)
        self.assertEqual(ul.occurrences(7) , 0)

    def test_occurrences_three(self):
        
        ul = UnorderedList()
        ul.add('a')
        ul.add('b')
        ul.add('a')        
        self.assertEqual(ul.occurrences('a'), 2 )
        self.assertEqual(ul.occurrences('b'), 1 )
        self.assertEqual(ul.occurrences('c'), 0 )

    def test_shrink_return_none(self):
        ul = UnorderedList()         
        self.assertEqual(ul.shrink(), None)
        
    def test_shrink_empty(self):
        ul = UnorderedList()            
        ul.shrink()
        self.assertEqual(ul.to_python(), [])

    def test_shrink_one(self):
        ul = UnorderedList()
        ul.add('a')
        ul.shrink()
        self.assertEqual(ul.to_python(), ['a'])

    def test_shrink_two(self):
        ul = UnorderedList()
        ul.add('b')
        ul.add('a')
        ul.shrink()
        self.assertEqual(ul.to_python(), ['a'])

    def test_shrink_three(self):
        ul = UnorderedList()
        ul.add('c')
        ul.add('b')
        ul.add('a')
        ul.shrink()
        self.assertEqual(ul.to_python(), ['a', 'c'])

        
    def test_shrink_four(self):
        ul = UnorderedList()
        ul.add('d')
        ul.add('c')
        ul.add('b')        
        ul.add('a')        
        
        ul.shrink()
        self.assertEqual(ul.to_python(), ['a','c'])

#unittest.main()        