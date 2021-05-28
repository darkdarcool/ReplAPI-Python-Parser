from classes.__init__ import getKarma
from classes.__init__ import getRaw
from gets.karma import getKarmaCount
compare = getKarmaCount("RayhanADev") # this is a private function and will not be shared with pip
class Parser:
  def __init__(self, request):
    self.data = request 
  def cycles(self):
    return getKarma(self.data)
  def raw(self):
    return getRaw(self.data)

e = Parser(compare)
newthing = e.raw()
newerthing = Parser(newthing)
print(newerthing.cycles())