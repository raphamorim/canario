import unittest, capivara, types

class TestInitialization(unittest.TestCase):
    def test_get_DOM_type(self):
        self.assertEquals(isinstance(capivara.get_DOM, 
        	types.FunctionType), True)
