import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
    def setUp(self):
        question = "what language?"
        self.my_survey=AnonymousSurvey(question)
        self.responses=['Eng','france','china']


    def test_store_single_response(self):
        self.my_survey.store_responses(self.responses[0])
        self.assertIn(self.responses[0], self.my_survey.responses)
    def test_store_three_response(self):
        for response in self.responses:
            self.my_survey.store_responses(response)
        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)

if __name__ == '__main__':
    unittest


