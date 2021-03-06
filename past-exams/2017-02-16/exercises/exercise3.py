import unittest


class DiGraph:
    """ This is a stripped own version of the DiGraph we saw during the lab.
    
        A simple graph data structure, represented as a dictionary of adjacency lists
    
        Verteces can be of any type, to keep things simple in this data model they coincide with their labels.
        Adjacency lists hold the target verteces. 
        Attempts to add duplicate targets will be silently ignored.
        
        For shorthand construction, see separate dig() function
    """
            
    def __init__(self):
        # The class just holds the dictionary _edges: as keys it has the verteces, and 
        # to each vertex associates a list with the verteces it is linked to.
        self._edges = {}
        
    def add_vertex(self, vertex):
        """ Adds vertex to the DiGraph. A vertex can be any object.
            
            If the vertex already exist, does nothing.
        """
        if vertex not in self._edges:            
            self._edges[vertex] = []
    
    def verteces(self):
        """ Returns a set of the graph verteces. Verteces can be any object. """
        
        # Note dict keys() return a list, not a set. Bleah.  
        # See http://stackoverflow.com/questions/13886129/why-does-pythons-dict-keys-return-a-list-and-not-a-set
        return set(self._edges.keys()) 
        
    def has_vertex(self, vertex):
        """ Returns true if graph contains given vertex. A vertex can be any object. """
        return vertex in self._edges
        
    def add_edge(self, vertex1, vertex2):
        """ Adds an edge to the graph, from vertex1 to vertex2
        
            If verteces don't exist, raises an Exception.
            If there is already such an edge, exits silently.            
        """
        
        if not vertex1 in self._edges:
            raise Exception("Couldn't find source vertex: " + str(vertex1))

        if not vertex2 in self._edges:
            raise Exception("Couldn't find target vertex: " + str(vertex2))        
            
        if not vertex2 in self._edges[vertex1]:
            self._edges[vertex1].append(vertex2)

    def has_edge(self, source, target):
        """  Returns True if there is an edge between source vertex and target vertex. 
             Otherwise returns False.

            If either source, target or both verteces don't exist raises an Exception.
        """
        if (not self.has_vertex(source)):
            raise Exception("There is no source vertex " + str(source))
            
        if (not self.has_vertex(target)):
            raise Exception("There is no source vertex " + str(target))
                
        return target in self._edges[source]                                

            
    def __str__(self):
        """ Returns a string representation like the following:
        
            >>> print gr('a',['b','c', 'd'],
                         'b', ['b'],
                         'c', ['a'])

            a: [b,c]
            b: [b]
            c: [a]         
            d: []
        
        """
        
        if (len(self._edges) == 0):
            return "\nDiGraph()" 
        
        max_len=0
        
        sorted_verteces = sorted(self._edges.keys())
        
        for source in self._edges:
            max_len = max(max_len, len(str(source)))
        
        strings = ["\n"]
        
        for source in sorted_verteces:
            
            strings.append(str(source).ljust(max_len))
            strings.append(': ')            
            strings.append(str(self._edges[source]))
            
            strings.append('\n')
        
        return ''.join(strings)
        
    def __repr__(self):              
        return self.__str__()



    def adj(self, vertex):
        """ Returns the verteces adjacent to vertex. 
            
            NOTE: verteces are returned in a NEW list.
            Modifying the list will have NO effect on the graph!
        """
        if not vertex in self._edges:
            raise Exception("Couldn't find a vertex " + str(vertex))
        
        return self._edges[vertex][:]
      
    def __eq__(self, other):
        """ !!!   NOTE: although we represent the set with adjanceny lists, for __eq__
            graph dig('a', ['b','c']) is considered equals to a graph dig('a', ['c', 'b']) !!! 
        """
            
        if not isinstance(other, DiGraph):
            return False            
        
        if self.verteces() != other.verteces():
            return False
        
        
        for source in self._edges:            
            if set(self._edges[source]) != set(other._edges[source]):
                return False
        
        return True
        
    def __ne__(self, other):
        """ not equal. 
            For the necessity of implementing it, see this: http://jcalderone.livejournal.com/32837.html 
        """
        result = self.__eq__(other)
        if result is NotImplemented:
            return result
        return not result        
        
    def is_empty(self):
        """  A DiGraph for us is empty if it has no verteces and no edges """
        
        return len(self._edges) == 0
   
        

