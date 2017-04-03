from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import sys
import os

from bom_parser2 import *
#Requestor
admin_name = "Alec Kanyuck"
admin_email = "alec@gmail.com"
pi_name = "Satyandra Gupta"
#Vendor
vendor_name = "Vendor Name"
#Items: do some sort of struct
print ("Selenium webdriver Version: %s" % (webdriver.__version__))

validFile = 0;
while (validFile == 0):
    if sys.version_info < (3, 0):
        bomFile = raw_input("Path to BOM file (format .tsv): ")
    else:
        bomFile = input("Path to BOM file (format .tsv): ")
    if os.path.isfile(bomFile):
        validFile = 1;
        print bomFile
    else:
        print "Incorrect file path"


driver = webdriver.Chrome("./chromedriver")
driver.get("http://viterbi.usc.edu/intranet/vba/rth-business-center/create_request.php")
#driver.get('http://www.google.com/xhtml');

# Switch into iFrame
iframe = driver.find_element_by_name('purchaserequest')
driver.switch_to_frame(iframe)

# Requestor information
admin_name_input = driver.find_element_by_id('admin_name')
admin_name_input.send_keys(admin_name)

admin_email_input = driver.find_element_by_id('admin_email')
admin_email_input.send_keys(admin_email)

pi_name_dropdown = Select(driver.find_element_by_id('pi_faculty_id'))
pi_name_dropdown.select_by_visible_text(pi_name)

# Vendor information
vendor_name_input = driver.find_element_by_id('vendor_name')
vendor_name_input.send_keys(vendor_name)

# Items to order
p = BomParser(bomFile)
parts = p.getItems()

i = 1
for p in parts:
    elem = driver.find_element_by_id("item_number_" + str(i))
    elem.send_keys(i)

    elem = driver.find_element_by_id("item_description_" + str(i))
    elem.send_keys(p.name)

    elem = driver.find_element_by_id("item_quantity_" + str(i))
    elem.clear()
    elem.send_keys(p.quantity_to_order)

    elem = driver.find_element_by_id("item_cost_" + str(i))
    elem.clear()
    elem.send_keys(str(p.cost))

    if i < len(parts):
        elem = driver.find_element_by_id("btnAdd")
        elem.click()
    i += 1

# For opening a new tab

#driver.switch_to.default_content()
#driver.execute_script("window.open('http://google.com', 'new_window')")
#driver.switch_to_window(driver.window_handles[-1])
# Additional Information
