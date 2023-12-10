[![](https://img.shields.io/badge/Project-Crawler-blue.svg?style=plastic)](https://github.com/Junwu0615/Crawler-Keywords-And-Use-LineBot) 
[![](https://img.shields.io/badge/Language-Python-blue.svg?style=plastic)](https://www.python.org/) </br>
[![](https://img.shields.io/badge/Package-BeautifulSoup-green.svg?style=plastic)](https://pypi.org/project/beautifulsoup4/) 
[![](https://img.shields.io/badge/Package-Requests-green.svg?style=plastic)](https://pypi.org/project/requests/) 
[![](https://img.shields.io/badge/Package-Pandas-green.svg?style=plastic)](https://pypi.org/project/pandas/) 
[![](https://img.shields.io/badge/Package-ArgumentParser-green.svg?style=plastic)](https://pypi.org/project/argumentparser/) 

## STEP.1　CLONE
```
git clone https://github.com/Junwu0615/Web-Crawler-News.git
```

## STEP.2　RUN
```
python Web-Crawler-News.py -h
```

## STEP.3　HELP

- -h　Help: Show this help message and exit.
- -t　Type: Give a type | ex :

  - [台灣水庫](https://fhy.wra.gov.tw/ReservoirPage_2011/StorageCapacity.aspx)　|　[空氣品質](https://data.gov.tw/dataset/40448)　|　[天氣預報](https://opendata.cwb.gov.tw/index)　|　[牌告匯率](https://rate.bot.com.tw/xrt)
  - [台灣股票](https://tw.tradingview.com/markets/stocks-taiwan/market-movers-all-stocks/)　|　[世界指數](https://tw.tradingview.com/markets/indices/quotes-major/)　|　[世界股票](https://tw.tradingview.com/markets/world-stocks/worlds-largest-companies/)　|　[虛擬貨幣](https://tw.tradingview.com/markets/cryptocurrencies/prices-all/)
  - [ETF 市場](https://tw.tradingview.com/markets/etfs/funds-largest/)　|　[外匯市場](https://tw.tradingview.com/markets/currencies/rates-all/)　|　[期貨市場](https://tw.tradingview.com/markets/futures/quotes-all/)

- -p　PathandFilename: Give a path and file name | ex :　./filename.csv

## STEP.4　EXAMPLE
### I.　查詢台灣水庫現況
至 **台灣水庫** 網頁，將其內容抓下來到當前目錄，並命名 **台灣水庫當前現況.csv** 。
  - `-t` 台灣水庫
  - `-p` ./台灣水庫當前現況.csv
```
python Web-Crawler-News.py -t 台灣水庫 -p ./台灣水庫當前現況.csv
```
  - 台灣水庫當前現況.csv
  - ![台灣水庫當前現況.csv](/sample_img/01.PNG)

### II.　查詢台灣股票現況
至 **台灣股票** 網頁，將其內容抓下來至當前目錄的檔案夾 ( 股票 ) ，並命名 **台灣股票.csv** 。
  - `-t` 台灣股票
  - `-p` ./股票/台灣股票.csv
```
python Web-Crawler-News.py -t 台灣股票 -p ./股票/台灣股票.csv
```
  - 台灣股票.csv
  - ![台灣股票.csv](/sample_img/00.PNG)

## 抓取資訊來源
- [台灣水庫即時水情](https://water.taiwanstat.com/)
- [台灣銀行牌告匯率](https://rate.bot.com.tw/xrt)
- [氣象資料開放平台](https://opendata.cwb.gov.tw/index)
- [政府資料開放平台](https://data.gov.tw/)
- [TrandingView](https://tw.tradingview.com)

## 參考資源
- [STEAM 教育學習網 | 爬取臺灣銀行牌告匯率 | 爬取天氣預報](https://steam.oxxostudio.tw/)
