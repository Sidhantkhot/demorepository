import unittest

class Paymentmethod(unittest.TestCase):
        
        def test_paymentin_doller(self):
            print("payment in doller")
            self.assertTrue(True)
        
        def test_paymentin_rupee(self):
            print("payment in rupee")
            self.assertTrue(True)
        
            
            
if __name__ == "__main__":
    unittest.main()