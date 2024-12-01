<a href='https://github.com/Junwu0615/Web-Crawler-News'><img alt='GitHub Views' src='https://views.whatilearened.today/views/github/Junwu0615/Web-Crawler-News.svg'> 
<a href='https://github.com/Junwu0615/Web-Crawler-News'><img alt='GitHub Clones' src='https://img.shields.io/badge/dynamic/json?color=success&label=Clone&query=count_total&url=https://gist.githubusercontent.com/Junwu0615/d1d16a79eeb95ac0c3e99a279c3b7365/raw/Web-Crawler-News_clone.json&logo=github'> </br>
[![](https://img.shields.io/badge/Project-Web_Crawler-blue.svg?style=plastic)](https://github.com/Junwu0615/Crawler-Keywords-And-Use-LineBot) 
[![](https://img.shields.io/badge/Language-Python_3.12.0-blue.svg?style=plastic)](https://www.python.org/) </br>
[![](https://img.shields.io/badge/Package-BeautifulSoup_4.12.2-green.svg?style=plastic)](https://pypi.org/project/beautifulsoup4/) 
[![](https://img.shields.io/badge/Package-Requests_2.31.0-green.svg?style=plastic)](https://pypi.org/project/requests/) 
[![](https://img.shields.io/badge/Package-Pandas_2.1.4-green.svg?style=plastic)](https://pypi.org/project/pandas/) 
[![](https://img.shields.io/badge/Package-ArgumentParser_1.2.1-green.svg?style=plastic)](https://pypi.org/project/argumentparser/) 

## STEP.1　CLONE
```python
git clone https://github.com/Junwu0615/Web-Crawler-News.git
```

## STEP.2　INSTALL PACKAGES
```python
pip install -r requirements.txt
```

## STEP.3　RUN
```python
python Entry.py -h
```
#If you encounter the following problems :
> ModuleNotFoundError: No module named 'python'.<br/>
> ModuleNotFoundError: No module named 'pip'. 
1. 去檢查 C:\Users\xxx\AppData\Local\Programs\Python 是否有檔案。
1. 若無，則去 [Python](https://www.python.org/downloads/) 官網下載並安裝。
1. 接著再次執行該指令；若一樣出現同樣錯誤，去 `系統環境變數` 當中新增 `2` 個路徑 ( Path ) 即可 :
    - C:\Users\ `xxx` \AppData\Local\Programs\Python\ `Python版本`
    - C:\Users\ `xxx` \AppData\Local\Programs\Python\ `Python版本` \Scripts

## STEP.4　HELP

- `-h` Help: Show this help message and exit.
- `-t` Type: Give a type | ex :
  - [台灣水庫](https://fhy.wra.gov.tw/ReservoirPage_2011/StorageCapacity.aspx)　|　[空氣品質](https://data.gov.tw/dataset/40448)　|　[天氣預報](https://opendata.cwb.gov.tw/index)　|　[牌告匯率](https://rate.bot.com.tw/xrt)
  - [台灣股票](https://tw.tradingview.com/markets/stocks-taiwan/market-movers-all-stocks/)　|　[世界指數](https://tw.tradingview.com/markets/indices/quotes-major/)　|　[世界股票](https://tw.tradingview.com/markets/world-stocks/worlds-largest-companies/)　|　[虛擬貨幣](https://tw.tradingview.com/markets/cryptocurrencies/prices-all/)
  - [ETF 市場](https://tw.tradingview.com/markets/etfs/funds-largest/)　|　[外匯市場](https://tw.tradingview.com/markets/currencies/rates-all/)　|　[期貨市場](https://tw.tradingview.com/markets/futures/quotes-all/)
- `-p` PathandFilename: Give a path and file name | ex :　./filename.csv

## STEP.5　EXAMPLE
### I.　查詢台灣水庫現況
至 **台灣水庫** 網頁，將其內容抓下來到 `downloads`，並命名 **台灣水庫當前現況.csv** 。
  - `-t` 台灣水庫
  - `-p` 台灣水庫當前現況.csv
```python
python Entry.py -t 台灣水庫 -p 台灣水庫當前現況.csv
```
  - 台灣水庫當前現況.csv
  - ![台灣水庫當前現況.csv](/sample/01.PNG)

### II.　查詢台灣股票現況
至 **台灣股票** 網頁，將其內容抓下來至 `downloads`，並命名 **台灣股票.csv** 。
  - `-t` 台灣股票
  - `-p` 股票/台灣股票.csv
```python
python Entry.py -t 台灣股票 -p 台灣股票.csv
```
  - 台灣股票.csv
  - ![台灣股票.csv](/sample/00.PNG)

## 抓取資訊來源
- [台灣水庫即時水情](https://water.taiwanstat.com/)
- [台灣銀行牌告匯率](https://rate.bot.com.tw/xrt)
- [氣象資料開放平台](https://opendata.cwb.gov.tw/index)
- [政府資料開放平台](https://data.gov.tw/)
- [TrandingView](https://tw.tradingview.com)

## 參考來源
- [STEAM 教育學習網 | 爬取臺灣銀行牌告匯率 | 爬取天氣預報](https://steam.oxxostudio.tw/)