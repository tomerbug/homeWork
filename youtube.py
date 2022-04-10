import time
from selenium import webdriver
from selenium.webdriver.common.by import By



driver = webdriver.Chrome(executable_path="C:Users\\Tomer\\OneDrive\\Documents\\chromedriver.exe")
driver.get("https://www.youtube.com/")
time.sleep(7)
driver.find_element(by=By.XPATH,value='/html/body/ytd-app/div[1]/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/div[1]/div[1]/input').click()
driver.find_element(by=By.XPATH,value='/html/body/ytd-app/div[1]/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/div[1]/div[1]/input').send_keys('tell me why brooklyn 99')
driver.find_element(by=By.XPATH, value='//*[@id="search-icon-legacy"]').click()
time.sleep(5)
driver.find_element(by=By.XPATH,value='/html/body/ytd-app/div[1]/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-video-renderer[1]/div[1]').click()
time.sleep(5)
driver.find_element(by=By.XPATH,value='/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/ytd-comments/ytd-item-section-renderer/div[1]/ytd-comments-header-renderer/div[5]/ytd-comment-simplebox-renderer/div[1]/yt-formatted-string').click()

driver.close()
