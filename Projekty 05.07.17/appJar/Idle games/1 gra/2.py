from appJar import gui

def press(rb):
    print(app.getRadioButton("song"))

app=gui()
app.addRadioButton("song", "Killer Queen")
app.addRadioButton("song", "Paradise City")

# call this function, when the RadioButton changes
app.setRadioButtonChangeFunction("song", press)

app.addButton("PLAY", press)
app.go()
