import pytest
import re

INVALID_PHONE_NUMBER = -1
INVALID_MESSAGE = -2


def validate_number(phone_number: str) -> bool:
    return bool(re.match(r'^\+\d{3}\.\d{9}$', phone_number))


def validate_message(message: str) -> bool:
    return len(message) <= 255


def send_sms(phone_number: str, message: str) -> int:
    if not validate_number(phone_number):
        return INVALID_PHONE_NUMBER
    if not validate_message(message):
        return INVALID_MESSAGE
    # Implementace odeslání SMS
    return 0


@pytest.mark.parametrize(
    "phone_number, message, expected_result",
    [
        ("+420.123456789", "Test message", 0),
        ("123456789", "Test message", INVALID_PHONE_NUMBER),
        ("+420.1234567890", "Test message", INVALID_PHONE_NUMBER),
        ("+420.1234567", "Test message", INVALID_PHONE_NUMBER),
        ("+420.123456789", "Some text in sms.", INVALID_MESSAGE),
        ("+1.123456789", "Test message", 0),
        ("+420.123456789", "A" * 256, INVALID_MESSAGE),
        ("+420.123456789", "Test message", 0),
        ("+420.12.3456789", "Test message", INVALID_PHONE_NUMBER),
        ("+420.1234.56789", "Test message", INVALID_PHONE_NUMBER),
        ("+420.12345.6789", "Test message", INVALID_PHONE_NUMBER),
        ("+420.123456.789", "Test message", INVALID_PHONE_NUMBER),
        ("+420.12..3456789", "Test message", INVALID_PHONE_NUMBER),
        ("+420.12345..6789", "Test message", INVALID_PHONE_NUMBER),
        ("+420.123456..789", "Test message", INVALID_PHONE_NUMBER),
        ("+420.12 3456 789", "Test message", INVALID_PHONE_NUMBER),
        ("+420.1234 56789", "Test message", INVALID_PHONE_NUMBER),
        ("+420.1234567 89", "Test message", INVALID_PHONE_NUMBER),
        ("+420 123456789", "Test message", INVALID_PHONE_NUMBER),
        ("+420123456789", "Test message", INVALID_PHONE_NUMBER),
        ("+420.12345678A", "Test message", INVALID_PHONE_NUMBER),
        ("+420.123,456789", "Test message", INVALID_PHONE_NUMBER),
        ("+420.123@456789", "Test message", INVALID_PHONE_NUMBER),
        ("+420.123456789!", "Test message", INVALID_PHONE_NUMBER),
        ("+420.12345#6789", "Test message", INVALID_PHONE_NUMBER),
        ("+420.12$3456789", "Test message", INVALID_PHONE_NUMBER),
        ("+420.1^3456789", "Test message", INVALID_PHONE_NUMBER),
        ("+420.12345&6789", "Test message", INVALID_PHONE_NUMBER),
        ("+420.123456=789", "Test message", INVALID_PHONE_NUMBER),
    ],
)
def test_send_sms(phone_number, message, expected_result):
    result = send_sms(phone_number, message)
    assert result == expected_result


if __name__ == "__main__":
    pytest.main()



