import json
from abc import ABCMeta, abstractmethod
from dataclasses import dataclass, field
from typing import List, Any

import pandas as pd
import datetime
import requests
import os
from bs4 import BeautifulSoup

@dataclass(init=True)
class Product:
    input_param: dict = field(default_factory=dict[str, Any])
    product_code: str = field(default_factory=str)
    type: str = field(default_factory=str)
    source: str = field(default_factory=str)
    url: str = field(init=False)
    product_data: dict = field(default_factory=str)

    @classmethod
    def from_dict(cls, product_param: dict[str, Any]):
        try:
            code = product_param["ProductCode"]
            ptype = product_param["Product Type"]
            src = product_param["Data Source"]
        except KeyError as e:
            raise KeyError(f"Missing required key: {e.args[0]}") from None

        return cls(
            input_param=product_param,
            product_code=code,
            type=ptype,
            source=src,
        )

    def __post_init__(self):
        if self.source == 'Boursorama': self.url = ("https://www.boursorama.com/cours/" + self.product_code)
        if self.source == 'FT': self.url = ("https://markets.ft.com/data/indices/tearsheet/summary?s="
                                            + self.product_code.replace(' ', ':'))


class ScrapperAbstract(metaclass=ABCMeta):
    @abstractmethod
    def _get_html_tag(self):
        raise NotImplemented

    @abstractmethod
    def _get_web_data(self) -> BeautifulSoup:
        raise NotImplemented

    @abstractmethod
    def get_data(self) -> dict[str, str]:
        raise NotImplemented


class Scrapper(ScrapperAbstract):

    def __init__(self, product: Product, headers_settings: dict):
        self._product_to_scrap = product
        self._headers = headers_settings
        self._web_data = BeautifulSoup()
        self._html_tag = list()
        self.__post_init__()

    def __post_init__(self):
        self._html_tag = self._get_html_tag()
        self._web_data = self._get_web_data()

    def _get_html_tag(self) -> List[List[str]]:
        """

        :return: tags for scrapping
        """
        pass

    def _get_web_data(self) -> BeautifulSoup:
        """

        :return: beautiful object to read html content
        """
        response = requests.get(url=self._product_to_scrap.url, headers=self._headers)
        return BeautifulSoup(response.text, 'html.parser')

    def get_data(self) -> dict[str, str]:
        """

        :return: dict data
        """
        pass


class FTScrapper(Scrapper):
    def _get_html_tag(self) -> dict:
        return {'timestamp_tag_type': 'div',
                'timestamp_tag_name': 'mod-disclaimer',
                'close_tag_type': 'span',
                'close_tag_name': 'mod-ui-data-list__value'
      }

    def get_data(self) -> dict[str, Any]:
        tags = self._get_html_tag()
        timestamp_layout = "Data delayed at least 15 minutes, as of "
        return_data = {'Product Code': self._product_to_scrap.product_code}
        return_data.update({"Timestamp": self._web_data.find(tags.get("timestamp_tag_type"),
                                                            {'class': tags.get("timestamp_tag_name")}).text.strip(timestamp_layout)})
        return_data.update({"Close": self._web_data.find(tags.get("close_tag_type"),
                                                        {'class': tags.get("close_tag_name")}).text})
        return return_data


class BoursoramaScrapper(Scrapper):
    def _get_html_tag(self) -> dict:
        return {'data_table_tag_type_general_info': 'div',
                'data_table_tag_name_general_info': 'c-faceplate',
                'attrs_general_info_dict': 'data-ist-init'}


    def get_data(self) -> dict[str, Any]:
        tags = self._get_html_tag()
        data_table_general_info = self._web_data.find(tags.get('data_table_tag_type_general_info'),
                                                        {'class': tags.get('data_table_tag_name_general_info')})

        general_info_dict = json.loads(data_table_general_info.attrs.get(tags.get("attrs_general_info_dict")))

        return_data = {'Product Code': self._product_to_scrap.product_code}
        return_data.update({"Timestamp": general_info_dict.get('tradeDate', None)})
        return_data.update({"Close": general_info_dict.get('last', None)})
        return_data.update({"Previous Close": general_info_dict.get('previousClose', None)})
        return_data.update({"1D Return": general_info_dict.get('variation', None)})

        return return_data



@dataclass(init=False)
class ScrapperLauncher(object):
    def __new__(cls, product_to_scrap: Product, headers_settings: dict) -> Scrapper:
        if product_to_scrap.source == "Boursorama":
            return BoursoramaScrapper(product_to_scrap, headers_settings)
        elif product_to_scrap.source == "FT":
            return FTScrapper(product_to_scrap, headers_settings)
        else:
            raise NotImplemented


if __name__ == "__main__":
    path = os.getcwd()
    headers_for_scrapping = {"User-Agent": "Mozilla/5.0", "Connection": "close"}

    product_list = [
                    {'ProductCode': "BTCS", 'Product Type': "Fund", 'Data Source': "Boursorama"},
                    {'ProductCode': "BTCT", 'Product Type': "Fund", 'Data Source': "Boursorama"},
                    {'ProductCode': "BRR CME", 'Product Type': "Index", 'Data Source': "FT"}
                    ]

    df_data = pd.DataFrame(
        data=[ScrapperLauncher(product_to_scrap=Product().from_dict(product_param=product_param),
                               headers_settings=headers_for_scrapping).get_data() for product_param in
              product_list]
    )

    df_data.to_excel(path + '_Extract_data_scrapped' + datetime.datetime.today().strftime('%m_%d_%Y') + '.xlsx',
                     sheet_name='Export_' + datetime.datetime.today().strftime('%m_%d_%Y'), index=False)