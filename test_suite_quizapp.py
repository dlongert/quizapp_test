import unittest

from readquiz_test import ReadQuizTest
from takequiz_test import TakeQuizTest

def quizapp_test_suite():
    suite = unittest.TestSuite()
    result = unittest.TestResult()
    suite.addTest(ReadQuizTest('test_read_quiz'))
    suite.addTest(ReadQuizTest('test_get_available_courses'))
    suite.addTest(ReadQuizTest('test_save_score'))
    suite.addTest(ReadQuizTest('test_get_percentage'))
    suite.addTest(TakeQuizTest('test_student_handler'))
    suite.addTest(TakeQuizTest('test_select_quiz'))
    runner = unittest.TextTestRunner()
    print(runner.run(suite))
quizapp_test_suite()