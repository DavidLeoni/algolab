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

    def norep(self):
        """ Removes all the consecutive repetitions from the list.
            Must perform in O(n), where n is the list size.
        
            For example, after calling norep:

            'a','a','b','c','c','c'   will become  'a','b','c'
            
            'a','a','b','a'   will become   'a','b','a'            
            
        """
        if self._head == None:
            return
        else:
            current = self._head.get_next()
            last = self._head        
        
        
        while current != None:
            
            if last.get_data() == current.get_data():    
                last.set_next(current.get_next())                
            else:
                last = current            
            current = current.get_next()
   
                  
    

def panino(lst):
    """ Returns a new UnorderedList having double the nodes of provided lst
        First nodes will have same elements of lst, following nodes will 
        have the same elements but in reversed order.
        
        For example:
            
            >>> panino(['a'])
            UnorderedList: a,a            
            
            >>> panino(['a','b'])
            UnorderedList: a,b,b,a

            >>> panino(['a','c','b'])
            UnorderedList: a,c,b,b,c,a
    
    """
    ret = UnorderedList()
    for e in lst:
        ret.add(e)
    for e in reversed(lst):
        ret.add(e)
    return ret
        
        
class PaninoTest(unittest.TestCase):
    
    def test_empty(self):
        self.assertEqual(panino([]).to_python(), [])
    
    def test_one(self):
        self.assertEqual(panino(['a']).to_python(), ['a','a'])
        
    def test_two(self):
        self.assertEqual(panino(['a', 'b']).to_python(), ['a','b','b','a'])

    def test_three(self):
        self.assertEqual(panino(['a', 'b', 'c']).to_python(), ['a','b','c','c','b','a'])



class NorepTest(unittest.TestCase):
    
    def test_empty(self):
        ul = UnorderedList()
        ul.norep()
        self.assertEqual(ul.to_python(), [])    
    
    def test_a(self):
        ul = UnorderedList()
        ul.add('a')
        ul.norep()
        self.assertEqual(ul.to_python(), ['a'])    
                
    def test_aa(self):
        ul = UnorderedList()
        ul.add('a')
        ul.add('a')        
        ul.norep()
        self.assertEqual(ul.to_python(), ['a'])    

    def test_aaa(self):
        ul = UnorderedList()
        ul.add('a')
        ul.add('a')        
        ul.add('a')        
        ul.norep()
        self.assertEqual(ul.to_python(), ['a'])    

    def test_aaab(self):
        ul = UnorderedList()
        ul.add('b')        
        ul.add('a')
        ul.add('a')        
        ul.norep()
        self.assertEqual(ul.to_python(), ['a', 'b'])    


    def test_baa(self):
        ul = UnorderedList()               
        ul.add('a')
        ul.add('a')        
        ul.add('b')        
        ul.norep()
        self.assertEqual(ul.to_python(), ['b', 'a'])    


    def test_aabb(self):
        ul = UnorderedList()                               
        ul.add('b')        
        ul.add('b')        
        ul.add('a')
        ul.add('a')        
        ul.norep()
        self.assertEqual(ul.to_python(), ['a', 'b'])    


    def test_aabba(self):
        ul = UnorderedList()                               
        ul.add('a')
        ul.add('b')        
        ul.add('b')        
        ul.add('a')
        ul.add('a')        
        ul.norep()
        self.assertEqual(ul.to_python(), ['a', 'b', 'a'])    

    def test_aabcc(self):
        ul = UnorderedList()                               
        ul.add('c')
        ul.add('c')        
        ul.add('b')        
        ul.add('a')
        ul.add('a')        
        ul.norep()
        self.assertEqual(ul.to_python(), ['a', 'b', 'c'])    

