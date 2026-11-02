def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))
    BMI=weight/(height*height)
    result=0
    print("BMI = "+str(BMI))
    if BMI<18.5:
        print("Under Weight")
        result=-1
    elif BMI>=18.5 and BMI<=25.0:
        print("Normal Weight")
        result=0
    else:
        print("Over Weight")
        result=1
    return result
bmi_output=calculate_bmi(weight=57, height=1.73)