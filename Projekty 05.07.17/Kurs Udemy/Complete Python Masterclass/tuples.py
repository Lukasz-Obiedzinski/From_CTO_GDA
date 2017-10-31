
    #--OPEN IN QPYTHON OR ANOTHER EDITOR--#
    #----------INPUTS ON RUNTIME----------#
    # ONLY FOR ANDROID 
    #
    # commands:
    # - go <direction>
    # - attack
    #
    
import re
from random import randint
from math import floor
import time
import sl4a
droid = sl4a.Android()
emptysign = "-"
def shift():
 print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
 print("\n\n\n\n\n\n\n\n\n\n")
 print("\n\n\n\n\n")
def printmap():
 print("{0}{1}{1}{1}{1}{1}{1}{1}{2}{3}{3}{3}{3}{3}{3}{3}{4}{5}{5}{5}{5}{5}{5}{5}{6}{7}{7}{7}{7}{7}{7}{7}{8}{9}{9}{9}{9}{9}{9}{9}{10}".format(ulcorner,a11udash,a11udasha12,a12udash,a12udasha13,a13udash,a13udasha14,a14udash,a14udasha15,a15udash,urcorner))
 print("{0}{6}{6}{6}{6}{6}{6}{6}{1}{7}{7}{7}{7}{7}{7}{7}{2}{8}{8}{8}{8}{8}{8}{8}{3}{9}{9}{9}{9}{9}{9}{9}{4}{10}{10}{10}{10}{10}{10}{10}{5}".format(a11lpipe,a11pipea12,a12pipea13,a13pipea14,a14pipea15,a15rpipe,a11space,a12space,a13space,a14space,a15space))
 print("{0}{6}{6}{6}{11}{6}{6}{6}{1}{7}{7}{7}{12}{7}{7}{7}{2}{8}{8}{8}{13}{8}{8}{8}{3}{9}{9}{9}{14}{9}{9}{9}{4}{10}{10}{10}{15}{10}{10}{10}{5}".format(a11lpipe,a11pipea12,a12pipea13,a13pipea14,a14pipea15,a15rpipe,a11space,a12space,a13space,a14space,a15space,a11playerspot,a12playerspot,a13playerspot,a14playerspot,a15playerspot))
 print("{0}{6}{6}{6}{6}{6}{6}{6}{1}{7}{7}{7}{7}{7}{7}{7}{2}{8}{8}{8}{8}{8}{8}{8}{3}{9}{9}{9}{9}{9}{9}{9}{4}{10}{10}{10}{10}{10}{10}{10}{5}".format(a11lpipe,a11pipea12,a12pipea13,a13pipea14,a14pipea15,a15rpipe,a11space,a12space,a13space,a14space,a15space))
 print("{0}{1}{1}{1}{1}{1}{1}{1}+{2}{2}{2}{2}{2}{2}{2}+{3}{3}{3}{3}{3}{3}{3}+{4}{4}{4}{4}{4}{4}{4}+{5}{5}{5}{5}{5}{5}{5}{6}".format(a11lpipea21,a11dasha21,a12dasha22,a13dasha23,a14dasha24,a15dasha25,a15rpipea25))
 print("{0}{6}{6}{6}{6}{6}{6}{6}{1}{7}{7}{7}{7}{7}{7}{7}{2}{8}{8}{8}{8}{8}{8}{8}{3}{9}{9}{9}{9}{9}{9}{9}{4}{10}{10}{10}{10}{10}{10}{10}{5}".format(a21lpipe,a21pipea22,a22pipea23,a23pipea24,a24pipea25,a25rpipe,a21space,a22space,a23space,a24space,a25space))
 print("{0}{6}{6}{6}{11}{6}{6}{6}{1}{7}{7}{7}{12}{7}{7}{7}{2}{8}{8}{8}{13}{8}{8}{8}{3}{9}{9}{9}{14}{9}{9}{9}{4}{10}{10}{10}{15}{10}{10}{10}{5}".format(a21lpipe,a21pipea22,a22pipea23,a23pipea24,a24pipea25,a25rpipe,a21space,a22space,a23space,a24space,a25space,a21playerspot,a22playerspot,a23playerspot,a24playerspot,a25playerspot))
 print("{0}{6}{6}{6}{6}{6}{6}{6}{1}{7}{7}{7}{7}{7}{7}{7}{2}{8}{8}{8}{8}{8}{8}{8}{3}{9}{9}{9}{9}{9}{9}{9}{4}{10}{10}{10}{10}{10}{10}{10}{5}".format(a21lpipe,a21pipea22,a22pipea23,a23pipea24,a24pipea25,a25rpipe,a21space,a22space,a23space,a24space,a25space))
 print("{0}{1}{1}{1}{1}{1}{1}{1}+{2}{2}{2}{2}{2}{2}{2}+{3}{3}{3}{3}{3}{3}{3}+{4}{4}{4}{4}{4}{4}{4}+{5}{5}{5}{5}{5}{5}{5}{6}".format(a21lpipea31,a21dasha31,a22dasha32,a23dasha33,a24dasha34,a25dasha35,a25rpipea35))
 print("{0}{6}{6}{6}{6}{6}{6}{6}{1}{7}{7}{7}{7}{7}{7}{7}{2}{8}{8}{8}{8}{8}{8}{8}{3}{9}{9}{9}{9}{9}{9}{9}{4}{10}{10}{10}{10}{10}{10}{10}{5}".format(a31lpipe,a31pipea32,a32pipea33,a33pipea34,a34pipea35,a35rpipe,a31space,a32space,a33space,a34space,a35space))
 print("{0}{6}{6}{6}{11}{6}{6}{6}{1}{7}{7}{7}{12}{7}{7}{7}{2}{8}{8}{8}{13}{8}{8}{8}{3}{9}{9}{9}{14}{9}{9}{9}{4}{10}{10}{10}{15}{10}{10}{10}{5}".format(a31lpipe,a31pipea32,a32pipea33,a33pipea34,a34pipea35,a35rpipe,a31space,a32space,a33space,a34space,a35space,a31playerspot,a32playerspot,a33playerspot,a34playerspot,a35playerspot))
 print("{0}{6}{6}{6}{6}{6}{6}{6}{1}{7}{7}{7}{7}{7}{7}{7}{2}{8}{8}{8}{8}{8}{8}{8}{3}{9}{9}{9}{9}{9}{9}{9}{4}{10}{10}{10}{10}{10}{10}{10}{5}".format(a31lpipe,a31pipea32,a32pipea33,a33pipea34,a34pipea35,a35rpipe,a31space,a32space,a33space,a34space,a35space))
 print("{0}{1}{1}{1}{1}{1}{1}{1}+{2}{2}{2}{2}{2}{2}{2}+{3}{3}{3}{3}{3}{3}{3}+{4}{4}{4}{4}{4}{4}{4}+{5}{5}{5}{5}{5}{5}{5}{6}".format(a31lpipea41,a31dasha41,a32dasha42,a33dasha43,a34dasha44,a35dasha45,a35rpipea45))
 print("{0}{6}{6}{6}{6}{6}{6}{6}{1}{7}{7}{7}{7}{7}{7}{7}{2}{8}{8}{8}{8}{8}{8}{8}{3}{9}{9}{9}{9}{9}{9}{9}{4}{10}{10}{10}{10}{10}{10}{10}{5}".format(a41lpipe,a41pipea42,a42pipea43,a43pipea44,a44pipea45,a45rpipe,a41space,a42space,a43space,a44space,a45space))
 print("{0}{6}{6}{6}{11}{6}{6}{6}{1}{7}{7}{7}{12}{7}{7}{7}{2}{8}{8}{8}{13}{8}{8}{8}{3}{9}{9}{9}{14}{9}{9}{9}{4}{10}{10}{10}{15}{10}{10}{10}{5}".format(a41lpipe,a41pipea42,a42pipea43,a43pipea44,a44pipea45,a45rpipe,a41space,a42space,a43space,a44space,a45space,a41playerspot,a42playerspot,a43playerspot,a44playerspot,a45playerspot))
 print("{0}{6}{6}{6}{6}{6}{6}{6}{1}{7}{7}{7}{7}{7}{7}{7}{2}{8}{8}{8}{8}{8}{8}{8}{3}{9}{9}{9}{9}{9}{9}{9}{4}{10}{10}{10}{10}{10}{10}{10}{5}".format(a41lpipe,a41pipea42,a42pipea43,a43pipea44,a44pipea45,a45rpipe,a41space,a42space,a43space,a44space,a45space))
 print("{0}{1}{1}{1}{1}{1}{1}{1}+{2}{2}{2}{2}{2}{2}{2}+{3}{3}{3}{3}{3}{3}{3}+{4}{4}{4}{4}{4}{4}{4}+{5}{5}{5}{5}{5}{5}{5}{6}".format(a41lpipea51,a41dasha51,a42dasha52,a43dasha53,a44dasha54,a45dasha55,a45rpipea55))
 print("{0}{6}{6}{6}{6}{6}{6}{6}{1}{7}{7}{7}{7}{7}{7}{7}{2}{8}{8}{8}{8}{8}{8}{8}{3}{9}{9}{9}{9}{9}{9}{9}{4}{10}{10}{10}{10}{10}{10}{10}{5}".format(a51lpipe,a51pipea52,a52pipea53,a53pipea54,a54pipea55,a55rpipe,a51space,a52space,a53space,a54space,a55space))
 print("{0}{6}{6}{6}{11}{6}{6}{6}{1}{7}{7}{7}{12}{7}{7}{7}{2}{8}{8}{8}{13}{8}{8}{8}{3}{9}{9}{9}{14}{9}{9}{9}{4}{10}{10}{10}{15}{10}{10}{10}{5}".format(a51lpipe,a51pipea52,a52pipea53,a53pipea54,a54pipea55,a55rpipe,a51space,a52space,a53space,a54space,a55space,a51playerspot,a52playerspot,a53playerspot,a54playerspot,a55playerspot))
 print("{0}{6}{6}{6}{6}{6}{6}{6}{1}{7}{7}{7}{7}{7}{7}{7}{2}{8}{8}{8}{8}{8}{8}{8}{3}{9}{9}{9}{9}{9}{9}{9}{4}{10}{10}{10}{10}{10}{10}{10}{5}".format(a51lpipe,a51pipea52,a52pipea53,a53pipea54,a54pipea55,a55rpipe,a51space,a52space,a53space,a54space,a55space))
 print("{0}{1}{1}{1}{1}{1}{1}{1}{2}{3}{3}{3}{3}{3}{3}{3}{4}{5}{5}{5}{5}{5}{5}{5}{6}{7}{7}{7}{7}{7}{7}{7}{8}{9}{9}{9}{9}{9}{9}{9}{10}".format(llcorner,a51ldash,a51ldasha52,a52ldash,a52ldasha53,a53ldash,a53ldasha54,a54ldash,a54ldasha55,a55ldash,lrcorner))
