import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

driver = None


def pytest_addoption(parser):
    parser.addoption(
        "--browser", action="store", default="chrome"
    )


@pytest.fixture(scope="class")
def setup(request):
    global driver
    browser = request.config.getoption("--browser")
    if browser == "chrome":
        options = Options()
        options.add_argument("--incognito")

        driver = webdriver.Chrome(options=options)
    elif browser == "firefox":
        driver = webdriver.Firefox()
    else:
        driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.delete_cookie("session")
    driver.delete_cookie("session.sig")
    driver.delete_all_cookies()

    driver.close()
    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        extra.append(pytest_html.extras.url("https://www.saucedemo.com/"))
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.rpartition("::")[2] + ".png"

            report_directory = os.path.join(os.path.dirname(os.path.abspath(__file__)), './Screenshots')
            os.makedirs(report_directory, exist_ok=True)
            file_path = os.path.join(report_directory,
                                     "fail_" + file_name)
            _capture_screenshot(file_path)

            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_path
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


def _capture_screenshot(name):
    driver.save_screenshot(name)
