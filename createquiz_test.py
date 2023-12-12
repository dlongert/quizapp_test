import unittest
import pandas as pd
import mock
import json 
from teacher.createquiz import Question, questionInput, convert_to_json, create_score_csv, create_quiz

READ_DATA = json.dumps([{"question":"Question 1","options":["A. A","B. B","C. C","D. D","E. E"],"answer":"A. A"}])
SCORE_DATA = "12345,Dylan Longert,95.0"

class CreateQuizTest(unittest.TestCase):
    @classmethod    
    def setUpClass(cls):
        print("In setUpClass()")
    
    def setUp(self):
        print("Setting up test")
        self.course = "Data-533"
        self.inputs = ["Question 1",["A. A", "B. B", "C. C", "D. D", "E. E"], "A. A"]
        self.SCORE_DATA = SCORE_DATA
        self.student_number = 12345
   
    @mock.patch("teacher.createquiz.input", create=True)
    def test_quiz_inputs(self, mocked_input):
        mocked_input.side_effect = ["Question 1", "A", "Y", "Y", "B", "Y", "C", "Y", "D", "Y", "E", "N", "N" ]
        results = questionInput().quiz_inputs()
        self.assertEqual(results, self.inputs)
        self.assertIsNotNone(results)
        self.assertTrue(results)
        self.assertIsInstance(results, list)

    @mock.patch('builtins.input', side_effect=['y', 'Question 1', 'A. A', 'y', 'n', 'Data-533'])
    @mock.patch('teacher.createquiz.questionInput.quiz_inputs', return_value=["Question 1", ["A. A"], "A. A"])
    @mock.patch('teacher.createquiz.Question.write_to_dict', return_value={"question": "Question 1", "options": ["A. A"], "answer": "A. A"})
    @mock.patch('teacher.createquiz.convert_to_json', return_value=True)
    @mock.patch('teacher.createquiz.create_score_csv', return_value=True)
    def test_create_quiz(self, mock_input, mock_quiz_inputs, mock_write_to_dict, mock_convert_to_json, mock_create_score_csv):
        result = create_quiz()
        self.assertIsNone(result)
      
    @mock.patch('builtins.open', new_callable=mock.mock_open, read_data='{"key": "value"}')
    def test_convert_to_json(self, mock_open):
        result = convert_to_json(self.course, self.inputs)
        expected_result = READ_DATA
        self.assertNotEqual(result, expected_result)
        self.assertIsNone(result)

    @mock.patch('builtins.open', mock.mock_open(), create=True)
    @mock.patch('pandas.DataFrame.to_csv', return_value=None)
    @mock.patch('pandas.read_csv', return_value=pd.DataFrame())
    def test_create_score_csv(self, mock_read_csv, mock_to_csv):
        result = create_score_csv(self.course)
        self.assertIsNone(result)
    
    def tearDown(self):
        del self.course
        del self.inputs

    @classmethod    
    def tearDownClass(cls):
        print("In tearDownClass()")

unittest.main(argv=[''], verbosity=2, exit=False)