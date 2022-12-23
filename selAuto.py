from selenium import webdriver
import pandas as pd
from selenium.webdriver.common.by import By
from time import sleep


class Auto:
    executable_path='/home/mrov/Scrapy/autostat/autostat/autostat/chromedriver'
    def __init__(self,url:str):
        self.url=url
        
        
    def GetJson(self):
        driver=webdriver.Chrome(executable_path='/home/mrov/Scrapy/autostat/autostat/autostat/chromedriver')
        driver.get(url=self.url)
        datadict={}
        try:
            datas=driver.find_element(By.CSS_SELECTOR,'.col.s12.m12.l6').find_elements(By.CSS_SELECTOR,'a')
            table = driver.find_element(By.CSS_SELECTOR,'.pad-top-6.ad-det')
            datadict["year"]=datas[1].text
            datadict["make"] =datas[2].text
            datadict["model"] =datas[3].text
            datadict["price"] = int(driver.find_element(By.CSS_SELECTOR,'.fnum').text.replace(" $","").replace(" ",""))
            datadict['mileage'] = int(table.find_elements(By.CSS_SELECTOR,'td')[1].text.replace(" մղոն",""))
        except:
            print('Error')
        return datadict
    
AllData=[]   
urls = []    
def GetAllAutos():
    driver = webdriver.Chrome('/home/mrov/Scrapy/autostat/autostat/autostat/chromedriver')    
    driver.get('https://auto.am/search/passenger-cars?q={"category":"1","page":"1","sort":"latest","layout":"list",\
        "user":{"dealer":"0","id":""},"make":["266"],"model":{"266":["2134"]},\
        "year":{"gt":"1911","lt":"2023"},"usdprice":{"gt":"0","lt":"100000000"},"mileage":{"gt":"10","lt":"1000000"}}')  
    span=driver.find_element(By.ID,"search-result")
    for i in range(5):
        for div in span.find_elements(By.CSS_SELECTOR,".card"):
            try:
                url=div.find_element('css selector','a').get_attribute('href')
                urls.append(url)
            except:
                continue
        if len(driver.find_elements(By.CSS_SELECTOR,'.waves-effect.clickable.nav'))==2:
                driver.find_elements(By.CSS_SELECTOR,'.waves-effect.clickable.nav')[1].click()
        else:
                driver.find_elements(By.CSS_SELECTOR,'.waves-effect.clickable.nav')[0].click()
            
def getAllData():
    GetAllAutos()
    for url in urls:
        auto=Auto(url)
        AllData.append(auto.GetJson())
    df=pd.DataFrame(AllData)
    df.to_csv('all_data.csv',index=False)

    
getAllData()