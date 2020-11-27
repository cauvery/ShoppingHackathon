from applitools.selenium import Eyes, Target
from applitools.common.config import BatchInfo
from core_utils import log

''' Create the batch object and set the ID '''
b = BatchInfo("Holiday Shopping")
b.id = "Holiday Shopping"

logger = log.getLogger(__name__)


# Task 1: Main Page
def test_main_page(Mgr, driver_setup, eyes_setup):
    driver = driver_setup
    eyes = eyes_setup
    eyes.batch = b
    eyes.open(driver, "AppliFashion", "Test 1", {'width': 1200, 'height': 800})
    eyes.force_full_page_screenshot = True

    conf = Mgr["conf"]
    DEMO_APP_URL = conf["system"]["DEMO_APP_URL"]

    driver.get(DEMO_APP_URL)

    eyes.check_window("main page", Target.window().fully().with_name("main page"))


# Task 2: Filtered Product Grid
def test_filtered_product_grid(Mgr, driver_setup, eyes_setup):
    driver = driver_setup
    eyes = eyes_setup
    eyes.batch = b
    eyes.open(driver, "AppliFashion", "Test 2", {'width': 1200, 'height': 800})
    # eyes.force_full_page_screenshot = True

    conf = Mgr["conf"]
    DEMO_APP_URL = conf["system"]["DEMO_APP_URL"]

    driver.get(DEMO_APP_URL)

    driver.find_element_by_id("colors__Black").click()

    driver.find_element_by_xpath("//button[@id='filterBtn']").click()

    product_grid = driver.find_element_by_id("product_grid")
    eyes.check_region(product_grid, "filter by color")


# Task 3: Product Details test
def test_product_details(Mgr, driver_setup, eyes_setup):
    driver = driver_setup
    eyes = eyes_setup
    eyes.batch = b
    eyes.open(driver, "AppliFashion", "Test 3", {'width': 1200, 'height': 800})
    eyes.force_full_page_screenshot = True

    conf = Mgr["conf"]
    DEMO_APP_URL = conf["system"]["DEMO_APP_URL"]

    driver.get(DEMO_APP_URL)

    driver.find_element_by_id("product_1").click()

    eyes.check_window("product details", fully=True)
