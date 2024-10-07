from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Set the path to the ChromeDriver executable
DRIVER_PATH = '/path/to/chromedriver'

# Initialize Chrome WebDriver options
chrome_options = Options()
chrome_options.add_argument('--headless')  # Run Chrome in headless mode

# Initialize the Chrome WebDriver
driver = webdriver.Chrome(executable_path=DRIVER_PATH, options=chrome_options)

# Navigate to a URL
driver.get('https://google.com')

# Perform actions, such as extracting page content
page_content = driver.page_source

# Close the browser
driver.quit()
