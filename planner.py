import csv
import random
menu = []
with open('Menu.csv', 'rb') as csvfile:
    menureader = csv.reader(csvfile, delimiter=',')
    for items in menureader:
        menu.append(items)
        

labelnames = menu.pop(0)
minamounts = menu.pop(0)
maxamounts = menu.pop(0)

    
def mealer(menu, calcountgoal):
    meal = []
    calcount = 0
    while calcount <= int(calcountgoal):
        mealadd = random.choice(menu)
        #print mealadd
        cals = int(mealadd[2])
        calcount += cals
        meal.append(mealadd)
    return mealeradv(meal)
    #return  meal, calcount

def mealeradv(meals):
    cost = 0 #1
    calories = 0 #2
    fat = 0 #3
    carb = 0 #4
    protien = 0 #5
    fiber = 0 #6
    mealsize = 0 #7
    for meal in meals:
        cost += float(meal[1])
        calories += float(meal[2])
        fat += float(meal[3])
        carb += float(meal[4])
        protien += float(meal[5])
        fiber += float(meal[6])
        mealsize += float(meal[7])
    return meals, cost, calories, fat, carb, protien, fiber, mealsize
    

def mealerminmax(menu, minamounts, maxamounts):
    itercount = 0
    while True:
        itercount += 1
        mealplan, cost, calories, fat, carb, protien, fiber, mealsize = mealer(menu, minamounts[2])
        if cost < int(minamounts[1]):
            print 'fail1'
            continue
        if cost > int(maxamounts[1]):
            print 'fail1b'
            continue
        if calories < int(minamounts[2]):
            continue
        if calories > int(maxamounts[2]):
            continue
        if fat < int(minamounts[3]):
            continue
        if fat > int(maxamounts[3]):
            continue
        if carb < int(minamounts[4]):
            continue
        if carb > int(maxamounts[4]):
            continue
        if protien < int(minamounts[5]):
            continue
        if protien > int(maxamounts[5]):
            continue
        if fiber < int(minamounts[6]):
            continue
        if fiber > int(maxamounts[6]):
            continue
        if mealsize < int(minamounts[7]):
            continue
        if mealsize > int(maxamounts[7]):
            continue
        return mealplan, cost, calories, fat, carb, protien, fiber, mealsize, itercount

mealplan, cost, calories, fat, carb, protien, fiber, mealsize, itercount =mealerminmax(menu, minamounts, maxamounts)
print
print
print
for items in mealplan:
    print items[0]
print
print "Cost: ", cost
print "Calroies: ", calories
print "Fat: ", fat
print "Carbs: ", carb
print "Protiens: ", protien
print "Fiber: ", fiber
print "MealSizeCount: ", mealsize
print "Attempts to get here: ", itercount
    

