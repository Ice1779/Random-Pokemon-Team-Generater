from bs4 import BeautifulSoup
import requests
import random
r=requests.get("https://pokemondb.net/pokedex/national")
print("Starting script...")
soup=BeautifulSoup(r.content,'html.parser')
allpokes=soup.find_all("a",class_="ent-name")
allpokes=[x.text for x in allpokes]
nums=soup.find_all("small")
nums=[z.text for z in nums]
numsfornums=[]
lp=0
nums2=[]
teamnums=[]
typesfortypes=[]
for x in nums:
    if nums.index(x)%2==0:
        numsfornums.append(x.strip("#"))
    else:
        typesfortypes.append(x)
counter=1
while counter!=891:
    nums2.append(counter)
    counter+=1

pxpx=0

counter=0
while counter!=6:
    zz=random.choice(allpokes)
    rr=requests.get(f"https://pokemondb.net/pokedex/{zz}")
    soup2=BeautifulSoup(rr.content,'html.parser')
    inf=soup2.find_all("b")
    inf=[x.text for x in inf]
    print(f"{zz}")
    teamnums.append(allpokes.index(zz)+1)
    pxpx+=int(inf[0])
    counter+=1

for x in teamnums:
    lp+=x
if lp/6<152:
    print(f"\nYour team is averagely based on the Kanto region and its average base stat total is {round(float(pxpx/6))}")

elif lp/6<252:
    print(f"\nYour team is averagely based on the Johto region and its average base stat total is {round(float(pxpx/6))}")

elif lp/6<387:
    print(f"\nYour team is averagely based on the Hoenn region and its average base stat total is {round(float(pxpx/6))}")

elif lp/6<494:
    print(f"\nYour team is averagely based on the Sinnoh region and its average base stat total is {round(float(pxpx/6))}")

elif lp/6<650:
    print(f"\nYour team is averagely based on the Unova region and its average base stat total is {round(float(pxpx/6))}")

elif lp/6<722:
    print(f"\nYour team is averagely based on the Kalos region and its average base stat total is {round(float(pxpx/6))}")

elif lp/6<810:
    print(f"\nYour team is averagely based on the Alola region and its average base stat total is {round(float(pxpx/6))}")

elif lp/6<891:
    print(f"\nYour team is averagely based on the Galar region and its average base stat total is {round(float(pxpx/6))}")
