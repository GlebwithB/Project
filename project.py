

import matplotlib.pyplot as plt

import pandas as pd

file = open("C:\\Users\\user\\Desktop\\PYTHON (.py)\\covid-info.txt")
ontariodates = file.read()

file2 = open("C:\\Users\\user\\Desktop\\PYTHON (.py)\\covid-cases.txt")
ontariocases = file2.read()

file3 = open("C:\\Users\\user\\Desktop\\PYTHON (.py)\\quebeccases.txt")
quebeccases = file3.read()

file4 = open("C:\\Users\\user\\Desktop\\PYTHON (.py)\\quebecdates.txt")
quebecdates = file4.read()


quebeccases = quebeccases.split()
quebecdates = quebecdates.split()
ontariodates = ontariodates.split()
ontariocases = ontariocases.split()



ontariocases = [int(case) for case in ontariocases]
quebeccases = [int(qcase) for qcase in quebeccases]


feb = 0

monthsinfo = {
    "01" : {"days" : 31, "monthlist": 0}, 

    "02" : {"days": feb, "monthlist" : 1},

    "03" : {"days" : 31, "monthlist": 2},

    "04" : {"days" : 30, "monthlist": 3},

    "05" : {"days" : 31, "monthlist": 4},

    "06" : {"days" : 30, "monthlist": 5},

    "07" : {"days" : 31, "monthlist": 6},

    "08" : {"days" : 31, "monthlist": 7},

    "09" : {"days" : 30, "monthlist": 8},

    "10" : {"days" : 31, "monthlist": 9},

    "11" : {"days" : 30, "monthlist": 10},

    "12" : {"days" : 31, "monthlist": 11},
        }


def translatedate(date):
    number = 0 
    #2020-01-01 = 1
    #2020-03-01
    date.split("-")
    #date = [2020, 03, 01]

    if date[0] == "2020" or date[0] == "2024":
        
    

        
        if date[0] == "2020" or date[0] == "2024":
            
            feb = 29

    else:
        feb = 28



    

        #jan, march, april, may, june, july, august, september, october, november, december = 31, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31

        
    

       #add months

    for x in range(monthsinfo[date[1]]["monthslist"]):
        number+= (monthsinfo["days"])


    #add days

    number += int(date[2])

    year = int(date[0]) - 2020
    #if covid started in 2020, we dont add the days in 2019 to the number 



    #adding years


    if year > 0 or year == 4:
        number +=  (year*365) + 1

    else:
        number+= (year*365) 


    print(str(number))


(translatedate("2021-08-12"))






plt.xlabel("Dates \n Orange - Quebec | Blue - Ontario")
plt.ylabel("Total Case Count (Millions)")


plt.plot(quebeccases)
plt.plot(ontariocases)
plt.show()









