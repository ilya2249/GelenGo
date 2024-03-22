def parserRestaurants():    
    from time import sleep
    from urllib.parse import unquote
    import re
    import pandas as pd
    from selenium import webdriver
    from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
    from selenium.webdriver.common.by import By
    from selenium.webdriver.remote.webdriver import WebDriver
    from selenium.webdriver.remote.webelement import WebElement
    main_banner = '/html/body/div[2]/div/div/div[3]/div[1]/div/div/div/div[2]'
    cookie_banner = '/html/body/div[2]/div/div/div[3]/footer/div[2]'
    items_count = '/html/body/div[2]/div/div/div[1]/div[1]/div[2]/div/div/div[2]/div/div/div/div[1]/header/div[3]/div/div[1]/div/div/a/span'
    main_blockXPATH = '/html/body/div[2]/div/div/div[1]/div[1]/div[2]/div/div/div[2]/div/div/div/div[2]/div[2]/div[1]/div/div/div/div[2]/div'
    titleXPATH = '/html/body/div[2]/div/div/div[1]/div[1]/div[2]/div[2]/div/div/div/div/div[2]/div[2]/div/div[1]/div/div/div/div/div[1]/h1/span[1]'
    phone_btn = '/html/body/div[2]/div/div/div[1]/div[1]/div[2]/div[2]/div/div/div/div/div[2]/div[2]/div/div[1]/div/div/div/div/div[2]/div[2]/div[1]/div[1]/div/div[3]/div[2]/div/button'
    phoneXPATH = '/html/body/div[2]/div/div/div[1]/div[1]/div[2]/div[2]/div/div/div/div/div[2]/div[2]/div/div[1]/div/div/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div[2]/div/a/bdo'
    addressXPATH = '/html/body/div[2]/div/div/div[1]/div[1]/div[2]/div[2]/div/div/div/div/div[2]/div[2]/div/div[1]/div/div/div/div/div[2]/div[2]/div[1]/div/div/div[1]/div[2]/div/div[2]/div[1]'
    next_page_btn = '/html/body/div[2]/div/div/div[1]/div[1]/div[2]/div[1]/div/div[2]/div/div/div/div[2]/div[2]/div[1]/div/div/div/div[3]/div[2]/div[2]'
    typeXPATH = '/html/body/div[2]/div/div/div[1]/div[1]/div[2]/div[2]/div/div/div/div/div[2]/div[2]/div/div[1]/div/div/div/div/div[1]/div[3]/span/span'
    descriptionXPATH = '/html/body/div[2]/div/div/div[1]/div[1]/div[2]/div[2]/div/div/div/div/div[2]/div[2]/div/div[1]/div/div/div/div/div[1]/div[5]/div/div[1]'
    imgXPATH = '/html/body/div[2]/div/div/div[1]/div[1]/div[2]/div[1]/div/div[2]/div/div/div/div[2]/div[2]/div[1]/div/div/div/div[2]/div/div[1]/div/div[1]/div/div[1]/div[2]/div'
    ratingXPATH = '/html/body/div[2]/div/div/div[1]/div[1]/div[2]/div[2]/div/div/div/div/div[2]/div[2]/div/div[1]/div/div/div/div/div[1]/div[4]/div/div[2]'

    



    def get_element_text(driver: WebDriver, path: str) -> str:
        try:
            return driver.find_element(By.XPATH, path).text
        except NoSuchElementException:
            return ''
    def get_element(driver: WebDriver, path: str) -> str:
        try:
            return driver.find_element(By.XPATH, path)
        except NoSuchElementException:
            return ''


    def move_to_element(driver: WebDriver, element: WebElement | WebDriver) -> None:
        try:
            webdriver.ActionChains(driver).move_to_element(element).perform()
        except StaleElementReferenceException:
            pass


    def element_click(driver: WebDriver | WebElement, path: str) -> bool:
        try:
            driver.find_element(By.XPATH, path).click()
            return True
        except:
            return False


    
    search_query = 'рестораны%20геленджик'
    url = f'https://2gis.ru/gelendzhik/search/{search_query}'
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(url)
    element_click(driver, main_banner)
    element_click(driver, cookie_banner)
    count_all_items = int(get_element_text(driver,items_count))
    pages = 7
    ParseDataRests = []
    for _ in range(pages):
        main_block = driver.find_element(By.XPATH, main_blockXPATH)
        count_items = len(main_block.find_elements(By.XPATH, 'div'))
        for item in range(1, count_items + 1):
            if main_block.find_element(By.XPATH, f'div[{item}]').get_attribute('class'):
                continue
            item_clicked = element_click(main_block, f'div[{item}]/div/div[2]')
            if not item_clicked:
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                element_click(main_block, f'div[{item}]/div/div[2]')
            title = get_element_text(driver, titleXPATH)
            phone_btn_clicked = element_click(driver, phone_btn)
            type = get_element_text(driver,typeXPATH)
            phone = get_element_text(driver, phoneXPATH) if phone_btn_clicked else ''
            rating = get_element_text(driver, ratingXPATH) 
            move_to_element(driver, main_block)
            link = unquote(driver.current_url)
            description = get_element_text(driver, descriptionXPATH)
            address = get_element_text(driver, addressXPATH)
            img = get_element(driver,imgXPATH)
            style_attribute = img.get_attribute('style')
            url = re.findall(r'url\(["\']?(.*?)["\']?\)', style_attribute)
            if type == 'Рестораны':
                type = 'Ресторан'
            elif (type.split(' '))[0]=='Ресторан':
                type = 'Ресторан'
            try:
                rating_value = float(rating)
                if rating_value>4.5:
                    RatingType = 'Отлично'
                elif rating_value>3.5:
                    RatingType = 'Хорошо'
                else:
                    RatingType = 'Удовлетворительно'
            except:
                RatingType = 'Не указано'
            RestKeys = {
                'type': type,
                "RatingType": RatingType,
                'rating': rating,
                'phone':phone,
                'adress': address,
                'title' : title,
                'description': description,
                'link': link,
                'img': url[0]
            }
            ParseDataRests.append(RestKeys)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        element_click(driver, next_page_btn)
        sleep(0.5)
    driver.quit()
    return ParseDataRests
        

