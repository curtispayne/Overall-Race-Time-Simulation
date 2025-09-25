import numpy as np
import pandas as pd

def calc(s1,s2,data):

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

    ##  One-Stop Simulation
    onestop_time = 20000

    results = []
    #Comparing to Get Stint 1 Values
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

    #Comparing to Get Stint 2 Values
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

    #Iterating through pitting on each lap
    for pit_lap in range(1,laps+1):
        stint_1 = 0
        stint_2 = 0
        #Calculating each laptime up to the pit lap
        for lap in range(1,pit_lap+1):
            cur_lap = lap1 + (lap-1)*deg1
            stint_1 = stint_1 + cur_lap
        #Calculating each laptime after the pit lap
        for lap in range (pit_lap+1,laps+1):
            cur_lap = lap2 + (lap-1)*deg2
            stint_2 = stint_2 + cur_lap
        #Calculating total race time for this pit lap
        tot_time = stint_1 + stint_2 + pit_time + lap1_add
        #Adding results
        results.append({"Time": tot_time,"Pit Lap": pit_lap,"Tyre 1": tyre1,"Tyre 2": tyre2})
                
    results = pd.DataFrame(results)
    results = results.sort_values(by="Time",ascending=True)
    return results