import unittest


class GenericTree:
    """ A tree in which each node can have any number of children. 
    
        Each node is linked to its parent and to its immediate sibling on the right
        
        This is a stripped down version of the GenericTree you say in the lab.
    """
    
    def __init__(self, data):
        self._data = data
        self._child = None
        self._sibling = None
        self._parent = None        

    def data(self):
        return self._data    
    
    def child(self):
        return self._child    
    
    def sibling(self):
        return self._sibling
    
    def parent(self):
        return self._parent
        
    def is_root(self):
        """ Return True if the node is a root of a tree, False otherwise
        
            A node is a root whenever it has no parent nor siblings.
        """
        return self._parent == None and self._sibling == None
    
    def is_subtree(self):
        """ Returns True if the node is a subtree of another tree
        
            A subtree always has a parent 
        """
        return self._parent != None
        
        
    def children(self):
        """ Returns the children as a Python list 
            NOTE: this function return the *nodes*, not the data.        
        """
        
        ret = []
        current = self._child
        while current != None:
            ret.append(current)
            current = current._sibling
        return ret    
        
    def __str__(self):
        """ Returns a pretty string of the tree """
        
        def str_branches(node, branches):
            """ Returns a string with the tree pretty printed. 

                branches: a list of characters representing the parent branches. Characters can be either ` ` or '|'            
            """
            strings = [str(node._data)]
            current = node._child
            while (current != None):
                if current._sibling == None:            
                    # there are better end characters but let's not upset 
                    # stupid Python with unicode problems
                    joint = '\-'  
                else:
                    joint = '|-'


                strings.append('\n')
                for b in branches:
                     strings.append(b)
                strings.append(joint)
                if current._sibling == None:            
                    branches.append('  ')
                else:
                    branches.append('| ')                        
                strings.append(str_branches(current, branches))
                branches.pop()
                current = current._sibling

            return "".join(strings)
        
        return str_branches(self, [])
                
    
    def __repr__(self):
        
        def sub(t):                
            pars = ', '.join(map(lambda x : sub(x), t.children())) 
            if len(t.children()) > 0:
                pars = ', ' + pars
            return 'gt(' + str(t._data) + pars + ')' 
            
        return sub(self)
    
    def insert_child(self, new_child):        
        """ Inserts new_child at the beginning of the children sequence. """
        
        new_child._sibling = self._child
        new_child._parent = self
        self._child = new_child
        

        
        
    def has_child(self):
        """ Returns True if this node has a child, False otherwise """

        return self._child != None
        
    
    def mirror(self):
        """ Modifies this tree by mirroring it, that is, reverses the order
            of all children of this node and of all its descendants
            
            - MUST work in O(n) where n is the number of nodes
            - MUST change the order of nodes, NOT the data (so don't touch the data !)
            - DON'T create new nodes            
            - It is acceptable to use a recursive method.
                    
            
            Example:
            
            a     <-    Becomes:    a
            |-b                     |-i
            | |-c                   |-e
            | \-d                   | |-h
            |-e                     | |-g
            | |-f                   | \-f 
            | |-g                   |-b
            | \-h                     |-d
            \-i                       \-c
            
              
        """
        
        cs = self.children()     
        self._child = None
    
        
        for c in cs:
            self.insert_child(c)
        
        for c in cs:
            c.mirror()

            
    def clone(self):
        """ Clones this tree, by returning an *entirely* new tree which is an 
            exact copy of this tree (so returned node and *all* its descendants must be new). 
            
            - MUST run in O(n) where n is the number of nodes
            - a recursive method is acceptable.
        """
        ret = GenericTree(self._data)
        
        for c in reversed(self.children()):
            ret.insert_child(c.clone())
        
        return ret

        
