#!/usr/bin/python

def scale(series):
	highest = 0
	lowest = 0

	for item in series:
		if item > highest and item != 0:
			highest = item
		if item < lowest and item != 0:
			lowest = item
	if lowest > 0:
		zero_scaler = lowest - (lowest*2)
	else:
		zero_scaler = abs(lowest)

	for i in range(0,len(series)):
		series[i] = series[i] + zero_scaler

	scaler = highest/100.0

	for i in range(0,len(series)):
		if series[i] != 0:
			series[i] = series[i]/scaler
	
	return(series)

