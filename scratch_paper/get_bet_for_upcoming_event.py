# -*- coding: utf-8 -*-

import header as h
import pandas as pd
import numpy as np
import fs_definitions as fsd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression 
import seaborn as sns
import matplotlib.pyplot as plt

fs = 'c3d'
number_of_fights = 11

df = h.create_fight_df('../data/event.csv')
old_df = df
df = h.get_test_probs(df,fs,75,number_of_fights, count_split=True)

display(df.columns)

#We need a fighter list:
    
fighter_list = old_df.get(["R_fighter", "B_fighter"]) 

event_fighter_list = fighter_list[:number_of_fights]
event_fighter_list = event_fighter_list.to_numpy()
print(event_fighter_list)


for index, row in df.iterrows():
    pass
    R_bet_ev = h.get_fighter_ev(row['R_prob'], row['R_ev_final'])
    B_bet_ev = h.get_fighter_ev(row['B_prob'], row['B_ev_final'])
    print(event_fighter_list[index][0], "has an EV of $", round(R_bet_ev, 2), 
          "he has a ", round(row['R_prob']*100, 2), "% chance of winning.", 
          "his return on a $100 bet would be", round(row['R_ev_final'],2),
          event_fighter_list[index][1], "has an EV of $", round(B_bet_ev,2),
    "he has a ", round(row['B_prob']*100, 2), "% chance of winning.",
    "his return on a $100 bet would be", round(row['B_ev_final'],2),
)

    print()


#df_results = h.get_bet_results(df)

#print(df_results)



#results = (h.get_bet_results_multiple(old_df, 10, fs))

#print(results.shape)

#print(results)

#results.to_csv('results.csv')