def gt(*args):
    """ Shorthand function that returns a GenericTree containing the provided 
        data and children. First parameter is the data, the following ones are the children.
        
        Usage examples:
        
        print gt('a')
        >>> a
        
        print gt('a', gt('b'), gt('c'))
        >>> a
            |-b
            \-c
                            
    """
    if (len(args) == 0):
        raise Exception("You need to provide at least one argument for the data!")
        
    data = args[0]
    children = args[1:]
    
    r = GenericTree(data)    
    for c in reversed(children):
        r.insert_child(c)
    return r

def str_trees(t1, t2, error_row=-1):
    """ Returns a string version of the two trees side by side
    
        If error_row is given, the line in error is marked.
        If error_row == -1 it is ignored 
    """
    
    s1 = str(t1)
    s2 = str(t2)

    lines1 = s1.split("\n")
    lines2 = s2.split("\n")                

    max_len1 = 0                
    for line in lines1:                                    
        max_len1 = max(len(line.rstrip().decode("utf-8")), max_len1)        
        
    max_len2 = 0                
    for line in lines2:                                    
        max_len2 = max(len(line.rstrip().decode("utf-8")), max_len2)
    
    strings = []

    i = 0

    while i < len(lines1) or i < len(lines2):

        if i < len(lines1): 
            strings.append(lines1[i].rstrip())
            len1 = len(lines1[i].rstrip().decode("utf-8"))
        else:
            len1 = 0
                       
        if (i < len(lines2)):
            len2 = len(lines2[i].rstrip().decode("utf-8"))
            
            pad_len1 = 4 + max_len1 - len1
            strings.append((" " * pad_len1) + lines2[i].rstrip()) 
        else:
            len2 = 0
            
        if (error_row == i):
            pad_len2 = 2 + max_len1 + max_len2 - len1 - len2
            strings.append((" " * pad_len2) + "<--- DIFFERENT ! ")
            
        strings.append("\n")

        i += 1
    
    return "".join(strings)

    
            
            
