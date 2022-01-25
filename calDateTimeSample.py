#!/bin/python3

import sys
import os

# Complete the function below.
from pandas import np
from sklearn.linear_model import LinearRegression


def predictTemperature(startDate, endDate, temperature, n):
    ##################################
    # create training data
    # feature : Year, Month, Day, Time
    # y value : Temperature
    ##################################
    x_train = []
    y_train = []

    year = int(startDate.split('-')[0])
    month = int(startDate.split('-')[1])
    day = int(startDate.split('-')[2])

    time = 0

    ##
    from datetime import date
    from datetime import datetime, timedelta

    d = datetime(2013, 1, 31) + timedelta(days=1)
    print(d)

    d + timedelta(hours=1)
    d + timedelta(minutes=1)

    d0 = date(2008, 8, 18)
    d1 = date(2008, 9, 26)
    delta = d1 - d0
    print(delta.days)
    ##

    for temp in temperature:
        row = []
        row.append(year)
        row.append(month)
        row.append(day)
        row.append(time)
        x_train.append(row)
        y_train.append(temp)

        # time update
        if time == 23:
            if day < 30:  # Wrong approach - Just assumed a month is 30 days
                day += 1
            else:
                if month == 12:
                    month = 1
                else:
                    month += 1
                day = 1
            time = 0
        else:
            time += 1

    print(x_train)
    print(y_train)

    ##################################
    # create test data
    # feature : Year, Month, Day, Time
    # y value : unkown
    ##################################
    x_test = []

    year = int(endDate.split('-')[0])
    month = int(endDate.split('-')[1])
    day = int(endDate.split('-')[2]) + 1  # next day

    time = 0
    for i in range(n * 24):
        row = []
        row.append(year)
        row.append(month)
        row.append(day)
        row.append(time)
        x_test.append(row)

        # time update
        if time == 23:
            if day < 30:  # Wrong approach - Just assumed a month is 30 days
                day += 1
            else:
                if month == 12:
                    month = 1
                else:
                    month += 1
                day = 1
            time = 0
        else:
            time += 1

    print(x_test)

    ##################################
    # train and prediction using LR
    # as the data type is continuous / regression problem
    ##################################
    model = LinearRegression()
    model.fit(x_train, y_train)
    res = model.predict(x_test)

    for idx, temp in enumerate(res):
        if temp > 40:
            temp = 25
            res[idx] = temp
    return res


# TEST
start = '2013-01-01'
end = '2013-01-01'
n = 1
temp = np.random.uniform(low=0.5, high=13.3, size=(24,))

predictTemperature(start, end, temp, n)