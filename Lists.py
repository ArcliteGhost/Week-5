#Temperature display using lists
#By Casey Eads

daily_temps = [68.8, 71, 67, 71.8, 73.4, 75.5, 75]

day = input("enter 'sun','mon','tue','wed','thur','fri' or 'sat': ")

if day == 'sun' :
  dayname = 'sunday'
  temp = daily_temps[0]

elif day == 'mon' :
  dayname = 'monday'
  temp = daily_temps[1]

elif day == 'tue' :
  dayname = 'tuesday'
  temp = daily_temps[2]

elif day == 'wed' :
  dayname = 'wednesday'
  temp = daily_temps[3]

elif day == 'thur' :
  dayname = 'thursday'
  temp = daily_temps[4]

elif day == 'fri' :
  dayname = 'friday'
  temp = daily_temps[5]

elif day == 'sat' :
  dayname = 'saturday'
  temp = daily_temps[6]

else:
  print("wrong input")
print("the temperature for: ", dayname, "was", temp, "degrees")