shift()
class Area:
 def __init__(self):
  self.visible = False
  self.enemies = []
  self.number = ""
  self.first = None
  self.second = None
  self.dif = None
class Item:
 location = None
 def examine(self):
  print("It's "+self.desc)
class Weapon(Item):
 def __init__(self, name, dmg, desc):
  self.name = name
  self.dmg = dmg
  self.desc = desc
foamSword = Weapon("Foam Sword", 5, "a toy sword made from foam, almost incapable of dealing damage.")
satanSword = Weapon("Sword of Satan", 666, "a sword that was found in the deepest depths of hell. It's made from an unknown substance, and appears to be self-conscious. Somehow...")
class Creature:
 area = None
 def init(self):
  allCreatures.append(self)
  self.nemezis = []
 def drop(self):
  omit = "this"
 def die(self):
  print("\n{0} died.".format(self.species))
  self.drop()
  self.vit = 0
  for i in allCreatures:
   if self in i.nemezis:
    i.nemezis.remove(self)
 def attack(self,target):
  time.sleep(1)
  miss = randint(1,6)
  if miss == 1:
   print("\n{0} attacked {1}, but he missed!".format(self.species,target.species))
   time.sleep(1)
  else:
   atb = randint(1,6)
   if self.dmg > target.hp:
    damage = target.hp
   else:
    damage = self.dmg
   target.hp -= damage
   print("\n{0} have been attacked by {1}! ({0}: -{2} HP)".format(target.species,self.species,damage))
   droid.vibrate()
   time.sleep(1)
   if atb in range(target.aggro):
    self.hp -= target.dmg
    print("\n{0} got mad and attacked {1} back! ({3}: -{2} HP)".format(target.species,self.species,target.dmg,self.species))
    droid.vibrate()
    time.sleep(1)
   if target.hp <= 0:
    target.die()
    time.sleep(1)
   if self.hp <= 0:
    self.die()
    time.sleep(1)
   if randint(1,4) in range(1,target.aggro+1) and target != player and not target in self.nemezis and target.vit == 1:
    self.nemezis.append(target)
    print("\n{0} will now attack {1} till death.".format(target.species,self.species))
    time.sleep(1)
