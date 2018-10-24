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
