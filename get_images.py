import requests
from bs4 import BeautifulSoup
import re
import json
import random

def get_google_images():
    search_url = "https://www.google.com/search?q=chuck+norris&tbm=isch&ved=2ahUKEwjWsYTCirX3AhWDKX0KHYN_ASMQ2-cCegQIABAA&oq=chuck+norris&gs_lcp=CgNpbWcQAzIHCCMQ7wMQJzIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDoECAAQEzoECAAQQ1D_BVj3FGCYFmgAcAB4AIABYIgBsQWSAQIxM5gBAKABAaoBC2d3cy13aXotaW1nwAEB&sclient=img&ei=gqdpYtboJoPT9AOD_4WYAg&bih=705&biw=1440&client=firefox-b-e"
    search_term = "puppies"
    
    
    response = requests.get(search_url)
    response.raise_for_status()
    search_results = response.text
    
    search_list = search_results.split("href=")
    
    img_list=[]
    
    for tumb in search_list:
        if "tbn" in tumb and "src=" in tumb:
            new_tumb = tumb.split("src=")
            new_tumb = (new_tumb[1].split(";")[0]).replace('"', "")
            img_list.append(new_tumb)
    
    random_number = random.randrange(0, len(img_list)-1)
    return img_list[random_number]
    
    