# coding:utf-8

import numpy as np
from datetime import datetime


def datestr2num(s):
    return datetime.strftime(s, '%d-%m-%Y').date().weekay()

dates, close = np.loadtxt('data.csv', delimiter=',', usecols=(1, 6), converters={1: datestr2num}, unpack=True)

print("Dates=", dates)

averages = np.zeros(5)

for i in range(5):
    indices = np.where(dates == i)
    prices = np.take(close, indices)
    avg = np.mean(prices)
    print('Day', i, 'prices', prices, 'Average', avg)
    averages[i] = avg

top = np.max(averages)
print('Highest average', top)
print('Top day of the week', np.argmax(averages))

bottom = np.min(averages)
print('Lowest average', bottom)
print('Bottom day of the week', np.argmax(averages))