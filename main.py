import numpy as np
import pandas as pd
import onestop
import twostop 
import threestop

data = {"hard_deg": 0.02,
        "hard_init": 98,
        "med_deg": 0.06,
        "med_init": 97.4,
        "soft_deg": 0.12,
        "soft_init": 96.6,
        "pit_stat": 2.7,
        "pit_mov": 18,
        "lap1": 7,
        "laps": 62}

tyre1 = input('Tyre 1: ')
tyre2 = input('Tyre 2: ')
tyre3 = input('Tyre 3: ')
tyre4 = input('Tyre 4: ')

if tyre3 in ('soft','med','hard'):
    if tyre4 in ('soft','med','hard'):
        result = threestop.calc(tyre1,tyre2,tyre3,tyre4,data)
    else:
        result = twostop.calc(tyre1,tyre2,tyre3,data)
else:
    result = onestop.calc(tyre1,tyre2,data)
print(result.head(20))