import time
import requests
import io
from selenium import webdriver
from selenium.webdriver.common.by import By
from PIL import Image

# Enter your path to chromedriver.exe
PATH = ""

wd = webdriver.Chrome(PATH)


def get_images_from_google(wd, delay, max_images):
    def scroll_down(wd):
        wd.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(delay)

    url = "https://www.google.com/search?q=dogs&sxsrf=APwXEdfvBdfmxRbyjpGuC-xWnxXFBypCrw:1680527183781&source=lnms&tbm=isch&sa=X&ved=2ahUKEwiqh8zO443-AhXKSfEDHX8cCM4Q_AUoAXoECAEQAw&biw=1536&bih=722&dpr=1.25"
    wd.get(url)

    image_urls = set()
    skip = 0

    while len(image_urls) + skip < max_images:
        scroll_down(wd)

        thumbnails = wd.find_elements(By.CLASS_NAME, "Q4LuWd")

        for img in thumbnails[len(image_urls) + skip:max_images]:
            try:
                img.click()
                time.sleep(delay)
            except:
                continue

            images = wd.find_elements(By.CLASS_NAME, "KAlRDb")
            for image in images:
                if image.get_attribute("src") in image_urls:
                    max_images += 1
                    skip += 1
                    break

                if image.get_attribute("src") and "http" in image.get_attribute("src"):
                    image_urls.add(image.get_attribute("src"))
                    print("Found image!")

    return image_urls


def download_image(download_path, url, file_name):
    try:
        image_content = requests.get(url).content
        image_file = io.BytesIO(image_content)
        image = Image.open(image_file)
        file_path = download_path + file_name

        with open(file_path, "wb") as f:
            image.save(f, "JPEG")

        print("Success")
    except Exception as e:
        print("FAILED with - ", e)


urls = get_images_from_google(wd, 2, 10)

for i, url in enumerate(urls):
    download_image("", url, str(i) + ".jpg")

wd.quit()
