import unittest
from chatbot import get_response

class TestChatbotResponses(unittest.TestCase):

    def test_booking_response(self):
        self.assertEqual(
            get_response("how can I book an appointment?"), 
            "You can book an appointment through our website, by calling us, or through our social media pages."
        )

    def test_unknown_question_response(self):
        self.assertEqual(
            get_response("unknown question"), 
            "Thank you for leaving your message. We will contact you soon."
        )

    def test_opening_hours_response(self):
        self.assertEqual(
            get_response("what are your opening hours?"), 
            "We are open from 10 AM to 7 PM, Monday through Saturday."
        )

    def test_payment_methods_response(self):
        self.assertEqual(
            get_response("how can I pay for services?"), 
            "You can pay for services via cash, card, or mobile payment apps such as eSewa and Khalti."
        )

if __name__ == '__main__':
    unittest.main()
