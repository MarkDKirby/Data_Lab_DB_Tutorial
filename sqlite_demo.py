import pandas as pd
import numpy as np
import sqlite3
from tkinter import *
import tkinter as tk

#### DATABASE SECTION ##########################################################

connection = sqlite3.connect("Whales.db")
cursor = connection.cursor()

"""This program creates a database of whales and the bodies of water in which the reside. It
also creates a GUI interface that will allow the user to insert information about the whales into
the whales table."""

try:
    cursor.execute("""CREATE TABLE Waters ("Name_" varchar(20), "AveDepth" int, "SaltOrFresh" Varchar(1), PRIMARY KEY ("Name_"));""")
except:
    print("You already created the Waters table")

whales_table = """
        CREATE TABLE Whales (
                "TrackingNumber" INT,
                "Length" REAL,
                "Weight" REAL,
                "Longitude" REAL,
                "Latitude" REAL,
                "Species" VARCHAR(20),
                "Ocean" VARCHAR(20),
                PRIMARY KEY ("TrackingNumber"),
                FOREIGN KEY ("Ocean") REFERENCES Waters ("Name_")
            );"""

# try:
#     cursor.execute(whales_table)
# except:
#     print("The Whales Table already exists")

Data_to_insert = """INSERT INTO Whales (TrackingNumber,Length,Weight,Longitude,Latitude,Species,Ocean)
VALUES (1,100,105,44.4311,25.1167,"Blue","Atlantic");"""
Data_to_insert1 = """INSERT INTO Whales (TrackingNumber,Length,Weight,Longitude,Latitude,Species,Ocean)
VALUES (2,54,30,40.2573,32.9931,"Wright","Atlantic");"""
Data_to_insert2 = """INSERT INTO Whales (TrackingNumber,Length,Weight,Longitude,Latitude,Species,Ocean)
VALUES (3,51,27,41.0009,33.8967,"Grey","Atlantic");"""
Data_to_insert3 = """INSERT INTO Whales (TrackingNumber,Length,Weight,Longitude,Latitude,Species,Ocean)
VALUES (4,49,29,-4.9341,40.0906,"Humpback","Mediterranean");"""
Data_to_insert4 = """INSERT INTO Whales (TrackingNumber,Length,Weight,Longitude,Latitude,Species,Ocean)
VALUES (5,63,27,-38.7769,-35.0134,"Sperm","Indian");"""
Data_to_insert5 = """INSERT INTO Whales (TrackingNumber,Length,Weight,Longitude,Latitude,Species,Ocean)
VALUES (6,77,27,31.7568,146.8129,"Finback","Pacific");"""
Data_to_insert6 = """INSERT INTO Whales (TrackingNumber,Length,Weight,Longitude,Latitude,Species,Ocean)
VALUES (7,105,117,44.5312,24.9968,"Blue","Atlantic");"""
Data_to_insert7 = """INSERT INTO Whales (TrackingNumber,Length,Weight,Longitude,Latitude,Species,Ocean)
VALUES (8,25,11,77.5312,43.9968,"Beluga","Great_Lakes");"""



try:
    cursor.execute(whales_table)
except:
    print("You already created this table")
try:
    cursor.execute(Data_to_insert)
except:
    print("You already created this row")
try:
    cursor.execute(Data_to_insert1)
except:
    print("You already created this row")
try:
    cursor.execute(Data_to_insert2)
except:
    print("You already created this row")
try:
    cursor.execute(Data_to_insert3)
except:
    print("You already created this row")
try:
    cursor.execute(Data_to_insert4)
except:
    print("You already created this row")
try:
    cursor.execute(Data_to_insert5)
except:
    print("You already created this row")
try:
    cursor.execute(Data_to_insert6)
except:
    print("You already created this row")
try:
    cursor.execute(Data_to_insert7)
except:
    print("You already created this row")

try:
    cursor.execute("""INSERT INTO Waters (Name_,AveDepth,SaltOrFresh) VALUES ("Atlantic", 4500, "S");""")
except:
    print("This record already exists")
