def get_all_open_tabs(driver):
    return driver.window_handles


def switch_to_last_tab(driver):
    all_tabs = get_all_open_tabs(driver)
    driver.switch_to.window(all_tabs[-1])
