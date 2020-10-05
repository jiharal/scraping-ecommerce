import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()


for x in range(10):
    driver.get(f"https://shopee.co.id/search?keyword=sepeda&page={x+1}")
    time.sleep(10)
    elem = driver.find_element_by_class_name("row.shopee-search-item-result__items")
    total = elem.find_elements_by_class_name("col-xs-2-4.shopee-search-item-result__item")
    for item in total:
        body = driver.find_element_by_tag_name('body')
        body.send_keys(Keys.PAGE_DOWN)
        time.sleep(1)
        try:
            url = item.find_element_by_tag_name("a").get_attribute("href")
        except Exception as err:
            print(err)
            url = ""
        try:
            imgUrl = item.find_element_by_class_name("_39-Tsj._1tDEiO").find_element_by_tag_name("img").get_attribute("src")
        except Exception as err:
            print(err)
            imgUrl = ""
        try:
            name = item.find_element_by_class_name("O6wiAW").text
        except Exception as err:
            print(err)
            name = ""
        try:
            price = item.find_element_by_class_name("_2lBkmX").text
        except Exception as err:
            print(err)
            price = ""
        try:
            location = item.find_element_by_class_name("_3amru2").text
        except Exception as err:
            print(err)
            location = ""
        print(f"url-{url}")
        print(f"imgUrl-{imgUrl}")
        print(f"name-{name}")
        print(f"price-{price}")
        print(f"location-{location}")
driver.close()
