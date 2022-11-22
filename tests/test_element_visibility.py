from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

CATALOG_URL_PATH = "/component/monitor"
CARD_PRODUCT_URL_PATH = "/component/monitor/samsung-syncmaster-941bw"
LOGIN_PAGE_URL_PATH = "/index.php?route=account/login"
REGISTER_PAGE_URL_PATH = "/index.php?route=account/register"


def test_main_page(driver):
    driver.get(driver.base_url)
    wait = WebDriverWait(driver=driver, timeout=1)
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#logo")))
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#menu")))
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#search")))
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#top-links")))
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#cart")))


def test_catalog(driver):
    driver.get(driver.base_url + CATALOG_URL_PATH)
    wait = WebDriverWait(driver=driver, timeout=1)
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#column-left")))
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#content")))
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[class='col-md-2 col-sm-6 hidden-xs']")))
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[class='breadcrumb']")))
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[class='col-sm-6 text-right']")))


def test_card_product(driver):
    driver.get(driver.base_url + CARD_PRODUCT_URL_PATH)
    wait = WebDriverWait(driver=driver, timeout=1)
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[class='thumbnail']")))
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[class='nav nav-tabs']")))
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[class='tab-content']")))
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#button-cart")))
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[class='rating']")))


def test_login_page(driver):
    driver.get(driver.base_url + LOGIN_PAGE_URL_PATH)
    wait = WebDriverWait(driver=driver, timeout=1)
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#input-email")))
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#input-password")))
    wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Forgotten Password")))
    wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Continue")))
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input[value='Login']")))


def test_register_page(driver):
    driver.get(driver.base_url + REGISTER_PAGE_URL_PATH)
    wait = WebDriverWait(driver=driver, timeout=1)
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#input-firstname")))
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#input-lastname")))
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#input-email")))
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#input-telephone")))
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#input-password")))
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#input-confirm")))
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input[name='agree']")))
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input[value='Continue']")))
