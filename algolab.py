import sys
import unittest
from IPython.core.display import HTML


def run(testcase):        
    suite = unittest.TestLoader().loadTestsFromTestCase(testcase)
    unittest.TextTestRunner(verbosity=1,stream=sys.stderr).run( suite )

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