class GenericTreeTest(unittest.TestCase):

    def assertReturnNone(self, ret, function_name):
        """ Asserts method result ret equals None """
        self.assertEquals(None, ret, 
                          function_name 
                          + " specs say nothing about returning objects! Instead you are returning " + str(ret))
    
    
    def assertTreeEqual(self, t1, t2):
        """ Asserts the trees t1 and t2 are equal """
        
        def rec_assert(c1, c2, row):                    

            if c1 == None:
                raise Exception("Found a None node in left tree! \n\n "
                                + str_trees(t1,t2,row))         
            if c2 == None:
                raise Exception("Found a None node in right tree !\n\n "
                                + str_trees(t1,t2,row))

            
            if c1.data() != c2.data():
                raise Exception("data() is different!\n\n " 
                                + str_trees(t1,t2,row))
            
            self.assertTrue(c1 == t1 or c1.parent() != None, 
                            "Left parent is None! "
                           + "\n\n" +  str_trees(t1,t2,row) )

            self.assertTrue(c2 == t2 or c2.parent() != None, 
                            "Right parent is None!" 
                             + "\n\n" +  str_trees(t1,t2,row) )            
            
            self.assertTrue(c1.parent() == None or isinstance(c1.parent(), GenericTree), 
                           "Left parent is not a GenericTree instance!"
                            + "\n\n" +  str_trees(t1,t2,row) )
            self.assertTrue(c2.parent() == None or isinstance(c2.parent(), GenericTree), 
                           "Right parent is not a GenericTree instance! "
                            + "\n\n" +  str_trees(t1,t2,row) )
            
            if (c1.parent() == None):
                if (c2.parent() != None):
                    raise Exception("Different parents! "
                                    + "Left parent = None   Right parent.data() = " + str(c2.parent().data()) 
                                    + "\n\n" + str_trees(t1,t2,row) )
                                    
            else:    
                if (c2.parent() == None):                    
                    raise Exception("Different parents! "
                                    + "Left parent.data() = " + str(c1.parent().data()) 
                                    + "   Right parent = None"
                                    + "\n\n" + str_trees(t1,t2,row)) 
                else: # let's just check data for now
                    self.assertEquals(c1.parent().data(), c2.parent().data(),
                                  "Different parents ! " 
                                 + "Left parent.data() = " + str(c1.parent().data()) 
                                    + "   Right parent.data() = " + str(c2.parent().data()
                                    + "\n\n" + str_trees(t1,t2,row) ))
            i = 0            
            
            cs1 = c1.children()
            cs2 = c2.children()
            if (len(cs1) != len(cs2)):
                raise Exception("Children sizes are different !\n\n"
                                + str_trees(t1, t2, row + min(len(cs1), len(cs2))) )
            while (i < len(cs1) ):
                rec_assert(cs1[i], cs2[i], row + 1)   
                i += 1 
        
        rec_assert(t1, t2, 0)
    
    def assertRoot(self, t):
        """ Checks provided node t is a root, if not raises Exception """
                          
        self.assertTrue(t.is_root(), "Detached node " + t.data() + " is not a root, does it have still the _parent or _sibling set to something ?")
    
    def test_str_trees(self):
        self.assertTrue('a' in str_trees(gt('a'), gt('b')))
        self.assertTrue('b' in str_trees(gt('a'), gt('b')))
        
        self.assertTrue('a' in str_trees(gt('a', gt('b')), gt('b', gt('c'))))
        self.assertTrue('c' in str_trees(gt('a', gt('b')), gt('b', gt('c'))))
    
    
    def test_assert_tree_equal(self):
        self.assertTreeEqual(gt('a'), gt('a'))
        self.assertTreeEqual(gt('a', gt('b')), gt('a', gt('b')))
        
        with self.assertRaises(Exception):
            self.assertTreeEqual(gt('a'), gt('b'))            
        with self.assertRaises(Exception):
            self.assertTreeEqual(gt('a', gt('b')), gt('a', gt('c')))
        
        # different structure
        with self.assertRaises(Exception):
            self.assertTreeEqual(gt('a', gt('b')), gt('a', gt('b',gt('c'))))

        with self.assertRaises(Exception):
            self.assertTreeEqual(gt('a', gt('b',gt('c'))), gt('a', gt('b')))        
                        
    
    def test_insert_child(self):        
        ta = GenericTree('a')
        self.assertEqual(ta.child(), None)
        tb = GenericTree('b')        
        ret = ta.insert_child(tb) 
        self.assertEqual(ret, None, self.assertReturnNone(ret, "insert_child"))
        self.assertEqual(ta.child(), tb)
        self.assertEqual(tb.parent(), ta)        
        self.assertEqual(tb.sibling(), None)
        self.assertEqual(tb.child(), None)
        
        tc = GenericTree('c')
        ta.insert_child(tc)
        self.assertEqual(ta.child(), tc)
        self.assertEqual(tc.sibling(), tb)
        self.assertEqual(tc.parent(), ta)
        self.assertEqual(tb.sibling(), None)


