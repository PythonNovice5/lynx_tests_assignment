import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from test_data.url_under_test import URLUnderTest


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name",
        action="store",
        default="chrome",
        help="Browser to use: chrome, firefox",
    )
    parser.addoption(
        "--headless", action="store_true", default=False, help="Headless browser"
    )


@pytest.fixture(scope="class", autouse=True)
def setup(request):
    global driver
    browser_name = request.config.getoption("browser_name")
    headless = request.config.getoption("headless")
    pytest.is_mobile = False
    if browser_name == "chrome":
        options = webdriver.ChromeOptions()
        options.add_argument("--disable-gpu")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--window-size=1920,1080")
        options.add_argument("--incognito")
        # options.add_experimental_option("detach", True)
        if headless:
            print("Tests running in headless mode")
            options.add_argument("--no-sandbox")
            options.add_argument("--headless")
            # options.add_experimental_option("detach", True)
        # driver = webdriver.Chrome(options=options)
        driver = webdriver.Chrome(service=Service(), options=options)
    elif browser_name == "firefox":
        # TODO: Add support for running firefox
        driver = webdriver.Firefox()

    driver.implicitly_wait(5)
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.execute_script("localStorage.clear();")
    driver.quit()


@pytest.fixture(params=URLUnderTest.sub_url)
def get_url_value(request):
    return request.param
