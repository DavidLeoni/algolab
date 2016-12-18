import unittest


class VisitLog:
    """ Represents a log of a search visit to DiGraph vertex
    """
    
    def __init__(self, vertex, discovery_time):
        self.vertex = vertex
        self.discovery_time = discovery_time
        self.finish_time = -1
       


class DiGraph:
    """ A simple graph data structure, represented as a dictionary of adjacency lists
    
        Verteces can be of any type, to keep things simple in this data model they coincide with their labels.
        Adjacency lists hold the target vertices. 
        Attempts to add duplicate targets will be silently ignored.
        
        For shorthand construction, see separate gr() function
    """
            
    def __init__(self):
        self._edges = {}
        
    def add_vertex(self, vertex):
        """ Adds vertex to the DiGraph. A vertex can be any object.
            
            If the vertex already exist, does nothing.
        """
        if vertex not in self._edges:            
            self._edges[vertex] = []
    
    def vertices(self):
        """ Returns a set of the graph vertices. Vertices can be any object. """
        
        # Note dict keys() return a list. Bleah.  
        # See http://stackoverflow.com/questions/13886129/why-does-pythons-dict-keys-return-a-list-and-not-a-set
        return set(self._edges.keys()) 
        
    def has_vertex(self, vertex):
        """ Returns true if graph contains given vertex. A vertex can be any object. """
        return vertex in self._edges
    
    def remove_vertex(self, vertex):
        """ Removes the provided vertex  and returns it
            
            If the vertex is not found, raises an Exception.
        """
                
        if not vertex in self._edges:
            raise Exception("Couldn't find vertex:" +str(vertex))
        
        for key in self.vertices:
            self.vertices[key].remove(vertex)
        
        return self.vertices.pop(vertex)
        
    def add_edge(self, vertex1, vertex2):
        """ Adds an edge to the graph, from vertex1 to vertex2
        
            If vertices don't exist, raises an Exception.
            If there is already such an edge, exits silently.            
        """
        
        if not vertex1 in self._edges:
            raise Exception("Couldn't find source vertex:" + str(vertex1))

        if not vertex2 in self._edges:
            raise Exception("Couldn't find target vertex:" + str(vertex2))        
            
        if not vertex2 in self._edges[vertex1]:
            self._edges[vertex1].append(vertex2)
            
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
            return "DiGraph()" 
        
        max_len=0
        
        for source in self._edges:
            max_len = max(max_len, len(str(source)))
        
        strings = []
        
        for source in self._edges:
            strings.append(str(source).ljust(max_len))
            strings.append(': ')            
            strings.append(str(self._edges[source]))
            
            strings.append('\n')
        
        return ''.join(strings)

    def adj(self, vertex):
        
        if not vertex in self._edges:
            raise Exception("Couldn't find a vertex " + str(vertex))
        
        return self._edges[vertex]

    def _dfs_helper(self, vertex,  on_discovery, on_finish, logs, time):    
        """ Private recursive method to perform the depth first search 
            
            Parameters: 
                vertex: the vertex from where to start performing the discovery
                on_discovery: a function that takes as parameters (DiGraph, vertex, logs, time)
                              which is called at every vertex discovery. Can be None.
                on_finish: a function that takes as parameters (DiGraph, vertex, logs, time)
                              which is called after a vertex search has finished. Can be None.
                logs: a dictionary vertex -> VisitLog with the logs of the previous visited nodes
                time: the current discovery time             
            
            Returns: the last timestamp when the search is finished.
        """
        logs[vertex] = VisitLog(vertex, time)
        
        if on_discovery != None:
            on_discovery(self, vertex, logs, time)
        
        for v in self.adj(vertex): 
            if not vertex in logs:
                new_time = self._dfs_helper(vertex, on_discovery, on_finish, logs, time + 1)
        
        logs[vertex].finish_time = new_time
        
        if on_finish != None:
            on_finish(self, vertex, logs, new_time)

        return new_time

    def dfs(self, vertex, on_discovery=None, on_finish=None):
        """ Performs Depth First Search starting from provided vertex  

            Parameters: 
            
                vertex: the vertex from where to start performing the discovery
                       If the vertes does not exist an Exception is raised
                on_discovery: an optional function that takes as parameters (DiGraph, vertex, logs, time)
                              which is called at every vertex discovery. Can be None.
                on_finish: an optional function that takes as parameters (DiGraph, vertex, logs, time)
                              which is called after a vertex search has finished. Can be None.
        
            Returns: the visit logs as a dictionary: vertex -> VisitLog
                        
        """
            
        if vertex not in self._edges:
            raise Exception("Couldn't find a vertex : " + str(vertex))
        
        logs = {}
        
        self._dfs_rec(vertex, on_discovery, on_finish, logs, 1)
        
        return logs
        
    def __eq__(self, other):
            
        if not isinstance(other, DiGraph):
            return False
        
        if self.vertices() != other.vertices():
            return False
        
        for source_vertex in self._edges:            
            if self._edges[source_vertex] != other._edges[source_vertex]:
                return False
        
        return True
        
        

