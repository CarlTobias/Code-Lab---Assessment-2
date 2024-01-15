import requests
import json
import re
from tkinter import *
import customtkinter

from PIL import ImageTk, Image


# Initially, I use these two lines of code to access the APIs...
# url = f"https://potterdb.com/spells?page[number]=1"
# response = requests.get(url)

# I then realized that the API split their database into multiple pages, so I tried using a for loop
# for x in range(4): 
#     url = f"https://potterdb.com/spells?page[number]={x}"
#     response = requests.get(url)
    
#     if response.status_code == 200:
#         spells = response.json()
#         print(response.status_code)

# But errors kept occurring and there was just nothing I could come up with or seearch online to fix the issue...
# My solution was to import the code from the API to a .json file instead

def openBook(): # When this function is called, the "book" will open
    global img2, spellsTitle, currentPage
    
    coverPageBG.destroy()
    openButton.destroy()
    
    spellsTitle = customtkinter.CTkLabel(
    root, text = "Spells", bg_color = '#413249', 
    font = garamond50, text_color = '#ffffff', 
    width = 150, height = 70
    )
    spellsTitle.place(relx = 0.5, rely = 0.11, anchor = CENTER)
    pageBG.place(x = 0, y = 0, relwidth = 1, relheight = 1)
    

def spellButton(index): # This function displays a page, it can be switched  to the previous or next page
    global spellsTitle, currentPage, prevButton, nextButton
    
    
    infoFrame = Frame(root)
    infoFrame.place(x = 0, y = 0, relwidth = 1, relheight = 1)
    
    infoFrameBG = Label(
        infoFrame, image = img2
    )
    infoFrameBG.place(x = 0, y = 0, relwidth = 1, relheight = 1)
    
    # Here we have a nested if-else statement...
    if spells['data'][index]['attributes']['incantation']:
        # If there is information in "incantation," it will be the new spell name
        newSpellName = str(spells['data'][index]['attributes']['incantation'])
        
        if newSpellName.__contains__("("):
            # If that new spell name has a parenthesis, it will be split and placed in a list and the extra ")" will be replaced with an empty string
            newSpellName, pronounce = newSpellName.split("(")
            pronounce = pronounce.replace(")", "")
        
        else:
            # ELse, the new spell name will be just the original name
            newSpellName = spells['data'][index]['attributes']['name']
            pronounce = ""
        
    else:
        # Same here
        newSpellName = spells['data'][index]['attributes']['name']
        pronounce = ""
    
    # This is done to remove redundancy...
    # Some spells have the same name and incantation, but the layout from the API's incantation is incantation(pronounciation)
    # So some steps are taken to remove separate the pronounciation in order to display it in a different widget and be able to compare name and incantation to see if both should be printed or just one
    
    # The section below are the widgets used in displaying the information of a spell chosen by the user
    spellFrame = Frame(
        infoFrame, bg = "#ffffff"
    )
    spellFrame.place(relx = 0.09, rely = 0.09)
    
    displaySpell = customtkinter.CTkLabel(
        spellFrame, text = f"{newSpellName}", 
        bg_color = '#ffffff', font = garamond40, text_color = '#413249', 
        justify = 'left', wraplength = 450
    )
    displaySpell.grid(row = 0, column = 0, padx = (0, 5), sticky = W)
    
    displayPronounce = customtkinter.CTkLabel(
        spellFrame, text = f"{pronounce}", 
        bg_color = '#ffffff', font = gothic18, text_color = '#413249', 
        justify = 'left', wraplength = 500
    )
    displayPronounce.grid(row = 1, column = 0, padx = (5, 0), sticky = W)
    
    
    centerFrame = Frame(
        infoFrame, bg = "#ffffff"
    )
    centerFrame.place(relx = 0.5, rely = 0.5, anchor = CENTER)
    
    # This statement checks to see if the name should be displayed along with the incantation
    if newSpellName != spells['data'][index]['attributes']['name']:
        displayName = customtkinter.CTkLabel(
            centerFrame, text = f"{spells['data'][index]['attributes']['name']}", 
            bg_color = '#ffffff', font = garamond40, text_color = '#413249', 
            wraplength = 450
        )
        displayName.grid(row = 0, column = 0)
    
    displaySpellInformation = Frame(centerFrame, bg = '#ffffff')
    displaySpellInformation.grid(row = 1, column = 0)
    
    customtkinter.CTkLabel(
        displaySpellInformation, text = "Category:", 
        bg_color = '#ffffff', font = garamond20, text_color = '#413249', 
        wraplength = 250
    ).grid(row = 0, column = 0, padx = (0, 5), pady = 5, sticky = NE)
    
    customtkinter.CTkLabel(
        displaySpellInformation, text = f"{spells['data'][index]['attributes']['category']}", 
        bg_color = '#ffffff', font = garamond20, text_color = '#413249', 
        justify = 'left', wraplength = 250
    ).grid(row = 0, column = 1, padx = (5, 0), pady = 5, sticky = NW)
    
    
    customtkinter.CTkLabel(
        displaySpellInformation, text = "Effect:", 
        bg_color = '#ffffff', font = garamond20, text_color = '#413249', 
        wraplength = 250
    ).grid(row = 1, column = 0, padx = (0, 5), pady = 5, sticky = NE)
    
    customtkinter.CTkLabel(
        displaySpellInformation, text = f"{spells['data'][index]['attributes']['effect']}", 
        bg_color = '#ffffff', font = garamond20, text_color = '#413249', 
        justify = 'left', wraplength = 200
    ).grid(row = 1, column = 1, padx = (5, 0), pady = 5, sticky = NW)
    
    
    customtkinter.CTkLabel(
        displaySpellInformation, text = "Light:", 
        bg_color = '#ffffff', font = garamond20, text_color = '#413249', 
        wraplength = 250
    ).grid(row = 2, column = 0, padx = (0, 5), pady = 5, sticky = NE)
    
    customtkinter.CTkLabel(
        displaySpellInformation, text = f"{spells['data'][index]['attributes']['light']}", 
        bg_color = '#ffffff', font = garamond20, text_color = '#413249', 
        justify = 'left', wraplength = 250
    ).grid(row = 2, column = 1, padx = (5, 0), pady = 5, sticky = NW)
    
    backButton = customtkinter.CTkButton(
        infoFrame, text="Back", 
        text_color = '#f4e46b', fg_color = '#413249', hover_color = '#181119', 
        font = garamond20, width = 100, command = infoFrame.destroy
    )
    backButton.place(relx = 0.92, rely = 0.92, anchor = E)


