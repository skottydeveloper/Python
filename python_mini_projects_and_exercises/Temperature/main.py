import sys
from temperature import temperature

temps = temperature(sys.argv[1])

# Begin here!
print("Monday" + " " + "was " + str(temps.getTemp(0)))
print("Tuesday" + " " + "was " + str(temps.getTemp(1)))
print("Wednesday" + " " + "was " + str(temps.getTemp(2)))
print("Thursday" + " " + "was " + str(temps.getTemp(3)))
print("Friday" + " " + "was " + str(temps.getTemp(4)))
print("Saturday" + " " + "was " + str(temps.getTemp(5)))
print("Sunday" + " " + "was " + str(temps.getTemp(6)))
print("The maximum was: " + str(temps.high()))
print("The minimum was: " + str(temps.low()))
print("The average was: " + str(temps.average()))