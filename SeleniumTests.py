from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import datetime

PATH = "C:\Webdrivers\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://dineoncampus.com/FLPoly/whats-on-the-menu")
lunchItemList = []
lunchDescList = []
lunchPortionList = []
lunchCalorieList = []
lunchLocationList = []
dinnerItemList = []
dinnerDescList = []
dinnerPortionList = []
dinnerCalorieList = []
dinnerLocationList = []
tableNames = []
tableSums = []
previousText = ""
try:
    #For Lunch menu
    link = WebDriverWait(driver,10).until(
        EC.presence_of_element_located((By.LINK_TEXT, "Dinner"))#waits till the dinner tab is loaded, meaning waiting till the webpage is fully loaded
        )
    allItems = driver.find_elements_by_css_selector('td')#selects all the food items stored in the table that is the menu
    allTables = driver.find_elements_by_css_selector('table')#selects all the tables on the website
    tableNames = driver.find_elements_by_css_selector('caption')#gets the names of all the tables on the website
    
    for i in range(len(allTables)):
        tableSums.append(len(allTables[i].find_elements_by_css_selector('td'))) #checks the amount of cells in the menu        

    for j in range(len(allTables)):
        for i in range(int((tableSums[j])/3)):
            lunchLocationList.append(tableNames[j].text)#distributes the correct table names to the right amount of cells 
    
    for i in range(0,len(allItems),3):
        itemtext = allItems[i].text
        x = itemtext.splitlines()#splits the first item into necessary pieces
        if x[0] != "Chef's Choice" and previousText != x[0]: #makes sure the item name is not a duplicate or a useless name
            lunchItemList.append(x[0])
            if x[2] != "":
                if x[2] != "Nutritional Info":
                    lunchDescList.append(x[2])#ensures the description exists
                else:
                    lunchDescList.append("") 
            else:
                lunchDescList.append("") 
            
            previousText = x[0]
            lunchPortionList.append(allItems[i+1].text)#appends the rest of the items to there respective lists
            lunchCalorieList.append(allItems[i+2].text + " calories")
        else:
            lunchItemList.append("Chef's Choice or Same as previous entry AKA null") #null cases to skip in the file appending
            lunchDescList.append("null")
            lunchPortionList.append("null")
            lunchCalorieList.append("null")
        
    link.click()
    time.sleep(10) #ensures the dinner page is loaded before grabbing information
    allItems = driver.find_elements_by_css_selector('td')
    tableNames.clear()#clearing of some lists
    tableSums.clear()
    allTables = driver.find_elements_by_css_selector('table')
    tableNames = driver.find_elements_by_css_selector('caption')
    previousText = ""
    #now the same thing that happened for lunch, happens for dinner
    for i in range(len(allTables)):
        tableSums.append(len(allTables[i].find_elements_by_css_selector('td')))        

    for j in range(len(allTables)):
        for i in range(int((tableSums[j])/3)):
            dinnerLocationList.append(tableNames[j].text)
    
    for i in range(0,len(allItems),3):
        itemtext = allItems[i].text
        x = itemtext.splitlines()
        if x[0] != "Chef's Choice" and previousText != x[0]:
            dinnerItemList.append(x[0])
            if x[2] != "":
                if x[2] != "Nutritional Info":#ensures the description exists
                    dinnerDescList.append(x[2])
                else:
                    dinnerDescList.append("") 
            else:
                dinnerDescList.append("") 
            previousText = x[0]
            dinnerPortionList.append(allItems[i+1].text)
            dinnerCalorieList.append(allItems[i+2].text + " calories")
        else:
            dinnerItemList.append("null")
            dinnerDescList.append("null")
            dinnerPortionList.append("null")
            dinnerCalorieList.append("null")
    
except:
    driver.quit()

outFile = open("WellnessDiningMenu.txt","w") #Open the output file
outFile.write("Wellness Dining Menus for "+datetime.datetime.now().strftime("%x")+"\n")#Keeps the date of the web scraping
outFile.write("Lunch Menu:\n")#Shows that this is the Lunch menu

for i in range(len(lunchDescList)):
    if lunchCalorieList[i]!= "null":#copies the lists to a file if they are not null
        if lunchDescList[i]!= "":
            outFile.write(lunchLocationList[i]+";"+lunchItemList[i]+";"+lunchDescList[i]+";"+lunchPortionList[i]+";"+lunchCalorieList[i]+";\n")
        else:
            outFile.write(lunchLocationList[i]+";"+lunchItemList[i]+";"+lunchDescList[i]+lunchPortionList[i]+";"+lunchCalorieList[i]+";\n")
        
for i in range(len(lunchDescList),len(lunchItemList)):
    if lunchCalorieList[i]!= "null":#copies the lists to a file if they are not null
        outFile.write(lunchLocationList[i]+";"+lunchItemList[i]+";"+lunchPortionList[i]+";"+lunchCalorieList[i]+";\n")

outFile.write("Dinner Menu:\n")#Shows that this is the Dinner menu

for i in range(len(dinnerDescList)):
    if dinnerCalorieList[i]!= "null":#copies the lists to a file if they are not null
        if dinnerDescList[i]!="":
            outFile.write(dinnerLocationList[i]+";"+dinnerItemList[i]+";"+dinnerDescList[i]+";"+dinnerPortionList[i]+";"+dinnerCalorieList[i]+";\n")
        else:
            outFile.write(dinnerLocationList[i]+";"+dinnerItemList[i]+";"+dinnerDescList[i]+dinnerPortionList[i]+";"+dinnerCalorieList[i]+";\n")
        
for i in range(len(dinnerDescList),len(dinnerItemList)):
    if dinnerCalorieList[i]!= "null":#copies the lists to a file if they are not null
        outFile.write(dinnerLocationList[i]+";"+dinnerItemList[i]+";"+dinnerPortionList[i]+";"+dinnerCalorieList[i]+";\n")

outFile.close()# close the outfile

driver.quit()#quits the file