allCreatures = []
class Player(Creature):
 def __init__(self,s):
  super().init()
  self.hp = 100
  self.aggro = 6
  self.maxhp = self.hp
  self.area = playerArea
  self.disc = []
  self.species = s
  self.wpn = foamSword
  self.dmg = self.wpn.dmg
  self.t = "This string isn't used anywhere ;)"
 def enter(self, dir):
  if dir == "up":
   try:
    exec("self.t = a{0}{1}".format(self.area.first-1,self.area.second))
    if not self.t in self.disc:
     self.disc.append(self.t)
    if self.t.visible == False:
     raise ValueError
    symbol = "^"
    areanow = self.t.name
    areabefore = self.area.name
    self.area = self.t
    return [symbol,areanow,areabefore]
   except:
    return("You can't go further up.")
  elif dir == "down":
   try:
    exec("self.t = a{0}{1}".format(self.area.first+1,self.area.second))
    if not self.t in self.disc:
     self.disc.append(self.t)
    if self.t.visible == False:
     raise ValueError
    symbol = "v"
    areanow = self.t.name
    areabefore = self.area.name
    self.area = self.t
    return [symbol,areanow,areabefore]
   except:
    return("You can't go further down.")
  elif dir == "left":
   try:
    exec("self.t = a{0}{1}".format(self.area.first,self.area.second-1))
    if not self.t in self.disc:
     self.disc.append(self.t)
    if self.t.visible == False:
     raise ValueError
    symbol = "<"
    areanow = self.t.name
    areabefore = self.area.name
    self.area = self.t
    return [symbol,areanow,areabefore]
   except:
    return("You can't go further left.")
  elif dir == "right":
   try:
    exec("self.t = a{0}{1}".format(self.area.first,self.area.second+1))
    if not self.t in self.disc:
     self.disc.append(self.t)
    if self.t.visible == False:
     raise ValueError
    symbol = ">"
    areanow = self.t.name
    areabefore = self.area.name
    self.area = self.t
    return [symbol,areanow,areabefore]
   except:
    return("You can't go further right.")
  else:
   print('There\'s no such direction as "{0}"'.format(dir))
