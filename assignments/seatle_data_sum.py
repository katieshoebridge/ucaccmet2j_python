import json

with open('precipitation.json') as file:
    data = json.load(file)


for measurement in data:
    print(measurement['station'])


seattle_data = [] 

for measurement in data:
    if measurement ['station'] == 'GHCND:US1WAKG0038':
        seattle_data.append(measurement)
#print(seattle_data)


january = 0 
february = 0
march = 0

#for my understanding
#     if '2010-01' in measurement ['date']: 
#         january = january + measurement['value']
#     if '2010-02' in measurement ['date']: 
#         february = february + measurement['value']
#     if '2010-03' in measurement ['date']: 
#         march = march + measurement['value']
# print(january, february, march)

#calculate monthly sum
monthly_sum_results = {'2010-01':0, '2010-02': 0, '2010-03':0, '2010-04':0, '2010-05':0, '2010-06':0, '2010-07':0, '2010-08':0, '2010-09':0, '2010-10':0, '2010-11':0, '2010-12':0}

for measurement in seattle_data: 
    date = measurement ['date'][:-3]
    monthly_sum_results[date] = monthly_sum_results[date] + measurement['value']
#print(monthly_sum)

print(monthly_sum_results.values())

#calculate yearly sum
print(sum(monthly_sum_results.values()))


#save json
with open ('result1.json', 'w') as file:
    json.dump({
	"Seattle": {
		"station": "GHCND:US1WAKG0038", 
		"state": "WA", 
		"totalMonthlyPrecipitation": list(monthly_sum_results.values()), 
		#"relativeMonthlyPrecipitation": [...], 
		"totalYearlyPrecipitation": sum(monthly_sum_results.values())
		
	}
}
       , file, indent=4)

#relative precipitation calculation
individual_months = {'2010-01':0, '2010-02': 0, '2010-03':0, '2010-04':0, '2010-05':0, '2010-06':0, '2010-07':0, '2010-08':0, '2010-09':0, '2010-10':0, '2010-11':0, '2010-12':0}

for month, value in monthly_sum_results.items():
    individual_months[month] = (value/sum(monthly_sum_results.values())*100)
print(individual_months)


with open ('result2.json', 'w') as file:
    json.dump({
	"Seattle": {
		"station": "GHCND:US1WAKG0038", 
		"state": "WA", 
		"totalMonthlyPrecipitation": list(monthly_sum_results.values()), 
		"relativeMonthlyPrecipitation": individual_months, 
		"totalYearlyPrecipitation": sum(monthly_sum_results.values())
		
	}
}
       , file, indent=4)


