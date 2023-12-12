import unittest
from teacher.checkstudentscores import get_student_scores, set_student_scores, quiz_score_statistics, score_driver, quiz_or_score
import mock

COURSE_CODE = "Data-533"
SCORE_DATA = "12345,Dylan Longert,95.0"

class CheckStudentScoreTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("In setUpClass()")

    def setUp(self):
        print("Setting up test")
        # Set up variables for reuse across tests
        self.course = "Data-533"
        self.student_number = 12345
        self.updated_score = 95.0
        self.file_path = "../assets/scores/Data-533_scores.csv"

    def test_get_student_scores(self):
        mock_open = mock.mock_open(read_data=SCORE_DATA)
        with mock.patch('builtins.open', mock_open):
            result = get_student_scores(self.course, self.student_number)
        # self.assertEqual(result, None)
        self.assertIsNotNone(result)

    def test_set_student_scores(self):
        mock_open = mock.mock_open(read_data=SCORE_DATA)
        with mock.patch('builtins.open', mock_open):
            result = set_student_scores(self.course, self.student_number, self.updated_score)
        self.assertEqual(result, None)

    def test_quiz_score_statistics(self):
        mock_open = mock.mock_open(read_data=SCORE_DATA)
        with mock.patch('builtins.open', mock_open):
            result = quiz_score_statistics(self.course)
        self.assertTrue(result, True)

    @mock.patch("teacher.checkstudentscores.input", create=True)
    def test_score_driver(self, mocked_input):
        mocked_input.side_effect = ["4"]
        result = score_driver()
        self.assertTrue(result, True)
    
    @mock.patch("teacher.checkstudentscores.input", create=True)
    def test_quiz_or_score(self, mock_input):
        mock_input.side_effect = ["3"]
        result = quiz_or_score()
        self.assertTrue(result, True)


    def tearDown(self):
        del self.course
        del self.student_number
        del self.updated_score
        del self.file_path

    @classmethod
    def tearDownClass(cls):
        print("In tearDownClass()")
    
unittest.main(argv=[''], verbosity=2, exit=False)