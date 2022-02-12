
import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as Choptions
from selenium.webdriver.firefox.options import Options as FFoptions

@pytest.fixture(scope="class")
def init_driver(request):
    supported_browsers =['chrome','ch','headlesschrome','firefox','ff','headlessfirefox']
    browser=os.environ.get('BROWSER')
    print( f'browser setup {browser}')
    if not browser:
        raise Exception("The environment variable browser is not set to any browser!!")
    browser =browser.lower()
    if browser not in supported_browsers:
        raise Exception("Provided browser {} is not available in supported browser .."
                        "Please set valid browser {}".format(browser,supported_browsers))

    if browser in ('chrome','ch'):
        driver=webdriver.Chrome()
    elif browser in ('firefox','ff'):
        driver =webdriver.Firefox()
    elif browser in ('headlesschrome'):
        option_chrome=Choptions()
        option_chrome.add_argument('--disbale-gpu')
        option_chrome.add_argument('--no-sandbox')
        option_chrome.add_argument('--headless')
        driver= webdriver.Chrome(options=option_chrome)
    elif browser in ('headlessfirefox'):
        option_chrome=FFoptions()
        option_chrome.add_argument('--disbale-gpu')
        option_chrome.add_argument('--no-sandbox')
        option_chrome.add_argument('--headless')
        driver= webdriver.Firefox(options=option_chrome)

    request.cls.driver=driver
    yield
    #driver.quit()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    pytest_html = item.config.pluginmanager.getplugin("html")
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, "extra", [])
    if report.when == "call":
        # always add url to report
        extra.append(pytest_html.extras.url("http://www.example.com/"))
        xfail = hasattr(report, "wasxfail")
        if (report.skipped and xfail) or (report.failed and not xfail):
            # only add additional html on failure
            is_front_test= True if 'init_driver' in item.fixturenames else False
            if is_front_test:
                result_dir=os.environ.get('RESULT_DIR')
                if not result_dir:
                    raise('Environment variable RESULT_DIR is not set!!!')
                screenshot_path=os.path.join(result_dir,item.name + '.png')
                driver_fixture=item.funcargs['request']
                driver_fixture.cls.driver.save_screenshot(screenshot_path)
                extra.append(pytest_html.extras.image(screenshot_path))
        report.extra = extra
