import sys
import unittest
from IPython.core.display import HTML


def run(testcase):        
    suite = unittest.TestLoader().loadTestsFromTestCase(testcase)
    unittest.TextTestRunner(verbosity=1,stream=sys.stderr).run( suite )

def init():
    css = open("./css/algolab.css", "r").read()

    js = open("./js/algolab.js", "r").read()

    html = "<style>\n" 
    html += css
    html += "\n </style>\n"
    html += "<script>\n"
    html += js
    html += "\n</script>\n"

    return  HTML(html)

