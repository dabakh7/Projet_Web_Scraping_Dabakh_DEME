import requests
from bs4 import BeautifulSoup
import database




url = 'https://www.jumia.sn/telephone-tablette/?q=apple'
reponse = requests.get(url)
soup = BeautifulSoup(reponse.content,'html.parser')
tableau = soup.find_all(class_='info')[0:15]
# print(tableau)



produits = []
for i in tableau:
    marque = i.find('h3').text
    prix = i.find('div', class_='prc').text.replace(' FCFA','')
    # produits['marque'] = marque
    # produits['prix'] = prix
    produits.append([marque,prix])
produits.pop(9)

for donne in produits:
    print(donne)
    marque = database.Telephone1(marque = donne[0], prix = donne[1])
    database.db.session.add(marque)
database.db.session.commit()


    

























#     produit=[]
#     for j in tableau[i]:
#         # v=tableau[i].find('h3',class_="name")
#         print(j)
#     break
# #         produit.append(j.text)
#     produits.append(produit)
# print(tableau)

# for m in produits:
#     prix = m[0].replace(' FCFA','')
#     print(prix)

# marques = []
# for k in range(len(tableau)):
#     marque = []
#     for m in tableau[k].find_all('h3',{"class":"name"}):
#         marque.append(m.text)
#     marques.append(marque)
# # print(marques)

# for nom in marques:
#     noms = nom[0]
#     print(noms)


