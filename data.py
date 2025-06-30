'''This script processes experimental data related to titration at different temperatures.'''
# Import necessary libraries
import numpy as np
import pandas as pd

#Import third party libraries
from result_class import Result_Titration

# Raw data for v_titrationexperiments at different temperatures
# Each temperature has its own set of data, including time, time error, titration volumes, and temperature readings.
# The data is structured in lists of numpy arrays for easy manipulation and analysis.

# Description of the data:
description = [
    {
        "type": "Titration",
        "temperature": "80",
        "temperature_unit": "ºC",
        "components": ["Octanoic acid", "Butanol", "PTSA·H2O"],
        "sample_volume": "0.1 mL",
        "titrant": "NaOH",
        "titrant_concentration": "0.1 M",
        "note": ""
    },
    {
        "type": "Titration",
        "temperature": "70",
        "temperature_unit": "ºC",
        "components": ["Octanoic acid", "Butanol", "PTSA·H2O"],
        "sample_volume": "0.1 mL",
        "titrant": "NaOH",
        "titrant_concentration": "0.1 M",
        "note": ""
    },
    {
        "type": "Titration",
        "temperature": "60",
        "temperature_unit": "ºC",
        "components": ["Octanoic acid", "Butanol", "PTSA·H2O"],
        "sample_volume": "0.1 mL",
        "titrant": "NaOH",
        "titrant_concentration": "0.1 M",
        "note": "First run",
    },
    {
        "type": "Titration",
        "temperature": "60",
        "temperature_unit": "ºC",
        "components": ["Octanoic acid", "Butanol", "PTSA·H2O"],
        "sample_volume": "0.1 mL",
        "titrant": "NaOH",
        "titrant_concentration": "0.1 M",
        "note": "Second run",
    },
    {
        "type": "Titration",
        "temperature": "60",
        "temperature_unit": "ºC",
        "components": ["Octanoic acid", "Butanol", "PTSA·H2O", "Toluene"],
        "sample_volume": "0.1 mL",
        "titrant": "NaOH",
        "titrant_concentration": "0.1 M",
        "note": "With Toluene addition",
    },
]
# 


# Time data for each temperature in minutes
time = [
    #80ºC
    np.array([0, 0, 15, 30, 45, 60, 90, 120, 180, 240, 300, 360, 460]),
    #70ºC
    np.array([0, 0, 15, 30, 45, 60, 90, 120, 180, 240, 300, 360, 420]),
    #60ºC #1
    np.array([0, 0, 15, 30, 45, 60, 90, 120, 180, 240, 300]),
    #60ºC #2
    np.array([
        0, 0, 15, 30, 45, 60, 90, 120, 180, 240, 300, 360,
              #420,
                430]),
    #60ºC #Tolueno
    np.array([0, 0, 15, 30, 45, 60, 90, 120, 180, 240, 300, 360, 420, 480]),
    ]

# Time error or offset data for each temperature in minutes
time_error = [
    #80ºC
    np.array([0, 2, 3, 1, 2, 0, 4, 2, 0, 0, 0, 3, 0]),
    #70ºC
    np.array([0, 2, 3,-1, 0, 0, 1, 0, 0, 0, 4, 0, 0]),
    #60ºC #1
    np.array([0, 2, 0, 1, 2, 1, 0, 2, 0, 2,-1]),
    #60ºC #2
    np.array([
        0, 2, 2, 3, 0, 0, 2, 1, 4, 0, 2, 2,
        #1,
        0]),
    #60ºC #Tolueno
    np.array([0, 3, 1, 0, 1, 3, 0, 1, 0, 0, 2, 7, 1, 0]),
    ]

# Sample volume for each titration experiment in mL
sample_volume = [
    # 80ºC
    0.1,  # mL
    # 70ºC
    0.1,  # mL
    # 60ºC #1
    0.1,  # mL
    # 60ºC #2
    0.1,  # mL
    # 60ºC #Tolueno
    0.1,  # mL
]


