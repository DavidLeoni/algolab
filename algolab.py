import sys
import unittest
import inspect

import networkx as nx
from IPython.core.display import HTML

# taken from here: http://stackoverflow.com/a/961057
def get_class(meth):
    for cls in inspect.getmro(meth.im_class):
        if meth.__name__ in cls.__dict__: 
            return cls
    return None


def run(classOrMethod):    
    """ Runs test class or method. Doesn't show code nor output in html.
    
        todo look at test order here: http://stackoverflow.com/a/18499093        
    """ 
    
    if  inspect.isclass(classOrMethod) and issubclass(classOrMethod, unittest.TestCase):        
        testcase = classOrMethod
        suite = unittest.TestLoader().loadTestsFromTestCase(testcase)
        unittest.TextTestRunner(verbosity=1,stream=sys.stderr).run( suite )
    elif inspect.ismethod(classOrMethod):
        meth = classOrMethod
        suite = unittest.TestSuite()
        testcase = get_class(meth)
        suite.addTest(testcase(meth.__name__))
        unittest.TextTestRunner(verbosity=1,stream=sys.stderr).run( suite )
    else:
        raise Exception("Accepted parameters are a TestCase class or a TestCase method. Found instead: " + str(classOrMethod))


def show_run(classOrMethod):    
    """ Runs test class or method. Code is not shown, but output is
    
        @since 0.19
    """    
    run(classOrMethod)
        
def init():
    css = open("./css/algolab.css", "r").read()

    tocjs = open("./js/toc.js", "r").read()

    js = open("./js/algolab.js", "r").read()
    

    ret = "<style>\n" 
    ret += css
    ret += "\n </style>\n"
    
    ret +="\n"
    
    ret += "<script>\n"
    ret += "\n"
    ret += tocjs
    ret += "\n"
    ret += js
    ret += "\n</script>\n"

    return  HTML(ret)

def assertNotNone(ret, function_name):
    return function_name + " specs say nothing about returning objects! Instead you are returning " + str(ret)



def show_distances():
    ret = nx.DiGraph()
    ret.graph['dpi'] = 80
    ret.add_nodes_from(['a  0','b  1', 'c  1', 'd  2', 'e  3', 'f  -1', 'g  -1'])
    ret.add_edges_from([('a  0','b  1'),('a  0', 'c  1'), ('b  1', 'd  2'),  ('c  1', 'd  2'), ('d  2', 'e  3') 
                      , ('e  3', 'd  2'),
                     ('f  -1', 'g  -1')])
    return ret
    
def to_nx(algolab_digraph):
    """ Convert an Algolab DiGraph into a NetworkX graph and return it. """
    ret = nx.DiGraph()
    ret.graph['dpi'] = 80
    ret.add_nodes_from(algolab_digraph.verteces())
    for sv in algolab_digraph.verteces():
        for tv in algolab_digraph.adj(sv):            
            ret.add_edge(sv, tv)
    return ret
    
# the draw here does not work ....     
#def draw_digraph(algolab_digraph):
#   nxg = to_networkx(algolab_digraph)
    # nxpd.draw(ret, show='ipynb') 