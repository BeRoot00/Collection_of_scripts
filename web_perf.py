import schedule
import time
import requests
import matplotlib.pyplot as plt
import numpy as np

tab = []

def job():
    for i in range(1000):
        timeStart = time.time()
        print(timeStart)
        req = requests.get("http://localhost:8084")
        timeEnd = time.time()
        duration = timeEnd - timeStart
        tab.append(duration)
        
    for i in range(1000):
        print(tab[i])
    
    mean = np.mean(tab)
    percentile_95 = np.percentile(tab, 95)
    percentile_99 = np.percentile(tab, 99)
    
    # Plotting
    plt.hist(tab, bins=50, edgecolor='black')
    plt.axvline(mean, color='r', linestyle='dashed', linewidth=1, label='Mean')
    plt.axvline(percentile_95, color='g', linestyle='dashed', linewidth=1, label='95th Percentile')
    plt.axvline(percentile_99, color='b', linestyle='dashed', linewidth=1, label='99th Percentile')
    plt.legend()
    plt.xlabel('Duration')
    plt.ylabel('Count')
    plt.title('Histogram of Durations')
    plt.show()

schedule.every(0.01).minutes.do(job)

while True:
    schedule.run_pending()
    time.sleep(10)

