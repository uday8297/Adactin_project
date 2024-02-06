from selenium import webdriver
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

# Initialize the WebDriver
driver = webdriver.Chrome()

#maximize the window

driver.maximize_window()

#Open a webpage
driver.get('https://adactinhotelapp.com/')



#Find the register button
driver.find_element(By.LINK_TEXT,"New User Register Here").click()


time.sleep(2)

#Find input fields and fill
username_input = driver.find_element(By.ID, 'username')
username_input.send_keys('udaysair')

username_input=driver.find_element(By.ID,'password')
username_input.send_keys('Uday@8297')

confirm_password=driver.find_element(By.ID,'re_password')
confirm_password.send_keys('Uday@8297')

full_name = driver.find_element(By.ID,'full_name')
full_name.send_keys('Uday Sairam')

email_address = driver.find_element(By.ID,'email_add')
email_address.send_keys('udaysairammuthyala@gmail.com')

captcha_text=driver.find_element(By.ID,'captcha-form')
captcha_text.send_keys('@jkjkjk')

check_box = driver.find_element(By.ID,'tnc_box')
check_box.click()

register_submit = driver.find_element(By.ID,'Submit')
register_submit.click()

#Navigating back to login home page
back_to_login_page = driver.find_element(By.LINK_TEXT,'Go back to Login page')
back_to_login_page.click()

#Login page credentials
username_input = driver.find_element(By.ID, 'username')
username_input.send_keys('udaysair')

username_input=driver.find_element(By.ID,'password')
username_input.send_keys('Uday@8297')

#Submit login button
login_button = driver.find_element(By.ID,'login')
login_button.click()


#selecting dropdowns
location_dropdown = Select(driver.find_element(By.ID,'location'))

#select an option by visibilty
location_dropdown.select_by_visible_text('Sydney')

Hotels_dropdown = Select(driver.find_element(By.ID,'hotels'))

Hotels_dropdown.select_by_visible_text('Hotel Creek')
Hotels_dropdown.select_by_visible_text('Hotel Sunshine')

time.sleep(2)

Room_dropdown = Select(driver.find_element(By.ID,'room_type'))
Room_dropdown.select_by_value('Standard')

time.sleep(1)

No_of_rooms = Select(driver.find_element(By.ID,'room_nos'))
No_of_rooms.select_by_value('2')

Check_in_Date = driver.find_element(By.ID,'datepick_in')
Check_in_Date.send_keys('06/02/2024')


Check_out_Date = driver.find_element(By.ID,'datepick_out')
Check_out_Date.send_keys('08/02/2024')

Adults_per_room = Select(driver.find_element(By.ID,'adult_room'))
Adults_per_room.select_by_value('2')

Child_per_room = Select(driver.find_element(By.ID,'child_room'))
Child_per_room.select_by_value('3')

driver.find_element(By.ID,'Submit').click()

driver.find_element(By.ID,'radiobutton_0').click()

#driver.find_element(By.ID,'cancel').click()

driver.find_element(By.ID,'continue').click()

#Book a hotel

driver.find_element(By.NAME,'first_name').send_keys('Uday')
driver.find_element(By.NAME,'last_name').send_keys('M')
driver.find_element(By.NAME,'address').send_keys('vijayawada')
driver.find_element(By.NAME,'cc_num').send_keys('1234567891234567')
Select(driver.find_element(By.NAME,'cc_type')).select_by_visible_text('American Express')
Select(driver.find_element(By.NAME,'cc_exp_month')).select_by_index(1)
Select(driver.find_element(By.NAME,'cc_exp_year')).select_by_value('2028')
driver.find_element(By.ID,'cc_cvv').send_keys('1234')


driver.find_element(By.ID,'book_now').click()
#driver.find_element(By.ID,'cancel').click()

#driver.find_element(By.ID,'search_hotel').click()


time.sleep(10)

current_url = driver.current_url
print("Current Url:", current_url)

#close the webdriver
driver.quit()
