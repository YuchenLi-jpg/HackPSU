from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://bulletins.psu.edu/undergraduate/colleges/information-sciences-technology/#majorsminorsandcertificatestext")
print(driver.title)

# major_names = driver.find_elements_by_tag_name("span")
# print(major_names)

total = driver.find_elements_by_link_text("Cybersecurity Analytics and Operations, B.S. (Information Sciences and Technology)")
total[0].click()
#driver.find_element_by_xpath('//a[contains(@href,"/undergraduate/colleges/information-sciences-technology/cybersecurity-analytics-operations-bs/")]').click()
#search.send_keys(Keys.RETURN)

time.sleep(2)

driver.quit()
