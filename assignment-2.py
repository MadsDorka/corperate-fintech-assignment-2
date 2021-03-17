# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 11:45:48 2021

@author: Max Festersen Hansen, Daniel Lindberg, Mads Duelund Dorka, Mathias Eriksen, Emilie Bruun Therp
"""

#%% Name and e-mail
print('Mads Duelund Dorka, mador17@student.sdu.dk')
print('Max Festersen Hansen, maxfh20@student.sdu.dk')
print('Mathias Eriksen, merik17@student.sdu.dk')
print('Daniel Lindberg, dlind16@student.sdu.dk')
print('Emilie Bruun Therp, emthe15@student.sdu.dk')

#%% Imports
import os # To set dir
import pprint # To print "stuff" pretty
import pandas as pd
import json # To work with json files
from textblob import TextBlob # To do Naïve Bayes classifification
from datetime import datetime # To format strings as dates


#%% Enviroment and Data imports
os.chdir(os.path.dirname(os.path.realpath(__file__))) # Set dir
filename = 'icoData_19092018.json'

with open(filename) as json_data:
    icoData = json.load(json_data) #Load data into a list


#%% Formatting data
icoData = [x for x in icoData if not len(x) == 1]  # Filter list - remove empty dirs

icoDataFiltPersonNum = []
icoDataFiltReview = []
icoDataFiltReviewNum = []

i = 0
personNum = 0
reviewNum = 0
# Loop all of icoData
for person in icoData:
    personNum += 1 # Count next person
    # Filter end-dates after 19-10-2018
    endDate = person['dates']["icoEnd"].split(" ")[0]
    if endDate != '0000-00-00' and datetime.strptime(endDate, "%Y-%m-%d") < datetime.strptime("2018-10-19", "%Y-%m-%d"):
        validDate = True # If the date is a valid date, and before 2018-10-19
    else:
        validDate = False
    if validDate:
        for rating in person['ratings']:
            if "review" in rating and len(rating["review"]) > 0:
                reviewNum += 1 # Count valid review
                # Save ratings review instance
                icoDataFiltPersonNum.append(personNum)
                icoDataFiltReviewNum.append(reviewNum)
                icoDataFiltReview.append(rating['review'])
    i+=1 # Increment instance counter

# Format as dataframe
reviewDt = pd.DataFrame({'#review': icoDataFiltReviewNum,'Person ID': icoDataFiltPersonNum, 'Review':icoDataFiltReview})

#%% Excersice 1
# Forventningsafsnit
pprint.pprint("")

# Udførelse af opgave

# Interpretation/Diskusion af øknomiske aspekter af resultatet
pprint.pprint("")

#%% Excersice 2
# Forventningsafsnit
pprint.pprint("")

# Matematiske udregninger
pprint.pprint("")

#%% Excersice 2 a
# Forventningsafsnit
pprint.pprint("")

# Matematiske udregninger
# Use pandas .describe + numpy .median to get the values they ask for!
pprint.pprint("")

# Udførelse af opgave

# Interpretation/Diskusion af øknomiske aspekter af resultatet
pprint.pprint("")

#%% Excersice 2 b
# Forventningsafsnit
pprint.pprint("")

# Matematiske udregninger
# Fog Index = 0.4 *(average # of words per sentence + 100 * percent of complex words)

pprint.pprint("")

# Udførelse af opgave

# Interpretation/Diskusion af øknomiske aspekter af resultatet
pprint.pprint("")

#%% Excersice 2 c
# Forventningsafsnit
pprint.pprint("")

# Matematiske udregninger

#See previous exercises made in class
pprint.pprint("")

# Udførelse af opgave

# Interpretation/Diskusion af øknomiske aspekter af resultatet
pprint.pprint("")

#%% Excersice 2 d
# Forventningsafsnit
pprint.pprint("")

# Matematiske udregninger
# OLS
# https://www.datarobot.com/blog/ordinary-least-squares-in-python/

# Logit Regression
# https://www.datacamp.com/community/tutorials/understanding-logistic-regression-python
pprint.pprint("")

# Udførelse af opgave
#%% Excersice 2 d i

#%% Excersice 2 d ii

# Interpretation/Diskusion af øknomiske aspekter af resultatet
pprint.pprint("")

#%% Excersice 2 outro
# Interpretation/Diskusion af øknomiske aspekter af resultatet
pprint.pprint("")


#%% Excersice 3
# Forventningsafsnit
pprint.pprint("")

# Matematiske udregninger
pprint.pprint("")

# Udførelse af opgave

#%% Excersice 3 part 1
# Forventningsafsnit
pprint.pprint("")

# Matematiske udregninger
pprint.pprint("")

# Udførelse af opgave

# Interpretation/Diskusion af øknomiske aspekter af resultatet
pprint.pprint("")

#%% Excersice 3 part 2
# Forventningsafsnit
pprint.pprint("")

# Matematiske udregninger
pprint.pprint("")

# Udførelse af opgave

# Interpretation/Diskusion af øknomiske aspekter af resultatet
pprint.pprint("")

#%% Excersice 3 part 3
# Forventningsafsnit
pprint.pprint("")

# Matematiske udregninger
pprint.pprint("")

#%% Excersice 3 part 3 a
# Forventningsafsnit
pprint.pprint("")

# Matematiske udregninger
pprint.pprint("")

# Udførelse af opgave

# Interpretation/Diskusion af øknomiske aspekter af resultatet
pprint.pprint("")

#%% Excersice 3 part 3 b
# Forventningsafsnit
pprint.pprint("")

# Matematiske udregninger
pprint.pprint("")

# Udførelse af opgave

# Interpretation/Diskusion af øknomiske aspekter af resultatet
pprint.pprint("")

#%% Excersice 3 part 3 c
# Forventningsafsnit
pprint.pprint("")

# Matematiske udregninger
pprint.pprint("")

# Udførelse af opgave

# Interpretation/Diskusion af øknomiske aspekter af resultatet
pprint.pprint("")

#%% Excersice 3 part 3 d
# Forventningsafsnit
pprint.pprint("")

# Matematiske udregninger
pprint.pprint("")

#%% Excersice 3 part 3 d i

#%% Excersice 3 part 3 d ii

# Interpretation/Diskusion af øknomiske aspekter af resultatet
pprint.pprint("")


#%% Excersice 3 part 3 outro
# Interpretation/Diskusion af øknomiske aspekter af resultatet
pprint.pprint("")

#%% Excersice 3 outro
# Interpretation/Diskusion af øknomiske aspekter af resultatet
pprint.pprint("")
