from selenium import webdriver

from bs4 import BeautifulSoup

driver = webdriver.Chrome('./chromedriver')
driver.implicitly_wait(10)
driver.get('https://www.cwb.gov.tw/m/o/real/CAAH6.htm')

"""
46693.htm 陽明山
46691.htm 鞍部
46692.htm 臺北
C0AC8.htm 文山
C0A98.htm 社子
C0A9A.htm 大直
C0A9B.htm 石牌
C0A9C.htm 天母
C0A9E.htm 士林
C0A9F.htm 內湖
C0AC7.htm 信義
C0AC4.htm 大屯山
A0A46.htm 文化大學
C0AH4.htm 平等
A0A01.htm 臺灣大學
C0AH7.htm 松山
CAAH6.htm 大安森林
"""

soup = BeautifulSoup(driver.page_source,'lxml')

time = soup.select('#obs > div > p > span')
print('time:', time[0].string.strip()[7:], sep=' ')


# soup = BeautifulSoup(fp,'lxml')
tag_temp1 = soup.select('table.table.table-bordered > tbody > tr > td > span.temp1')
print('temp:', tag_temp1[0].string.strip(), sep=' ')

tag_td7 = soup.select('table.table.table-bordered > tbody > tr:nth-child(7) > td')
print('humidity:', tag_td7[0].string.strip(), sep=' ')


tag_rain = soup.select("table.table.table-bordered > tbody > tr > td > font[color='black']")
print('rain:', tag_rain[0].string.strip(), sep=' ')


driver.quit()