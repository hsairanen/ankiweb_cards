# -*- coding: utf-8 -*-
"""
Created on Sun Jun 14 10:27:59 2026

@author: heidi
"""

import os
import requests
from dotenv import load_dotenv

load_dotenv()

PEXELS_API_KEY = os.getenv("PEXELS_API_KEY")
STORE_DIRECTORY = os.getcwd() + "\\images"


#%%

def search_pexels_images(query, per_page, pexel_api_key):

    url = "https://api.pexels.com/v1/search"

    headers = {
        "Authorization": pexel_api_key
    }

    params = {
        "query": query,
        "per_page": per_page,
        "orientation": "landscape"
    }

    response = requests.get(url, headers=headers, params=params, timeout=15)
    response.raise_for_status()

    data = response.json()
    return data.get("photos", [])


def download_image(image_url, output_path):
    response = requests.get(image_url, timeout=20)
    response.raise_for_status()

    with open(output_path, "wb") as file:
        file.write(response.content)
        

def search_and_download_image(query,count,image_api_key=PEXELS_API_KEY,directory=STORE_DIRECTORY):
   
    photos = search_pexels_images(query,count,image_api_key)

    if not photos:
        print("No images found.")
        return

    output_paths = []

    for index, photo in enumerate(photos, start=1):
        image_url = photo["src"]["medium"]

        clean_query = query.strip().replace(" ","_")
        filename = f"{clean_query}_{index}.jpg"
        output_path = os.path.join(directory, filename)

        download_image(image_url, output_path)
        
        output_paths.append(output_path)
    
    return output_paths
    



