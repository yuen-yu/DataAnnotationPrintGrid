import requests
import sys
#from bs4 import BeautifulSoup
import pandas as pd

#text = "0█00█10█21▀11▀22▀12▀23▀2"
#text = "0█00█10█21▀1"
text  = ""
grid = {}
inputReady = False

def retrieveInputData():
    global text
    url = input("Enter a url for the Google doc: ")
    response = requests.get(url)
    
    if response.status_code == 200:
        #inputReady = True
        df = pd.read_html(url, encoding='utf-8', skiprows=1, header=None)
        text = df[0].to_string(index=False,header=False)
        #text = "".join(text.split())
        print(f"text = {text}")     
    else:
        print(f'URL access error: {response.status_code}')


def createGrid():
    # This forces the output to use utf-8 regardless of the terminal settings
    global text
    global grid
    print("createGrid")  
    #char_list = list(text)
    #print(text)
    #print(char_list)

    lines = text.splitlines()
    for line in lines:
        chunks = line.split()
        grid[(int(chunks[0]), int(chunks[2]))] = ord(chunks[1])
        print (chr(grid[(int(chunks[0]), int(chunks[2]))]))
        print(ord(chunks[1]))
        print (chr(ord(chunks[1])))

    #for i in range(0, len(char_list), 3):
        #chunk = char_list[i:i+3]
        #print(f"chunk =  {chunk}")
        # Only process if we have a full chunk of 3
        #if len(chunk) == 3:
            # 1st and 3rd items as key, 2nd as value
            #grid[(int(chunk[0]), int(chunk[2]))] = ord(chunk[1])
            #print (chr(grid[(chunk[0], chunk[2])]))
            #print (chr(grid[(int(chunk[0]), int(chunk[2]))]))
            #print(ord(chunk[1]))
            #print (chr(ord(chunk[1])))


def printGrid():
    global gird
    # Determine grid size
    max_x = max(k[0] for k in grid.keys())
    max_y = max(k[1] for k in grid.keys())
    # Print the grid
    for y in reversed (range(max_y + 1)):
        row=""
        for x in range(max_x + 1):
            char_code = grid.get((x, y), 32)
            row += chr(char_code)
        print(row)

def main():
    retrieveInputData()
    createGrid()
    printGrid()

if __name__ == "__main__":
    main()