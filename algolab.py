import sys
import unittest
import inspect

from IPython.core.display import HTML

# taken from here: http://stackoverflow.com/a/961057
def get_class(meth):
    for cls in inspect.getmro(meth.im_class):
        if meth.__name__ in cls.__dict__: 
            return cls
    return None


# todo look at test order here: http://stackoverflow.com/a/18499093
def run(classOrMethod):    
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


import networkx as nx
from nxpd import draw

def show_distances():
    G = nx.DiGraph()
    G.graph['dpi'] = 80
    G.add_nodes_from(['a  0','b  1', 'c  1', 'd  2', 'e  3', 'f  -1', 'g  -1'])
    G.add_edges_from([('a  0','b  1'),('a  0', 'c  1'), ('b  1', 'd  2'),  ('c  1', 'd  2'), ('d  2', 'e  3') 
                      , ('e  3', 'd  2'),
                     ('f  -1', 'g  -1')])
    return G