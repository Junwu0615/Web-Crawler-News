import os
import requests
import pandas as pd
from bs4 import BeautifulSoup
from argparse import ArgumentParser


def parse_args():
    parse = ArgumentParser()
    parse.add_argument("-t", "--type", 
                       help = "give a type | ex: '台灣水庫 / 空氣品質 / 天氣預報 / 牌告匯率 / 台灣股票 / 世界指數 / \n世界股票 / 虛擬貨幣 / ETF市場 / 外匯市場 / 期貨市場'", 
                       default = "type", type = str)   
    parse.add_argument("-p", "--pathANDname", 
                       help = "give a path and filename | ex: './filename.csv'", 
                       default = "filename.csv", type = str)
    args = parse.parse_args()
    return args

def mkdir(path):
    split_temp = path.split('/')
    path = path[:-len(split_temp[-1])]
    if path == './':
        pass
    else:
        folder = os.path.exists(path)
        if not folder:
            os.makedirs(path)
            print("建立成功")
        else:
            print(path+"目錄已存在")
        
def web_take_df_to_csv(type_, pathANDname):
    #web type
    if type_ == "台灣水庫":
        url = 'https://fhy.wra.gov.tw/ReservoirPage_2011/StorageCapacity.aspx'
    elif type_ == '台灣股票':
        url = 'https://tw.tradingview.com/markets/stocks-taiwan/market-movers-all-stocks/'
    elif type_ == '世界指數':
        url = 'https://tw.tradingview.com/markets/indices/quotes-major/'
    elif type_ == '世界股票':
        url = 'https://tw.tradingview.com/markets/world-stocks/worlds-largest-companies/'
    elif type_ == '虛擬貨幣':
        url = 'https://tw.tradingview.com/markets/cryptocurrencies/prices-all/'
    elif type_ == 'ETF市場':
        url = 'https://tw.tradingview.com/markets/etfs/funds-largest/'
    elif type_ == '外匯市場':
        url = 'https://tw.tradingview.com/markets/currencies/rates-all/'
    elif type_ == '期貨市場':
        url = 'https://tw.tradingview.com/markets/futures/quotes-all/'
    elif type_ == '空氣品質':
        url = 'https://data.moenv.gov.tw/api/v2/aqx_p_432?api_key=e8dd42e6-9b8b-43f8-991e-b3dee723a52d&limit=1000&sort=ImportDate%20desc&format=JSON'
    elif type_ == '天氣預報':
        url = 'https://opendata.cwb.gov.tw/api/v1/rest/datastore/F-C0032-001?Authorization=CWA-05929DE5-EBFA-4974-8727-C2CC8EB8E816&format=JSON'
    elif type_ == '牌告匯率':
        url = 'https://rate.bot.com.tw/xrt/flcsv/0/day'
    
    if type_ == '空氣品質': #有提供API
        data = requests.get(url)
        data_json = data.json()
        label = data_json['fields']
        records = data_json['records']
        label_list = []
        records_list = []
        for i, j in zip(label, records):
            label_list.append(i['info']['label'])
            records_list.append([j['sitename'],j['county'],j['aqi'], j['pollutant'],
            j['status'],j['so2'],j['co'],j['o3'],j['o3_8hr'],j['pm10'],j['pm2.5'],j['no2'],
            j['nox'],j['no'],j['wind_speed'],j['wind_direc'],j['publishtime'],j['co_8hr'],
            j['pm2.5_avg'],j['pm10_avg'],j['so2_avg'],j['longitude'],j['latitude'],j['siteid']])
    
        df = [label_list]
        for i in records_list:
            df.append(i)
        new_df = pd.DataFrame(df)
    
    elif type_ == '天氣預報': #有提供API
        data = requests.get(url)
        data_json = data.json()
        lists = data_json['records']['location']
        records_list = [["地點", "日期", "起始時間", "結束時間", "天氣狀況", "下雨機率", "最高溫度", "最低溫度", "體感"]]         
        for i in lists:
            for j in range(0, 3):
                name = i["locationName"]
                tag = i["weatherElement"]
                date = tag[0]['time'][j]['startTime'][:10]
                st = tag[0]['time'][j]['startTime'][10:]
                et = tag[0]['time'][j]['endTime'][10:]
                state = tag[0]['time'][j]['parameter']['parameterName']
                pop = tag[1]['time'][j]['parameter']['parameterName']
                mint = tag[2]['time'][j]['parameter']['parameterName']
                ci = tag[3]['time'][j]['parameter']['parameterName']
                maxt = tag[4]['time'][j]['parameter']['parameterName']
                records_list.append([name, date, st, et, state, pop, maxt, mint, ci])

        df = []
        for i in records_list:
            df.append(i)
        new_df = pd.DataFrame(df)

    else:
        #beautifulsoup
        headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'}
        cookies = {'over18':'1'}
        web = requests.get(url, headers = headers, cookies = cookies) 
        web.encoding = 'utf-8'

        if type_ == '牌告匯率':
            web = web.text
            lists = web.split('\n')
            records_list = []
            for i in lists:
                temp = i.split(',') 
                check = temp[0:4]+temp[11:14]
                records_list.append(check)
            df = []
            for i in records_list:
                df.append(i)
            new_df = pd.DataFrame(df)
            new_df = new_df.drop(index = new_df.index[-1])
            
        elif type_ == "台灣水庫":
            df = pd.read_html(url, encoding='utf-8',header=0)[0]
            new_df = df
            new_df = new_df.iloc[1:-1, 0:-1]
            new_df.columns = ["1", "2", "3", "4", "5", "6" , "7", "8", "9", "10", "11"]
            new_df = new_df[['1', '2', '8', '9', '10', '11']]
            new_df.columns = ["水庫名稱", "有效容量(萬立方公尺)", "水情時間", "水位(公尺)", "有效蓄水量(萬立方公尺)", "蓄水量百分比(%)"]
       
        else:
            df = pd.read_html(url, encoding='utf-8',header=0)[0]
            new_df = df
        
    #存儲csv檔
    #filename = '台灣水庫即時水情_webcrawler.csv'
    print(new_df)
    new_df.to_csv(pathANDname, encoding = 'utf-8-sig',index = True)


if __name__ == "__main__":
    args = parse_args()
    mkdir(args.pathANDname)
    web_take_df_to_csv(args.type, args.pathANDname)