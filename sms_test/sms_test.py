import unittest
from sms import sms


class SMSTestCase(unittest.TestCase):
    def test_send_sms_valid(self):
        phone_number = "+123.456789"
        message = "Test message"
        result = sms.send_sms(phone_number, message)
        self.assertEqual(result, 0)

    def test_send_sms_invalid_number(self):
        phone_number = "123456789"  # Neplatné telefonní číslo
        message = "Test message"
        result = sms.send_sms(phone_number, message)
        self.assertNotEqual(result, 0)

    def test_send_sms_invalid_message(self):
        phone_number = "+123.456789"
        message = ""  # Neplatná zpráva
        result = sms.send_sms(phone_number, message)
        self.assertNotEqual(result, 0)


if __name__ == '__main__':
    unittest.main()