class Rabbit(Creature):
 def __init__(self):
  super().init()
  self.vit = 1
  self.dmg = 666
  self.hp = floor(16.661)
  self.maxhp = self.hp
  if randint(66,6666) == 666:
   self.species = "Rabbit, son of satan"
   emptysign = "6"
   self.aggro = 666
  else:
   self.species = "Rabbit"
   self.aggro = 0
  self.satan = 6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
class Rat(Creature):
 def __init__(self):
  super().init()
  self.vit = 1
  self.dmg = 2
  self.hp = 25
  self.aggro = 1
  self.maxhp = self.hp
  self.species = "Rat"
class Goblin(Creature):
 def __init__(self):
  super().init()
  self.vit = 1
  self.dmg = 5
  self.hp = 100
  self.aggro = 2
  self.maxhp = self.hp
  self.species = "Goblin"
class Orc(Creature):
 def __init__(self):
  super().init()
  self.vit = 1
  self.dmg = 10
  self.hp = 150
  self.aggro = 3
  self.maxhp = self.hp
  self.species = "Orc"
class SupGob(Creature):
 def __init__(self):
  super().init()
  self.vit = 1
  self.dmg = 20
  self.hp = 300
  self.aggro = 4
  self.maxhp = self.hp
  self.species = "Suphram-Goblin"
