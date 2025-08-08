

import numpy as np

temp = np.array([0.0, 5.2, 3.1, 0.0, 12.4, 0.0, 7.5])

total_rainfall = np.sum(temp)
round_rainfall = round(total_rainfall, 2)

Average_rainfall = np.mean(temp)

round_avg = round(Average_rainfall, 2)

No_rain = np.where( temp <= 0)

Index = np.where(temp > 5)

#round_index = round(Index, 2)

print("The total rainfall for the week:", round_rainfall)

print("The Average rainfall in a week is:", round_avg)

print("the week days where no rainfall was seen(0=monday, 6=sunday):", No_rain[0])

print("the week days where no rainfall was seen(0=monday, 6=sunday):", Index[0])
