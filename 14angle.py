#smallest angle between hour and minutes 
#Given a string s representing time in 24-hour format "HH:MM", 
#compute the smallest angle in degrees between the hour and minute hands of an analog clock.
s = input("Enter time (HH:MM): ")
hours, minutes = map (int, s.split(":"))
minutes_angle= minutes*6
hour_angle= (hours %12)*30 +minutes * 1/2
angle = abs(hour_angle - minutes_angle)
smallest_angle= min(angle, 360 - angle)
print("Smallest angle is:", smallest_angle)

#code padho toh samjh jaoge aur map k use krke split b use kiya h hour angle p dhyaan do