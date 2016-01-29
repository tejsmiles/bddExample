# -- FILE: features/environment.py
# USE: behave -D BEHAVE_DEBUG_ON_ERROR         (to enable  debug-on-error)
# USE: behave -D BEHAVE_DEBUG_ON_ERROR=yes     (to enable  debug-on-error)
# USE: behave -D BEHAVE_DEBUG_ON_ERROR=no      (to disable debug-on-error)
import os
from behaving import environment as benv
from selenium import webdriver
from behave import when
from behaving.web.steps import *
from behaving.sms.steps import *
from behaving.mail.steps import *
from behaving.personas.steps import *

default_browser = webdriver.Chrome()

def before_all(context):

    #basedir = os.path.join(os.path.dirname(__file__), 'tests')
    #desired_capabilities = webdriver.DesiredCapabilities.FIREFOX
    #context.browser = webdriver.Remote(
    #    desired_capabilities=desired_capabilities,
    #    command_executor="http://hub.testingbot.com:4444/wd/hub"
    #)
    #screenshots_dir = os.path.join(basedir, 'screenshots')
    context.browser = default_browser
    #context.screenshots_dir = screenshots_dir
    benv.before_all(context)


def _mkdir(path):
    return os.makedirs(path) if not os.path.exists(path) else None

def after_all(context):
    context.browser.quit()
    benv.after_all(context)
