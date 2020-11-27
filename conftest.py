import pytest
from applitools.common import ScreenOrientation

from core_utils import config, log
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import Chrome, DesiredCapabilities
import os

from applitools.selenium import (
    logger,
    VisualGridRunner,
    Eyes,
    Target,
    BatchInfo,
    BrowserType,
    DeviceName,
)

logger = log.getLogger(__name__)


def pytest_addoption(parser):
    parser.addoption("--env", action="store", default="v1",
                     help="options: v1 or v2 or dev")
    parser.addoption("--config-file", action="store", default=None,
                     help="specify your config file")


@pytest.fixture(scope="session", autouse=True)
def envopt(request):
    return request.config.getoption("--env")


@pytest.fixture(scope="session", autouse=True)
def configopt(request):
    return request.config.getoption("--config-file")


@pytest.fixture(scope="function")
def Mgr(request, envopt, configopt):
    env = envopt
    cf = config.getConfig(env=envopt)

    if configopt:
        cf = config.getConfig(config=configopt)
        env = cf["system"]["env"]

    return {"conf": cf,
            "env": env,
            "driver": None}


@pytest.fixture(scope="function", autouse=False)
def driver_setup(request):
    driver = Chrome(executable_path=ChromeDriverManager().install())
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


@pytest.fixture(scope="function", autouse=False)
def eyes_setup(request):
    # Create a runner with concurrency of 10
    ultrafast_grid_runner = VisualGridRunner(10)

    # Initialize Eyes with Ultrafast Grid Runner
    eyes = Eyes(ultrafast_grid_runner)

    # logger.set_logger( logger.StdoutLogger() )

    # Create SeleniumConfiguration.
    (
        eyes.configure
            .set_api_key(os.environ['APPLITOOLS_API_KEY'])  # APPLITOOLS_API_KEY
            .set_app_name("AppliFashion")
            .set_batch(BatchInfo("Holiday Shopping”"))
            .add_browser(1200, 800, BrowserType.CHROME)
            .add_browser(1200, 800, BrowserType.FIREFOX)
            .add_browser(1200, 800, BrowserType.EDGE_CHROMIUM)
            .add_browser(1200, 800, BrowserType.SAFARI)
            .add_device_emulation(DeviceName.iPhone_X, ScreenOrientation.PORTRAIT)
    )

    yield eyes

    results = eyes.close(False)
    # results = ultrafast_grid_runner.get_all_test_results()
    print(results)
    eyes.abort()
