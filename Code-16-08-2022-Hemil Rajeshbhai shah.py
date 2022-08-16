options = [{"Gender": "Male", "HeightCm": 171, "WeightKg": 96 },
{ "Gender": "Male", "HeightCm": 161, "WeightKg": 85 },
{ "Gender": "Male", "HeightCm": 180, "WeightKg": 77 },
{ "Gender": "Female", "HeightCm": 166, "WeightKg": 62},
{"Gender": "Female", "HeightCm": 150, "WeightKg": 70},
{"Gender": "Female", "HeightCm": 167, "WeightKg": 82}]

# Table :1 Took as Dict
table = [{"BMI Category": "Underweight", "BMI Range (kg/m2)": "18.4 and below", "Health risk": "Malnutrition risk"},
{ "BMI Category": "Normal weight", "BMI Range (kg/m2)": "18.5 - 24.9", "Health risk": "Low risk"},
{ "BMI Category": "Overweight", "BMI Range (kg/m2)": "25 - 29.9", "Health risk": "Enhanced risk"},
{ "BMI Category": "Moderately obese", "BMI Range (kg/m2)": "30 - 34.9", "Health risk": "Medium risk"},
{"BMI Category": "Severely obese", "BMI Range (kg/m2)": "5 - 39.9", "Health risk": "High risk"},
{"BMI Category": "Very severely obese", "BMI Range (kg/m2)": "40 and above", "Health risk": "Very high risk"}]

over_Weight = []
for i in options:
    Height_m = i['HeightCm'] / 100
    weigh_kg = i['WeightKg']
    Bmi = weigh_kg / Height_m
    for table_data in table:
        overweight_value = table_data['BMI Range (kg/m2)']
        startpoint = overweight_value.split()[0]
        endpoint = overweight_value.split()[-1]
        if "below" in endpoint:
            if float(startpoint) >= Bmi:
                print(table_data['Health risk'])
                break
        elif "above" in endpoint:
            if float(startpoint) <= Bmi:
                print(table_data['Health risk'])
                break
        else:
            if float(startpoint)<= Bmi <= float(endpoint):
                print(table_data['Health risk'])
                if table_data['BMI Category'] == 'Overweight':
                    over_Weight.append(Bmi)
                    break

over_Weighted_count = len(over_Weight)
print("Total Over Weighted Count :- ",over_Weighted_count)
