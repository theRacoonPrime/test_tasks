import pytest
from sms_and_sms_test.sms import (INVALID_PHONE_NUMBER,
                                  send_sms,
                                  INVALID_MESSAGE,
                                  send_sms_from_csv,
                                  validate_message,
                                  validate_number)
from unittest.mock import patch


def test_send_sms_from_csv(tmpdir):
    csv_content = "123456789;Test message\n+420.123456789;Another message\n"
    csv_file = tmpdir.join("test.csv")
    csv_file.write(csv_content)

    with patch("builtins.print") as mock_print:
        send_sms_from_csv(str(csv_file))

    mock_print.assert_not_called()


@pytest.mark.parametrize(
    "message, expected_result",
    [
        ("", True),
        ("A" * 255, True),
        ("A" * 256, False),
    ]
)
@pytest.mark.parametrize(
    "phone_number, expected_result",
    [
        ("+420.123456789", True),
        ("(123)456-789-012", True),
        ("123456789", False),
        ("+420.1234567890", False),
        ("+420.1234567", False),
    ]
)
def test_validate_number(phone_number, expected_result):
    assert validate_number(phone_number) == expected_result


def test_validate_message(message, expected_result):
    assert validate_message(message) == expected_result


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
        ("420123456789", "Test message", INVALID_PHONE_NUMBER),
        ("(420)123456789", "Test message", INVALID_PHONE_NUMBER),

    ],
)
def test_send_sms(phone_number, message, expected_result):
    result = send_sms(phone_number, message)
    assert result == expected_result


if __name__ == "__main__":
    pytest.main()







