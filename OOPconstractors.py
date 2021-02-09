class Car:
    def __init__(self, **kwargs):
        self.Data = kwargs
    def GetOwner(self):
        print("Owner is ", self.Data["Name"])
        print("Model ", self.Data["Model"])
        print("Year ", self.Data["Year"])
    def SetModel(self, Model):
        self.Data["Model"] = Model
    def GetModel(self):
        print("Model ", self.Data["Model"])




def main():
    myCar = Car(Name="Youssef", Model="x1", Year=2021)
    myCar.GetOwner()
    yoCar = Car(Name="ynoam", Model="x1", Year=2021)
    yoCar.GetOwner()
    yoCar.SetModel("2030")
    yoCar.GetModel()

main()