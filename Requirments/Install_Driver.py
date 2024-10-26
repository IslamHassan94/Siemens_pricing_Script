from selenium import webdriver

options = webdriver.EdgeOptions()
options.add_argument("--headless")  # Run Edge in headless mode
options.add_argument("--disable-gpu")  # Disable GPU for headless mode

print('Installing Edge Driver........')
driver = webdriver.Edge(options)
driver.get('https://www.google.com')
driver.quit()
print('Installation DONE..')
