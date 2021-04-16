import sqlite3
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk

'''In this program we create a database using the SQL language inside Python. We also create
a way to access this database using a graphical user interface. To do this we use the sqlite3
and the Tkinter packages.'''

#### DATABASE SECTION ##########################################################
"""This part of the program creates a database of whales and the bodies of water in which the reside."""

connection = sqlite3.connect("Whales.db")
cursor = connection.cursor()

data = pd.DataFrame()


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


### Creates a list of strings that can be used to input the data into the SQL database using the cursor.execute below
Data_to_insert = []
Data_to_insert.append("""INSERT INTO Whales (TrackingNumber,Length,Weight,Longitude,Latitude,Species,Ocean)
VALUES (1,100,105,44.4311,25.1167,"Blue","Atlantic");""")
Data_to_insert1 = """INSERT INTO Whales (TrackingNumber,Length,Weight,Longitude,Latitude,Species,Ocean)
VALUES (2,54,30,40.2573,32.9931,"Wright","Atlantic");"""
Data_to_insert.append( """INSERT INTO Whales (TrackingNumber,Length,Weight,Longitude,Latitude,Species,Ocean)
VALUES (3,51,27,41.0009,33.8967,"Grey","Atlantic");""")
Data_to_insert.append("""INSERT INTO Whales (TrackingNumber,Length,Weight,Longitude,Latitude,Species,Ocean)
VALUES (4,49,29,-4.9341,35.0906,"Humpback","Mediterranean");""")
Data_to_insert.append("""INSERT INTO Whales (TrackingNumber,Length,Weight,Longitude,Latitude,Species,Ocean)
VALUES (5,63,27,-38.7769,-35.0134,"Sperm","Indian");""")
Data_to_insert.append("""INSERT INTO Whales (TrackingNumber,Length,Weight,Longitude,Latitude,Species,Ocean)
VALUES (6,77,27,146.8129,31.7568,"Finback","Pacific");""")
Data_to_insert.append("""INSERT INTO Whales (TrackingNumber,Length,Weight,Longitude,Latitude,Species,Ocean)
VALUES (7,105,117,44.5312,24.9968,"Blue","Atlantic");""")
Data_to_insert.append("""INSERT INTO Whales (TrackingNumber,Length,Weight,Longitude,Latitude,Species,Ocean)
VALUES (8,25,11,77.5312,43.9968,"Beluga","Great_Lakes");""")


# Tests to make sure the database has not already entered the same data point into the database.
try:
    cursor.execute(whales_table)
except:
    print("You already created the whales_table")

for data in range(0,len(Data_to_insert)):
    try:
        cursor.execute(Data_to_insert[data])
    except:
        print("You already created this row")

waters_to_insert = []
waters_to_insert.append("""INSERT INTO Waters (Name_,AveDepth,SaltOrFresh) VALUES ("Atlantic", 4500, "S");""")
waters_to_insert.append("""INSERT INTO Waters (Name_,AveDepth,SaltOrFresh) VALUES ("Pacific", 4900, "S");""")
waters_to_insert.append("""INSERT INTO Waters (Name_,AveDepth,SaltOrFresh) VALUES ("Indian", 4200, "S");""")
waters_to_insert.append("""INSERT INTO Waters (Name_,AveDepth,SaltOrFresh) VALUES ("Arctic", 3500, "S");""")
waters_to_insert.append("""INSERT INTO Waters (Name_,AveDepth,SaltOrFresh) VALUES ("Mediterranean", 1500, "S");""")
waters_to_insert.append("""INSERT INTO Waters (Name_,AveDepth,SaltOrFresh) VALUES ("Great_Lakes", 1000, "F");""")


for water in range(0,len(waters_to_insert)):
    try:
        cursor.execute(waters_to_insert[water])
    except:
        print("This record already exists in the database")

#### GUI SECTION ############################################################
'''Here we create the graphical user interface with a light blue background and
several different frames, labels, buttons and Entry text boxes.'''

class GUI:
    def __init__(self):
        self.main_window = tk.Tk()
        self.main_window.title("Enter a Whale")

        #frame the parts of the GUI
        self.framearray = []
        
        for i in range(0,8):
            self.framearray.append(tk.Frame(self.main_window))
            self.framearray[i].configure(bg='lightblue')

        self.textlist = []
        self.textlist.append("Enter the Whale Tracking Number:                         ")
        self.textlist.append("Enter the Whale Length:                                  ")
        self.textlist.append("Enter the Whale Weight:                                  ")
        self.textlist.append("Enter the Whale Longitude at the last reading:           ")
        self.textlist.append("Enter the Whale Latitude at the last reading:            ")
        self.textlist.append("Enter the Whale Species:                                 ")
        self.textlist.append("Enter the Body of Water where the Whale was last located:")
        
        self.entry = []
        self.prompt_label = []

        for i in range(0,len(self.textlist)):#contents of framearray[i]
            self.prompt_label.append(tk.Label(self.framearray[i], text = self.textlist[i]))
            self.prompt_label[i].config(font = ('Courier',15),bg = 'lightblue')
            self.entry.append(tk.Entry(self.framearray[i], width = 10))
            self.prompt_label[i].pack(side = 'left')
            self.entry[i].pack(side='left')

        #contents of framearray[7]
        self.button_Ntr = tk.Button(self.framearray[7], text = "Enter", command=self.enter) #enter method defined below
        self.button_Qt = tk.Button(self.framearray[7], text = "Quit", command=self.main_window.destroy)
        self.button_Qt.pack(side = 'right')
        self.button_Ntr.pack(side = 'right')

        #pack the frames into the window
        for i in range(0,8):
            self.framearray[i].pack(side = 'top', fill = 'both')

        tk.mainloop()


    # Enters the information that the user input into the GUI into the database
    def enter(self):
        e = []

        for i in range(0,7):
            e.append(self.entry[i].get())

        try:    
            cursor.execute("INSERT INTO Whales VALUES (?,?,?,?,?,?,?);", (e[0], e[1], e[2], e[3], e[4], e[5], e[6]))
        except:
            print("This record already exists in the database")
        
        for i in range(0,7):
            self.entry[i].delete(0,'end')
        



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