# Reads AESO hourly power load data 
# and exports average for each hour

import csv

IN_FILE = './data/AESO Hourly Power Load 2016.csv'
OUT_FILE = './data/AESO Hourly Power Load Averaged.csv'

with open(OUT_FILE, 'w', encoding='utf8', newline='') as outFile:
    internalLoadStat = {}
    systemLoadStat = {}
    meteredLoadStat = {}

    for i in range(24):
        internalLoadStat[i] = []
        systemLoadStat[i] = []
        meteredLoadStat[i] = []

    with open(IN_FILE, 'r', encoding='utf8') as inFile:
        reader = csv.reader(inFile, delimiter=',')
        for line in reader:
            hour = int(line[1])
            internalLoad = int(line[4])  # Alberta internal load
            systemLoad = int(line[5])    # System implied load
            meteredLoad = int(line[6])   # Metered load

            # Add to stat
            internalLoadStat[hour].append(internalLoad)
            systemLoadStat[hour].append(systemLoad)
            meteredLoadStat[hour].append(meteredLoad)
    
    # Summarize results
    writer = csv.writer(outFile, delimiter=',')
    writer.writerow(['hour, internal load', 'system implied load', 'metered load'])
    for i in range(24):
        hourlyInternalLoad = sum(internalLoadStat[i]) / len(internalLoadStat[i])
        hourlySystemLoad = sum(systemLoadStat[i]) / len(systemLoadStat[i])
        hourlyMeteredLoad = sum(meteredLoadStat[i]) / len(meteredLoadStat[i])

        print(str(i) + ':\t' + str(hourlyInternalLoad) + '\t' + 
        str(hourlySystemLoad) + '\t' + str(hourlyMeteredLoad))

        # Write to file
        writer.writerow([
            '%d:00' % i,
            '%.2f' % hourlyInternalLoad,
            '%.2f' % hourlySystemLoad,
            '%.2f' % hourlyMeteredLoad
        ])