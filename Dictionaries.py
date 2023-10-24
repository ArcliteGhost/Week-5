#Temperature display using dictionaries
#By Casey Eads

daily_temps = {'sun':68.8, 'mon':71, 'tue':67, 'wed':71.8, 'thur':73.4, 'fri':75.5, 'sat':75.5}
dayname = {'sun':'sunday', 'mon':'monday', 'tue':'tuesday', 'wed':'wednesday', 'thur':'thursday', 'fri':'friday', 'sat':'saturday'}
day = input("enter 'sun','mon','tue','wed','thur','fri' or 'sat': ")

print("The temp for", dayname[day], "was", daily_temps[day], "degrees")