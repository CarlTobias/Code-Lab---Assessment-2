import requests
import json
import re
from tkinter import *
import customtkinter

from PIL import ImageTk, Image

# TO DO LIST:
# - fix the back button
# - create the "previous" and "next" buttons to scroll
# - fix the starting page

# Documented errors faced so far:
# - Can't import from PotterDB properly
# - infoFrame wouldn't display content if it was like "infoFrame.place()" it has to be "Frame(root).place()"
# - goBack() has an AttributeError saying "'NoneType' object has no attribute 'destroy'"
# - prev and next buttons have an error "reference before assignment"

def openBook():
    global img2, spellsTitle, currentPage
    
    coverPageBG.destroy()
    openButton.destroy()
    
    pageBG.place(x = 0, y = 0, relwidth = 1, relheight = 1)
    
    spellsTitle = customtkinter.CTkLabel(
    root, text = "Spells", bg_color = '#413249', 
    font = garamond50, text_color = '#ffffff', 
    width = 150, height = 70
    )
    spellsTitle.place(relx = 0.5, rely = 0.11, anchor = CENTER)
    
    
    prevButton.place(relx = 0.09, rely = 0.92, anchor = W)
    nextButton.place(relx = 0.92, rely = 0.92, anchor = E)
    

def spellButton(index):
    global spellsTitle, currentPage, prevButton, nextButton
    
    infoFrame = Frame(root).place(relx = 0.5, rely = 0.5, anchor = CENTER)
    
    spellsTitle.place_forget()
    currentPage.place_forget()
    prevButton.place_forget()
    nextButton.place_forget()
    
    
    
    if spells['data'][index]['attributes']['incantation'] != None:
        nameMatch = re.search(r'([^()]+)\((.*?)\)', spells['data'][index]['attributes']['incantation'])
        spellMatch = re.search(r'\((.*?)\)', spells['data'][index]['attributes']['incantation'])
        newSpellName = nameMatch.group(1)
        pronounce = spellMatch.group(1)
        
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
        
        displayName = customtkinter.CTkLabel(
            centerFrame, text = f"{spells['data'][index]['attributes']['name']}", 
            bg_color = '#ffffff', font = garamond40, text_color = '#413249', 
            wraplength = 450
        )
        displayName.grid(row = 0, column = 0)
        
        # JSONimg = ImageTk.PhotoImage(Image.open(f"{spells['data'][index]['attributes']['image']}"))
        # imageJSON = Label(
        #     infoFrame, image = JSONimg
        # )
        # imageJSON.place(relx = 0.5, rely = 0.4)
        
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
        
        
    else:
        displayName = customtkinter.CTkLabel(
            infoFrame, text = f"{spells['data'][index]['attributes']['name']}", 
            bg_color = '#ffffff', font = garamond40, text_color = '#413249', 
            justify = 'left', wraplength = 450
        )
        displayName.place(relx = 0.09, rely = 0.09)
        
        # JSONimg = ImageTk.PhotoImage(Image.open(f"{spells['data'][index]['attributes']['image']}"))
        # imageJSON = Label(
        #     infoFrame, image = JSONimg
        # )
        # imageJSON.place(relx = 0.5, rely = 0.4)
        
        
        displaySpellInformation = Frame(infoFrame, bg = '#ffffff')
        displaySpellInformation.place(relx = 0.5, rely = 0.5, anchor = CENTER)
        
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
            justify = 'left', wraplength = 250
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
        font = garamond20, width = 100, command = lambda: goBack(infoFrame)
    )
    backButton.place(relx = 0.92, rely = 0.92, anchor = E)
    
    return infoFrame

def prevPage(p):
    global spellsList
    if p > 0:
        p -= 1
        currentPage.place_forget()
    
    currentPage = spellsList[p]
    currentPage.place(relx = 0.5, rely = 0.55, anchor = CENTER)
    print(p)

def nextPage(p):
    global spellsList
    if p < 17:
        p += 1
        currentPage.place_forget()
    
    currentPage = spellsList[p]
    currentPage.place(relx = 0.5, rely = 0.55, anchor = CENTER)
    print(p)

def goBack(infoFrame):
    infoFrame.destroy()
    spellsTitle.place(relx = 0.5, rely = 0.11, anchor = CENTER)
    currentPage.place(relx = 0.5, rely = 0.55, anchor = CENTER)
    
    
    


root = Tk()
root.title("The Unofficial Ultimate Harry Potter Spellbook")
root.geometry("611x800")
root.resizable(0, 0)

garamond20 = customtkinter.CTkFont('Garamond', 16)
garamond40 = customtkinter.CTkFont('Garamond', 40, 'bold')
garamond50 = customtkinter.CTkFont('Garamond', 50, 'bold')

gothic18 = customtkinter.CTkFont('Century Gothic', 18, 'bold')

spellsList = [] # empty list to store the 16 pages


with open("spells.json", "r") as file:
    spells = json.load(file)
    

    for p in range(16): # Amount of pages
        pages = Frame(
            root, bg = '#ffffff'
        )
        spellsList.append(pages)
        
        for x in range(20): # Amount of items in each page
            index = x + p * 10 # counts the spells sooo 1-10 for the first page, 11-20, and so on
            if index < 312:
                row = x % 10 + (p % 2) * 2
                column = x // 10
                customtkinter.CTkButton(
                    pages, text=f"{spells['data'][index]['attributes']['name']}", 
                    text_color = '#f4e46b', fg_color = '#413249', hover_color = '#181119', 
                    font = garamond20, width = 250, command = lambda i = index: spellButton(i)
                ).grid(row = row, column = column, padx = (5, 0), pady = 5, ipady = 8)
    
    prevButton = customtkinter.CTkButton(
        root, text="<--", 
        text_color = '#f4e46b', fg_color = '#413249', hover_color = '#181119', 
        font = garamond20, width = 75, command = lambda page = p: prevPage(page)
    )

    nextButton = customtkinter.CTkButton(
        root, text="-->", 
        text_color = '#f4e46b', fg_color = '#413249', hover_color = '#181119', 
        font = garamond20, width = 75, command = lambda page = p: nextPage(page)
    )

currentPage = spellsList[0]
currentPage.place(relx = 0.5, rely = 0.52, anchor = CENTER)


img1 = ImageTk.PhotoImage(Image.open("coverPage.png"))
coverPageBG = Label(
    root, image = img1
)
coverPageBG.place(x = 0, y = 0, relwidth = 1, relheight = 1)

img2 = ImageTk.PhotoImage(Image.open("page.png"))
pageBG = Label(
    root, image = img2
)

openButton = customtkinter.CTkButton(
    root, text="Open Book", 
    text_color = '#ffffff', bg_color = '#413249', fg_color = '#181119', hover_color = '#f4e46b', 
    font = garamond20, width = 250, command = openBook
)
openButton.place(relx = 0.492, rely = 0.64, anchor = CENTER)


root.mainloop()

# for index, __ in enumerate(spells['data']): # example: {0 : Age-line}
#     print(spells['data'][index]['attributes']['name'])
#     print(spells['data'][index]['attributes']['effect']) # will get the effect (change the last one to changge what u get in the api)