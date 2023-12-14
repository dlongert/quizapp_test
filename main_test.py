import unittest
import mock
import main

class MainTest(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        print("In setUpClass()")      
        
    def setUp(self):
        self.role = [1]
        
    @mock.patch('main.input', create=True)
    @mock.patch('student.takequiz.select_quiz', return_value = None)
    def test_start(self, mocked_input, mocked_select_quiz):
        mocked_input.side_effect = [1]
        result = main.start()
        self.assertEquals(result, None)
        self.assertIsNone(result)
    
    @mock.patch('main.input', create=True)
    @mock.patch('teacher.checkstudentscores.quiz_or_score', return_value = None)
    def test_start_2(self, mocked_input, mocked_quiz_or_score):
        mocked_input.side_effect = [2]
        result = main.start()
        self.assertEquals(result, None)
        self.assertIsNone(result)
    
    @mock.patch('main.input', create=True)
    def test_start_3(self, mocked_input):
        mocked_input.side_effect = [3]
        result = main.start()
        self.assertEquals(result, None)
        self.assertIsNone(result)
        
    def tearDown(self):
        del self.role
        
    @classmethod
    def tearDownClass(cls):
        print("In tearDownClass()")
        
unittest.main(argv=[''], verbosity=2, exit=False)