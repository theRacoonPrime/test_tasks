import pytest
from sms_and_sms_test.sms import INVALID_PHONE_NUMBER, send_sms
from sms_and_sms_test.sms import INVALID_MESSAGE
from sms_and_sms_test.sms import validate_message
from sms_and_sms_test.sms import validate_number


@pytest.mark.parametrize(
    "csv_content",
    [
        "123456789;Test message\n+420.123456789;Another message\n",
        "987654321;Message 1\n+1.123456789;Message 2\n",
        "+123.456789;Message 3\n9876543210;Message 4\n",
    ]
)
def test_open_csv_file(tmpdir, csv_content):
    csv_file = tmpdir.join("test.csv")
    csv_file.write(csv_content)

    # Perform the open and read operation on the CSV file
    with open(csv_file, "r") as file:
        file_content = file.read()

    assert file_content == csv_content


@pytest.mark.parametrize(
    "phone_number, expected_result",
    [
        ("+420.123456789", True),  # Valid phone number format
        ("(123)456-789-012", True),  # Valid phone number format
        ("123456789", False),  # Invalid phone number format
        ("+420.1234567890", False),  # Invalid phone number length
        ("+420.1234567", False),  # Invalid phone number length
        ("+420.123456789", True),  # Valid phone number format
        ("+1.123456789", True),  # Valid phone number format
        ("+420.12.3456789", False),  # Invalid phone number format
        ("+420.1234.56789", False),  # Invalid phone number format
        ("+420.12345.6789", False),  # Invalid phone number format
        ("+420.123456.789", False),  # Invalid phone number format
    ]
)
def test_validate_number(phone_number, expected_result):
    assert validate_number(phone_number) == expected_result


@pytest.mark.parametrize(
    "phone_number",
    [
        "+420.123456789",
        "+1.123456789",
        "(123)456-789-012",
    ]
)
def test_validate_number_valid_cases(phone_number):
    assert validate_number(phone_number) == True


@pytest.mark.parametrize(
    "phone_number",
    [
        "123456789",
        "+420.1234567890",
        "+420.1234567",
        "+420.12.3456789",
        "+420.1234.56789",
        "+420.12345.6789",
        "+420.123456.789",
    ]
)
def test_validate_number_invalid_cases(phone_number):
    assert validate_number(phone_number) == False


@pytest.mark.parametrize(
    "message, expected_result",
    [
        ("", True),  # Empty message is valid
        ("A" * 255, True),  # Maximum allowed length is valid
        ("A" * 256, False),  # Length exceeding the limit is invalid
    ]
)
def test_validate_message(message, expected_result):
    assert validate_message(message) == expected_result


@pytest.mark.parametrize(
    "message",
    [
        "Valid message",
        "Another valid message",
        "Testing 123",
        "A" * 254,
    ]
)
def test_validate_message_valid_cases(message):
    assert validate_message(message) == True


@pytest.mark.parametrize(
    "message",
    [
        "A" * 257,
        "Too long message",
        "Invalid!@#$%^&*()",
        "",
    ]
)
def test_validate_message_invalid_cases(message):
    assert validate_message(message) == False


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





