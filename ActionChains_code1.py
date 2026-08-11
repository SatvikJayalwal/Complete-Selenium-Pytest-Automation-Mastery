# Hover, Drag & Drop, Double/Right click, Keyboard combos, Scrolling

# SELENIUM ACTIONCHAINS 
# Purpose: Used for complex, low-level human interactions (hovering, 
#          right-clicking, holding keys) that standard commands can't handle.
#
# *** THE GOLDEN RULE ***
# ActionChains only queue up commands in memory. NOTHING HAPPENS until you 
# append .perform() to the end of the chain to trigger the execution!


# CORE METHODS (Requires: from selenium.webdriver import ActionChains)
# 
# .move_to_element(elem)    -> Hovers the mouse over the center of the element.
#                              (Use case: Triggering CSS hover menus/tooltips)
#
# .context_click(elem)      -> Simulates a Right-Click on the element.
#                              (Use case: Opening custom context menus)
#
# .double_click(elem)       -> Simulates a Double-Click.
#                              (Use case: Highlighting text, opening files)
#
# .drag_and_drop(src, tgt)  -> Clicks source, holds, moves to target, releases.
#                              (Use case: File uploads, Kanban/Trello boards)
#
# .key_down(key)            -> Presses and holds a key down (e.g., Keys.SHIFT).
# .key_up(key)              -> Releases the held key.
#                              (Use case: Keyboard shortcuts, holding CTRL to click)
#
# .scroll_to_element(elem)  -> Native scrolling to bring element into viewport.
#                              (Note: Introduced in Selenium 4.2)
#
# EXAMPLE USAGE:
# actions = ActionChains(driver)
# actions.move_to_element(menu_hover).context_click(item).perform()


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
import time

driver = webdriver.Chrome()
driver.maximize_window()
actions = ActionChains(driver)

driver.get("https://the-internet.herokuapp.com/hovers")

image1 = driver.find_element(By.XPATH,"(//div[@class='figure']/img)[1]")

actions.move_to_element(image1).perform()

hidden_text = driver.find_element(By.XPATH,"(//div[@class='figcaption'])[1]")
if hidden_text.is_displayed() :
    print(f"Text is displayed : {hidden_text.text}")


time.sleep(1)

driver.get("https://the-internet.herokuapp.com/context_menu")

box = driver.find_element(By.ID,"hot-spot")
actions.move_to_element(box).context_click(box).perform()

wait = WebDriverWait(driver,10)
alert = wait.until(EC.alert_is_present())
print(f"Alert says : {alert.text}")
alert.accept()

driver.quit()