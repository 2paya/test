from selenium import webdriver
import unittest
from selenium.webdriver.common.keys import Keys


class YandexSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    # Проверка на наличие поля поиска
    def test_01_input_field(self):

        driver = self.driver
        driver.get('https://yandex.ru')
        assert 'text' in driver.page_source

    # Проверка на наличие таблицы с подсказками
    def test_02_suggest_filed(self):

        driver = self.driver
        driver.get('https://yandex.ru')
        input_field = driver.find_element_by_id('text')
        input_field.send_keys('Тензор')
        assert 'suggest' in driver.page_source

    # Проверка, что первые пять результатов содержат ссылку
    def test_03_check_result(self):

        driver = self.driver
        driver.get('https://yandex.ru')
        input_field = driver.find_element_by_xpath('//*[@id="text"]')
        input_field.send_keys('Тензор')
        input_field.send_keys(Keys.ENTER)
        links = driver.find_elements_by_class_name('Path-Item')
        for link in links:
            while link != links[5]:
                assert "tensor.ru" in link.text

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()


class YandexImage(unittest.TestCase):

    def setUp(self):

        self.driver = webdriver.Chrome()

    # Проверка на наличие ссылки
    def test_04_image_field(self):

        driver = self.driver
        driver.get('https://yandex.ru')
        assert 'images' in driver.page_source

    # Проверка, что выполнен переход на юрл
    def test_05_url_image(self):

        driver = self.driver
        driver.get('https://yandex.ru')
        new_url_page = driver.find_element_by_xpath('//*[@data-id="images"]').get_attribute("href")
        driver.get(new_url_page)
        assert 'https://yandex.ru/images/' in driver.current_url

    # Проверка, при нажатии на первую категорю, в поле поиска верный текст
    def test_06(self):

        driver = self.driver
        driver.get('https://yandex.ru')
        new_url_page = driver.find_element_by_xpath('//*[@data-id="images"]').get_attribute("href")
        driver.get(new_url_page)
        first_category_element = driver.find_element_by_class_name('PopularRequestList-Item_pos_0')
        category_name = first_category_element.get_attribute("data-grid-text")
        url_category_element = first_category_element.find_element_by_class_name('Link').get_attribute("href")
        driver.get(url_category_element)
        input_field = driver.find_element_by_tag_name('input').get_attribute("value")
        assert category_name == input_field

    # Проверка, при нажатии на картинку она открывается
    def test_07(self):

        driver = self.driver
        driver.get('https://yandex.ru')
        new_url_page = driver.find_element_by_xpath('//*[@data-id="images"]').get_attribute("href")
        driver.get(new_url_page)
        first_category_element = driver.find_element_by_class_name('PopularRequestList-Item_pos_0')
        url_category_element = first_category_element.find_element_by_class_name('Link').get_attribute("href")
        driver.get(url_category_element)
        first_image = driver.find_element_by_class_name('serp-item_pos_0')
        url_first_image = first_image.find_element_by_tag_name('a').get_attribute("href")
        title_first_image = first_image.find_element_by_tag_name('a').find_element_by_tag_name('img').\
            get_attribute('alt')
        first_image.click()
        assert title_first_image in driver.page_source

# Проверка, при нажатии кнопки вперед картинка изменяется
#    def test_08(self):
#
#       driver = self.driver
#       driver.get('https://yandex.ru')
#       new_url_page = driver.find_element_by_xpath('//*[@data-id="images"]').get_attribute("href")
#       driver.get(new_url_page)
#       first_category_element = driver.find_element_by_class_name('PopularRequestList-Item_pos_0')
#       url_category_element = first_category_element.find_element_by_class_name('Link').get_attribute("href")
#       driver.get(url_category_element)
#       first_image = driver.find_element_by_class_name('serp-item_pos_0')
#       title_first_image = first_image.find_element_by_tag_name('a').find_element_by_tag_name('img').get_attribute(
#           'alt')
#       url_first_image = first_image.find_element_by_tag_name('a').get_attribute("href")
#       second_image = driver.find_elements_by_class_name('serp-item_pos_1')
#       title_second_image = second_image.find_element_by_tag_name('a').find_element_by_tag_name('img').get_attribute(
#           'alt')
#       driver.get(url_first_image)
#       first_image.send_keys(Keys.RIGHT)
#       assert title_first_image != title_second_image

    def tearDown(self):

        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
