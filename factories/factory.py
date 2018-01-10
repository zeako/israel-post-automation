from selenium.webdriver import *


# class DriverAdapter:
#     VENDOR_NAME = None
#
#     def __init__(self, options, driver):
#         self.options =
#         self.driver = driver
#
#     def __enter__(self):
#         return self.driver
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         self.driver.quit()
#
#     @classmethod
#     def check_vendor(cls, vendor_name):
#         return vendor_name == cls.VENDOR_NAME
#
#     def create(self):
#         raise NotImplementedError()
#
#
# class ChromeAdapter(DriverAdapter):
#     VENDOR_NAME = 'chrome'
#     DRIVER, OPTIONS = Chrome, ChromeOptions
#
#     def __init__(self):
#         super().__init__(self.OPTIONS, self.DRIVER)
#
#     def create(self):
#         pass
#         # def __init__(self, driver):
#         #     super().__init__(Chrome)
#
#
# class FirefoxAdapter(DriverAdapter):
#     VENDOR_NAME = 'firefox'
#
#
# class DriverFactory:
#     VENDORS = (ChromeAdapter, FirefoxAdapter)
#
#     def __init__(self, vendor_name):
#         self.vendor_name = vendor_name
#
#     def create(self):
#         for vendor in self.VENDORS:
#             if vendor.check_vendor(self.vendor_name):
#                 return vendor()

class DriverAdapter:
    VENDOR_NAME = None

    def __init__(self, driver):
        self.driver = driver

    def __enter__(self):
        return self.driver

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.driver.quit()


def driver_factory(driver_config):
    vendors = {
        'chrome': (Chrome, ChromeOptions),
        'firefox': (Firefox, FirefoxOptions)
    }

    def get_vendor_classes():
        for k, v in vendors.items():
            if k == driver_config['vendor']:
                return v
        else:
            raise Exception('supported driver must be supplied')

    def create_driver():
        driver_cls, options_cls = get_vendor_classes()
        options = options_cls()

        if driver_config['headless']:
            options.add_argument('--headless')

        driver = driver_cls(executable_path=driver_config['executable_path'],
                            options=options)
        driver.implicitly_wait(5)
        return driver

    return DriverAdapter(create_driver())
