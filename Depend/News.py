# -*- coding: utf-8 -*-
"""
@author: PC
Update Time: 2024-12-01
"""
import os, copy, json, requests
import pandas as pd

class News:
    def __init__(self, obj):
        self.type = obj.type
        self.pathname = obj.pathname
        self.download_path = './Downloads/'
        self.headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'}

    @staticmethod
    def check_folder(path: str):
        folder = os.path.exists(path)
        if not folder:
            os.makedirs(path)

    @staticmethod
    def get_source_url(source_type) -> str:
        if source_type == '台灣水庫':
            return 'https://fhy.wra.gov.tw/ReservoirPage_2011/StorageCapacity.aspx'
        elif source_type == '台灣股票':
            return 'https://tw.tradingview.com/markets/stocks-taiwan/market-movers-all-stocks/'
        elif source_type == '世界指數':
            return 'https://tw.tradingview.com/markets/indices/quotes-major/'
        elif source_type == '世界股票':
            return 'https://tw.tradingview.com/markets/world-stocks/worlds-largest-companies/'
        elif source_type == '虛擬貨幣':
            return 'https://tw.tradingview.com/markets/cryptocurrencies/prices-all/'
        elif source_type == 'ETF市場':
            return 'https://tw.tradingview.com/markets/etfs/funds-largest/'
        elif source_type == '外匯市場':
            return 'https://tw.tradingview.com/markets/currencies/rates-all/'
        elif source_type == '期貨市場':
            return 'https://tw.tradingview.com/markets/futures/quotes-all/'
        elif source_type == '空氣品質':
            api_key = 'e8dd42e6-9b8b-43f8-991e-b3dee723a52d'
            return f'https://data.moenv.gov.tw/api/v2/aqx_p_432?api_key={api_key}&limit=1000&sort=ImportDate%20desc&format=JSON'
        elif source_type == '天氣預報':
            api_key = 'CWA-05929DE5-EBFA-4974-8727-C2CC8EB8E816'
            return f'https://opendata.cwb.gov.tw/api/v1/rest/datastore/F-C0032-001?Authorization={api_key}&format=JSON'
        elif source_type == '牌告匯率':
            return 'https://rate.bot.com.tw/xrt/flcsv/0/day'
        else:
            return 'None'

    def preprocess(self, url):
        if self.type in ['空氣品質']:
            res = requests.get(url, headers=self.headers)
            loader = json.loads(res.text)
            count, title, content = 0, [], []
            for lab, rec in zip(loader['fields'], loader['records']):
                title += [lab['info']['label']]
                content += [rec['sitename'], rec['county'], rec['aqi'], rec['pollutant'], rec['status'],
                            rec['so2'], rec['co'], rec['o3'], rec['o3_8hr'], rec['pm10'], rec['pm2.5'],
                            rec['no2'], rec['nox'], rec['no'], rec['wind_speed'], rec['wind_direc'],
                            rec['publishtime'], rec['co_8hr'], rec['pm2.5_avg'], rec['pm10_avg'],
                            rec['so2_avg'], rec['longitude'], rec['latitude'], rec['siteid']]
            df = [title]
            for i in range(int(len(content)/len(title))):
                df += [content[count:count+24]]
                count = count + 24
            new_df = pd.DataFrame(df)

        elif self.type in ['天氣預報']:
            res = requests.get(url, headers=self.headers)
            loader = json.loads(res.text)
            records_list = [['地點', '日期', '起始時間', '結束時間', '天氣狀況', '下雨機率', '最高溫度', '最低溫度', '體感']]
            for i in loader['records']['location']:
                for idx in range(0, 3):
                    name = i['locationName']
                    tag = i['weatherElement']
                    date = tag[0]['time'][idx]['startTime'][:10]
                    st = tag[0]['time'][idx]['startTime'][10:]
                    et = tag[0]['time'][idx]['endTime'][10:]
                    state = tag[0]['time'][idx]['parameter']['parameterName']
                    pop = tag[1]['time'][idx]['parameter']['parameterName']
                    mint = tag[2]['time'][idx]['parameter']['parameterName']
                    ci = tag[3]['time'][idx]['parameter']['parameterName']
                    maxt = tag[4]['time'][idx]['parameter']['parameterName']
                    records_list.append([name, date, st, et, state, pop, maxt, mint, ci])
            new_df = pd.DataFrame(records_list)

        elif self.type in ['牌告匯率']:
            res = requests.get(url, headers=self.headers)
            res.encoding = 'utf-8'
            lists = res.text.split('\n')
            new_df = pd.DataFrame([i.split(',')[0:4] + i.split(',')[11:14] for i in lists])
            new_df = new_df.drop(index=new_df.index[-1])

        elif self.type in ['台灣水庫']:
            df = pd.read_html(url, encoding='utf-8', header=0)[0]
            new_df = df.iloc[1:-1, 0:-1]
            new_df.columns = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11']
            new_df = new_df[['1', '2', '8', '9', '10', '11']]
            new_df.columns = ['水庫名稱', '有效容量(萬立方公尺)', '水情時間', '水位(公尺)', '有效蓄水量(萬立方公尺)', '蓄水量百分比(%)']

        else:
            new_df = pd.read_html(url, encoding='utf-8', header=0)[0]

        print(new_df)
        new_df.to_csv(self.download_path + self.pathname, encoding='utf-8-sig', index=True)

    def main(self):
        News.check_folder(self.download_path)
        url = News.get_source_url(self.type)
        self.preprocess(url) if url != 'None' else print(f'Match Error... -> {self.type}')