# import os
# from seleniumbase import BaseCase
# from sbvirtualdisplay import Display
# from seleniumbase import Driver
import time


# from seleniumbase import SB
#
# with SB(uc=True, test=True, incognito=True, locale="en", agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36") as sb:
#     url = "https://apply.workable.com/two95-international-inc-3/j/E91B0F3F46/apply/"
#     sb.uc_open_with_reconnect(url)  # The bot-check is later
#     try:
#         sb.uc_click('[data-ui="cookie-consent-accept"]')
#     except Exception as e:
#         print(f"Error clicking on cookie consent: {e}")
#     sb.uc_click('button[aria-haspopup="true"]')
#
#     time.sleep(5)
#
#     sb.choose_file('[id="file-upload"]', '/Users/talib/Documents/GitHub/resume.pdf')
#
#     time.sleep(20)
#
#     sb.type('[data-ui="lastname"]', 'Narsingarhwala')
#
#     sb.scroll_to('[data-ui="apply-button"]')
#
#     time.sleep(10)
#
#     sb.uc_click('[data-ui="apply-button"]')
#
#     time.sleep(5)
#     try:
#         sb.uc_click('[id^="turnstile-container-"] div')
#     except Exception as e:
#         print(f"Error clicking on Turnstile container: {e}")
#
#     time.sleep(1000)
#
#     sb.scroll_to('[data-ui="successful-submit"]')


    # sb.cdp.scroll_into_view('[data-ui="apply-button"]')
    # sb.type(input_field, "github.com/seleniumbase/SeleniumBase")
    # sb.reconnect(0.1)
    # sb.uc_click(submit_button, reconnect_time=4)
    # sb.uc_gui_click_captcha()
    # sb.wait_for_text_not_visible("Checking", timeout=12)
    # sb.highlight('p:contains("github.com/seleniumbase/SeleniumBase")')
    # sb.highlight('a:contains("Top 100 backlinks")')
    # sb.set_messenger_theme(location="bottom_center")
    # sb.post_message("SeleniumBase wasn't detected!")




# display = Display(visible=0, size=(1440, 1880))
# display.start()
# BaseCase.main(__name__, __file__)

# from seleniumbase import BaseCase
# BaseCase.main(__name__, __file__)
#
# class MyTestClass(BaseCase):
#     def test_basics(self):
#         url = "https://apply.workable.com/two95-international-inc-3/j/E91B0F3F46/apply/"
#         self.uc_open(url, uc=True)
#         try:
#             self.click('[data-ui="cookie-consent-accept"]')
#         except Exception as e:
#             print(f"Error clicking on cookie consent: {e}")
#         self.click('button[aria-haspopup="true"]')
#         # sb.cdp.find_element('button[aria-haspopup="true"]', best_match=False, timeout=10).mouse_click()
#         self.choose_file('[id="file-upload"]', '/Users/talib/Documents/GitHub/resume.pdf')
#         time.sleep(10)
#
#
#         sb.cdp.find_element('[data-ui="lastname"]', best_match=False, timeout=10).send_keys('Narsingarh wala')
#         #     sb.sleep(5)
#         #     sb.cdp.scroll_into_view('[data-ui="apply-button"]')
#         #     sb.sleep(5)
#         #     sb.cdp.find_element('[data-ui="apply-button"]', best_match=False, timeout=10).mouse_click()
#         #     # sb.cdp.find_element('[data-ui="apply-button"]', best_match=False, timeout=10).mouse_click()
#         #     sb.sleep(10)
#         #     try:
#         #         sb.cdp.find_element('[id^="turnstile-container-"] div', best_match=False, timeout=5).mouse_click()
#         #     except Exception as e:
#         #         print(f"Error clicking on reCAPTCHA: {e}")
#
#         #     sb.sleep(15)
#         #     sb.cdp.save_screenshot('abc.png', folder=None, selector=None)
#         #     sb.cdp.find_element('[data-ui="successful-submit"]', best_match=False, timeout=10)



