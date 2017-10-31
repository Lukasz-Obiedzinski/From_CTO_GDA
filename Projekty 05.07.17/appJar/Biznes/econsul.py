from appJar import gui

win=gui("Biznes","300x500")


def przyciski(btn):
    print ('nic')

win.addOptionBox('o1', ['cos1','cos2'])


win.addButtons(['b1','b2'], przyciski)














win.go()