areas = []
current = []
currentQueue = []
done = []
for a in range(5):
 for b in range(5):
  exec("a{0}{1} = Area()".format(a+1,b+1))
  exec("a{0}{1}.name = 'a{0}{1}'".format(a+1,b+1))
  exec("a{0}{1}.first = {0}".format(a+1,b+1))
  exec("a{0}{1}.second = {1}".format(a+1,b+1))
  exec("areas.append(a{2}{1})".format(a,b+1,a+1))
first = randint(1,7)
if first in range(3,6):
 second = randint(1,2)
 first -= 1
 if second == 2:
  second = 5
else:
 if first == 2:
  first = 1
 elif first == 6 or first == 7:
  first = 5
 second = randint(1,5)
exec("a{0}{1}.visible = True".format(first,second))
exec("playerArea = a{0}{1}".format(first,second))
exec("current.append(a{0}{1})".format(first,second))
difSet = 0
difChange = 1
while True:
 for i in current:
  if i in done:
   continue
  done.append(i)
  i.dif = floor(difSet)
  if i.first > 1:
   exec("first = a{0}{1}".format(i.first-1,i.second))
   if not randint(1,3) == 1:
    if not first in done and not first in current:
     first.visible == True
     currentQueue.append(first)
   else:
    done.append(first)
  if i.first < 5:
   exec("second = a{0}{1}".format(i.first+1,i.second))
   if not randint(1,3) == 1:
    if not second in done and not second in current:
     second.visible = True
     currentQueue.append(second)
   else:
    done.append(second)
  if i.second > 1:
   exec("third = a{0}{1}".format(i.first,i.second-1))
   if not randint(1,3) == 1:
    if not third in done and not third in current:
     third.visible = True
     currentQueue.append(third)
   else:
    done.append(third)
  if i.second < 5:
   exec("fourth = a{0}{1}".format(i.first,i.second+1))
   if not randint(1,3) == 1:
    if not fourth in done and not fourth in current:
     fourth.visible = True
     currentQueue.append(fourth)
   else:
    done.append(fourth)
 if difSet < 4:
  difSet += difChange
 if difSet == 2:
  difChange = 1
 if currentQueue == []:
  break
 current = currentQueue
 currentQueue = []
for i in areas:
 if i.visible == True:
  if i.first > 1:
   exec("first = a{0}{1}".format(i.first-1,i.second))
  else:
   first = Area()
   first.visible = False
  if i.first < 5:
   exec("second = a{0}{1}".format(i.first+1,i.second))
  else: 
   second = Area()
   second.visible = False
  if i.second > 1:
   exec("third = a{0}{1}".format(i.first,i.second-1))
  else:
   third = Area()
   third.visible = False
  if i.second < 5:
   exec("fourth = a{0}{1}".format(i.first,i.second+1))
  else:
   fourth = Area()
   fourth.visible = False
  if first.visible == False and second.visible == False and third.visible == False and fourth.visible == False:
   if first.visible == False:
    first.visible = True
    first.dif = 2
   if second.visible == False:
    second.visible = True
    second.dif = 2
   if third.visible == False:
    third.visible = True
    third.dif = 2
   if fourth.visible == False:    
    fourth.visible = True
    fourth.dif = 2
for i in areas:
 if i.visible and i.dif == None:
  i.visible = False
 elif i.visible != True and i.dif != None:
  i.visible = True
