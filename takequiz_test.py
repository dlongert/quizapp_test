import unittest
import json
import mock

from student import takequiz
from student.takequiz import Student
from student.readquiz import Quiz
from student.readquiz import Problem

COURSE_CODE = 'DATA-531'

student = Student('Student A', 123)
options = ['A. A', 'B. B', 'C. C', 'D. D', 'E. E']
problem = Problem("Question 1", options, 'A')
quiz = Quiz(COURSE_CODE, [problem])

class ReadQuizTest(unittest.TestCase):
    
    @mock.patch('student.takequiz.input', create=True)
    def test_student_handler(self, mocked_input):
        mocked_input.side_effect = ['Student A', 123]
        result = takequiz.student_handler()
        self.assertEquals(result.student_number, student.student_number)

    # @mock.patch('student.takequiz.input', create=True)
    # def test_start_quiz(self, mocked_input):
    #     mocked_input.side_effect = ['A']
    #     self.assertEquals(takequiz.start_quiz(quiz), 100.0)

    @mock.patch('student.takequiz.input', create=True)
    @mock.patch('student.readquiz.read_quiz', return_value = quiz)
    @mock.patch('student.readquiz.save_score', return_value = True)
    @mock.patch('student.readquiz.get_percentage', return_value = 100)
    def test_select_quiz(self, mocked_input, mocked_read_quiz, mocked_save_score, mocked_get_percentage):
        mocked_input.side_effect = ['Student A', 123, 1, 1]
        self.assertEquals(takequiz.select_quiz(), None)
        
unittest.main(argv=[''], verbosity=2, exit=False)

