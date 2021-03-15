import bs4
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq


def delish(search):
    # searching in delish
    search= search.split()
    # print(search)
    search_str = ('https://www.delish.com/search/?q=')
    for i in search:
        search_str += i+'+'        
    search_str = search_str[:-1]
    print(search_str)

    uClient =uReq(search_str)    
    results_html = uClient.read()
    uClient.close

    #html parsing
    page_soup = soup(results_html,"html.parser")

    containers= page_soup.findAll("div",{"class":"simple-item grid-simple-item grid-simple-item-last-mobile"})
    count =0
    noofrecipe =0

    rname = []
    imglinks = []
    descriptions = []
    alink =[]

    for container in containers:
        count=count +1
        value =container.findAll('a',{"class":"item-parent-link simple-item-parent-link"})
        recipeornot =value[0].text 
        if( 'Recipes' in recipeornot):
            noofrecipe += 1
            if(noofrecipe >20):
                break
            else:    
                recipenamelist=container.find('a',{"class":"simple-item-title item-title"})
                recipename =recipenamelist.text
                rname.append(recipename)
                
                alinklist=container.find('a',{"class":"simple-item-title item-title"})
                alinkname =alinklist['href']
                alinkname="https://www.delish.com"+alinkname
                alink.append(alinkname)
                

                image_src =container.find('img',{"class":"lazyimage lazyload"})
                image_src1 =image_src['data-src']
                imglinks.append(image_src1)

                desc=container.find('div',{"class":"simple-item-dek item-dek"})
                description =desc.text
                if(len(description)>100):
                    description = description[:100]
                descriptions.append(description)


    return rname,imglinks,descriptions,alink



def epicurious(search):
    # searching in bbcgoodfood
    search= search.split()
    # print(search)
    search_str = ('https://www.epicurious.com/search/')
    for i in search:
        search_str += i+'%20'        
    search_str = search_str[:-3]
    print(search_str)


    uClient =uReq(search_str)    
    results_html = uClient.read()
    uClient.close

    #html parsing
    page_soup = soup(results_html,"html.parser")

    container= page_soup.find("div",{"class":"results-group"})
    noofrecipe =0

    rname = []
    imglinks = []
    descriptions = []
    alink =[]

    values =container.findAll('article',{"class":"recipe-content-card"})
    for value in values:
        noofrecipe += 1
        if(noofrecipe >20 ):
            break
        else:    
            recipenamelist=value.find('h4',{"class":"hed"})
            recipename =recipenamelist.text
            # print(recipename)
            rname.append(recipename)
                
            alinklist=recipenamelist.find('a')
            alinkname =alinklist['href']
            alinkname ="https://www.epicurious.com/"+alinkname
            # print(alinkname)    
            alink.append(alinkname)
                
            uimage = uReq(alinkname)
            results_html = uimage.read()
            uimage.close
            page_soup = soup(results_html,"html.parser")
            
            image_src =page_soup.find('picture',{"class":"photo-wrap"})
            image_src1 =image_src.find('img')
            image_src1 =image_src1['srcset']
            # print(image_src1)
            imglinks.append(image_src1)

            desc=value.find('p',{"class":"dek"})
            description =desc.text
            # print(description)
            if(len(description)>100):
                description = description[:100]
            descriptions.append(description)


    return rname,imglinks,descriptions,alink




