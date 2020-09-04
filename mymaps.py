from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
import time
desired_Capabilites = {
   "deviceName": "9888da46375831354c",
   "platformName": "Android",
   "appPackage" : "com.google.android.apps.maps",
   "appActivity" : "com.google.android.maps.MapsActivity",
   "newCommandTimeout": 600
}
driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_Capabilites)
driver.implicitly_wait(50)
tap_screen = TouchAction(driver)

# 1st step - click on hamburger menu
driver.find_element_by_id("com.google.android.apps.maps:id/search_omnibox_menu_button").click()
time.sleep(1)

# 2nd step - click on Your places
tap_screen.tap(x=288,y=333).perform()
time.sleep(2)

# 3rd step - swipe right to Maps option
driver.swipe(1019,283,71,283)
time.sleep(1)

# 4th step - click on the Maps option
tap_screen.tap(x=964,y=288).perform()
time.sleep(1)

# 5th step - select desired My maps
tap_screen.tap(x=308,y=439).perform()
time.sleep(1)

# driver.find_element_by_id("com.google.android.apps.m4b:id/terms_accept_button").click()
# time.sleep(1)

"""
MyMaps
tap_screen.tap(x=121,y=2019).perform()
time.sleep(1)
tap_screen.tap(x=391,y=929).perform()
time.sleep(1)
tap_screen.tap(x=893,y=1327).perform()
time.sleep(2)
tap_screen.tap(x=373,y=343).perform()
time.sleep(1)
tap_screen.tap(x=373,y=343).perform()
time.sleep(3)
tap_screen.tap(x=964,y=1686).perform()
time.sleep(3)
driver.find_element_by_id("com.android.packageinstaller:id/permission_allow_button").click()
"""

file_coords = open(r"C:\Users\RickyCarrera\Desktop\coords.txt")
# print(file_coords.read())
longitude = []
latitude = []
altitude = []
for i in file_coords:
   row = i.split()
   longitude.append(row)
   latitude.append(row)
   altitude.append(row)

# Longitudes
longitudes=[longitudes[0].split(',') for longitudes in longitude]
longitudes_Split = [longitudes_Split[0].split(',') for longitudes_Split in longitudes]
# print(longitudes_Split)

# Latitude
latitudes = [latitudes[0].split(',') for latitudes in latitude]
latitudes_Split = [latitudes_Split[1].split(',') for latitudes_Split in latitudes]
# print(latitudes_Split)

# Altitude
Altitudes = [Altitudes[0].split(',') for Altitudes in altitude]
Altitudes_Split = [Altitudes_Split[2].split(',') for Altitudes_Split in Altitudes]
# print(Altitudes_Split[:])

for i in range(8):
   driver.set_location(latitudes_Split[i], longitudes_Split[i], Altitudes_Split[i])
   # print(latitudes_Split[i], longitudes_Split[i], Altitudes_Split[i])
   time.sleep(1)

for i in reversed(range(8)):
   driver.set_location(latitudes_Split[i], longitudes_Split[i], Altitudes_Split[i])
   time.sleep(1)