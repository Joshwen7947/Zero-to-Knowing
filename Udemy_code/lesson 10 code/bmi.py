def calc_bmi(weight, height):
    calculation = weight / (height *height)
    return calculation

def results(weight, height):
    calculate = calc_bmi(weight, height)
    if calculate <= 18.5:
        print("Under weight!")
    elif calculate > 18.5 and calculate <= 25:
        print("Normal weight")
    else:
        print("Overweight")
        