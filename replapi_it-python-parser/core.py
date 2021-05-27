from classes.__init__ import getKarma
from gets.karma import getKarmaCount
compare = getKarmaCount("RayhanADev") # this is a private function and will not be shared with pip
class Parser:
  def __init__(self, request):
    self.data = request 
  def cycles(self):
    return getKarma(self.data)

e = Parser(compare) 
print(e.cycles())