for a in areas:
 fTypeCount = 0
 sTypeCount = 0
 tTypeCount = 0
 fType = "()"
 sType = "()"
 tType = "()"
 if a.dif == 1:
  fType = "Rabbit()"
  sType = "Rat()"
  if randint(1,5) == 5:
   fTypeCount = randint(2,4)
   sTypeCount = 1
  else:
   fTypeCount = randint(2,5)
 elif a.dif == 2:
  fType = "Rat()"
  sType = "Rabbit()"
  tType = "Goblin()"
  if randint(1,100) in range(36):
   if randint(1,100) in range(16):
    fTypeCount = randint(2,3)
    sTypeCount = 1
    tTypeCount = 1
   else:
    fTypeCount = randint(2,3)
    sTypeCount = 1
  else:
   if randint(1,100) in range(16):
    fTypeCount = randint(2,3)
    sTypeCount = 0
    tTypeCount = 1
   else:
    fTypeCount = randint(2,4)
 elif a.dif == 3:
  fType = "Goblin()"
  sType = "Orc()"
  if randint(1,100) in range(36):
   fTypeCount = randint(1,3)
   sTypeCount = randint(2,6)
   if not sTypeCount == 2:
    sTypeCount = 1
  else:
   fTypeCount = randint(1,4)
 elif a.dif == 4:
  fType = "Orc()"
  sType = "SupGob()"
  if randint(1,100) in range(36):
   fTypeCount = randint(1,3)
   sTypeCount = randint(2,6)
   if not sTypeCount == 2:
    sTypeCount = 1
  else:
   fTypeCount = randint(1,4)
 for n in range(1,fTypeCount+1):
  fTypeCut = fType
  fTypeCut = fTypeCut.replace("(","")
  fTypeCut = fTypeCut.replace(")","")
  exec("{0}{1}{2} = {3}".format(a.name,fTypeCut,n,fType))
  exec("{0}.enemies.append({0}{1}{2})".format(a.name,fTypeCut,n))
  exec("{0}{1}{2}.area = {0}".format(a.name,fTypeCut,n))
 for n in range(1,sTypeCount+1):
  sTypeCut = sType
  sTypeCut = sTypeCut.replace("(","")
  sTypeCut = sTypeCut.replace(")","")
  exec("{0}{1}{2} = {3}".format(a.name,sTypeCut,n,sType))
  exec("{0}.enemies.append({0}{1}{2})".format(a.name,sTypeCut,n))
  exec("{0}{1}{2}.area = {0}".format(a.name,sTypeCut,n))
 for n in range(1,tTypeCount+1):
  tTypeCut = tType
  tTypeCut = tTypeCut.replace("(","")
  tTypeCut = tTypeCut.replace(")","")
  exec("{0}{1}{2} = {3}".format(a.name,tTypeCut,n,tType))
  exec("{0}.enemies.append({0}{1}{2})".format(a.name,tTypeCut,n))
  exec("{0}{1}{2}.area = {0}".format(a.name,tTypeCut,n))
for i in areas:
 if i.visible == True and i.enemies == [] and i != playerArea:
  i.visible = False
for i in areas:
  if i.first == 1:
   exec("{0}udash = emptysign".format(i.name))
   exec("a{0}udash{1} = emptysign".format(str(i.first)+str(i.second-1),i.name))
   exec("{0}udasha{1} = emptysign".format(i.name,str(i.first)+str(i.second+1)))
  elif i.first == 5:
   exec("{0}ldash = emptysign".format(i.name))
   exec("a{0}ldash{1} = emptysign".format(str(i.first)+str(i.second-1),i.name))
   exec("{0}ldasha{1} = emptysign".format(i.name,str(i.first)+str(i.second+1)))
  if i.second == 1:
   exec("{0}lpipe = emptysign".format(i.name))
   exec("a{0}lpipe{1} = emptysign".format(str(i.first-1)+str(i.second),i.name))
   exec("{0}lpipea{1} = emptysign".format(i.name,str(i.first+1)+str(i.second)))
  if i.second == 5:
   exec("{0}rpipe = emptysign".format(i.name))
   exec("a{0}rpipe{1} = emptysign".format(str(i.first-1)+str(i.second),i.name))
   exec("{0}rpipea{1} = emptysign".format(i.name,str(i.first+1)+str(i.second)))
  exec("{0}pipea{1} = emptysign".format(i.name,str(i.first)+str(i.second+1)))
  exec("a{1}pipe{0} = emptysign".format(i.name,str(i.first)+str(i.second-1)))
  exec("{0}dasha{1} = emptysign".format(i.name,str(i.first+1)+str(i.second)))
  exec("a{0}dash{1} = emptysign".format(str(i.first-1)+str(i.second),i.name))
  exec("{0}space = emptysign".format(i.name))
  exec("{0}playerspot = emptysign".format(i.name))
