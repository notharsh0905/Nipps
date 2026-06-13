#Write a program that will determine weather when the value of 
#temperature and humidity is provided by the user.
#TEMPERATURE(C)                          HUMIDITY(%)         WEATHER

#      >= 30                             >=90                Hot and Humid
#      >= 30                             < 90                Hot
#      < 30                              >= 90               Cool and Humid
#      < 30                              < 90                Cool
tem=float(input("Enter the temperature: "))
hum=float(input("Enter the humidity: "))
if tem>=30 and hum>=90:
    print("Weather is Hot and Humid.")
elif tem>=30 and hum<=90:
    print("Weather is Hot.")
elif tem<30 and hum>=90:
    print("Weather is Cool and Humid.")
elif tem<30 and hum<90:
    print("Weather is Cool.")