try:
    cursor.execute("""INSERT INTO Waters (Name_,AveDepth,SaltOrFresh) VALUES ("Pacific", 4900, "S");""")
except:
    print("This record already exists")
try:
    cursor.execute("""INSERT INTO Waters (Name_,AveDepth,SaltOrFresh) VALUES ("Indian", 4200, "S");""")
except:
    print("This record already exists")
try:
    cursor.execute("""INSERT INTO Waters (Name_,AveDepth,SaltOrFresh) VALUES ("Arctic", 3500, "S");""")
except:
    print("This record already exists")
try:
    cursor.execute("""INSERT INTO Waters (Name_,AveDepth,SaltOrFresh) VALUES ("Mediterranean", 1500, "S");""")
except:
    print("This record already exists")
try:
    cursor.execute("""INSERT INTO Waters (Name_,AveDepth,SaltOrFresh) VALUES ("Great_Lakes", 1000, "F");""")
except:
    print("This record already exists")

#### GUI SECTION ############################################################

class GUI:
    def __init__(self):
        self.main_window = tk.Tk()
        self.main_window.title("Enter a Whale")

        #frame the parts of the GUI
        self.frame1 = tk.Frame(self.main_window)
        self.frame1.configure(bg='lightblue')
        self.frame2 = tk.Frame(self.main_window)
        self.frame2.configure(bg='lightblue')
        self.frame3 = tk.Frame(self.main_window)
        self.frame3.configure(bg='lightblue')
        self.frame4 = tk.Frame(self.main_window)
        self.frame4.configure(bg='lightblue')
        self.frame5 = tk.Frame(self.main_window)
        self.frame5.configure(bg='lightblue')
        self.frame6 = tk.Frame(self.main_window)
        self.frame6.configure(bg='lightblue')
        self.frame7 = tk.Frame(self.main_window)
        self.frame7.configure(bg='lightblue')
        self.frame8 = tk.Frame(self.main_window)
        self.frame8.configure(bg='lightblue')

        #contents of frame1
        self.prompt_label1 = tk.Label(self.frame1, text = "Enter a Whale Tracking Number:                           ")
        self.prompt_label1.config(font = ('Courier',15),bg = 'lightblue')
        self.TN = tk.Entry(self.frame1, width = 10)
        self.prompt_label1.pack(side = 'left')
        self.TN.pack(side='left')

        #contents of frame2
        self.prompt_label2 = tk.Label(self.frame2, text = "Enter the Whale Length:                                  ")
        self.prompt_label2.config(font = ('Courier',15),bg = 'lightblue')
        self.Len = tk.Entry(self.frame2, width = 10)
        self.prompt_label2.pack(side = 'left')
        self.Len.pack(side='left')

        #contents of frame3
        self.prompt_label3 = tk.Label(self.frame3, text = "Enter the Whale Weight:                                  ")
        self.prompt_label3.config(font = ('Courier',15),bg = 'lightblue')
        self.We = tk.Entry(self.frame3, width = 10)
        self.prompt_label3.pack(side = 'left')
        self.We.pack(side='left')

        #contents of frame4
        self.prompt_label4 = tk.Label(self.frame4, text = "Enter the Whale Longitude at the last reading:           ")
        self.prompt_label4.config(font = ('Courier',15),bg = 'lightblue')
        self.Lon = tk.Entry(self.frame4, width = 10)
        self.prompt_label4.pack(side = 'left')
        self.Lon.pack(side='left')

        #contents of frame5
        self.prompt_label5 = tk.Label(self.frame5, text = "Enter the Whale Latitude at the last reading:            ")
        self.prompt_label5.config(font = ('Courier',15),bg = 'lightblue')
        self.Lat = tk.Entry(self.frame5, width = 10)
        self.prompt_label5.pack(side = 'left')
        self.Lat.pack(side='left')

        #contents of frame6
        self.prompt_label6 = tk.Label(self.frame6, text = "Enter the Whale Species:                                 ")
        self.prompt_label6.config(font = ('Courier',15),bg = 'lightblue')
        self.S = tk.Entry(self.frame6, width = 10)
        self.prompt_label6.pack(side = 'left')
        self.S.pack(side='left')

        #contents of frame7
        self.prompt_label7 = tk.Label(self.frame7, text = "Enter the Body of Water where the Whale was last located:")
        self.prompt_label7.config(font = ('Courier',15),bg = 'lightblue')
        self.O = tk.Entry(self.frame7, width = 10)
        self.prompt_label7.pack(side = 'left')
        self.O.pack(side='left')


        #contents of frame8
        self.button_Ntr = tk.Button(self.frame8, text = "Enter", command=self.enter)
        self.button_Qt = tk.Button(self.frame8, text = "Quit", command=self.main_window.destroy)
        self.button_Qt.pack(side = 'right')
        self.button_Ntr.pack(side = 'right')


        self.frame1.pack(side = 'top', fill = 'both')
        self.frame2.pack(side = 'top', fill = 'both')
        self.frame3.pack(side = 'top', fill = 'both')
        self.frame4.pack(side = 'top', fill = 'both')
        self.frame5.pack(side = 'top', fill = 'both')
        self.frame6.pack(side = 'top', fill = 'both')
        self.frame7.pack(side = 'top', fill = 'both')
        self.frame8.pack(side = 'top', fill = 'both')

        tk.mainloop()



    def enter(self):
        tn = self.TN.get()
        len = self.Len.get()
        we = self.We.get()
        lon = self.Lon.get()
        lat = self.Lat.get()
        s = self.S.get()
        o = self.O.get()
        cursor.execute("INSERT INTO Whales VALUES (?,?,?,?,?,?,?);", (tn, len, we, lon, lat, s, o))
        self.TN.delete(0,'end')
        self.Len.delete(0,'end')
        self.We.delete(0,'end')
        self.Lon.delete(0,'end')
        self.Lat.delete(0,'end')
        self.S.delete(0,'end')
        self.O.delete(0,'end')



