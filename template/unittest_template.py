import unittest

class CustomTests(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        print('run 1 time')
        pass
    @classmethod
    def tearDownClass(self):
        pass
    
    def setUp(self):
        print('run every time')
        pass
    def tearDown(self):
        pass
    
    def test_run1(self):
        print("    test run1")
        pass

    def test_run2(self):
        print("    test run2")
        self.assertEqual("a", "b")
        pass


if __name__ == '__main__':
    unittest.main()