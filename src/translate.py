import json
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from configs import get_driver_options, DEST_SENTENCES, DEST_TRANSLATED
import time
from selenium.webdriver.common.by import By
from pyperclip import paste


class GoogleTranslate:
    service = Service(ChromeDriverManager().install())
    SERVICE_OPTIONS = get_driver_options()

    def __init__(self) -> None:
        try:
            driver = webdriver.Chrome(
                service=self.service, options=self.SERVICE_OPTIONS)
            self.translate_en_to_mn(driver)
        except Exception as e:
            print(f'[-] Error: {e}')
        finally:
            self.die(driver)

    def translate_en_to_mn(self, driver):
        translated_data = []

        with open(DEST_SENTENCES, 'r') as f:
            data = json.load(f)

        print(f'[*] Translate len: {len(data)}')

        driver.get('https://translate.google.com/?sl=en&tl=mn')
        time.sleep(1)

        index = 0

        for sentence in data:
            if index != 0:
                driver.find_element(
                    By.XPATH, "//button[@aria-label='Clear source text']").click()
                time.sleep(0.5)
            driver.find_element(
                By.XPATH, '//textarea').send_keys(sentence['content'])
            time.sleep(2)
            driver.find_element(
                By.XPATH, "//button[@aria-label='Copy translation']").click()
            time.sleep(0.5)
            translated_text = paste()
            translated_data.append({
                'content': translated_text.lower(),
                'start': sentence['start'],
                'end': sentence['end'],
                'index': sentence['index']
            })
            # print(f'\t[*] Process: {index}')
            if index % 50 == 0:
                print(f'\t[*] Process: {index}')
            index += 1

        with open(DEST_TRANSLATED, 'w') as f:
            json.dump(translated_data, f, ensure_ascii=False, indent=2)

    @classmethod
    def translate(self, text: str):
        a = self.translator.translate(text, dest='mn', src='en')
        print(a.text)

    def die(self, driver) -> None:
        print('[+] Shutting down google translate')
        driver.stop_client()
        driver.close()
        driver.quit()
        self.service.stop()
