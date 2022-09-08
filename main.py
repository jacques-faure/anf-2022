print("Ceci est un test")
def MaFonction():
  print("Ceci est une fonction")
MaFonction()

import os
import sys

FileName = sys.argv[1]

f = open(FileName, 'r')
print(FileName)
