import pandas
from sklearn import linear_model

cars = pandas.read_csv("cars.csv")

X =cars[['Weight', 'Volume']]
y = cars['CO2']

regr = linear_model.LinearRegression()
regr.fit(X, y)

#predict the CO2 emission of a car where the weight is 2300kg, and the volume is 1300cm3:
predictedCO2 = regr.predict([[200, 13000]])

print(predictedCO2)
#Coefficient
print(regr.coef_)


