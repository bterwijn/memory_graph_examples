import math

mainterminal = input("What do you want to calculate? \n (a)rithmetic \n (s)quare/cubic feet \n (g)eneral conversion \n (cir)ircumference \n (ar)ea \n (f)unction \n").lower()

#aritmetic
if mainterminal == "a":
    answer = (input("(a)ddition, (s)ubtraction, (m)ultiply, (d)ivision, or (e)xponentiation? "))
    firstnum = float(input("What is your first number? "))
    secondnum = float(input("What is your second number? "))

    if answer == "a":
        print(firstnum + secondnum)

    elif answer == "s":
        print(firstnum - secondnum)

    elif answer == "m":
        print(firstnum * secondnum)

    elif answer == "d":
        if firstnum == 0 or secondnum == 0:
            print("error, please input a different number.")    
        else:
            print(firstnum / secondnum)

    elif answer == "e":
        print(firstnum ** secondnum)

    else:
            print("Invalid operator")
        

#sqft/cuft
elif mainterminal == "s":
    terminalsqft = input("What dimensions do you want to use? \n (c)ubic feet \n (s)quare feet \n ").lower()
    
    if terminalsqft == "s":
        lengtha = float(input("length?: "))
        widtha = float(input("width?: "))

        x = lengtha*widtha

        print(f"that is {x} SQFT")
    
    elif terminalsqft == "c": 
        lengthb = float(input("length: "))
        widthb = float(input("width: "))
        heightb = float(input("height: ")) 

        y = lengthb*widthb*heightb

        print(f"{y} cubic feet.")

    else:
        print("Invalid operator")

#general converstion     
elif mainterminal == "g":
    terminalconvert = input("What do you want to convert? \n (l)ength \n (t)emperature \n").lower() 
    
    if terminalconvert == "length" or terminalconvert == "l":   
        convert = input("What do you want to convert? \n (m)eters to xxxxmeters \n (f)eet to miles/yards \n")
        
        if convert == "m":
            unitsmetr = {
                "mm": ["millim", "millimeter", "millimeters"],
                "cm": ["centim", "centimeter", "centimeters"],
                "dm": ["decim", "decimeter", "decimeters"],
                "m":  ["meter", "meters"],
                "dam": ["decam", "decameter", "decameters"],
                "hm": ["hexam", "hectometer", "hectometers"],
                "km": ["kilom", "kilometer", "kilometers"]
            }

            valuesmetr = {
                "mm": 0.001,
                "cm": 0.01,
                "dm": 0.1,
                "m": 1,
                "dam": 10,
                "hm": 100,
                "km": 1000
            }

            unitmetr = input("What unit is it? ").lower()
            unitmetr1 = input("What unit do you want to convert to? ").lower()
            amountmetr = float(input(f"How many {unitmetr} do you have? "))

            resultmetr = amountmetr * valuesmetr[unitmetr] / valuesmetr[unitmetr1]

            print(f"That is {resultmetr}{unitmetr1}.")

        elif convert == "f":
            unitsft = {
                "yards": ["yard", "yd"],
                "miles": ["miles", "mi"]
            }

            unitft = float(input("How many feet do you have?")).lower()
            resultft = input("What do you want to convert it to? \n miles \n yards").lower()

            if resultft == "yards" or resultft == "yard" or resultft == "yd":
                print(unitft / 3)

            elif resultft == "miles" or resultft == "mile" or resultft == "mi":
                print (unitft / 5280)

        else:
            print("Invalid operator")

    elif terminalconvert == "temperature" or terminalconvert == "t":
        temp = input("What is your starting value? \n Celsius \n Fahrenheit \n Kelvin \n").lower()

        if temp == "celsius" or temp == "c":
            tempc = float(input("What is your temperature? \n"))
            convertc = input("What do you want to convert it to? \n Fahrenheit \n Kelvin \n ").lower()

            if convertc == "fahrenheit" or convertc == "f":
                print(f"That is about {(tempc * 1.8) + 32} degree(s) fahrenheit.")

            elif convertc == "kelvin" or convertc == "k":
                print(f"That is about  {tempc + 273.15} degree(s) kelvin.")

        elif temp == "fahrenheit" or temp == "f":
            tempf = float(input("What is your temperature? \n"))
            convertf = input("What do you want to convert it to? \n Celsius \n Kelvin \n").lower()

            if convertf == "celsius" or convertf == "c":
                print(f"That is about {(tempf - 32) / 1.8} degree(s) celsius.")

            elif convertf == "kelvin" or convertf == "k":
                print(f"That is about  {(tempf - 32 ) / 1.8 + 273.15} degree(s) kelvin.")

        elif temp == "kelvin" or temp == "k":
            tempk = float(input("What is your temperature? \n"))
            convertk = input("What do you want to convert it to? \n Celsius \n Fahrenheit \n").lower()

            if convertk == "celsius" or convertk == "c":
                print(f"That is about {tempk - 273.15} degree(s) celsius.")

            elif convertk == "fahrenheit" or convertk == "f":
                print(f"That is about {(tempk - 273.15) * 1.8 + 32} degree(s) fahrenheit")   
        else:
            print("Invalid operator")
#circumference
elif mainterminal == "cir":
    radcir = float(input("What is the radius of this circle? "))

    circum = 2 * math.pi * radcir

    print(f"The circumference is {round(circum, 4)}.")

#area / diameter
elif mainterminal == "ar":
    terminalar = input(f"What do you want to use? \n circle \n rectangle \n triangle \n ").lower()
    
    if terminalar == "circle":
        rada = float(input("radius: "))

        area = rada * rada * math.pi
        dia = rada * 2

        print(f"The area of this circle is {round(area, 4)}, and the diameter is {round(dia, 4)}. ")

    elif terminalar == "rectangle":
        l = float(input("length?: "))
        w = float(input("width?: "))
        a = l*w
        
        print(f"the area of this quadrilateral is {a}. ")

    elif terminalar == "triangle":
        l = float(input("base?: "))
        w = float(input("height?: "))
        a = l*w/2
                
        print(f"the area of this triangle is {a}. ")

    else:
        print("Invalid operator")

 #square root / sine / cosine / tangent      
elif mainterminal == "f":
    terminalrsct = input("What function do you want to do? \n sqrt \n sin \n cos \n tan \n")
    if terminalrsct == "sqrt":
        
        numsqrt = float(input("Give me a number: "))
        anssqrt = math.sqrt(numsqrt)
            
        print(f"The square root of {numsqrt} is {anssqrt}.")

    elif terminalrsct == "sin":

        numsin = float(input("Give me a number: "))
        anssin = math.sin(math.radians(numsin))

        print(f"The sine of {numsin} is {anssin}.")

    elif terminalrsct == "cos":

        numcos = float(input("Give me a number: "))
        anscos = math.cos(math.radians(numcos))

        print(f"The cosine of {numcos} is {anscos}.")

    elif terminalrsct == "tan":

        numtan = float(input("Give me a number: "))
        anstan = math.tan(math.radians(numtan))

        print(f"The tangent of {numtan} is {anstan}.")

    else:
        print("Invalid operator.")

else:
    print("Invalid, please reload and try again.")