def str_compare_digraphs(actual, expected):
    """ Returns a string representing a comparison side by side 
        of the provided digraphs
    
    """

    if actual == None and expected == None:
        return "Both graphs are None."

    if (actual == None) ^ (expected == None):
        if actual == None:
            what = ""
        else:
            what = "NOT"
        return "ACTUAL GRAPH IS " + what + " None ! " +"\n\nACTUAL: \n" + str(actual)  +"\n\nEXPECTED: \n" + str(expected) 


    if actual.is_empty() ^ expected.is_empty():
        if actual.is_empty():
            what = ""
        else:
            what = "NOT"
            
        return " ACTUAL GRAPH IS " + what + " EMPTY ! " +"\n\nACTUAL: \n" + str(actual)  +"\n\nEXPECTED: \n" + str(expected) 


    max_len1_keys = 0    
    for source in actual.verteces():
        max_len1_keys = max(max_len1_keys, len(str(source)+": " ))

    
    max_len1 = 0    
    for line in str(actual).split("\n"):
        max_len1 = max(max_len1, len(line))
    max_len1 = max(max_len1, len("ACTUAL"))

    max_len2_keys = 0    
    for source in expected.verteces():
        max_len2_keys = max(max_len2_keys, len(str(source)+": " ))
    
            
    max_len2 = 0    
    for line in str(expected).split("\n"):
        max_len2 = max(max_len2, len(line))
    max_len2 = max(max_len1, len("EXPECTED"))
    
    strings = []
    

    vs = sorted(set(actual.verteces()).union( expected.verteces()))
    
    strings = []

    dist = 2
    dist2 = - max_len2_keys
    
    strings.append((" " * max_len1_keys + "ACTUAL").ljust(max_len1 + dist))
    strings.append("  EXPECTED\n")
    
    for vertex in vs:
                
        strings.append(str(vertex))
        strings.append(': ')
                
        if vertex in actual.verteces():
            strings.append(str(actual.adj(vertex)).ljust(max_len1 + dist))
        else:
            strings.append("--" + " " * (max_len1 + dist - 2))
            
        if vertex in expected.verteces():            
            strings.append(str(expected.adj(vertex)).ljust(max_len2 + dist2))
        else:
            strings.append("--" + " " * (max_len2 + dist2 - 2))
        
        if (not vertex in actual.verteces()
            or not vertex in expected.verteces()
            or set(actual.adj(vertex)) != set(expected.adj(vertex))):
            strings.append("  <---- DIFFERENT ! ")
        
        strings.append("\n")
            
    return ''.join(strings)



def dig(*args):
    """ Shorthand to construct a DiGraph with provided arguments
    
        To use it, provide source vertex / target vertex pairs like in the following examples:        
        
        >>> print dig()        
        
        DiGraph()
        
        >>> print dig('a',['b','c'])
                
        a: [b,c]
        b: []
        c: []
        
        >>> print dig('a',['b','c'],
                     'b', ['b'],
                     'c', ['a'])
                
        a: [b,c]
        b: [b]
        c: [a]                
        
    """
    
    g = DiGraph()
        
    if len(args) % 2 == 1:
        raise Exception("Number of arguments must be even! You need to provide"
                    + " vertex/list pairs like 'a',['b', 'c'], b, ['d'], ... !")

    i = 1        
    for a in args:
        
        if i % 2 == 1:
            vertex = a
            g.add_vertex(vertex)            
            
        else:
            try:
                iter(a)
            except TypeError:
                raise Exception('Targets of ' + str(vertex) + ' are not iterable: ' + str(a) )
            for target in a:
                if not g.has_vertex(target):
                    g.add_vertex(target)
                g.add_edge(vertex, target)
        i += 1
    
    return g    
    
def pie(n):
    """ Returns a DiGraph with n+1 verteces, displaced like a polygon with a perimeter 
        of n verteces progressively numbered from 1 to n. A central vertex numbered zero 
        has outgoing edges to all other verteces.
        
        For n = 0, return the empty graph.
        For n = 1, return vertex zero connected to node 1, and node 1 has a self-loop.
        
    """
        
    raise Exception("TODO IMPLEMENT ME !")
        
def flux(depth):
    """ Returns a DiGraph with 1 + (d * 3) verteces displaced like a Y:

        - from a central node numbered 0, three branches depart  
        - all edges are directed outward
        - on each branch there are 'depth' verteces. 
                
        For example, for depth=2 we get the following graph (suppose arrows point outward):
        
             4         5
              \       /
               1     2
                \   /
                  0
                  |
                  3
                  |
                  6
        
    """
    
    raise Exception("TODO IMPLEMENT ME !")    

