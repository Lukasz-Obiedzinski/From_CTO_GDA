__author__='dev'

age=24
print("Moj wiek to " +str(age)+" lat")

print("Moj wiek to {0} lat".format(age)) 

print("Tu jest {0} dni w {1}, {2}, {3}, {4}, {5}, {6} and {7} ".format(31,
    "Styczen", "Luty", "Marzec", "Kwiecien", "Maj", "Czerwiec", "Lipiec"))

print("Moj wiek to %d years" % age)
print("Moj wiek to %d %s, %d %s" %(age, "lat", 6, "miesiecy"))

for i in range(1,12):
    print("No, {0:2}  squared is {1:4} and cubed is {2:4}".format(i, i**2, i**3))

print("Pi is approximately %12.50f" %(22/7))

for i in range(1,12):
    print("No, {0:<2}  squared is {1:<4} and cubed is {2:>4}".format(i, i**2, i**3))


print("Pi is approximately {0:12.50}".format(22/7))

