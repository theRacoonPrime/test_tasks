import csv


def send_sms(phone_number: str, message: str) -> int:
    # Metoda pro odeslání SMS
    # Implementace zde
    pass


def validate_number(phone_number: str) -> bool:
    # Metoda pro validaci telefonního čísla
    # Implementace zde
    pass


def validate_message(message: str) -> bool:
    # Metoda pro validaci zprávy
    # Implementace zde
    pass


def process_message(phone_number: str, message: str) -> int:
    # Metoda pro zpracování zprávy
    # Implementace zde
    pass


def send_sms_from_csv(csv_file_path: str) -> None:
    with open(csv_file_path, 'r') as file:
        reader = csv.reader(file, delimiter=';')
        for row in reader:
            if len(row) == 2:
                phone_number = row[0]
                message = row[1]
                if validate_number(phone_number) and validate_message(message):
                    result = send_sms(phone_number, message)
                    if result != 0:
                        print(f"Chyba při odesílání SMS na číslo {phone_number}. Kód chyby: {result}")
                else:
                    print(f"Chybný záznam v CSV souboru: {row}")
            else:
                print(f"Chybný formát záznamu v CSV souboru: {row}")

# Jak by vypadal skript


csv_file_path = input("Zadejte cestu k CSV souboru: ")
send_sms_from_csv(csv_file_path)

