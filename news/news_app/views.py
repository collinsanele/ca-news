from django.shortcuts import render
from bs4 import BeautifulSoup
import requests

#Scraping section here.

def scrape_nairaland():
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"}
    r = requests.get("https://nairaland.com", headers=headers)
    soup = BeautifulSoup(r.content, "html.parser")
    links = [item.get("href") for item in soup.find("td", class_="featured").find_all("a")][:65]
    links_text = [item.text for item in soup.find("td", class_="featured").find_all("a")][:65]
    
    return {
        
                "links_data":zip(links_text, links)
                
        
            }
    





def scrape_punch():

    imgs = []
    titles = []
    links = []
    
    r = requests.get("https://punchng.com/")
    soup = BeautifulSoup(r.content, "html.parser")

    for item in soup.findAll("div", class_="cat-sections_item"):
        img = None
        title = None
        link = None

        try:
            img = item.find("div", class_="cat-sections_image").get("data-src")

        except:
            pass

        try:
            title = item.find("div", class_="title-box").text.strip()

        except:
            pass
        
        try:
            link = item.find("a").get("href")
            
        except:
            pass

        imgs.append(img)
        titles.append(title)
        links.append(link)
        
    return zip(titles, imgs, links)
	
	
	
	
	
def scrape_sun():

    imgs = []
    titles = []
    links = []

    r = requests.get("https://www.sunnewsonline.com/?p=*****")
    soup = BeautifulSoup(r.content, "html.parser")

    for item in soup.findAll("article"):
        
        title = ""
        link = ""
        img = ""
        
        
        try:
            link = item.find("a").get("href")
        except:
            pass

        try:
            img = item.find("img").get("data-src")

        except:
            pass

        try:
            title = item.find("h3").text.strip()

        except:
            pass

        links.append(link)
        imgs.append(img)
        titles.append(title)

    return zip(titles, imgs, links)
	
	
	
def scrape_vanguard():

    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"}

    r = requests.get("https://www.vanguardngr.com/category/national-news/", headers=headers)

    soup = BeautifulSoup(r.content, "html.parser")


    imgs = []
    links = []
    titles = []
    bodies = []

    for item in soup.findAll("article"):
        link = ""
        img = ""
        title = ""
        body = ""
		
        try:
            img= item.find("div", class_="rtp-post-thumbnail").find("img").get("src")

        except:
            pass

        try:
            title = item.find("h2").text

        except:
            pass

        try:
            link = item.find("a").get("href")

        except:
            pass

        try:
            body = item.find("div", class_="entry-content").text.strip()

        except:
            pass

        titles.append(title)
        imgs.append(img)
        links.append(link)
        bodies.append(body)


    return zip(titles, imgs, links, bodies)
	
	
	
	
	




def scrape_sahara():
    imgs = []
    links = []
    titles = []
    
    r = requests.get("http://saharareporters.com/")
    soup = BeautifulSoup(r.content, "html.parser")

    for item in soup.findAll(class_="views-row"):
        img=""
        link = ""
        title = ""
        try:
            img = item.find("img").get("src")

        except:
            pass

        try:
            link = item.find("a").get("href")
            link = "http://saharareporters.com"+link

        except:
            pass

        try:
            title = item.find("div", class_="block-module-content-header").find("span").text.strip()
            print(title)
            print()

        except:
            pass
        
        links.append(link)
        imgs.append(img)
        titles.append(title)
        
    return zip(titles, imgs, links)
	
	




def scrape_aljazeera():

    r = requests.get("https://www.aljazeera.com/news/")
    soup = BeautifulSoup(r.content, "html.parser")

    imgs = []
    titles = []
    links = []

    for item in soup.findAll("div", class_="default-style"):
        link = ""
        img = ""
        title = ""

        try:
            link = item.find("a").get("href")
            link = "https://www.aljazeera.com"+link

        except:
            pass

        try:
            potential_imgs = item.findAll("img")
            for item_ in potential_imgs:
                if item_.get("src") and "DefaultAvatar" not in item_.get("src") and "video-programmes.png" not in item_.get("src"):
                    img = item_.get("src")
                    
                    
                if item_.get("data-src"):
                    img = item_.get("data-src")
            
            
            img = "https://www.aljazeera.com"+img

        except Exception as e:
            print(e)
            pass

        try:
            title = item.find("h2").text

        except:
            pass

        imgs.append(img)
        titles.append(title)
        links.append(link)

    return zip(links, imgs, titles)
	
	
	
	
def scrape_sportinglife():
    r = requests.get("https://sportinglife.ng/")
    soup = BeautifulSoup(r.content, "html.parser")

    imgs = []
    titles = []
    links = []

    for item in soup.find("div", class_="row-2").findAll(class_="item-inner"):
        img = ""
        title = ""
        link = ""

        try:
            img = item.find("a", class_="img-holder").get("data-src")

        except Exception as e:
            pass


        try:
            title = item.find("h3", class_="title").text.strip()

        except Exception as e:
            pass


        try:
            link = item.find("h3", class_="title").find("a").get("href")

        except Exception as e:
            pass

        imgs.append(img)
        links.append(link)
        titles.append(title)
        
    return zip(links, imgs, titles)
    
    
        








# Create your views here.

def index(request):
	nairaland_data = scrape_nairaland()
	context = {"data":nairaland_data}
	
	return render(request, "news_app/index.html", context)
	
	
	
	
def punch(request):
	punch_data = scrape_punch()
	context = {"data":punch_data}
	
	return render(request, "news_app/punch.html", context)
	
	
	
	
	
	
	
def sun(request):
	sun_data = scrape_sun()
	context = {"data":sun_data}
	
	return render(request, "news_app/sun.html", context)
	
	
	
def vanguard(request):
	vanguard_data = scrape_vanguard()
	context = {"data":vanguard_data}
	
	return render(request, "news_app/vanguard.html", context)
	
	
def sahara(request):
	sahara_data = scrape_sahara()
	context = {"data":sahara_data}
	
	return render(request, "news_app/sahara.html", context)
	
	
def aljazeera(request):
	aljazeera_data = scrape_aljazeera()
	context = {"data":aljazeera_data}
	
	return render(request, "news_app/aljazeera.html", context)
	
	
def sportinglife(request):
	sportinglife_data = scrape_sportinglife()
	context = {"data":sportinglife_data}
	
	return render(request, "news_app/sportinglife.html", context)















