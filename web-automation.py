#SELENIUM TEST
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
opts = Options()
opts.set_headless()
assert opts.headless 
browser = Chrome(options=opts)
browser.get('https://duckduckgo.com')

#YO NEED CRHOMEDRIVER IN PATH!
# https://chromedriver.storage.googleapis.com/index.html?path=78.0.3904.70/

search_form = browser.find_element_by_id('search_form_input_homepage')
search_form.send_keys('socker.dev')
search_form.submit()
results = browser.find_elements_by_class_name('result')
print(results[0].text)
browser.close()
quit()