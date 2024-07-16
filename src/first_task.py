import typing as t
import aiohttp
import asyncio
import dataclasses
from tabulate import tabulate


@dataclasses.dataclass
class CountryInfo(list):
    name: str
    capital: str | None
    flag_png: str

    @classmethod
    def from_dict(cls, dict_: dict) -> t.Self:
        try:
            capital = ", ".join(dict_["capital"])
        except KeyError:
            capital = None

        return cls(name=dict_["name"]["common"], capital=capital, flag_png=dict_["flags"]["png"])


class Country:
    def __init__(self, url: str) -> None:
        self.url = url

    async def get_all_country(self) -> dict:
        async with aiohttp.ClientSession() as session:
            async with session.get(self.url) as response:
                return await response.json()

    async def get_countries(self) -> list[CountryInfo]:
        countries = []
        for country in await self.get_all_country():
            countries.append(CountryInfo.from_dict(country))
        return countries

    async def get_tabular_form(self) -> str:
        return tabulate(await self.get_countries(), headers=["Name", "Capital", "Flag PNG"])


if __name__ == "__main__":
    init = Country(url="https://restcountries.com/v3.1/all")
    print(asyncio.run(init.get_tabular_form()))
