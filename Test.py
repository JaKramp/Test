import sys
import math
from PyQt5.QtMultimedia import QSound
from PyQt5.QtGui import (QIcon, QPixmap)
from PyQt5.QtCore import (QTime, QTimer)
from PyQt5.QtWidgets import (QMenu, QLineEdit, QMessageBox, QLCDNumber, QLabel,
                             QPushButton, QApplication, QMainWindow, QAction,
                             QWidget, QTextEdit, QCheckBox, QComboBox,QInputDialog)
import time
import sqlite3
import random
def db():
    conn = sqlite3.connect('tutorial.db')
    c = conn.cursor()

    c.execute('create table if not exists users(name TEXT NOT NULL,password TEXT NOT NULL, grade TEXT )')
    c.execute('select * from users')
    data=c.fetchall()
    conn.commit()
    c.close()
    conn.close()
class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):
        self.loggedin=False
        self.imieg=''
        self.haslog=''
        self.tlo = 0
        self.koncwynik=0
        self.zrobione=False
        self.ispassed=False
        self.cwiczenie=False
        self.btns = []

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.zmianatla)
        self.timer.start(1000)

        self.zalogowanyg=QLineEdit(self)
        self.zalogowanyg.resize(150,30)
        self.zalogowanyg.setText("Nikt nie jest zalogowany")
        self.zalogowanyg.setReadOnly(True)

        self.btn1 = QPushButton("Zaloguj", self)
        self.btn1.move(160, 25)
        self.btn1.resize(80, 30)
        self.btn1.clicked.connect(self.loginbutton)
        self.btns.append(self.btn1)

        self.btn2 = QPushButton("Wyniki", self)
        self.btn2.move(160, 75)
        self.btn2.resize(80, 30)
        self.btns.append(self.btn2)
        self.btn2.clicked.connect(self.wyniki)

        self.btn3 = QPushButton("Wyjscie", self)
        self.btn3.move(160, 125)
        self.btn3.resize(80, 30)
        self.btns.append(self.btn3)
        self.btn3.clicked.connect(self.zamykanie)

        self.btn4=QPushButton('Sprawdzian',self)
        self.btn4.move(40,50)
        self.btn4.resize(80,30)
        self.btn4.clicked.connect(self.starttest)
        self.btns.append(self.btn4)

        self.cmbbox = QComboBox(self)
        self.cmbbox.addItem('Cwiczenie Pierwsze')
        self.cmbbox.addItem('Cwiczenie Drugie')
        self.cmbbox.resize(120,30)
        self.cmbbox.move(20,90)


        self.btn5=QPushButton('Cwicz!',self)
        self.btn5.move(40, 130)
        self.btn5.resize(80,30)
        self.btns.append(self.btn5)
        self.btn5.clicked.connect(self.ktorytest)



        self.chckbox=QCheckBox('Migajace Tlo',self)
        self.chckbox.move(300,160)

        self.setGeometry(300, 300, 400, 200)
        self.move(0, 150)
        self.setWindowTitle('Tescik')
        self.setStyleSheet("background-color: lightgreen")
        self.show()

    def ktorytest(self):
        if self.cmbbox.currentText()=='Cwiczenie Pierwsze':
            self.starttest1()
        elif self.cmbbox.currentText()=='Cwiczenie Drugie':
            self.starttest2()


    def starttest(self):
        if self.imieg!='':
            QMessageBox.about(self, "Zasady ", """Witaj w pierwszym tescie!
            Twoje zadanie polega na jak najszybszym wcisnieciu zielonego przycisku.
            Wcisniecie czerwonego przycisku spowoduje utrate punktu""")
            self.cwiczenie=False
            self.pierwsz=test()
            self.pierwsz.show()
        else:
            QMessageBox.about(self, "Error", "Nikt nie jest zalogowany")

    def starttest1(self):
        if True:
            QMessageBox.about(self, "Zasady ", """Witaj w pierwszym tescie!
            Twoje zadanie polega na jak najszybszym wcisnieciu zielonego przycisku.
            Wcisniecie czerwonego przycisku spowoduje utrate punktu""")
            self.cwiczenie=True
            self.pierwsz=test()
            self.pierwsz.show()
        else:
            QMessageBox.about(self, "Error", "Nikt nie jest zalogowany")

    def starttest2(self):
        if True:
            QMessageBox.about(self, "Zasady ", """Witaj w drugim  tescie!
            Twoje zadanie polega na jak najszybszym wcisnieciu przycisku ktory pojawi sie w losowym miejscu""")
            self.cwiczenie=True
            self.drug=test2()
            self.drug.show()
        else:
            QMessageBox.about(self, "Error", "Nikt nie jest zalogowany")
    def zamykanie(self):
        wyjscie = QMessageBox.question(self, 'Zamykanie', "Czy na pewno chcesz wyjsc?",
                                       QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        print(self.imieg)
        if wyjscie == QMessageBox.Yes:
            sys.exit(app.exec_())

    def zmianatla(self):
        if self.tlo % 3 == 0 and self.chckbox.isChecked():
            self.setStyleSheet("background-color: green")
            for btn in self.btns:
                btn.setStyleSheet("background-color: none")
            self.tlo += 1
            print(self.koncwynik)


        elif self.tlo % 3 == 1:
            self.setStyleSheet("background-color: red")
            for btn in self.btns:
                btn.setStyleSheet("background-color: none")
            self.tlo += 1

        elif self.tlo % 3 == 2:
            self.setStyleSheet("background-color: yellow")
            for btn in self.btns:
                btn.setStyleSheet("background-color: none")
            self.tlo += 1

    def loginbutton(self):
        if self.btn1.text()=='Wyloguj':
            self.wyloguj()
        elif self.btn1.text()=='Zaloguj':
            self.login()



    def login(self):
        self.log=login()
        self.log.show()


    def wyloguj(self):
        self.btn1.setText("Zaloguj")
        self.zalogowanyg.setText('Nikt nie jest zalogowany')
        self.btn1.clicked.connect(self.login)
        self.loggedin=False
        self.imieg=''

    def wyniki(self):
        self.score=wynikowe()
        self.score.show()

    def zmienwynik(self):
        with sqlite3.connect('tutorial.db') as db:
            c = db.cursor()
            c.execute(("INSERT INTO users VALUES(?,?,?)"),self.imieg,self.haslog (str(self.koncwynik)))
            c.execute(('DELETE from users WHERE name=? and grade=?'), (self.imieg, ''))
            db.commit()
        c.close()
        db.close()
class wynikowe(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI4()

    def initUI4(self):
        self.wyniki = QTextEdit(self)
        self.wyniki.setReadOnly(True)

        self.setGeometry(300, 300, 300, 250)
        self.move(0, 150)
        self.setWindowTitle("Login")
        self.wyswietl()

        self.lnedit1=QLineEdit(self)
        self.lnedit1.move(0, 200)

        self.btn1=QPushButton('Filtruj',self)
        self.btn1.resize(80,30)
        self.btn1.move(150,200)
        self.btn1.clicked.connect(self.filtruj)

        self.btn2=QPushButton('Sredni wynik',self)
        self.btn2.resize(80,30)
        self.btn2.move(250,200)
        self.btn2.clicked.connect(self.mean)
        self.btn2.hide()

        self.btn3=QPushButton('Pokaz wszystkie',self)
        self.btn3.resize(80,30)
        self.btn3.move(350,200)
        self.btn3.clicked.connect(self.showall)
        self.btn3.hide()

    def wyswietl(self):
        wynik=''
        with sqlite3.connect('tutorial.db') as db:
            c = db.cursor()
            c.execute("SELECT * FROM users")
            data = c.fetchall()
            db.commit()
            for row in data:
                if row[2]!='':
                    wynik=wynik+'Gracz: '+row[0]+' '+'Czas: '+row[2]+'\n'
                self.wyniki.setText(wynik)
        print(wynik)
        c.close()
        db.close()

    def filtruj(self):
        wynik = ''
        name1 = self.lnedit1.text()
        with sqlite3.connect('tutorial.db') as db:
            c = db.cursor()
            c.execute('SELECT * FROM users WHERE name = ? ',(name1,))
            data = c.fetchall()
            db.commit()
            for row in data:
                if row[2] != '':
                    wynik = wynik + 'Gracz: ' + row[0] + ' ' + 'Czas: ' + row[2] + '\n'
                self.wyniki.setText(wynik)
        c.close()
        db.close()
        self.btn1.clicked.disconnect()
        self.btn1.setText('Pokaz Najlepszy')
        self.btn1.clicked.connect(self.highscore)
        self.btn2.show()
        self.btn3.show()






    def highscore(self):
        najlepszy=1000
        name1=self.lnedit1.text()
        with sqlite3.connect('tutorial.db') as db:
            c = db.cursor()
            c.execute("SELECT * FROM users WHERE name=?",(name1,))
            data = c.fetchall()
            db.commit()
            for row in data:
                if float(row[2])<najlepszy:
                    wynik='Gracz: '+row[0]+' '+'Czas: '+row[2]+'\n'
                    najlepszy=float(row[2])
            self.wyniki.setText(wynik)
        c.close()
        db.close()



    def mean(self):
        suma=0
        srednia=0
        i=1
        wynik=''
        name1=self.lnedit1.text()
        with sqlite3.connect('tutorial.db') as db:
            c = db.cursor()
            c.execute("SELECT * from users where name=?",(name1,))
            data = c.fetchall()
            db.commit()
            for row in data:
                print(suma,i,srednia,round(srednia,3),name1)
                if row[2]!='':
                    suma+=float(row[2])
                    i+=1
                    srednia=float(suma/i)
            wynik = 'Gracz: {} Sredni Czas: {}'.format(name1,round(srednia,2))
        print(wynik)
        self.wyniki.setText(wynik)
        c.close()
        db.close()

    def showall(self):
        self.wyswietl()
        self.lnedit1.setText('')
        self.btn1.clicked.disconnect()
        self.btn1.setText('Filtruj')
        self.btn1.clicked.connect(self.filtruj)
        self.btn2.hide()
        self.btn3.hide()
class login(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI2()

    def initUI2(self):


        self.imie = QLineEdit(self)
        self.imie.setGeometry(100, 100, 100, 40)
        self.imie.setPlaceholderText("Tu wpisz imie")
        self.imie.move(150, 30)

        self.haslo = QLineEdit(self)
        self.haslo.setGeometry(100, 100, 100, 40)

        self.haslo.setPlaceholderText("Tu wpisz haslo")
        self.haslo.setEchoMode(QLineEdit.Password)
        self.haslo.returnPressed.connect(self.zaloguj)
        self.haslo.move(150, 80)

        self.clsbutton = QPushButton("Wyjscie",self)
        self.clsbutton.resize(80, 30)
        self.clsbutton.move(20, 100)
        self.clsbutton.clicked.connect(self.close)

        self.okbutton = QPushButton("Ok", self)
        self.okbutton.resize(80, 30)
        self.okbutton.move(20, 60)
        self.okbutton.clicked.connect(self.zaloguj)

        self.cracc=QPushButton("Utworz Konto",self)
        self.cracc.resize(80, 30)
        self.cracc.move(20, 20)
        self.cracc.clicked.connect(self.createacc)


        self.setGeometry(300, 300, 300, 150)
        self.move(0, 150)
        self.setWindowTitle("Login")
        # self.show()

    def createacc(self):
        self.account=create()
        self.account.show()

    def zaloguj(self):

        with sqlite3.connect('tutorial.db') as db:
            c = db.cursor()

        username = str(self.imie.text())
        password = str(self.haslo.text())


        c.execute('SELECT * FROM users WHERE name = ? and password = ?', (username, password))
        data = c.fetchone()
        db.commit()
        print(data)
        if data != None:
           # print('wszedles')
            ex.imieg=username
            ex.haslog=password
            ex.zalogowanyg.setText('Zalogowany gracz: '+username)
            print(ex.imieg)
            ex.loggedin=True
            print(ex.loggedin)
            ex.btn1.setText("Wyloguj")
            self.close()
        else:
            #print('nie wszedles')
class create(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI3()

    def initUI3(self):
        self.imie = QLineEdit(self)
        self.imie.setGeometry(100, 100, 100, 40)
        self.imie.setPlaceholderText("Tu wpisz imie")
        self.imie.move(150, 30)

        self.haslo = QLineEdit(self)
        self.haslo.setGeometry(100, 100, 100, 40)
        self.haslo.setPlaceholderText("Tu wpisz haslo")
        self.haslo.setEchoMode(QLineEdit.Password)
        self.haslo.move(150, 80)

        self.clsbutton = QPushButton("Wyjscie",self)
        self.clsbutton.resize(80, 30)
        self.clsbutton.move(20, 20)
        self.clsbutton.clicked.connect(self.close)

        self.okbutton = QPushButton("Ok", self)
        self.okbutton.resize(80, 30)
        self.okbutton.move(20, 60)
        self.haslo.returnPressed.connect(self.dodaj)
        self.okbutton.clicked.connect(self.dodaj)

        self.setGeometry(300, 300, 300, 150)
        self.move(0, 150)
        self.setWindowTitle("Stworz konto")
        # self.show()


    def dodaj(self):
        with sqlite3.connect('tutorial.db') as db:
            c = db.cursor()

        username = str(self.imie.text())
        password = str(self.haslo.text())
        c.execute("INSERT INTO users VALUES(?,?,?)", (username, password,''))
        c.execute("SELECT * from users")
        data=c.fetchall()
        db.commit()
        print(data)
        self.close()
class test(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI5()

    def initUI5(self):
        self.pressed=True
        self.score=0
        self.highs=0
        self.highs1=0
        self.ended=False
        self.btns=[]

        self.label = QLabel("Aktualny Wynik",self)
        self.label.move(20,90)
        self.label.show()
        if ex.cwiczenie==True:
            self.label.hide()

        self.curscr=QLineEdit(self)
        self.curscr.resize(120,30)
        self.curscr.move(20,110)
        self.curscr.setText('Wynik:  Czas:  s')
        self.curscr.setReadOnly(True)
        if ex.cwiczenie==True:
            self.curscr.hide()

        self.buton1=QPushButton("Zacznij",self)
        self.buton1.move(60, 25)
        self.buton1.clicked.connect(self.rozgrzewka)
        self.buton1.resize(90, 30)
        self.btns.append(self.buton1)


        self.btn2=QPushButton('Rozpocznij test',self)
        self.btn2.move(160, 25)
        self.btn2.resize(90, 30)
        self.btn2.clicked.connect(self.rozgrzewka)
        self.btn2.hide()
        self.btns.append(self.btn2)

        self.btn3=QPushButton('Stop Test',self)
        self.btn3.move(200,110)
        self.btn3.resize(90,30)
        self.btn3.clicked.connect(self.close)
        self.btn3.hide()

        self.setGeometry(300, 300, 300, 150)
        self.move(0, 150)
        self.setWindowTitle("Test1")
        self.show()


    def rozgrzewka(self):
        x=0
        self.buton1.setText('')
        self.btn2.setText('')
        self.btn2.show()
        self.buton1.setStyleSheet("background-color: none")
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.losowanie)
        self.timer.start(1000)
    def losowanie(self):
        if ex.cwiczenie==True:
            self.score=0
            self.btn3.show()
        if self.pressed==True and self.score<2 :
            for i in range(100):
                y=random.randrange(1,3)
                x=random.randrange(1,6)
                time.sleep(0.5)
                print(x,y,self.buton1.text())
                if x==5:
                    if y==1:
                        self.buton1.setText('Zielony')
                        self.buton1.setStyleSheet('background-color: green')
                        self.buton1.clicked.disconnect()
                        self.buton1.clicked.connect(self.punkt)

                        self.btn2.setText('Czerwony')
                        self.btn2.setStyleSheet("background-color: red")
                        self.btn2.clicked.disconnect()
                        self.btn2.clicked.connect(self.minusp)
                        self.czas = time.time()
                        self.pressed=False
                        #self.iteracje+=1
                        break
                        break
                    elif y==2:
                        self.btn2.setText('Zielony')
                        self.btn2.setStyleSheet('background-color: green')
                        self.btn2.clicked.disconnect()
                        self.btn2.clicked.connect(self.punkt)

                        self.buton1.setText('Czerwony')
                        self.buton1.setStyleSheet("background-color: red")
                        self.buton1.clicked.disconnect()
                        self.buton1.clicked.connect(self.minusp)
                        self.czas = time.time()
                        self.pressed = False
                        # self.iteracje+=1
                        break
                        break
        elif self.score>1 and self.ended!=True :
            print(self.highs1)
            string='Gratulacje, ukonczyles test pierwszy w %s sekund' %self.highs1
            print(string)
            QMessageBox.about(self,'Wygrana',string)
            self.xd = test2()
            self.xd.show()
            ex.koncwynik+=self.highs1
            self.ended=True

            self.close()




    def punkt(self):
        self.pressed=True
        self.czas1=time.time()
        self.czasa=self.czas1-self.czas
        self.score+=1
        self.highs+=self.czasa
        self.highs1=round(self.highs,3)
        string = 'Wynik {} Czas {}s'.format(self.score, self.highs1)
        self.curscr.setText(string)
        self.buton1.setText('')
        self.buton1.clicked.disconnect()
        self.buton1.clicked.connect(self.zlykilk)
        self.btn2.setText('')
        self.btn2.clicked.disconnect()
        self.btn2.clicked.connect(self.zlykilk)
        self.buton1.setStyleSheet("background-color: none")
        self.btn2.setStyleSheet('background-color: none')


    def minusp(self):
        self.pressed=True
        self.czas2=time.time()
        self.czasb=(self.czas2-self.czas)+1
        self.score=self.score-1
        self.highs+=self.czasb
        self.highs1=round(self.highs,3)
        string = 'Wynik {} Czas {}s'.format(self.score, self.highs1)
        self.curscr.setText(string)
        self.buton1.setText('')
        self.buton1.clicked.disconnect()
        self.buton1.clicked.connect(self.zlykilk)
        self.btn2.setText('')
        self.btn2.clicked.disconnect()
        self.btn2.clicked.connect(self.zlykilk)
        self.buton1.setStyleSheet("background-color: none")
        self.btn2.setStyleSheet('background-color: none')

    def zlykilk(self):
        QMessageBox.about(self, "Zasady ","Kliknales w zlym momencie")
        self.highs1+=1
        self.score-=1
class test2(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI6()

    def initUI6(self):
        self.score = 0
        self.highs = 0
        self.highs1 = 0
        self.pressed=True
        self.ended=False
        self.istest=True

        self.buton1 = QPushButton("Start", self)
        self.buton1.move(60, 25)
        self.buton1.clicked.connect(self.refleks1)
        self.buton1.resize(90, 30)

        self.btn3 = QPushButton('Stop',self)
        self.btn3.move(200,110)
        self.btn3.resize(90,30)
        self.btn3.clicked.connect(self.close)
        self.btn3.hide()


        self.curscr=QLineEdit(self)
        self.curscr.resize(120,30)
        self.curscr.move(20,110)
        self.curscr.setText('Wynik:  Czas:  s')
        self.curscr.setReadOnly(True)
        if ex.cwiczenie==True:
            self.curscr.hide()

        self.setGeometry(300, 300, 300, 150)
        self.move(0, 150)
        self.setWindowTitle("Test2")
        self.show()

    def refleks1(self):
        self.buton1.hide()
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.refleks)
        self.timer.start(1000)

    def refleks(self):
        if  ex.cwiczenie==True:
            self.score = 0
            self.btn3.show()
        if self.score<5 and self.pressed==True:
            for i in range(100):
                e = random.randrange(1, 6)
                x = random.randrange(1, 200)
                y = random.randrange(1,50)
                time.sleep(0.5)
                print(e)
                if e == 5:
                    self.buton1.resize(70, 50)
                    self.buton1.move(x,y)
                    self.buton1.show()
                    self.buton1.setText('Kliknij Mnie!')
                    self.buton1.setStyleSheet('background-color: green')
                    self.buton1.clicked.disconnect()
                    self.buton1.clicked.connect(self.punkt)
                    self.czas = time.time()
                    self.pressed = False
                    break
                    break
        elif self.score > 4 and self.ended != True:
            print(self.highs1)
            string = 'Gratulacje, ukonczyles test drugi w %s sekund' % self.highs1
            print(string)
            QMessageBox.about(self, 'Wygrana', string)
            self.ended = True
            ex.koncwynik+=self.highs1
            self.zmienwynik()
            self.close()

    def punkt(self):
        self.pressed = True
        self.czas1 = time.time()
        self.czasa = self.czas1 - self.czas
        self.score += 1
        self.highs += self.czasa
        self.highs1 = round(self.highs, 3)
        string = 'Wynik {} Czas {}s'.format(self.score, self.highs1)
        self.curscr.setText(string)
        self.buton1.hide()
    def zmienwynik(self):
        with sqlite3.connect('tutorial.db') as db:
            c = db.cursor()
            wynik=str(round(ex.koncwynik,3))
            c.execute(("INSERT INTO users VALUES(?,?,?)"),(ex.imieg,ex.haslog,wynik))
            c.execute(('DELETE from users WHERE name=? and grade=?'), (ex.imieg, ''))
            db.commit()
        c.close()
        db.close()


class test3(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI6()

    def initUI6(self):
        self.score = 0
        self.highs = 0
        self.highs1 = 0
        self.pressed=True
        self.ended=False
        self.istest=True
        i=0
        j=0
        for i in range(10):
            i+=1
            for j in range(5):
                j+=1
                btn=QPushButton(self)
                btn.resize(10,10)
                btn.move(10*i,10*j)


        self.setGeometry(300, 300, 300, 150)
        self.move(0, 150)
        self.setWindowTitle("Test2")
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    db()
    ex = Example()
    sys.exit(app.exec_())