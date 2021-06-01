from selenium import webdriver

def createHeadLessFirefoxBrowser():
    options = webdriver.FirefoxOptions()
    options.add_argument('--headless')
    return webdriver.Firefox(options=options)

def before_all(context):

    context.browser = createHeadLessFirefoxBrowser()
    context.browser.implicitly_wait(1)
    context.browser.server_url = 'http://localhost:8000'

def after_all(context):

    context.browser.quit()

def before_feature(context, feature):

    pass