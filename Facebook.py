from selenium import webdriver

# Launch Chrome Browser
driver = webdriver.Chrome()

# Navigate to Facebook Login Page
driver.get('https://www.facebook.com/')

# Find Email or Phone Number Input Field
email_field = driver.find_element_by_id('email')

# Enter Email or Phone Number
email_field.send_keys('your_email_or_phone_number')

# Find Password Input Field
password_field = driver.find_element_by_id('pass')

# Enter Password
password_field.send_keys('your_password')

# Find Login Button and Click It
login_button = driver.find_element_by_name('login')
login_button.click()

# Close the Browser
driver.quit()
