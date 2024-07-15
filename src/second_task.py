import re

import requests
import json
from bs4 import BeautifulSoup


class Goods:
    def __init__(self, url):
        response = requests.get(url)
        self.url = url
        self.soup = BeautifulSoup(response.content, "html.parser")

    def get_header(self):
        return self.soup.find("h1", class_="x-item-title__mainTitle").find("span").text

    def get_photo_url(self):
        images = self.soup.find("div", class_="ux-image-carousel").find_all("img")
        images_url = []
        for image in images:
            images_url.append(image["data-zoom-src"])
        return images_url

    def get_url(self):
        return self.url

    def get_price(self):
        return self.soup.find("div", class_="x-price-primary").find("span").text

    def get_seller_name(self):
        return (
            self.soup.find("div", class_="x-sellercard-atf__info__about-seller").find("span").text
        )

    def get_shipping_value(self):
        value = self.soup.find(
            "div", class_="ux-labels-values__values col-9", string=re.compile(r".*\$.*")
        )
        if value is None:
            return "Does not shipping in Ukraine"
        else:
            return value

    def get_json(self):
        json_obj = {
            "header": self.get_header(),
            "photo_url": self.get_photo_url(),
            "url": self.get_url(),
            "price": self.get_price(),
            "seller_name": self.get_seller_name(),
            "shipping_value": self.get_shipping_value(),
        }
        return json.dumps(json_obj)
