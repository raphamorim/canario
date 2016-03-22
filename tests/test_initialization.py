import unittest, capivara, types

class TestInitialization(unittest.TestCase):
    def test_capivara_get_DOM_type(self):
        self.assertEquals(isinstance(capivara.get_DOM, 
        	types.FunctionType), True)

    def test_capivara_result(self):
        self.assertEquals(capivara.get_DOM("a"), True)

