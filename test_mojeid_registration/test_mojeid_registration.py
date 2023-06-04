import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

chromedriver_path = '~/Desktop/chromedriver_mac64/chromedriver'


class MojeIDRegistraceTest(unittest.TestCase):
    def setUp(self):
        service = Service(executable_path=chromedriver_path)
        self.driver = webdriver.Chrome(service=service)
        self.driver.get("https://mojeid.regtest.nic.cz/registration/")

    def tearDown(self):
        self.driver.quit()

    def test_registrace(self):
        wait = WebDriverWait(self.driver, 10)

        # Počkej, dokud se stránka nenačte a element nebude viditelný
        wait.until(EC.visibility_of_element_located((By.ID, "id_personal_data_first_name")))

        # Přidej krátkou prodlevu před vyhledáním elementu (volitelné)
        time.sleep(2)  # Upravte prodlevu podle potřeby

        # Vyplňte všechny povinné údaje
        self.driver.find_element(By.ID, "id_personal_data_first_name").send_keys("Jan")
        self.driver.find_element(By.ID, "id_personal_data_last_name").send_keys("Novák")
        self.driver.find_element(By.ID, "id_personal_data_email").send_keys("jan.novak@priklad.com")
        self.driver.find_element(By.ID, "id_personal_data_password").send_keys("Heslo123")

        # Odešli formulář
        registration_button = self.driver.find_element(By.XPATH, "//button[contains(text(),'Registrovat')]")
        registration_button.click()

        # Ověř validační zprávu u captcha
        captcha_error_message = wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".captcha-error"))
        ).text

        expected_error_message = "The control code does not agree, try again."
        self.assertEqual(captcha_error_message, expected_error_message)


if __name__ == "__main__":
    unittest.main()





