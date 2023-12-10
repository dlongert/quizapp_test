import unittest
import json
import mock

from student import readquiz as rq

from student.takequiz import Student
from student.readquiz import Quiz
from student.readquiz import Problem

COURSE_CODE = 'DATA-531'
READ_DATA = json.dumps([{"question":"Question 1","options":["A. A","B. B","C. C","D. D","E. E"],"answer":"A. A"}])


class ReadQuizTest(unittest.TestCase):    
        
    def setUp(self):
        self.options = ['A. A', 'B. B', 'C. C', 'D. D', 'E. E']
        self.problem = Problem("Question 1", self.options, 'A')
        self.quiz = Quiz(COURSE_CODE, [self.problem])
        self.student = Student('Student A', 12345)
    
    def test_read_quiz(self):
        mock_open = mock.mock_open(read_data=READ_DATA)
        with mock.patch('builtins.open', mock_open):
            result = rq.read_quiz(COURSE_CODE)
        self.assertEquals(result.name, self.quiz.name)
        
    def test_get_available_courses(self):
        result = rq.get_available_courses()
        self.assertNotEquals(len(result), 0)
    
    def test_save_score(self):
        mock_open = mock.mock_open(read_data=READ_DATA)
        with mock.patch('builtins.open', mock_open):
            result = rq.save_score(self.student, COURSE_CODE, 10)
        self.assertEquals(result, True)
        
    def test_get_percentage(self):
        mock_open = mock.mock_open(read_data=READ_DATA)
        with mock.patch('builtins.open', mock_open):
            result = rq.get_percentage(self.student)
        self.assertEquals(result, 0)
        
    def tearDown(self):
        del self.student
        del self.options
        del self.quiz
        del self.problem
unittest.main(argv=[''], verbosity=2, exit=False)