import zipfile
from bs4 import BeautifulSoup
import requests
import wget


addon_url = input("Enter url of addon page : ") 
install_location = "./install_location" 


urls = []

def findMore(req, soup):
    for div in soup.findAll('div', {'class': 'jumbotron'}):
        links = div.select('a')
        for link in links:
            if link.get('href') != None:
                if 'https://' in link.get('href') or 'http://' in link.get('href'):
                    dep = str(link.get('href'))
                else:
                    dep = ('https://orbithangar.com' + link.get('href')) # Convert relative URL to absolute URL
            if ("showAddon" in dep) or ("searchid") in dep:
                addonpage_to_download(dep)




def addonpage_to_download(addon_url):
    
    req = requests.get(addon_url)
    addon_url = req.url

    if addon_url in urls:
        return
    else:
        urls.append(addon_url)

    print(addon_url)

    soup = BeautifulSoup(req.text, "html.parser")

    link_tags = soup.findAll("a", {"id": "file_download"})
    for link_tag in link_tags:
        zip_link = str(link_tag.get("href"))
        zip_name = zip_link.split('/')[-1]
        print("Downloading: " + zip_name)
        wget.download(zip_link)
        print(" ")

        with zipfile.ZipFile(zip_name,"r") as zip_ref:
            print("Extracting: " + zip_name)
            zip_ref.extractall(install_location)
            

    findMore(req, soup)

#TODO - check if addon is already installed, maybe by having a text file with the addon name and version

addonpage_to_download(addon_url)

 
