from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

CATALOG_URL_PATH = "/component/monitor"
CARD_PRODUCT_URL_PATH = "/component/monitor/samsung-syncmaster-941bw"
LOGIN_ADMIN_PAGE_URL_PATH = "/admin"
REGISTER_PAGE_URL_PATH = "/index.php?route=account/register"


def test_main_page(driver):
    driver.get(driver.base_url)
    wait = WebDriverWait(driver=driver, timeout=5)
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div#slideshow0")))
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".slideshow div.swiper-button-next")))
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".slideshow div.swiper-button-prev")))
    wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "div[class*='swiper-pagination slideshow0'] span")))
    wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "#content .row .product-layout")))
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div[id = carousel0]")))
    wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "div[class*='swiper-pagination carousel0'] span")))
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".carousel div.swiper-button-next")))
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".carousel div.swiper-button-prev")))


def test_catalog(driver):
    driver.get(driver.base_url + CATALOG_URL_PATH)
    wait = WebDriverWait(driver=driver, timeout=5)
    wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "#column-left .list-group-item")))
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#list-view")))
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#grid-view")))
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#input-sort")))
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#input-limit")))
    wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "#content .product-layout")))


def test_card_product(driver):
    driver.get(driver.base_url + CARD_PRODUCT_URL_PATH)
    wait = WebDriverWait(driver=driver, timeout=5)
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "a[class='thumbnail']")))
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "ul[class$='nav-tabs']")))
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button[data-original-title*='Add to Wish List']")))
    wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "button[data-original-title*='Compare this Product']")))
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#input-quantity")))
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button[id='button-cart']")))


def test_login_admin_page(driver):
    driver.get(driver.base_url + LOGIN_ADMIN_PAGE_URL_PATH)
    wait = WebDriverWait(driver=driver, timeout=5)
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#input-username")))
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#input-password")))
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "span[class='help-block'] a")))
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button[class$='btn-primary']")))
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#footer a")))


def test_register_page(driver):
    driver.get(driver.base_url + REGISTER_PAGE_URL_PATH)
    wait = WebDriverWait(driver=driver, timeout=5)
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#input-firstname")))
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#input-lastname")))
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#input-email")))
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#input-telephone")))
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#input-password")))
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#input-confirm")))
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input[name='agree']")))
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input[value='Continue']")))
