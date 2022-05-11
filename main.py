#Import
from math import *
import re
from os import system


#Store answer
ans = 0

#Set window title
system("title " + "Python Eval Calculator")

#Commandline Colors
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

while True:
    #Ask for input
    expression = input(f"{bcolors.BOLD}Enter an expression: {bcolors.ENDC}")

    #Convert input to lowercase
    expression = expression.lower()

    #Replace characters
    expression = expression.replace(',', '.')
    expression = expression.replace('^', '**')
    expression = expression.replace('√', 'sqrt')
    expression = expression.replace('π', 'pi')
    expression = expression.replace('log', 'log10')
    expression = expression.replace('ln', 'log')
    expression = expression.replace('×', '*')
    expression = expression.replace('⋅', '*')
    expression = expression.replace('÷', '/')
    expression = expression.replace('−', '-')
    expression = expression.replace('≥', '>=')
    expression = expression.replace('≤', '<=')
    expression = expression.replace('≠', '!=')
    expression = expression.replace('mod', '%')

    #Convert functions to python.math friendly
    expression = re.sub('cos\((.*?)\)', r'cos(radians(\1))', expression)
    expression = re.sub('sin\((.*?)\)', r'sin(radians(\1))', expression)
    expression = re.sub('tan\((.*?)\)', r'tan(radians(\1))', expression)

    expression = re.sub('cos-1\((.*?)\)', r'degrees(acos(\1))', expression)
    expression = re.sub('sin-1\((.*?)\)', r'degrees(asin(\1))', expression)
    expression = re.sub('tan-1\((.*?)\)', r'degrees(atan(\1))', expression)

    expression = re.sub('(.*?)!', r'factorial(\1)', expression)

    #Clear
    if expression == 'cls':
        ans = 0
        continue

    #Print help
    if expression == 'help':
        print(f"{bcolors.BOLD}-- AVAILABLE FUNCTIONS --{bcolors.ENDC}\n\nFactorial (!) - Usage {bcolors.BOLD}x!{bcolors.ENDC}\nExponent (^ or **) - Usage {bcolors.BOLD}a^b{bcolors.ENDC}\nSquare root (√ or sqrt) - Usage {bcolors.BOLD}√(x){bcolors.ENDC}\n" +
        f"Log (log) - Usage {bcolors.BOLD}log(x){bcolors.ENDC}\nLn (ln) - Usage {bcolors.BOLD}log(x){bcolors.ENDC}\n" + 
        f"Sine (sin) - Usage {bcolors.BOLD}sin(x){bcolors.ENDC}\nCosine (cos) - Usage {bcolors.BOLD}cos(x){bcolors.ENDC}\nTangent (tan) - Usage {bcolors.BOLD}tan(x){bcolors.ENDC}\n" + 
        f"Arc sine (asin) - Usage {bcolors.BOLD}asin(x){bcolors.ENDC}\nArc cosine (acos) - Usage {bcolors.BOLD}acos(x){bcolors.ENDC}\nArc tangent (atan) - Usage {bcolors.BOLD}atan(x){bcolors.ENDC}\n" +
        f"Degrees (degrees) - Usage {bcolors.BOLD}degrees(x radians){bcolors.ENDC}\nRadians (radians) - Usage {bcolors.BOLD}radians(x degrees){bcolors.ENDC}\n" +
        f"Inverse sine (sin-1) - Usage {bcolors.BOLD}sin-1(x){bcolors.ENDC}\nInverse cosine (cos-1) - Usage {bcolors.BOLD}cos-1(x){bcolors.ENDC}\nInverse tangent (tan-1) - Usage {bcolors.BOLD}tan-1(x){bcolors.ENDC}\n" +
        
        f"\n{bcolors.BOLD}-- AVAILABLE OPERATORS --{bcolors.ENDC}\n\nAddition (+)\nSubtraction (-)\nGreater than (>)\nLess than (<)\nGreater than or equal to (≥ or >=)\nLess than or equal to (≤ or <=)\nParanthases (( ))\n" +
        f"Addition (* or × or ⋅)\nDivision (÷ or /)\nModulo (mod or %)\nDecimal point (. or ,)\n" + 
        f"\n{bcolors.BOLD}-- AVAILABLE VARIABLES --{bcolors.ENDC}\n\nAns - The answer of the last equation\n" + 
        f"\n{bcolors.BOLD}-- AVAILABLE CONSTANTS --{bcolors.ENDC}\n\nPi (π or pi)\nEuler's number (e)\n" +
        f"\n{bcolors.BOLD}----\n\nClear (cls){bcolors.ENDC}\n")
        continue
    
    #Check if expression is valid
    try:
        #Evaluate expression
        ans = eval(expression)
        print(f"{bcolors.OKGREEN}{ans}{bcolors.ENDC}")
        
    #Handle errors
    except ValueError:
        print(f"{bcolors.FAIL}Math Error{bcolors.ENDC}")
    except:
        print(f"{bcolors.FAIL}Syntax Error{bcolors.ENDC}")