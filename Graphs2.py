import matplotlib.pyplot as plt
import numpy as np


#Histogram

ages = [4, 12, 3, 7, 15, 17, 20, 8, 6]
groups = [0, 5, 10, 15, 20, 25]

plt.hist(ages, groups)

plt.show()

#Scatter plot

x = [1, 3, 5, 7, 9]
y = [2, 4, 6, 7, 8]

plt.scatter(x, y, color = "blue")

plt.show()

#Pie chart

plt.title("What is produced and how much in Apple")

product = ["iphone", "ipad", "macbook", "ipod", "airpods"]
amount = [50, 30, 36, 23, 33]

plt.pie(amount, labels = product)

plt.show()

#Stack plot

plt.title("What is produced and how much in Samsung")

product = ["Phones(S series)", "Phones(A series)", "Laptop", "Watch", "Keyboard"]
amountS = [60, 57, 68, 70, 85]
amountA = [48, 56, 68, 57, 60]
amountL = [50, 73, 86, 63, 65]
amountW = [36, 34, 23, 46, 45]
amountK = [30, 45, 43, 31, 38]

plt.stackplot(product, amountS, amountA, amountL, amountW, amountK)
plt.plot([], [], label = "Series S", color = "blue")
plt.plot([], [], label = "Series A", color = "orange")
plt.plot([], [], label = "Laptop", color = "green")
plt.plot([], [], label = "Watch", color = "red")
plt.plot([], [], label = "Keyboard", color = "purple")
plt.legend()

plt.show()






