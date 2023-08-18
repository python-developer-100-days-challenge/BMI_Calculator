#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# BMI US Calculator
# BMI =  weight (lb) / [height (in)]2 x 703
height = float(input("enter your height in inches: "))
weight = float(input("enter your weight in lb: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
h = float(height **2)
w = float(weight)
bmi = 703 * (w / h)
bmi_r = round(bmi)
#bmi_r2 = round(bmi,2)
print(bmi)
print(bmi_r)

if bmi > 35:
    print(f"Your bmi is {bmi_r} you are Clinically Obese.")
elif bmi > 30:
    print(f"Your bmi is {bmi_r} You are obess")
elif bmi > 25:
    print(f"Your bmi is {bmi_r} You are slightly overweight")
elif bmi > 18.5:
    print(f"Your bmi is {bmi_r} You are normal")
elif bmi < 18.5:
    print(f"Your bmi is {bmi_r} You are underweight")