# Create in instance of the GUI class
G = GUI()


#to commit the execute statements above to the database
connection.commit()

#### QUERY SECTION ##########################################################

#select all the records from the Whales table
cursor.execute("SELECT * FROM Whales;")
result = cursor.fetchall()

#Make a dataframe to display the data
df_result = pd.DataFrame(result)
df_result.columns = ["Tracking Number", "Length", "Weight", "Longitude", "Latitude", "Species","Ocean"]
print("-----------------------------")
print(df_result)


Blue_len = cursor.execute("SELECT Length FROM Whales WHERE Species = 'Blue';")
Blue_len = list(Blue_len)
ave_blue = np.sum(Blue_len)/len(Blue_len)

blat = cursor.execute("SELECT Latitude FROM Whales WHERE Species ='Blue';")
blat = list(blat)
blon = cursor.execute("SELECT Longitude FROM Whales WHERE Species = 'Blue';")
blon = list(blon)
#find the species of whales that live in fresh watter
fresh = cursor.execute("SELECT Species, Name_, Latitude, Longitude FROM Whales INNER JOIN Waters ON Whales.Ocean=Waters.Name_ "
                          "WHERE SaltOrFresh = 'F'; ")
fresh = list(fresh)

print("The following whales are not safe in fresh water: ",fresh)
#drop the tables we created
dropTables = """DROP TABLE Whales;"""
cursor.execute(dropTables)
cursor.execute("DROP TABLE Waters;")

print(np.shape(blon))
Distance = np.sqrt((blon[0][0] - blon[1][0])**2 + (blat[0][0] - blat[1][0])**2)

print("The number of Blue whales in our Data is: ", len(Blue_len))
print("The Blue Whales in our Data are", np.round(Distance*69.407,4),"Miles Apart")
print("They are: ", end='')
for i in range(0,(len(Blue_len)-1)):
    print(Blue_len[i][0], ', ',end='')
print("and", Blue_len[len(Blue_len)-1][0], "Feet long.")
print("The Average Length of the Blue whales in our Data is: ", ave_blue)


#commit the action to memory and close the database connection
connection.commit()
connection.close()

