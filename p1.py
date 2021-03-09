import pandas as pd

data = [
	{"Gender": "Male", "HeightCm": 171, "WeightKg": 96 },
	{ "Gender": "Male", "HeightCm": 161, "WeightKg": 85 },
	{ "Gender": "Male", "HeightCm": 180, "WeightKg": 77 },
	{ "Gender": "Female", "HeightCm": 166, "WeightKg": 62},
	{"Gender": "Female", "HeightCm": 150, "WeightKg": 70},
	{"Gender": "Female", "HeightCm": 167, "WeightKg": 82}
]

#Coverting dataset to Dataframe
#df = pd.DataFrame(data)

#Getting data from CSV
df = pd.read_csv('data.csv')

#Calculating BMI
df['BMI'] = round(df['WeightKg']/((df['HeightCm']/100)*(df['HeightCm']/100)), 2)

#Calculating BMI_Category and Health_Risk
bmi_category = []
health_risk = []
for x in df.iloc:
	if x.BMI <= 18.4:
		bmi_category.append('Underweight')
		health_risk.append('Mainutrition Risk')
	elif x.BMI >= 18.5 and x.BMI <= 24.9:
		bmi_category.append('Normal Weight')
		health_risk.append('Low Risk')
	elif x.BMI >= 25 and x.BMI <= 29.9:
		bmi_category.append('Overweight')
		health_risk.append('Enhanced Risk')
	elif x.BMI >= 30 and x.BMI <= 34.9:
		bmi_category.append('Moderately Obese')
		health_risk.append('Medium Risk')
	elif x.BMI >= 35 and x.BMI <= 39.9:
		bmi_category.append('Severely Obese')
		health_risk.append('High Risk')
	elif x.BMI >= 40:
		bmi_category.append('Very Severely Obese')
		health_risk.append('Very High Risk')
df['BMI_Category'] = bmi_category 
df['Health_Risk'] = health_risk
print(df)