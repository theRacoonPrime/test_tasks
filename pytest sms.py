import pytest
import sms


def test_send_sms_valid():
    phone_number = "+123.456789"
    message = "Test message"
    result = sms.send_sms(phone_number, message)
    assert result == 0


def test_send_sms_invalid_number():
    phone_number = "123456789"  # Neplatné telefonní číslo
    message = "Test message"
    result = sms.send_sms(phone_number, message)
    assert result != 0


def test_send_sms_invalid_message():
    phone_number = "+123.456789"
    message = ""  # Neplatná zpráva
    result = sms.send_sms(phone_number, message)
    assert result != 0


if __name__ == '__main__':
    pytest.main()

