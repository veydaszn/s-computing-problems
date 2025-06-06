# a) Plotting a line graph of temperature readings over a week
import matplotlib.pyplot as plt

temperatures = [20, 22, 19, 23, 21, 24, 20]
days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

plt.plot(days, temperatures, marker='o', linestyle='-', color='blue')
plt.title('Weekly Temperature Readings')
plt.xlabel('Day of the Week')
plt.ylabel('Temperature (°C)')
plt.grid(True)
plt.show()