def str_compare_digraphs(dg1, dg2):
    """ Returns a string representing a comparison side by side 
        of the provided digraphs
    
    """

    if (dg1 == None) ^ (dg1 == None):
        return "At least one graph is None ! " +"\n\n Graph 1: " + str(dg1)  +"\n\n Graph 2: " + str(dg2) 
    
    max_len1 = 0    
    for source in dg1.vertices():
        max_len1 = max(max_len1, len(str(source)))

    max_len2 = 0    
    for source in dg2.vertices():
        max_len2 = max(max_len2, len(str(source)))

    
    strings = []
    

    common_edges = set(dg1.vertices()) & set(dg2.vertices())

    all_edges = set(dg1.vertices()).union( dg2.vertices())
    
    different_edges = all_edges - common_edges
    
    if len(different_edges > 0):
        vs = list(common_edges)
        vs.extend(different_edges)
    else:
        vs = dg1.vertices()

    strings = []

    for vertex in vs:
                
        strings.append(vertex)
        strings.append(': ')
                
        if vertex in dg1.vertices():
            strings.append(str(dg1.adj(vertex)).ljust(max_len1 + 4))
        else:
            strings.append(" " * (max_len1 + 4))
            
        if vertex in dg2.vertices():
            strings.append(dg2.adj(vertex))
        else:
            strings.append(" " * (max_len2 + 4))
        
        if (dg1.adj(vertex) != dg2.adj(vertex)):
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
    
  
        
        
    
   
    
def gen_graphs(n):
    
    """ Returns a list with all the possible 2^(n^2) graphs of size n 
    
        Vertices will be identified with numbers from 1 to n 
    """    

    def gen_bits(n):
        """  Generates a sequence of 2^(n^2) lists, each of n^2 0 / 1 ints  """
        
        bits = n*n;    
        nedges = 2**bits    
        
        ret = []
        for i in range(0, nedges):
                    
            right = [int(x) for x in bin(i)[2:]]
            lst = ([0] * (bits - len(right)))
            lst.extend(right)
    
            ret.append(lst)
        return ret
    
    i = 0
    
    ret = []

    for lst in gen_bits(n):
        
        g = DiGraph()
        for j in range(1, n+1):
            g.add_vertex(j)
        
        source = 0
        for b in lst:            
            if i % n == 0:
                source += 1
            if b:
                g.add_edge(source, (i % n) + 1)
            i += 1
        ret.append(g)
    return ret
      

graphs_3 = gen_graphs(3)

class DiGraphTest(unittest.TestCase):
        
    
    def assertDiGraphEqual(self, dg1, dg2):                    
        if not dg1 == dg2:            
            raise Exception("Graphs are different: \n\n" + str_compare_digraphs )
        
    def test_str(self):
        self.assertTrue("DiGraph()" in str(dig()))
        self.assertTrue("x" in str(dig('x',['y'])))
        self.assertTrue("y" in str(dig('x',['y'])))
        self.assertEquals(set(['x','y']), dig('x',['y']).vertices())
        self.assertEquals(set(['x','y','z','w', 'z']),
                          dig('x',['y'], 'z', ['w','x']).vertices())
        
    def test_gen_graphs(self):
        
        gs1 = gen_graphs(1)        
        
        self.assertEquals(2, len(gs1))    
        self.assertTrue(dig(1, []) in gs1)
        
    def test_assert_dig(self):
        
        self.assertDiGraphEqual(dig(), dig())
        
        with self.assertRaises(Exception):
            self.assertDiGraphEqual(dig(), dig('a',[]))        

        
unittest.main()
    
    