import sys    
import unittest

def run(testcase):        
    suite = unittest.TestLoader().loadTestsFromTestCase(testcase)
    unittest.TextTestRunner(verbosity=1,stream=sys.stderr).run( suite )
