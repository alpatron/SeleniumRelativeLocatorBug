from selenium import webdriver
from selenium.webdriver.support.relative_locator import locate_with
from selenium.webdriver.common.by import By
from pathlib import Path

driver = webdriver.Chrome()
driver.get(Path('bug.html').absolute().as_uri()) # Computes a file:// URI to the bug.html file; replace with a hardcoded path if there are problems with this.
driver.find_element(
    locate_with(By.ID,"rect1").near({By.ID:"rect2"})
)
driver.close()