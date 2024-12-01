# -*- coding: utf-8 -*-
"""
@author: PC
Update Time: 2024-11-24
"""
from argparse import ArgumentParser, Namespace

class AP:
    def __init__(self, obj):
        self.obj = obj

    @staticmethod
    def parse_args() -> Namespace:
        parse = ArgumentParser()
        parse.add_argument("-t", "--type",
                           help="give a type | ex: '台灣水庫 / 空氣品質 / 天氣預報 / 牌告匯率 / 台灣股票 / "
                                "世界指數 / 世界股票 / 虛擬貨幣 / ETF市場 / 外匯市場 / 期貨市場'",
                           default="台灣水庫", type=str)

        parse.add_argument("-p", "--pathname",
                           help="give a path and filename | ex: './filename.csv'",
                           default="filename.csv", type=str)

        return parse.parse_args()

    def config_once(self):
        args = AP.parse_args()
        self.obj.type = args.type
        self.obj.pathname = args.pathname