class MirrorTest(unittest.TestCase):

    def assertReturnNone(self, ret, function_name):
        """ Asserts method result ret equals None """
        self.assertEquals(None, ret, 
                          function_name 
                          + " specs say nothing about returning objects! Instead you are returning " + str(ret))
    
    
    def assertTreeEqual(self, t1, t2):
        """ Asserts the trees t1 and t2 are equal """
        
        def rec_assert(c1, c2, row):                    

            if c1 == None:
                raise Exception("Found a None node in left tree! \n\n "
                                + str_trees(t1,t2,row))         
            if c2 == None:
                raise Exception("Found a None node in right tree !\n\n "
                                + str_trees(t1,t2,row))

            
            if c1.data() != c2.data():
                raise Exception("data() is different!\n\n " 
                                + str_trees(t1,t2,row))
            
            self.assertTrue(c1 == t1 or c1.parent() != None, 
                            "Left parent is None! "
                           + "\n\n" +  str_trees(t1,t2,row) )

            self.assertTrue(c2 == t2 or c2.parent() != None, 
                            "Right parent is None!" 
                             + "\n\n" +  str_trees(t1,t2,row) )            
            
            self.assertTrue(c1.parent() == None or isinstance(c1.parent(), GenericTree), 
                           "Left parent is not a GenericTree instance!"
                            + "\n\n" +  str_trees(t1,t2,row) )
            self.assertTrue(c2.parent() == None or isinstance(c2.parent(), GenericTree), 
                           "Right parent is not a GenericTree instance! "
                            + "\n\n" +  str_trees(t1,t2,row) )
            
            if (c1.parent() == None):
                if (c2.parent() != None):
                    raise Exception("Different parents! "
                                    + "Left parent = None   Right parent.data() = " + str(c2.parent().data()) 
                                    + "\n\n" + str_trees(t1,t2,row) )
                                    
            else:    
                if (c2.parent() == None):                    
                    raise Exception("Different parents! "
                                    + "Left parent.data() = " + str(c1.parent().data()) 
                                    + "   Right parent = None"
                                    + "\n\n" + str_trees(t1,t2,row)) 
                else: # let's just check data for now
                    self.assertEquals(c1.parent().data(), c2.parent().data(),
                                  "Different parents ! " 
                                 + "Left parent.data() = " + str(c1.parent().data()) 
                                    + "   Right parent.data() = " + str(c2.parent().data()
                                    + "\n\n" + str_trees(t1,t2,row) ))
            i = 0            
            
            cs1 = c1.children()
            cs2 = c2.children()
            if (len(cs1) != len(cs2)):
                raise Exception("Children sizes are different !\n\n"
                                + str_trees(t1, t2, row + min(len(cs1), len(cs2))) )
            while (i < len(cs1) ):
                rec_assert(cs1[i], cs2[i], row + 1)   
                i += 1 
        
        rec_assert(t1, t2, 0)
    
    def assertRoot(self, t):
        """ Checks provided node t is a root, if not raises Exception """
                          
        self.assertTrue(t.is_root(), "Detached node " + t.data() + " is not a root, does it have still the _parent or _sibling set to something ?")
    
    """
    a  <-   Becomes:   a
    """
    def test_root(self):
        t = gt('a')
        t.mirror()
        self.assertTreeEqual(t, gt('a'))

    """
    a   <-   Becomes  a
    \-b               \-b
    """       
    def test_ab(self):
        t = gt('a',gt('b'))
        t.mirror()
        self.assertTreeEqual(t, gt('a', gt('b')))
    

    """
    a   <-   Becomes:  a
    |-b                |-c
    \-c                \-b
    
    """    
    def test_abc(self):
        t = gt('a',gt('b'),gt('c'))
        t.mirror()
        self.assertTreeEqual(t, gt('a', gt('c'), gt('b')))


    """
    a   <-     Becomes:     a
    |-b                     |-f
    | |-c                   \-b
    | |-d                     |-e
    | \-e                     |-d
    \-f                       \-c 
                          
    """    
    def test_abcdef(self):
        t = gt('a',gt('b', gt('c'), gt('d'), gt('e')),gt('f'))
        t.mirror()
        self.assertTreeEqual(t, gt('a', gt('f'), gt('b', gt('e'), gt('d'), gt('c'))))
    
    
    """
    a                         a 
    |-b   <-     Becomes:     |-b
    | |-c                     | |-d
    | \-d                     | \-c
    \-e                       \-e
    """
    def test_non_root(self):
        tb = gt('b', gt('c'), gt('d'))        
        ta = gt('a',tb,gt('e'))
        tb.mirror()
        self.assertTreeEqual(ta, gt('a', gt('b', gt('d'), gt('c')),  gt('e')))
    

