from urllib.parse import urljoin


from selenium import webdriver

from utilities.configurations import settings


class WebApp:
    instance = None

    @classmethod
    def get_instance(cls):
        if cls.instance is None:
            cls.instance = WebApp()
        return cls.instance

    def __init__(self):
        # if str(settings['browser']).lower() is "firefox":
        #     self.driver = webdriver.Firefox()
        # elif str(settings['browser']).lower() is "chrome":
            self.driver = webdriver.Chrome()
        # else:
        #     self.driver = webdriver.Firefox()

    def get_driver(self):
        return self.driver

    def load_website(self):
        self.driver.get('https://www.udemy.com/')

    def goto_page(self, page):
        self.driver.get('https://www.udemy.com/', page.lower())

    def verify_component_exists(self, component):
        # Simple implementation
        assert component in self.driver.find_element_by_tag_name('body').text, \
            "Component {} not found on page".format(component)


webapp = WebApp.get_instance()