# Titration volume data for each temperature
v_titration= [
    np.array([
    # 80ºC
    3.84, 3.84, 3.72, 
    3.4, 3.38, 3.38, 
    1.53, 1.43, 1.5, 
    1.35, 1.23, 1.34, 
    1.16, 1.1, 1.15, 
    1.16, 1.18, 1.13,
    1.1, 1.08, 1.04,
    1.01, 0.99, 1.03,
    1, 0.96, 0.97,
    0.88, 0.94, 0.94,
    0.91, 0.95, 0.94,
    0.94, 0.89, 0.95,
    0.9, 0.92, 0.9
    ]),
    # 70ºC
    np.array([
    3.75,3.88,3.84,
    3.45,3.50,3.67,
    1.86,2.18,1.87,
    1.73,1.90,1.60,
    1.50,1.44,1.70,
    1.70,1.37,1.30,
    1.51,1.29,1.32,
    1.25,1.19,1.22,
    1.06,1.28,1.10,
    1.06,1.12,1.08,
    1.04,1.05,1.05,
    1.01,1,1,
    0.96,0.96,0.97
    ]),
    # 60ºC #1
    np.array([
    4.12,4.40,4.40,
    0.00,0.00,0.00,
    2.81,2.78,2.34,
    2.17,2.00,2.07,
    1.93,1.48,1.40,
    1.67,1.21,1.55,
    1.31,0.93,1.11,
    1.40,1.43,1.08,
    1.33,0.96,1.07,
    0.90,1.04,1.25,
    0.82,0.84,0.98,
    ]),
    # 60ºC #2
    np.array([
        3.97,3.86,4.00,
        3.93,3.76,3.89,
        2.50,2.45,2.57,
        1.90,2.00,1.97,
        1.80,1.80,1.85,
        1.64,1.64,1.63,
        1.50,1.51,1.56,
        1.39,1.33,1.40,
        1.23,1.30,1.23,
        1.19,1.17,1.18,
        1.11,1.07,1.14,
        1.12,1.13,1.12,
        #1.06,1.00,1.00,
        1.09,1.06,1.01
    ]),
    # 60ºC #Tolueno
    np.array([
        2.73,2.70,2.785,
        2.64,2.46,2.66,
        1.90,1.92,1.83,
        1.40,1.50,1.30,
        1.34,1.23,1.37,
        1.205,1.19,1.20,
        1.10,1.08,1.11,
        1.09,1.04,1.00,
        0.89,0.90,0.85,
        0.85,0.87,0.85,
        0.83,0.80,0.79,
        0.75,0.76,0.75,
        0.75,0.78,0.74,
        0.75,0.76,0.74,
    ]),
    ]

# Temperature data for each titration experiment
temperature=[
    # 80ºC
    np.array([79,77,79,80,80,80,80,80,80,80,80,80,80]),
    # 70ºC
    np.array([69,66,69,68,70,70,70,70,70,70,70,70,70]),
    # 60ºC #1
    np.array([21, 0,58,59,59,59,59,59,59,59,59]),
    # 60ºC #2
    np.array([
        58,59,60,60,60,60,60,60,60,60,60,60,
              #60,
              60]),
    # 60ºC #Tolueno
    np.array([59,59,59,60,60,60,60,60,60,60,60,60,60,60]),
    ]

# Weight of the titration system sample at different temperatures.
weight =[
    # 80ºC
    [
        # Reaction weights
        # Empty
        np.array([
            0.87195,0.87195,0.87195,
            0.84582,0.84582,0.84582,
            0.89385,0.89385,0.89385,
            0,0,0,
            0.86690,0.86690,0.86690,
            0,0,0,
            0.86810,0.86810,0.86810,
            0,0,0,
            0.87454,0.87454,0.87454,
            0,0,0,
            0.87636,0.87636,0.87636,
            0,0,0,
            0.86485,0.86485,0.86485
            ]),
        # Filled
        np.array([
            0.94593,0.94593,0.94593,
            0.92413,0.92413,0.92413,
            0.96705,0.96705,0.96705,
            0,0,0,
            0.94823,0.94823,0.94823,
            0,0,0,
            0.94212,0.94212,0.94212,
            0,0,0,
            0.95798,0.95798,0.95798,
            0,0,0,
            0.95439,0.95439,0.95439,
            0,0,0,
            0.94255,0.94255,0.94255
        ]),
        # Two phases
        # Empty
        np.array([
            0.86963,0.88239
        ]),
        # Filled
        np.array([
            0.94025,0.99702
        ])
    ],
    # 70ºC
    [],
    # 60ºC #1
    [],
    # 60ºC #2
    [
        # Reaction
        # 60ºC Empty
        np.array([
            0.86454,0.85173,0.89721,
            0,0,0,
            0,0,0,
            0,0,0,
            0,0,0,
            0.86500,0.87305,0.86594,
            0,0,0,
            0.87042,0.88489,0.88329,
            0,0,0,
            0,0,0,
            0.87577,0.89495,0.85190,
            0,0,0,
            #0.89094,0.86164,0.79512,
            0,0,0,
        ]),
        # 60ºC Filled
        np.array([
            0.94374,0.92961,0.97819,
            0,0,0,
            0,0,0,
            0,0,0,
            0,0,0,
            0.94562,0.94971,0.94631,
            0,0,0,
            0.94839,0.96504,0.96426,
            0,0,0,
            0,0,0,
            0.95601,0.97738,0.93304,
            0,0,0,
            #0.97030,0.94071,0.87527,
            0,0,0,
        ]),
        # 60ºC TwoPhases
        # Empty
        np.array([
            1.02097,0.90546
        ]),
        # Filled
        np.array([
            1.09563,1.00515
        ]),
    ],
    # 60ºC #Toluene
    [
        # Reaction
        # 60ºC Empty
        np.array([
            0.91618,0.91607,0.90937,
            0,0,0,
            0,0,0,
            0,0,0,
            0,0,0,
            1.07003,0.86181,0.90876,
            0,0,0,
            0,0,0,
            0,0,0,
            0.90742,0.92667,1.02933,
            0,0,0,
            0,0,0,
            1.02994,0.85866,1.02358,
            0.85355,1.00984,1.01063,
        ]),
        # 60ºC Filled
        np.array([
            0.99220,0.99188,0.98890,
            0,0,0,
            0,0,0,
            0,0,0,
            0,0,0,
            1.14868,0.93195,0.99005,
            0,0,0,
            0,0,0,
            0,0,0,
            0.99004,1.00602,1.11249,
            0,0,0,
            0,0,0,
            1.12260,0.94879,1.10856,
            0.93600,1.08812,1.09484,
        ]),
        # 60ºC TwoPhases
        # Empty
        np.array([1.03655,0.93359]),
        # Filled
        np.array([1.11682,1.04815]),
    ]]