ulcorner,urcorner,llcorner,lrcorner = emptysign,emptysign,emptysign,emptysign
for i in areas:
 if i.visible == True:
  if i.first == 1:
   exec("{0}udash = '-'".format(i.name))
   exec("a{0}udash{1} = '-'".format(str(i.first)+str(i.second-1),i.name))
   exec("{0}udasha{1} = '-'".format(i.name,str(i.first)+str(i.second+1)))
  elif i.first == 5:
   exec("{0}ldash = '-'".format(i.name))
   exec("a{0}ldash{1} = '-'".format(str(i.first)+str(i.second-1),i.name))
   exec("{0}ldasha{1} = '-'".format(i.name,str(i.first)+str(i.second+1)))
  if i.second == 1:
   exec("{0}lpipe = '|'".format(i.name))
   exec("a{0}lpipe{1} = '|'".format(str(i.first-1)+str(i.second),i.name))
   exec("{0}lpipea{1} = '|'".format(i.name,str(i.first+1)+str(i.second)))
  if i.second == 5:
   exec("{0}rpipe = '|'".format(i.name))
   exec("a{0}rpipe{1} = '|'".format(str(i.first-1)+str(i.second),i.name))
   exec("{0}rpipea{1} = '|'".format(i.name,str(i.first+1)+str(i.second)))
  exec("{0}pipea{1} = '|'".format(i.name,str(i.first)+str(i.second+1)))
  exec("a{1}pipe{0} = '|'".format(i.name,str(i.first)+str(i.second-1)))
  exec("{0}dasha{1} = '-'".format(i.name,str(i.first+1)+str(i.second)))
  exec("a{0}dash{1} = '-'".format(str(i.first-1)+str(i.second),i.name))
  exec("{0}space = ' '".format(i.name))
  exec("{0}playerspot = '?'".format(i.name))
if a11.visible == True:
 ulcorner = ","
if a15.visible == True:
 urcorner = ","
if a51.visible == True:
 llcorner = "'"
if a55.visible == True:
 lrcorner = "'"
username = None
while username == None:
 username = droid.dialogGetInput("This is a tale of...?").result
exec("player = Player({0})".format('"'+username+'"'))
exec("{}playerspot = '×'".format(player.area.name))
allEnemies = []
for i in allCreatures:
 allEnemies.append(i)
allEnemies.remove(player)
shift()
printmap()
if len(player.species) > 12:
 uslen = "\n"
else:
 uslen = ""
while True:
 usin = input("\n{0} | Current item\n{1} {4}HP: {2}/{3} >> ".format(player.wpn.name,player.species,player.hp,player.maxhp,uslen))
 shift()
 printmap()
 for c in allCreatures:
  for n in c.nemezis:
   if c.area == player.area:
    if n.area == player.area:
     n.attack(c)
   else:
    print("You hear a silent rumour, like {0} attacking {1} far away.".format(n.species,c.species))
    c.hp -= n.dmg
    if c.hp <= 0:
     c.vit = 0
     print("It seems like he died.")
 if re.match("go",usin):
  usinB = re.findall(r"[a-zA-Z]+\b",usin)
  try:
   playerEnterList = player.enter(usinB[1])
   if playerEnterList[1] == "omit this":
    omit = "this"
   exec("{0}playerspot = ' '".format(playerEnterList[2]))
   exec("{0}playerspot = '{1}'".format(playerEnterList[1],playerEnterList[0]))
   shift()
   printmap()
  except:
   omit = "this"
 if re.match("attack",usin):
  if not player.area == playerArea:
   attackList = []
   index = 0
   for i in player.area.enemies:
    index += 1
    attackTarget = "{0}. ".format(index)
    attackTarget += i.species
    if i.vit == 1:
     attackTarget += " ({0}/{1} HP)".format(i.hp,i.maxhp)
    else:
     attackTarget += " (Dead)"
    attackList.append(attackTarget)
   droid.dialogCreateAlert("Which enemy?")
   droid.dialogSetItems(attackList)
   droid.dialogShow()
   response = droid.dialogGetResponse().result
   try:
    while player.area.enemies[response['item']].vit == 0:
     droid.dialogCreateAlert("{0} is already dead".format(player.area.enemies[response['item']].species))
     droid.dialogSetItems(attackList)
     droid.dialogShow()
     response = droid.dialogGetResponse().result
    player.attack(player.area.enemies[response['item']])
   except:
    omit = "This"
