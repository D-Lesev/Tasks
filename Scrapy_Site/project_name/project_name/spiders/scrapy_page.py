from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import scrapy
from scrapy.spiders import CrawlSpider


class CrawlingSpider(CrawlSpider):

    name = "clothes"

    # def start_requests(self):
    #     # Configure the Chrome WebDriver
    #     options = webdriver.ChromeOptions()
    #     options.add_argument("--headless")  # Run in headless mode without a GUI
    #     driver = webdriver.Chrome(options=options)
    #
    #     # Navigate to the URL
    #     driver.get("https://shop.mango.com/bg-en/women/skirts-midi/midi-satin-skirt_17042020.html")
    #
    #     # Wait for dynamically loaded content to appear (replace with appropriate conditions)
    #     WebDriverWait(driver, 10).until(
    #         EC.presence_of_element_located((By.CSS_SELECTOR, "div.dynamic-content"))
    #     )
    #
    #     # Get the updated page source
    #     updated_html = driver.page_source
    #
    #     # Close the WebDriver
    #     driver.quit()
    #
    #     # Pass the updated HTML to Scrapy for parsing
    #     yield scrapy.Request(url="https://shop.mango.com/bg-en/women/skirts-midi/midi-satin-skirt_17042020.html", callback=self.parse_item, body=updated_html)

    def start_requests(self):
        start_url = "https://shop.mango.com/bg-en/women/skirts-midi/midi-satin-skirt_17042020.html"
        yield scrapy.Request(url=start_url, callback=self.parse_item)

    def parse_item(self, response):
        yield {
            "name": response.css(".product-name::text").get(),
            "price": response.css(".sAobE qXIEx text-title-l::text").get(),
            "colour": response.css(".colors-info-name::text").get(),
            "size": response.css(".text-title-m gk2V5::text").get(),
        }
