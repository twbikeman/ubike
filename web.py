from selenium import webdriver
import time as computer_time
from bs4 import BeautifulSoup
# linux use linux_chromedrive
driver = webdriver.Chrome()
driver.implicitly_wait(10)


"""
46693.htm 陽明山 /北投
46691.htm 鞍部 /北投
46692.htm 臺北 / 中正
C0AC8.htm 文山 /文山
C0A98.htm 社子 /士林
C0A9A.htm 大直 /中山
C0A9B.htm 石牌 /北投
C0A9C.htm 天母 /士林
C0A9E.htm 士林 /士林
C0A9F.htm 內湖 /內湖
C0AC7.htm 信義 /信義
C0AC4.htm 大屯山 /北投
A0A46.htm 文化大學 /士林
C0AH4.htm 平等 /士林
A0A01.htm 臺灣大學 /大安
C0AH7.htm 松山 /松山
CAAH6.htm 大安森林 /大安
"""

sta ={'陽明山': '46693.htm', 
'鞍部': '46691.htm', 
'臺北': '46692.htm', 
'文山': 'C0AC8.htm', 
'社子': 'C0A98.htm', 
'大直': 'C0A9A.htm', 
'石牌': 'C0A9B.htm', 
'天母': 'C0A9C.htm',
'士林': 'C0A9E.htm',
'內湖': 'C0A9F.htm', 
'信義': 'C0AC7.htm', 
'大屯山': 'C0AC4.htm' ,
'文化大學': 'A0A46.htm' ,
'平等': 'C0AH4.htm' ,
'臺灣大學': 'A0A01.htm', 
'松山': 'C0AH7.htm', 
'大安森林': 'CAAH6.htm' 
}



for (i,j) in sta.items():
    driver.get('https://www.cwb.gov.tw/m/o/real/' + j)
    soup = BeautifulSoup(driver.page_source,'lxml')
    print('--------' + i + '----------')

    time = soup.select('#obs > div > p > span')
    tag_temp1 = soup.select('table.table.table-bordered > tbody > tr > td > span.temp1')

    recTemp = float(tag_temp1[0].string.strip())



    tag_td7 = soup.select('table.table.table-bordered > tbody > tr:nth-child(7) > td')
    tag_rain = soup.select("table.table.table-bordered > tbody > tr > td > font[color='black']")
    print('time:', time[0].string.strip(), sep=' ')
    print('temp:', recTemp, sep=' ')
    print('humidity:', tag_td7[0].string.strip(), sep=' ')
    print('rain:', tag_rain[0].string.strip(), sep=' ')

    computer_time.sleep(1)
driver.quit()