def prevPage(p): # When this function is called, it switches to the previous page (if it's the first page, nothing happens)
    global currentPage
    
    if p > 0:
        currentPage.place_forget()
        
        p -= 1
        currentPage = spellsList[p]
        currentPage.place(relx = 0.5, rely = 0.56, height = 620, anchor = CENTER)

def nextPage(p): # When this function is called, it switches to the next page (if it's the last page, nothing happens)
    global currentPage
    
    if p < 15:
        currentPage.place_forget()
        
        p += 1
        currentPage = spellsList[p]
        currentPage.place(relx = 0.5, rely = 0.56, height = 620, anchor = CENTER)
  
    
    

# Initialized root window here
root = Tk()
root.title("The Unofficial Ultimate Harry Potter Spellbook")
root.geometry("611x800")
root.resizable(0, 0)

# Set font sizes
garamond20 = customtkinter.CTkFont('Garamond', 16)
garamond40 = customtkinter.CTkFont('Garamond', 40, 'bold')
garamond50 = customtkinter.CTkFont('Garamond', 50, 'bold')
gothic18 = customtkinter.CTkFont('Century Gothic', 18, 'bold')


# Set the image for the main background (book page)
img2 = ImageTk.PhotoImage(Image.open("page.png"))
pageBG = Label(
    root, image = img2
)

spellsList = [] # Empty list to store the 16 pages


with open("spells.json", "r") as file: # Opened the .json file that stores the information from the API
    spells = json.load(file)
    
    # The nested for loop makes all the pages and each spell button
    for p in range(16): # The outer loop is for the amount of pages
        pages = Frame(
            root, bg = '#ffffff'
        )
        spellsList.append(pages)
        
        for col in range(2): # This inner-outer loop allows for making two columns;
            for row in range(10): # With 10 rows for each column
                index = row + (p * 20) + (col * 10) # counts the spells sooo 1-20 for the first page, 21-40, and so on
                if index < 312:
                    customtkinter.CTkButton(
                        pages, text=f"{spells['data'][index]['attributes']['name']}", 
                        text_color = '#f4e46b', fg_color = '#413249', hover_color = '#181119', 
                        font = garamond20, width = 250, command = lambda i = index: spellButton(i)
                    ).grid(row = row, column = col, padx = (5, 0), pady = 5, ipady = 8)
    
        prevButton = customtkinter.CTkButton(
            pages, text="<--", 
            text_color = '#f4e46b', fg_color = '#413249', hover_color = '#181119', 
            font = garamond20, width = 75, command = lambda page = p: prevPage(page)
        )
        prevButton.place(relx = 0, rely = 0.975, anchor = W)

        nextButton = customtkinter.CTkButton(
            pages, text="-->", 
            text_color = '#f4e46b', fg_color = '#413249', hover_color = '#181119', 
            font = garamond20, width = 75, command = lambda page = p: nextPage(page)
        )
        nextButton.place(relx = 1, rely = 0.975, anchor = E)


# Initialized the first page
currentPage = spellsList[0]
currentPage.place(relx = 0.5, rely = 0.56, height = 620, anchor = CENTER)


# Cover page (which will be layered on top of currentPage until the first function is called)
img1 = ImageTk.PhotoImage(Image.open("coverPage.png"))
coverPageBG = Label(
    root, image = img1
)
coverPageBG.place(x = 0, y = 0, relwidth = 1, relheight = 1)

# Button that goes on top of the cover page (when pressed, it calls the first function)
openButton = customtkinter.CTkButton(
    root, text="Open Book", 
    text_color = '#ffffff', bg_color = '#413249', fg_color = '#181119', hover_color = '#f4e46b', 
    font = garamond20, width = 250, command = openBook
)
openButton.place(relx = 0.492, rely = 0.64, anchor = CENTER)



root.mainloop()