import requests
from bs4 import BeautifulSoup
import re
from tkinter import filedialog
import time
error_count =0
def read_file_and_create_list(filename):
    with open(filename, 'r') as file:
        # Read the entire content of the file and split it by newline characters
        content = file.read()
        items_list = content.split('\n')

    # Remove any empty elements from the list
    items_list = list(filter(None, items_list))

    return items_list
def extract_ids_from_text(text):
    mod_id_pattern = r"Mod ID:\s*(\w+)"
    workshop_id_pattern = r"Workshop ID:\s*(\w+)"

    mod_id_match = re.search(mod_id_pattern, text)
    workshop_id_match = re.search(workshop_id_pattern, text)

    mod_id = mod_id_match.group(1) if mod_id_match else None
    workshop_id = workshop_id_match.group(1) if workshop_id_match else None

    return mod_id, workshop_id

def scrape_steam_data(url):
    mod_id = ""
    workshop_id = ""
    response = requests.get(url)
    if response.status_code != 200:
        error_count+=1
        print("Failed to fetch the page.")
        return mod_id, workshop_id

    soup = BeautifulSoup(response.content, 'html.parser')

    workshop_description = str(soup.find('div', class_='workshopItemDescription'))
    mod_id, workshop_id = extract_ids_from_text(workshop_description)
    
    return mod_id, workshop_id


def choose_input_file():
   

    # Ask the user to choose the input file using the file dialog
    file_path = filedialog.askopenfilename(title="Select your Mod.txt file")

    return file_path

# ANSI escape codes for text colors
class TextColors:
    RESET = "\033[0m"
    BLACK = "\033[30m"
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    MAGENTA = "\033[35m"
    CYAN = "\033[36m"
    WHITE = "\033[37m"

if __name__ == "__main__":
    print(TextColors.YELLOW,"\nWelcome to Zomboid Server Modder!"+TextColors.RESET)
    
    print("Please select a Mods.txt file")
    
    time.sleep(0.3)
    input_file_path = choose_input_file()
    steam_urls = read_file_and_create_list(input_file_path)

    mod_ids_list = []
    workshop_ids_list = []
    
    mods_count = len(steam_urls)
    i=0
    for steam_url in steam_urls:
        
        print(f"Processing webpage {i + 1}/{mods_count}", flush=True)
        i+=1
        mod_id, workshop_id = scrape_steam_data(steam_url)
        if mod_id:
            mod_ids_list.append(mod_id)
        if workshop_id:
            workshop_ids_list.append(workshop_id)
    print("Mod file has been made!")
    if error_count>0:
        print(TextColors.RED+str(error_count),"errors found!"+TextColors.RESET)
    print(TextColors.GREEN+"No errors found"+TextColors.RESET)
   
    # Join the items using ";" and remove the extra ";"
    mod_ids_string = ";".join(mod_ids_list)
    workshop_ids_string = ";".join(workshop_ids_list)

    

    with open("output.txt", 'w') as file:
        file.write("Mods= "+ mod_ids_string + "\n")
        file.write("WorkshopItems= "+ workshop_ids_string + "\n")
   

    
    