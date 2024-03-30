from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from time import sleep


# Open the browser and navigate to the jQuery UI droppable page
driver = webdriver.Chrome()
driver.get("https://jqueryui.com/droppable/")

# Switch to the iframe containing the draggable elements
iframe = driver.find_element(By.TAG_NAME,"iframe")
driver.switch_to.frame(iframe)
sleep(2)

# Find the draggable element
draggable_element = driver.find_element(By.ID,"draggable")
sleep(2)

# Find the droppable element
droppable_element = driver.find_element(By.ID,"droppable")
sleep(2)

# Perform the drag and drop operation
action_chains = ActionChains(driver)
action_chains.drag_and_drop(draggable_element, droppable_element).perform()
sleep(10)

# Switch back to the default content
driver.switch_to.default_content()
sleep(10)

# Close the browser
driver.quit()