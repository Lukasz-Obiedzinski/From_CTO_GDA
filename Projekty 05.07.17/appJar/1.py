from appJar import gui

win=gui()
def przycisk(btn):
    zapis=win.getEntry("e1")
    print (zapis)
    dzien=win.getOptionBox("-Dzien-")
    print (dzien)
    miesiac=win.getOptionBox("-Miesiac-")
    print (miesiac)
    rok=win.getOptionBox("-Rok-")
    print (rok)


win.addLabelOptionBox("-Dzien-",["1", "2", "3", "4", "5", "6", "7",
                              "8", "9", "10", "11", "12", "13", "14", "15",
                              "16", "17", "18", "19", "20", "21", "22", "23",
                              "24", "25", "26", "27", "28", "29", "30", "31",])

win.addLabelOptionBox("-Miesiac-",["Styczen", "Luty", "Marzec", "Kwiecien", "Maj",
                                   "Czerwiec", "Lipiec","Sierpien", "Wrzesien",
                                   "Pazdziernik", "Listopad", "Grudzien"])

win.addLabelOptionBox("-Rok-",["2017","2018"])

win.addEntry("e1")
win.setEntryDefault("e1", "Data")
win.addEntry("e2")








win.addLabelEntry("Name")

win.setEntryDefault("e2", "Age here")

win.addButton("zapisz", przycisk)
win.go()


