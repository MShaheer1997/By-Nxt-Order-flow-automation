from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Initialize the Chrome driver
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")  # Maximizing window
driver = webdriver.Chrome(options=options)

# Initialize the Chrome driver
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")  # Maximizing window
driver = webdriver.Chrome(options=options)

# Credentials
username = "shaheer.m@brandigo.co.uk"
password = "Shaheer@123"
Postcode = "New York, NY 10003, USA"
Apartment_House_No = "318A Commercial Road"
Addressdetails = "London"
Step1_url = "https://s-7080.bynext.co/order-home-cleaning/#/"

# Open the website
driver.get(Step1_url)

# Wait for the login button and click it
login_button = WebDriverWait(driver, 50).until(
    EC.element_to_be_clickable(
        (By.XPATH, "/html[1]/body[1]/div[1]/div[1]/header[1]/div[1]/div[1]/a[2]"))
)
login_button.click()
print("Clicked login button!")
time.sleep(5)
# Wait for username input and enter username
username_input = WebDriverWait(driver, 50).until(
    EC.presence_of_element_located(
        (By.XPATH, "(//input[@placeholder='Enter your email'])[1]"))
)
username_input.send_keys(username)
print("Entered username!")
time.sleep(5)
# Locate and enter password
password_input = WebDriverWait(driver, 25).until(
    EC.presence_of_element_located(
        (By.XPATH, "(//input[@placeholder='Your password'])[1]"))
)
password_input.send_keys(password)
print("Entered password!")
time.sleep(5)
# Locate and click login submit button
login_submit = WebDriverWait(driver, 50).until(
    EC.element_to_be_clickable(
        (By.XPATH, "(//button[normalize-space()='Login'])[1]"))
)
login_submit.click()
print("Submitted login form!")
time.sleep(5)

# Click Book Now Button
Book_Now = WebDriverWait(driver, 50).until(
    EC.element_to_be_clickable(
        (By.XPATH, "((//a[normalize-space()='Book Now'])[1])")
    ))
Book_Now.click()
print("Click Book Now Button")
time.sleep(5)

# Select Service
Select_Service = WebDriverWait(driver, 50).until(
    EC.element_to_be_clickable(
        (By.TAG_NAME, "figure"))
)
Select_Service.click()
time.sleep(5)
print("Service Selected")

# Select address
Select_Address = WebDriverWait(driver, 50).until(
    EC.element_to_be_clickable(
        (By.XPATH, "(//i[@class='caret pull-right'])[1]"))
)
Select_Address.click()
time.sleep(5)
print("Searching Adress")

SelectAddress_input = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable(
        (By.CSS_SELECTOR, "div[id='ui-select-choices-row-1-8'] a[class='ui-select-choices-row-inner']"))
)
SelectAddress_input.click()
time.sleep(5)
print("Adress Selected")

Next_Button = WebDriverWait(driver, 50).until(
    EC.element_to_be_clickable(
        (By.XPATH, "//a[normalize-space()='NEXT']"))
)
Next_Button.click()
time.sleep(5)
print("Click Next Button")

# Choose Service
Choose_one_service = WebDriverWait(driver, 50).until(
    EC.element_to_be_clickable(
        (By.XPATH, "(//div[@class='action'])[1]"))
)
Choose_one_service.click()
time.sleep(5)
print("Wash and Fold Service Selected")

# Choose Service
Choose_one_service = WebDriverWait(driver, 50).until(
    EC.element_to_be_clickable(
        (By.XPATH, "(//div[@class='action'])[2]"))
)
Choose_one_service.click()
time.sleep(5)
print("Laundred Shirt Service Selected")


Next_Button = WebDriverWait(driver, 50).until(
    EC.element_to_be_clickable(
        (By.XPATH, "(//a[normalize-space()='NEXT'])[1]"))
)
Next_Button.click()
time.sleep(5)
print("Click Next Button")


# Click Checkbox for leaving bag at your door?
Click_Checkbox = WebDriverWait(driver, 50).until(
    EC.element_to_be_clickable(
        (By.XPATH, "(//div[@class='custom-checkbox'])[3]"))
)
Click_Checkbox.click()
print("Click for leaving bag at your door?")

OK_Button = WebDriverWait(driver, 50).until(
    EC.element_to_be_clickable(
        (By.XPATH, "(//button[normalize-space()='OK, GREAT'])[1]"))
)
OK_Button.click()
time.sleep(5)

# Click Checkbox for delivery by your door?
Click_Checkbox = WebDriverWait(driver, 50).until(
    EC.element_to_be_clickable(
        (By.XPATH, "(//div[@class='custom-checkbox'])[7]"))
)
Click_Checkbox.click()
print("Click for delivery by your door?")

OK_Button = WebDriverWait(driver, 50).until(
    EC.element_to_be_clickable(
        (By.XPATH, "(//button[normalize-space()='OK, GREAT'])[1]"))
)
OK_Button.click()
time.sleep(5)

Next_Button = WebDriverWait(driver, 50).until(
    EC.element_to_be_clickable(
        (By.XPATH, "(//a[normalize-space()='NEXT'])[1]"))
)
Next_Button.click()
print("Click Next Button")
time.sleep(5)

Add_tip = WebDriverWait(driver, 50).until(
    EC.element_to_be_clickable(
        (By.XPATH, "(//label[normalize-space()='$0'])[1]"))
)
Add_tip.click()
print("Add Tip")
time.sleep(5)


# Click Place Order Button
Place_Order = WebDriverWait(driver, 50).until(
    EC.element_to_be_clickable(
        (By.XPATH, "/html[1]/body[1]/div[1]/div[1]/section[1]/div[2]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/a[1]"))
)
Place_Order.click()
print("Order has been placed")

# Order confirmation Done
Order_Confirm = WebDriverWait(driver, 50).until(
    EC.element_to_be_clickable(
        (By.LINK_TEXT, "DONE"))
)
Order_Confirm.click()
print("Order confirmation")

time.sleep(50)  # Allow time to observe

driver.quit()

# Wait for the postcode input field and enter postcode
'''postcode_input = WebDriverWait(driver, 40).until(
    EC.element_to_be_clickable(
        (By.XPATH, "(//input[@id='address'])[1]"))
)
postcode_input.clear()
postcode_input.send_keys(Postcode)
print(" Postcode entered.")

time.sleep(20)

#postcode_input = WebDriverWait(driver, 40).until(
    #EC.presence_of_element_located(
        #(By.CLASS_NAME, "(//div[@class='form-group cfg'])[1]"))
)
#postcode_input.click()'''
# Allow UI to process input

'''Apartment_House_No = WebDriverWait(driver, 40).until(
    EC.element_to_be_clickable(
        (By.ID, "apt"))
).click()'''
