import asyncio
import json
from pprint import pprint
from src.first_task import Country
from src.second_task import Goods


if __name__ == "__main__":
    selection = input(
        "1 тестове завдання - 1\n2 тестове завдання - 2\nНапишіть на натисніть enter: "
    )
    if selection == "1":
        init = Country(url="https://restcountries.com/v3.1/all")
        print(asyncio.run(init.get_tabular_form()))  # Відповідно до завдання таблиця.
    if selection == "2":
        while True:
            url = input("Надішліть мені url продукту: ")
            goods = Goods(url=url)
            print("------------------------------------------------------------")
            pprint(json.loads(goods.get_json()), compact=True)
            print("------------------------------------------------------------")
