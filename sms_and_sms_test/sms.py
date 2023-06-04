import csv
import os
import re

INVALID_PHONE_NUMBER = -1
INVALID_MESSAGE = -2


def send_sms(phone_number: str, message: str) -> int:
    if not validate_number(phone_number):
        return INVALID_PHONE_NUMBER
    if not validate_message(message):
        return INVALID_MESSAGE
    return process_message(phone_number, message)


def validate_number(phone_number: str) -> bool:
    return bool(re.match(r'^\+\d{1,3}\.\d{6,}$', phone_number))


def validate_message(message: str) -> bool:
    return len(message) <= 255


def process_message(phone_number: str, message: str) -> int:
    # Metoda pro zpracování zprávy
    # Implementace zde
    return 0


def send_sms_from_csv(csv_file_path: str) -> None:
    if not os.path.exists(csv_file_path):
        print(f"Soubor '{csv_file_path}' neexistuje.")
        return

    try:
        with open(csv_file_path, 'r') as file:
            reader = csv.reader(file, delimiter=';')
            for row in reader:
                if len(row) != 2:
                    print(f"Chybný formát záznamu v CSV souboru: {row}")
                    continue

                phone_number, message = row[0], row[1]
                result = send_sms(phone_number, message)
                if result != 0:
                    print(f"Chyba při odesílání SMS na číslo {phone_number}. Kód chyby: {result}")

    except IOError as e:
        print(f"Chyba při čtení souboru: {e}")


# Jak by vypadal skript

csv_file_path = input("Zadejte cestu k CSV souboru: ")
send_sms_from_csv(csv_file_path)