#------------------------
# Processing the data 
# Initialize density array to store calculated densities for each temperature
density_raw = [
    # 80ºC
    np.array([]),
    # 70ºC
    np.array([]),
    # 60ºC #1
    np.array([]),
    # 60ºC #2
    np.array([]),
    # 60ºC #Tolueno
    np.array([]),

]
def get_results():
    '''This function processes the raw data and returns a list of Result_Titration objects containing the processed data.'''
    for i,_ in enumerate(weight):
        if len(weight[i]) != 0:
            density_raw [i]=(weight[i][1]-weight[i][0]) / sample_volume[i]

    # Calculate the mean density for each temperature from the raw data
    # The density is calculated as the difference between filled and empty weights divided by the volume (0.1 mL)
    density_mean = []
    for i,_ in enumerate(density_raw ):
        density_mean.append([])
        for j in range(0, len(density_raw [i]), 3):
            if len(density_raw[i]) > 0:
                density_mean[i].append(np.mean(density_raw[i][j:j+3]).round(3))
            else:
                density_mean.append(None)

    # Delete all zero values of density_mean
    density_reaction = [list(filter(lambda x: x != 0, d)) for d in density_mean]

    density_system = []
    for i,_ in enumerate(density_mean):
        density_system.append([])
        for j in range(0, len(density_mean[i])):
            if len(density_mean[i]) > 0:
                if j == 0:
                    density_system[i].append(density_reaction[i][0])
                else:
                    density_system[i].append(
                        np.mean(density_reaction[i][1:]).round(3))
            else:
                density_system.append(None)

    # I want the density at 60ºC #1 to be the same as the density at 60ºC #2
    if len(density_system[3]) > 0:
        minimum_length = min(len(time[2]), len(time[3]))
        density_system[2] = np.zeros(minimum_length)
        for j in range(minimum_length):
            density_system[2][j] = (density_system[3][j])


    # I want the density at 70ºC to be the mean of the densities at 80ºC and 60ºC #2
    if len(density_system[0]) > 0 and len(density_system[3]) > 0:
        minimum_length = min(len(density_system[0]), len(density_system[3]))
        density_system[1] = np.zeros(minimum_length)
        for j in range(minimum_length):
            density_system[1][j] = ((density_system[0][j] + density_system[3][j]) / 2).round(3)

    titration_results = []

    for i,_ in enumerate(v_titration):
        titration_vol = [[],[],[],]
        for j in range(0,len(v_titration[i]),3):
            titration_vol[0].append(v_titration[i][j])
            titration_vol[1].append(v_titration[i][j+1])
            titration_vol[2].append(v_titration[i][j+2])
        # Convert lists to numpy arrays for consistency
        titration_vol = [np.array(vol) for vol in titration_vol]
        # Ensure the lengths match for DataFrame creation
        df = pd.DataFrame({
            '#': np.arange(1, len(titration_vol[0]) + 1),
            't': time[i],
            't (offset)': time_error[i],
            'T': temperature[i],
            'T (unit)': 'ºC',
            't (unit)': 'min',
            'vt_01': titration_vol[0].round(2),
            'vt_02': titration_vol[1].round(2),
            'vt_03': titration_vol[2].round(2),
            'vt (unit)': 'mL',
            'd': density_system[i] if len(density_system[i]) > 0 else None,
            'd (unit)': 'g/mL',

        })
        df['vt_median'] = np.median([df['vt_01'], df['vt_02'], df['vt_03']], axis=0).round(3)
        df['vt_mean'] = np.mean([df['vt_01'], df['vt_02'], df['vt_03']], axis=0).round(3)
        df['vt_stderr'] = (np.std([df['vt_01'], df['vt_02'], df['vt_03']], axis=0, ddof=1) / np.sqrt(3)).round(3)
        result_titration = Result_Titration(
            name=f"Titration Result {i + 1}",
            description=description[i],
            data=df
        )
        titration_results.append(result_titration)
    return titration_results

if __name__ == "__main__":
    for result in get_results():
        print(result.get_name())
        print(result.get_description())
        print(result.get_data())
        print("\n")