# from seleniumbase import Driver
# import time
# driver = Driver(uc=True)
# url = "https://apply.workable.com/two95-international-inc-3/j/E91B0F3F46/apply/"
# driver.uc_open_with_reconnect(url, 4)
# try:
#     driver.uc_click('[data-ui="cookie-consent-accept"]', reconnect_time=4)
# except Exception as e:
#     print(f"Error clicking on cookie consent: {e}")
# driver.uc_click('button[aria-haspopup="true"]', reconnect_time=4)
# # sb.cdp.find_element('button[aria-haspopup="true"]', best_match=False, timeout=10).mouse_click()
# driver.type('[id="file-upload"]', '/Users/talib/Documents/GitHub/resume.pdf')
#
# time.sleep(10)
# # sb.cdp.find_element('[id="file-upload"]', best_match=False, timeout=10).send_file('/app/resume.pdf')
# driver.uc_gui_click_captcha()
# driver.quit()




from seleniumbase import SB

with SB(uc=True, test=True, locale="en") as sb:
    url = "https://apply.workable.com/two95-international-inc-3/j/E91B0F3F46/apply/"
    sb.activate_cdp_mode(url)
    try:
        sb.cdp.find_element('[data-ui="cookie-consent-accept"]', best_match=False, timeout=10).mouse_click()
    except Exception as e:
        print(f"Error clicking on cookie consent: {e}")
    sb.cdp.find_element('button[aria-haspopup="true"]', best_match=False, timeout=10).mouse_click()
    # sb.cdp.gui_click_element('button[aria-haspopup="true"]')
    sb.cdp.find_element('[id="file-upload"]', best_match=False, timeout=10).send_file('/Users/talib/Documents/GitHub/resume.pdf')
    sb.sleep(10)
    sb.cdp.find_element('[data-ui="lastname"]', best_match=False, timeout=10).send_keys('Narsingarh wala')
    sb.sleep(5)
    sb.cdp.scroll_into_view('[data-ui="apply-button"]')
    sb.sleep(5)
    sb.cdp.find_element('[data-ui="apply-button"]', best_match=False, timeout=10).mouse_click()
    # sb.cdp.find_element('[data-ui="apply-button"]', best_match=False, timeout=10).mouse_click()
    # sb.sleep(10)
    sb.uc_gui_handle_cf()
    try:
        sb.uc_gui_handle_cf()
        # sb.cdp.find_element('[id^="turnstile-container-"] div', best_match=False, timeout=5).mouse_click()
    except Exception as e:
        print(f"Error clicking on reCAPTCHA: {e}")
    
    sb.sleep(10)
    sb.cdp.save_screenshot('abc.png', folder=None, selector=None)
    sb.cdp.find_element('[data-ui="successful-submit"]', best_match=False, timeout=10)

# display.stop()

"""A complete end-to-end test for an e-commerce website."""
# from seleniumbase import BaseCase
# BaseCase.main(__name__, __file__)
#
#
# class MyTestClass(BaseCase):
#     def test_swag_labs(self):
#         self.open("https://www.saucedemo.com")
#         self.type("#user-name", "standard_user")
#         self.type("#password", "secret_sauce\n")
#         self.assert_element("div.inventory_list")
#         self.assert_exact_text("Products", "span.title")
#         self.click('button[name*="backpack"]')
#         self.click("#shopping_cart_container a")
#         self.assert_exact_text("Your Cart", "span.title")
#         self.assert_text("Backpack", "div.cart_item")
#         self.click("button#checkout")
#         self.type("#first-name", "SeleniumBase")
#         self.type("#last-name", "Automation")
#         self.type("#postal-code", "77123")
#         self.click("input#continue")
#         self.assert_text("Checkout: Overview")
#         self.assert_text("Backpack", "div.cart_item")
#         self.assert_text("29.99", "div.inventory_item_price")
#         self.click("button#finish")
#         self.assert_exact_text("Thank you for your order!", "h2")
#         self.assert_element('img[alt="Pony Express"]')
#         self.js_click("a#logout_sidebar_link")
#         self.assert_element("div#login_button_container")