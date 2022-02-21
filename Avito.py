from fileinput import filename
import requests, os
from bs4 import BeautifulSoup as Bs 


Suspect = input('Что ищем на авито--')
name_file = f"Exit_Avito\Exit_Avito_{Suspect}.txt"
print(Suspect)


try:
    os.makedirs('Exit_Avito')
except Exception:
    pass
try:
    os.remove(name_file)
except Exception:
    pass    


url = f"https://www.avito.ru/saratov?q={Suspect}"
main_url = "https://www.avito.ru"
r = requests.get(url).text
print(url)


soup = Bs(r, 'lxml')
bbs = soup.find('div', class_="items-items-kAJAg")


def get_content(page_html):
    one_block = page_html.find_all('div', class_="iva-item-content-rejJg")
    for i in one_block:
        txt_url = i.find("div",class_="iva-item-titleStep-pdebR")
        name = txt_url.find('a').get('title')
        price = i.find('meta', itemprop="price").get('content')
        item_url = txt_url.find('a').get('href')
        out_text = f"Название - {name} | Цена - {price} | Ссылка - {main_url+item_url}\n"
        out_out(text=out_text)


def out_out(text):
    with open(name_file, 'a', encoding='utf8')as file:
        for line in str(text):
            file.write(line)      


if __name__=="__main__":
    bTEMP = bbs
    get_content(page_html=bTEMP)   
os.startfile(name_file)        