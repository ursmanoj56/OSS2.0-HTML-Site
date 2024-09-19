from _ast import arguments
from datetime import time

import pyautogui
import pyperclip
from selenium.common import TimeoutException
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common import window
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC




class BasePage:

    def __init__(self,driver):
        self.driver = driver

    def get_title(self):
        return self.driver.title

    def get_current_url(self):
        return self.driver.current_url

    def refresh_page(self):
        self.driver.refresh()

    def text_input(self, locator,text):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(locator)
        )
        element.clear()
        element.send_keys(text)

    def text_inputs(self, locator,text):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(locator)
        )
        element.send_keys(text)

    def click_button(self, locator):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(locator)
        )
        element.click()

    # def get_text(self, locator):
    #     element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
    #     return element.text

    def get_text(self, locator):
        try:
            element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
            return element.text
        except TimeoutException:
            return None  # Or return "" to handle it as an empty string

    def is_displayed(self, locator):
        try:
            element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator))
            self.driver.execute_script("arguments[0].style.zIndex = '1000';", element)
            return element.is_displayed()
        except:
            return False

    def scroll_into_view(self, locator):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator))
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def select_dropdown_option_by_visible_text(self, locator, visible_text):
        dropdown_element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator)) # find the dropdown element
        dropdown_select = Select(dropdown_element)  # create a Select object
        dropdown_select.select_by_visible_text(visible_text)

    def select_dropdown_option_by_index(self, locator, index):
        dropdown = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
        dropdown_select = Select(dropdown)
        dropdown_select.select_by_index(index)

    def select_dropdown_option_by_value(self, locator, value):
        dropdown = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
        dropdown_select = Select(dropdown)
        dropdown_select.select_by_value(value)

    def press_enter(self):
        ActionChains(self.driver).send_keys(Keys.ENTER).perform()

    def upload_file(self, locator, path):
        file_input = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
        file_input.send_keys(path)

    # def upload_image(self, locator, image_path):
    #     file_input = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
    #     file_input.click()
    #     # time.sleep(2)
    #     pyautogui.write(image_path)
    #     pyautogui.press('enter')
    #     # Enter the file path into the file input element
    #     file_input.send_keys(image_path)

    def upload_image(self, browse_button_locator, file_input_locator, image_path):
        # Click the "browse" button to trigger the file input
        browse_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(browse_button_locator))
        browse_button.click()

        # Locate the hidden file input element and upload the file
        file_input = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(file_input_locator))
        file_input.send_keys(image_path)

    def drag_and_drop_file(driver, target_locator,file_path):
        target = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(target_locator))
        ActionChains(driver).move_to_element(target).perform()

        target.click()
        time.sleep(2)
        pyautogui.write(file_path)
        pyautogui.press('enter')

    # def is_element_enabled(self, locator):
    #         element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
    #         element.is_enabled()

    def is_element_enabled(self, locator):
        try:
            element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator))
            return element.is_enabled()
        except:
            return False

    def clickable(self, locator):
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator))
            return True

    def javascript_click(self, locator):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator))
        self.driver.execute_script("arguments[0].click();", element)

    def upload_file_js(self,locator, file_path):
        file_input = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator))
        self.driver.execute_script("arguments[0].style.display = 'block';", file_input)
        self.driver.execute_script("arguments[0].scrollIntoView();", file_input)
        file_input.send_keys(file_path)

    def scroll_up(self):
       self.driver.execute_script("window.scrollTo(0, document.body.scrollTop);")

    def press_escape_key(self):
        action = ActionChains(self.driver)
        action.send_keys(Keys.ESCAPE).perform()

    def get_alert_text(self):
        alert = WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        return alert.text

    def take_screenshot(self, filename):
        self.driver.save_screenshot(filename)

    def press_tab(self):
        ActionChains(self.driver).send_keys(Keys.TAB).perform()

    def press_DOWN(self):
        ActionChains(self.driver).send_keys(Keys.ARROW_DOWN).perform()

    def is_selected(self, locator):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator))
        return element.is_selected()

    def scroll_down(self, pixels):
        self.driver.execute_script(f"window.scrollBy(0, {pixels});")

    def scroll_to_bottom(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def move_to_element(self, locator):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator))
        self.actions = ActionChains(self.driver)
        self.actions.move_to_element(element).perform()

    def switch_to_frame(self, frame_reference, timeout=10):
        WebDriverWait(self.driver, 10).until(EC.frame_to_be_available_and_switch_to_it(frame_reference))

    def switch_to_default_content(self):
        self.driver.switch_to.default_content()

    def is_element_selected(self, locator):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator))
        return self.driver.execute_script("return arguments[0].checked;", element)

    def get_css_property_value(self,locator, property_name):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator))
        return element.value_of_css_property(property_name)

    # def get_css_value_psudeo_element(self,locator,value):
    #     element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator))
    #     script = window.getComputedStyle(element, '::after').getPropertyValue(value)
    #     return self.driver.execute_script(script, element)

    def get_css_value_pseudo_element(self, locator, property_name):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator))
        script = """
        var element = arguments[0];
        var style = window.getComputedStyle(element, ':after');
        return style.getPropertyValue(arguments[1]);
        """
        return self.driver.execute_script(script, element, property_name)

    def deselect_checkbox(self, locator):
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator))
        script = """
           var element = arguments[0];
           element.checked = false;
           """
        self.driver.execute_script(script, element)

    def has_required_attribute(self, locator):
        """Check if the input field has the 'required' attribute."""
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator))
        return element.get_attribute('required') is not None

    def get_required_message(self, locator):
        # Locate the input field
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator))

        # Attempt to submit the form (you may need to adjust this depending on your form structure)
        element.submit()  # Assuming the input is within a form

        # Use JavaScript to get the validation message
        message = self.driver.execute_script("return arguments[0].validationMessage;", element)

        return message

    def is_element_disabled(self, locator):
        """Check if the element is disabled."""
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator))
        return element.get_attribute("disabled") is not None

    def is_checkbox_checked(self, locator):
        """Check if the checkbox is checked."""
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator))
        return element.get_attribute("checked") is not None







