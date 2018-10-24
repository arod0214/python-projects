# Write a complete class that keeps tracks of information about train lines. Your class, TrainLine should contain instance variables for the name, length, dailyRidership andcoverageArea, and should have:

# a constructor method,
# a method, getLength(), that returns the train length a method, and
# a method, riderDensity() that calculates rider density ("dailyRidership/coverageArea")
# Outside of your class, write a function that takes as input a list of TrainLines, called subway, and returns the sum of the length of the train lines in the list. The function signature should be:

#		def overallLength(subway):
	
# Include a main() in your file that demostrates that your class and function work.



class train:

    def __init__(self,initName,initLength,initDailyRides,initCoverageArea):
        self.name=initName
        self.length=initLength
        self.dailyRidership=initDailyRides
        self.coverageArea=initCoverageArea

    def getLength(self):
        return self.length

    def riderDensity(self):
        return self.dailyRidership/self.coverageArea

    def overallLength(subway):
        length = 0
        for i in len(subway):
            length = length + subway[i].getLength
        return length

    def main():
        TrainLines = input("Enter a list of Train Lines separated by commas:")
        subway = TrainLines.split(",")
        print("The sum of the length of the train lines is",str(overallLength(subway))+".")
        

    main()
