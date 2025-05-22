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
    sb.cdp.find_element('[id="file-upload"]', best_match=False, timeout=10).send_file('/Users/runner/app/resume.pdf')
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
