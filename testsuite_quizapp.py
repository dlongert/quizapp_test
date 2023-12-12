import unittest

from createquiz_test import CreateQuizTest
from checkstudentscore_test import CheckStudentScoreTest

def quizapp_test_suite():
    suite = unittest.TestSuite()
    result = unittest.TestResult()
    suite.addTest(CreateQuizTest("test_create_quiz"))
    suite.addTest(CreateQuizTest("convert_to_json"))
    suite.addTest(CreateQuizTest("create_score_csv"))
    suite.addTest(CreateQuizTest("create_quiz"))
    suite.addTest(CheckStudentScoreTest("test_get_student_scores"))
    suite.addTest(CheckStudentScoreTest("test_set_student_scores"))
    suite.addTest(CheckStudentScoreTest("test_quiz_score_statistics"))
    suite.addTest(CheckStudentScoreTest("test_score_driver"))
    suite.addTest(CheckStudentScoreTest("test_quiz_or_score"))

    runner = unittest.TextTestRunner()
    print(runner.run(suite))
quizapp_test_suite()