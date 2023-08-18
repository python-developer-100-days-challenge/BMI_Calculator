#!/usr/bin/env python
# coding: utf-8

# In[1]:


#BMI UK Calculator(UK)
# BMI =  weight (kg) / [height (m)]2
# This script calculates your Body Mass Index (BMI) based on your height and weight.

# Input height and weight from the user
height = float(input("Enter your height in meters: "))
weight = float(input("Enter your weight in kg: "))

# Calculate BMI using the formula: weight / (height^2)
x = float(height ** 2)
y = float(weight)
bmi = y / x

# Round the calculated BMI to the nearest integer
bmi_r = round(bmi)

# Print both the exact and rounded BMI
print("Exact BMI:", bmi)
print("Rounded BMI:", bmi_r)

# Categorize BMI and provide corresponding health information
if bmi > 35:
    print(f"Your BMI is {bmi_r}. You are Clinically Obese.")
elif bmi > 30:
    print(f"Your BMI is {bmi_r}. You are Obese.")
elif bmi > 25:
    print(f"Your BMI is {bmi_r}. You are Slightly Overweight.")
elif bmi > 18.5:
    print(f"Your BMI is {bmi_r}. You are Normal.")
else:
    print(f"Your BMI is {bmi_r}. You are Underweight.")


# In[ ]:




