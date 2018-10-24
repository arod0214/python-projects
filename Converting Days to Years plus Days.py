# Write a program that asks the user for a time in days and prints out the equivalent number of years and (leftover) days.

# Assume that a year has 365 days and use "years" and "days" in the last lineeven when grammatically incorrect.


days = int(input("Enter the number of days:"))
y = 365
years = days // y
remainingDays = days % y
print("That is", years, "year(s) and", remainingDays, "days.")
        
