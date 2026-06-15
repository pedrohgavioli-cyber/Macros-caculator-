def tbm(sex, age:int, weight:float, height:float):
    imc = weight / (height/100)**2
    if sex == 'm' and imc < 25:
        result = 204 - (4*age) + (weight * 11.69) + (height * 450.5)
        return result
    elif sex == 'm' and imc >= 25:
        result = 293 - (3.8*age) + (weight * 10.12) + (height * 456.4)
        return result
    elif sex == 'f' and imc < 25:
        result = 255 - (2.35*age) + (weight * 9.39) + (height * 361.6)
        return result 
    else:
        result = 247 - (2.67*age) + (weight * 8.6) + (height * 401.5)
        return result


'''
1 = 1.2 * tbm sedentary (non or little exercise)
2 = 1.375 * tbm slightly active (exercise 1-3 days/week)
3 = 1.55 * tbm moderately active (exercise 3-5 days/week)
4 = 1.725 * tbm active (exercise 6-7 days/week)
5 = 1.9 * tbm super active (very hard exercise & physical job or 2x training)
'''

def get(tbm, activity_level):
    if activity_level == 1:
        result = 1.2 * tbm
        return result
    elif activity_level == 2:
        result = 1.375 * tbm
        return result
    elif activity_level == 3:
        result = 1.55 * tbm
        return result
    elif activity_level == 4:
        result = 1.725 * tbm
        return result
    else:
        result = 1.9 * tbm
        return result