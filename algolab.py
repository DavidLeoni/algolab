import sys
import unittest
from IPython.core.display import HTML


def run(testcase):        
    suite = unittest.TestLoader().loadTestsFromTestCase(testcase)
    unittest.TextTestRunner(verbosity=1,stream=sys.stderr).run( suite )

def init():
    html = open("./custom.html", "r").read()
    return HTML(html)

