import requests
from bs4 import BeautifulSoup
import pandas

r=requests.get("http://pyclass.com/real-estate/rock-springs-wy/LCWYROCKSPRINGS/", headers={'User-agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0 Gecko/20100101 Firefox/61.0'})
c=r.content
soup=BeautifulSoup(c)
#all=soup.find_all("div",{"class":"propertyRow"})
#all[0].find("h4",{"class":"propPrice"}).text.replace("\n","").replace(" ","")
page_nr=soup.find_all("a",{"class":"Page"})[-1].text
print(page_nr)
l=[]
base_url="http://pyclass.com/real-estate/rock-springs-wy/LCWYROCKSPRINGS/t=0&s="
for page in range(0,int(page_nr)*10,10):
    print(base_url+str(page)+".html")
    r=requests.get(base_url+str(page)+".html", headers={'User-agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0 Gecko/20100101 Firefox/61.0'})
    c=r.content
    soup=BeautifulSoup(c,"html.parser")
    for item in all:
        df={}
        df["Address"]=item.find_all("span",{"class":"propAddressCollapse"})[0].text
        df["Locality"]=item.find_all("span",{"class":"propAddressCollapse"})[1].text
        df["Price"]=item.find("h4",{"class":"propPrice"}).text.replace("\n","").replace(" ","")
        try:
            df["Beds"]=item.find("span",{"class":"infoBed"}).find("b").text
        except:
            df["Beds"]=None
        try:
            df["Baths"]=item.find("span",{"class":"infoValueFullBath"}).find("b").text
        except:
            df["Baths"]=None
        try:
            df["Area"]=item.find("span",{"class":"infoSqFt"}).find("b").text
        except:
            df["Area"]=None
        try:
            df["HalfBaths"]=item.find("span",{"class":"infoValueHalfBath"}).find("b").text
        except:
            df["HalfBaths"]=None

        for columngroup in item.find_all("div",{"class":"columnGroup"}):
            for featuregroup, featurename in zip(columngroup.find_all("span",{"class":"featureGroup"}),columngroup.find_all("span",{"class":"featureName"})):
                if "Lot Size" in featuregroup.text:
                    df["Lot Size"]=featurename.text
        l.append(df)
    

dataframe=pandas.DataFrame(l)
dataframe.to_csv("Output.csv")