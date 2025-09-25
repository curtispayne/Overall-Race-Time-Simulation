import numpy as np
import pandas as pd

def calc(s1,s2,s3,s4,data):

    ##  Defining initial parameters
    #Deg per lap
    hard_deg = data["hard_deg"]
    med_deg = data["med_deg"]
    soft_deg = data["soft_deg"]

    #Initial Laptimes
    hard_init = data["hard_init"]
    med_init = data["med_init"]
    soft_init = data["soft_init"]
    lap1_add = data["lap1"]

    #Pit Loss Time
    pit_stat = data["pit_stat"]
    pit_mov = data["pit_mov"]
    pit_time = pit_stat + pit_mov

    #Number of Laps
    laps = data["laps"]

    ##  Three-Stop Simulation
    threestop_time = 20000

    results = []
    #First loop for tyre choice in first stint
    if s1 == 'hard':
        lap1 = hard_init
        deg1 = hard_deg
        tyre1 = 'hard'
    elif s1 == 'med':
        lap1 = med_init
        deg1 = med_deg
        tyre1 = 'med'
    else:
        lap1 = soft_init
        deg1 = soft_deg
        tyre1 = 'soft'
    #Second loop for tyre choice in second stint
    if s2 == 'hard':
        lap2 = hard_init
        deg2 = hard_deg
        tyre2 = 'hard'
    elif s2 == 'med':
        lap2 = med_init
        deg2 = med_deg
        tyre2 = 'med'
    else:
        lap2 = soft_init
        deg2 = soft_deg
        tyre2 = 'soft'
    #Third loop for tyre choice in third stint
    if s3 == 'hard':
        lap3 = hard_init
        deg3 = hard_deg
        tyre3 = 'hard'
    elif s3 == 'med':
        lap3 = med_init
        deg3 = med_deg
        tyre3 = 'med'
    else:
        lap3 = soft_init
        deg3 = soft_deg
        tyre3 = 'soft'
    #Fourth Loop for tyre choice in fourth stint
    if s4 == 'hard':
        lap4 = hard_init
        deg4 = hard_deg
        tyre4 = 'hard'
    elif s4 == 'med':
        lap4 = med_init
        deg4 = med_deg
        tyre4 = 'med'
    else:
        lap4 = soft_init
        deg4 = soft_deg
        tyre4 = 'soft'
    #Iterating through first stop on each lap
    for pit_lap1 in range(1,laps-1):
        #Iterating through second stop on each lap
        for pit_lap2 in range(pit_lap1+1,laps):
            #Iteration through third stop on each lap
            for pit_lap3 in range(pit_lap2+1,laps+1):
                stint_1 = 0
                stint_2 = 0
                stint_3 = 0
                stint_4 = 0
                #Calculating each laptime in first stint
                for lap in range(1,pit_lap1+1):
                    cur_lap = lap1 + (lap-1)*deg1
                    stint_1 = stint_1 + cur_lap
                #Calculating each laptime in second stint
                for lap in range (pit_lap1+1,pit_lap2+1):
                    cur_lap = lap2 + (lap-1)*deg2
                    stint_2 = stint_2 + cur_lap
                #Calculating each laptime in third stint
                for lap in range(pit_lap2+1,pit_lap3+1):
                    cur_lap = lap3 + (lap-1)*deg3
                    stint_3 = stint_3 + cur_lap
                #Calculating each laptime in fourth stint
                for lap in range(pit_lap3+1,laps+1):
                    cur_lap = lap4 + (lap-1)*deg4
                    stint_4 = stint_4 + cur_lap
                #Calculating total race time for this pit lap
                tot_time = stint_1 + stint_2 + stint_3 + stint_4 + 3*pit_time + lap1_add
                #Ensuring two sets of tyres are used
                if tyre1 == tyre2 == tyre3 == tyre4:
                    tot_time = 100000
                #Adding results
                results.append({"Time": tot_time,"Pit Lap 1": pit_lap1,"Pit Lap 2": pit_lap2,"Pit Lap 3":pit_lap3,"Tyre 1": tyre1,"Tyre 2": tyre2,"Tyre 3": tyre3,"Tyre 4": tyre4})

    results = pd.DataFrame(results)
    results = results.sort_values(by="Time",ascending=True)
    return results