class DiGraphTest(unittest.TestCase):        
    
    def assertDiGraphEqual(self, actual, expected,  msg=None):                    
        if not expected == actual:            
            if msg == None:
                the_msg = "Graphs are different:"
            else:
                the_msg = msg
            raise AssertionError(the_msg + " \n\n" + str_compare_digraphs(actual, expected) )    
    
 
    def test_adj(self):
        self.assertEqual(dig('a', []).adj('a'), 
                         [])
        self.assertEqual(dig('a', ['b']).adj('a'),
                         ['b'])
        self.assertEqual(dig('a', ['b', 'c']).adj('a'),
                         ['b', 'c'])
        g = dig('a', ['b'])
        lst = g.adj('a')
        lst[0] = 'c'
        self.assertEqual(['b'], g.adj('a'))
        
    def test_has_edge(self):
        self.assertTrue(dig('a',['b']).has_edge('a','b'))    
        self.assertFalse(dig('a',['b']).has_edge('a','a'))    
        self.assertTrue(dig('a',['b'],
                            'a',['c']).has_edge('a','c'))
                            
        with self.assertRaises(Exception):
            self.assertTrue(dig('a',['b']).has_edge('a','c'))

    def test_eq(self):
        
        self.assertEqual(dig('a', ['b','c']),
                         dig('a', ['c', 'b']))        
                                         
        self.assertTrue(dig('a', ['b','c']) == dig('a', ['c', 'b']))                         
        self.assertFalse(dig('a', ['b']) == dig('a', ['c', 'b']))                         
    
    def test_str(self):
        self.assertTrue("DiGraph()" in str(dig()))
        self.assertTrue("x" in str(dig('x',['y'])))
        self.assertTrue("y" in str(dig('x',['y'])))
        self.assertEquals(set(['x','y']), dig('x',['y']).verteces())
        self.assertEquals(set(['x','y','z','w', 'z']),
                          dig('x',['y'], 'z', ['w','x']).verteces())
       
        
    def test_assert_dig(self):
        
        self.assertDiGraphEqual(dig(), dig())
        
        with self.assertRaises(Exception):
            self.assertDiGraphEqual(dig(), dig('a',[]))        

class PieTest(unittest.TestCase):
    
    def assertDiGraphEqual(self, actual, expected,  msg=None):                    
        if not expected == actual:            
            if msg == None:
                the_msg = "Graphs are different:"
            else:
                the_msg = msg
            raise AssertionError(the_msg + " \n\n" + str_compare_digraphs(actual, expected) )    
    
    
    def test_pie_0(self):        
        self.assertDiGraphEqual(pie(0), dig())

    def test_pie_1(self):        
        self.assertDiGraphEqual(pie(1), dig(0, [1],
                                            1, [1]))

    def test_pie_2(self):        
        self.assertDiGraphEqual(pie(2), dig(0, [1,2],
                                            1, [2],
                                            2, [1]))

    def test_pie_3(self):
        self.assertDiGraphEqual(pie(3), dig(0, [1,2,3],
                                            1, [2],
                                            2, [3],
                                            3, [1]))

    def test_pie_4(self):
        self.assertDiGraphEqual(pie(4), dig(0, [1,2,3,4],
                                            1, [2],
                                            2, [3],
                                            3, [4],
                                            4, [1]))

class FluxTest(unittest.TestCase):
    
    def assertDiGraphEqual(self, actual, expected,  msg=None):                    
        if not expected == actual:            
            if msg == None:
                the_msg = "Graphs are different:"
            else:
                the_msg = msg
            raise AssertionError(the_msg + " \n\n" + str_compare_digraphs(actual, expected) )    
    
    
    def test_flux_zero(self):
        self.assertDiGraphEqual(flux(0), dig())

    def test_flux_one(self):        
        self.assertDiGraphEqual(flux(1), dig(0, [1,2,3]))
    
    def test_flux_two(self):        
        self.assertDiGraphEqual(flux(2), dig(0, [1,2,3],
                                             1, [4],
                                             2, [5],
                                             3, [6]))

    def test_flux_three(self):        
        self.assertDiGraphEqual(flux(3), dig(0, [1,2,3],
                                             1, [4],
                                             2, [5],
                                             3, [6],
                                             4, [7],
                                             5, [8],
                                             6, [9]))
        