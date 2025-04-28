"""
Determines the characteristics of a package based on its dimensions and mass.
A package is considered bulky if:
- Its volume (width * height * length) is greater than or equal to 1,000,000 cm³, or
- Any one of its dimensions (width, height, or length) is greater than or equal to 150 cm.
Parameters:
width (float): The width of the package in centimeters.
height (float): The height of the package in centimeters.
length (float): The length of the package in centimeters.
mass (float): The mass of the package in kilograms.
Returns:
stack (string) : The stack where the package is going, SPECIAL, STANDARD or REJECTED.
"""
def sort(width, height, length, mass):
    if width <= 0 or height <= 0 or length <= 0 or mass <= 0:
        raise ValueError("All dimensions and mass must be greater than zero.")
    if type(width) is str or type(height) is str or type(length) is str or type(mass) is str:
        raise TypeError("All values must be numeric")

    isBulky = False
    isHeavy = False
    if width >= 150 or height >= 150 or length >= 150:
        isBulky = True
    elif width*height*length >= 1000000:
        isBulky = True
    
    if mass >= 20:
        isHeavy = True
    
    if isHeavy and isBulky:
        return "REJECTED"
    elif isHeavy or isBulky:
        return "SPECIAL"
    else:
        return "STANDARD"


def convertUnit(value, unit):
    return float(value) * unitSwitch[unit]

if __name__ == "__main__":
    # Considering the input comes in numbers in the right unit (omitted)
    package = [120,30,50,10]
    print(sort(package[0],package[1],package[2],package[3])) 
    package = [150,30,50,1]
    print(sort(package[0],package[1],package[2],package[3])) 
    package = [120,120,120,10]
    print(sort(package[0],package[1],package[2],package[3])) 
    package = [150,36,10,20]
    print(sort(package[0],package[1],package[2],package[3])) 
    #package = [0,30,50,20]
    #print(sort(package[0],package[1],package[2],package[3])) 
    package = [100000,100000,100000,10000]
    print(sort(package[0],package[1],package[2],package[3])) 
    package = ['a',12,33,1]
    print(sort(package[0],package[1],package[2],package[3])) 


    # if input comes with any measurement unit 
    # considering there is a space between the number and unit, if not
    # just switch to regex split instead of string split
    unitSwitch = {
        "m":100.0,
        "g": 0.001,
        "cm": 1,
        "kg": 1
    }
    package = ["0.2 m", "120 cm", "0.1 m", "3000 g"]
    for i in range(0,len(package)):
        split = package[i].split(" ")
        package[i] = convertUnit(split[0], split[1])
    print(package)
    print(sort(package[0],package[1],package[2],package[3]))   # Rejected
    