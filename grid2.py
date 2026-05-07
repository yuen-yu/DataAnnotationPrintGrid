import requests
import pandas as pd

#text = "0█00█10█21▀11▀22▀12▀23▀2"

def printGrid():
    text = ""
    grid = {}
    url = input("Enter a url for the Google doc: ")
    response = requests.get(url)
    if response.status_code == 200:
        df = pd.read_html(url, encoding='utf-8', skiprows=1, header=None)   #retreive the required information
        text = df[0].to_string(index=False,header=False)                    #load information to a string
        
        lines = text.splitlines()
        for line in lines:
            chunks = line.split()
            grid[(int(chunks[0]), int(chunks[2]))] = ord(chunks[1])         #load teh grid
                                                                            
        max_x = max(k[0] for k in grid.keys())                              # Determine grid size
        max_y = max(k[1] for k in grid.keys())
                                                                            
        for y in reversed (range(max_y + 1)):                               # Print the grid
            row=""
            for x in range(max_x + 1):
                char_code = grid.get((x, y), 32)
                row += chr(char_code)
            print(row)
    else:
        print(f'URL access error: {response.status_code}')


def main():
    printGrid()
 
if __name__ == "__main__":
    main()