from appJar import gui
import sys
import time


win=gui("Pamietnik CTO","800x600")
win.setResizable(True)
def przycisk(btn):
    if btn=="Zapisz":
        zapisdaty=win.getDatePicker("datownik")
# zapis pliku jako data 
        data=time.strftime("%d.%m.%y" " - " "%H.%M.%S.txt")
        f=open(str(data),'w')
# zapis tesktu do pliku
        tekst=win.getTextArea("t1")
        f.write(str(zapisdaty))
        f.write(str(godzina))
        f.write(str(tekst))
        f.close()
    elif btn=="Wyjdz":
        win.stop()
        


    
godzina=time.strftime(" godzina: %H:%M:%S \n \n")
win.addDatePicker("datownik")
win.setDatePickerRange("datownik", 1900, 2100)
win.setDatePicker("datownik")
win.addScrolledTextArea("t1")
zapis=win.getDatePicker("datownik")
#przycisk zapisz
win.addButtons(["Zapisz","Wyjdz"], przycisk)



# Kolorystyka i pierdoly





win.go()

















