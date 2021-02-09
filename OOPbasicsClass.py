class Car:
    def SetOwner(self, Name):
        self.Name = Name
    def GetOwner(self):
        print("Owner is ", self.Name)




def main():
    myCar = Car()
    myCar.SetOwner("Youssef Noam")
    myCar.GetOwner()
    yoCar = Car()
    yoCar.SetOwner("ynoam")
    yoCar.GetOwner()

if __name__ == "__main__":
    main()