class CloneTest(unittest.TestCase):
    def assertReturnNone(self, ret, function_name):
        """ Asserts method result ret equals None """
        self.assertEquals(None, ret, 
                          function_name 
                          + " specs say nothing about returning objects! Instead you are returning " + str(ret))
    
    
    def assertTreeEqual(self, t1, t2):
        """ Asserts the trees t1 and t2 are equal """
        
        def rec_assert(c1, c2, row):                    

            if c1 == None:
                raise Exception("Found a None node in left tree! \n\n "
                                + str_trees(t1,t2,row))         
            if c2 == None:
                raise Exception("Found a None node in right tree !\n\n "
                                + str_trees(t1,t2,row))

            
            if c1.data() != c2.data():
                raise Exception("data() is different!\n\n " 
                                + str_trees(t1,t2,row))
            
            self.assertTrue(c1 == t1 or c1.parent() != None, 
                            "Left parent is None! "
                           + "\n\n" +  str_trees(t1,t2,row) )

            self.assertTrue(c2 == t2 or c2.parent() != None, 
                            "Right parent is None!" 
                             + "\n\n" +  str_trees(t1,t2,row) )            
            
            self.assertTrue(c1.parent() == None or isinstance(c1.parent(), GenericTree), 
                           "Left parent is not a GenericTree instance!"
                            + "\n\n" +  str_trees(t1,t2,row) )
            self.assertTrue(c2.parent() == None or isinstance(c2.parent(), GenericTree), 
                           "Right parent is not a GenericTree instance! "
                            + "\n\n" +  str_trees(t1,t2,row) )
            
            if (c1.parent() == None):
                if (c2.parent() != None):
                    raise Exception("Different parents! "
                                    + "Left parent = None   Right parent.data() = " + str(c2.parent().data()) 
                                    + "\n\n" + str_trees(t1,t2,row) )
                                    
            else:    
                if (c2.parent() == None):                    
                    raise Exception("Different parents! "
                                    + "Left parent.data() = " + str(c1.parent().data()) 
                                    + "   Right parent = None"
                                    + "\n\n" + str_trees(t1,t2,row)) 
                else: # let's just check data for now
                    self.assertEquals(c1.parent().data(), c2.parent().data(),
                                  "Different parents ! " 
                                 + "Left parent.data() = " + str(c1.parent().data()) 
                                    + "   Right parent.data() = " + str(c2.parent().data()
                                    + "\n\n" + str_trees(t1,t2,row) ))
            i = 0            
            
            cs1 = c1.children()
            cs2 = c2.children()
            if (len(cs1) != len(cs2)):
                raise Exception("Children sizes are different !\n\n"
                                + str_trees(t1, t2, row + min(len(cs1), len(cs2))) )
            while (i < len(cs1) ):
                rec_assert(cs1[i], cs2[i], row + 1)   
                i += 1 
        
        rec_assert(t1, t2, 0)
    
    def assertRoot(self, t):
        """ Checks provided node t is a root, if not raises Exception """
                          
        self.assertTrue(t.is_root(), "Detached node " + t.data() + " is not a root, does it have still the _parent or _sibling set to something ?")
        
    
    """
    a
    """
    def test_root(self):
        ta = gt('a')
        t2 = ta.clone()        

        self.assertTreeEqual(ta,t2)
        ta._data = 'b'  # if we change the original data, clone should be unaffected
        self.assertTreeEqual(t2, gt('a'))        
        ta.insert_child(gt('c')) # same if we insert an extra child 
        self.assertTreeEqual(t2, gt('a'))        
        

    """
    a
    \-b
    """
    def test_ab(self):
        tb= gt('b')
        ta = gt('a', tb)
        
        t2 = ta.clone()        

        self.assertTreeEqual(ta,t2)
        ta._data = 'x'  # if we change the original, clone should be unaffected
        tb._data = 'y'        
        self.assertTreeEqual(t2, gt('a',gt('b')))

    """
    a
    |-b
    |-c
      \-d
    """
    def test_abcd(self):
        td = gt('d')
        tc= gt('c', td)
        tb= gt('b')
        ta = gt('a', tb, tc)
        t2 = ta.clone()  
        
        self.assertTreeEqual(ta,t2)
        ta._data = 'x'  # if we change the original, clone should be unaffected
        tb._data = 'y' 
        tc._data = 'y'
        td._data = 'w'
        self.assertTreeEqual(t2, gt('a',gt('b'), gt('c', gt('d'))))

