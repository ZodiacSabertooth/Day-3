class Boat:

  isAnchorDropped=False

  currentSpeed=0

  currentfuel=100

  def __init__(self, engineSizeInput, colorInput, patterInput, frametypeinput, sizeinput, boatName):
    self.engine=engineSizeInput
    self.color=colorInput
    self.pattern=patterInput
    self.frame=frametypeinput
    self.size=sizeinput
    self.name=boatName

  def refuel(self):
    while self.currentFuel < 100:
      self.currentFuel += 1
      print("Your fuel level is "+str(self.currentFuel))

  def speedUp(self,speedChange):
    self.currentSpeed += speedChange
    if self.currentfuel - speedChange/2 <= 0:
      print("WARNING - FUEL TANK IS EMPTY")
    self.currentfuel -= speedChange/2
    print("Your speed is "+str(self.currentSpeed))
    print("Your fuel level is: "+str(self.currentfuel))

  def slowdown(self,speedChange):
    self.currentSpeed -= speedChange
    print("Your speed is "+str(self.currentSpeed))

  def anchorDrop(self):
    if self.isAnchorDropped==False:
      self.isAnchorDropped==True
      print("Drop Anchor")
    else:
     print("Anchor Already Dropped")

print("welcome to Anderson Boat Customizer")
print("what size engine do you want?")
userEngineInput=input()
print("what color boat do you want?")
userColorInput=input()
print("what type of patter do you want on your boat?")
userPatterInput=input()
print("what type of frame do you want?")
userFrameTypeinput=input()
print("what size boat do you want?")
userSizeinput=input()\

print("what will you name your boat?")
userBoatNameInput=input()

AndersonBoat=Boat(userBoatNameInput, userColorInput, userEngineInput, userFrameTypeinput, userPatterInput, userSizeinput)

AndersonBoat.speedUp(10)
AndersonBoat.speedUp(190)
AndersonBoat.anchorDrop()
AndersonBoat.refuel()

print(AndersonBoat.engine)
print(AndersonBoat.color)
print(AndersonBoat.pattern)
print(AndersonBoat.frame)
print(AndersonBoat.size)
print(AndersonBoat.name)