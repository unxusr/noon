from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import logging
import os
from allure_behave.hooks import allure_report

def before_scenario(context, scenario):

    # Choosing which browser to run the test on
    # If nothing provided in the command line Chrome will be the default 

    if 'browser' in context.config.userdata.keys():
        if context.config.userdata['browser'] is None:
            browser = 'chrome'
        else:
            browser = context.config.userdata['browser']
    else:
        browser = 'chrome'

    if browser == 'chrome':
        #chrome_options = Options()
        #chrome_options.add_argument("--kiosk")
        context.browser = webdriver.Chrome()
    elif browser == 'firefox':
        context.browser = webdriver.Firefox()

    context.browser.implicitly_wait(30)
    context.browser.maximize_window()
    context.browser.execute_script("return document.readyState")
    
    # On which environment will run the test
    # for now if nothing provided production will be the default

    if 'env' in context.config.userdata.keys():
        if context.config.userdata['env'] is None:
            env = 'production'
        else:
            env = context.config.userdata['env']
    else:
        env = 'production'

    if env == 'production':
        context.browser.get('https://noon.com/egypt-en')
    elif env == 'testing':
        context.browser.get('https://test.noon.com')
    elif env == 'staging':
        context.browser.get('https://stage.noon.com')

def after_scenario(context, scenario):
    print("scenario status: ", scenario.name, scenario.status)
    
    # taking screenshot for every failing scenario

    if scenario.status == "failed":
        if not os.path.exists("failed_scenarios_screenshots"):
            os.makedirs("failed_scenarios_screenshots")
        os.chdir("failed_scenarios_screenshots")
        context.browser.save_screenshot(scenario.name + "_failed.png")
    context.browser.quit()

