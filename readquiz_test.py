import unittest
import json
import mock

from student import readquiz as rq

from student.takequiz import Student
from student.readquiz import Quiz
from student.readquiz import Problem


COURSE_CODE = 'DATA-531'
READ_DATA = json.dumps([{"question":"Question 1","options":["A. A","B. B","C. C","D. D","E. E"],"answer":"A. A"}])

options = ['A. A', 'B. B', 'C. C', 'D. D', 'E. E']
problem = Problem("Question 1", options, 'A')
quiz = Quiz(COURSE_CODE, [problem])
student = Student('Student A', 12345)

class ReadQuizTest(unittest.TestCase):
    
    def test_read_quiz(self):
        mock_open = mock.mock_open(read_data=READ_DATA)
        with mock.patch('builtins.open', mock_open):
            result = rq.read_quiz(COURSE_CODE)
        self.assertEquals(result.name, quiz.name)
        
    def test_get_available_courses(self):
        result = rq.get_available_courses()
        self.assertNotEquals(len(result), 0)
    
unittest.main(argv=[''], verbosity=2, exit=False)