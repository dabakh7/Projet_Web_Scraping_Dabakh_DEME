import requests
from bs4 import BeautifulSoup
import database
import math


url = 'https://fr.shopping.rakuten.com/nav/Tel-PDA_Telephones-mobiles/f1/Apple#ft=u&xtatc=PUB-[fonc]-[Header]-[c2c]-[telephonie]-[iphone-occasion]-[]-[]'
reponse = requests.get(url,headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'})
soup = BeautifulSoup(reponse.content,'html.parser')
tableau = soup.find_all(class_='productList_layoutContent_Q06')[0:7]

phones = []
for n in tableau:
    marque = n.find(class_ = 'description_styleTitle_KPO').text
    prix   = (n.find(class_ = 'f20').text.replace(' €',''))
    prix = round(float(prix.replace(',','.').replace(' ',''))*650)
    # print(prix)
    phones.append([marque,prix])
    for iphone in phones:
        print(iphone)
        tel = database.Telephone2(marque = iphone[0], prix = iphone[1])
        database.db.session.add(tel)
    database.db.session.commit()
        




    

