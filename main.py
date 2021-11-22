import tkinter as tk
from tkinter import messagebox as MessageBox
from tkinter import ttk

import mysql.connector as mysql

#Tabok
def on_tab_selected(event):
    selected_tab = event.widget.select()
    tab_text = event.widget.tab(selected_tab, "text")

    if tab_text == "Emberek":
        showEmber()

    if tab_text == "Épületek":
        showEpulet()

    if tab_text == "Telkek":
        showTelek()

    if tab_text == "Listázások":
        showListazasok()

    if tab_text == "Kereskedések":
        showEpuletKereskedesek()
        showTelekKereskedesek()

def showEmber():
   con = mysql.connect(host=dbhost, user=dbuser, password=dbpass, database=dbname)
   cursor = con.cursor()
   cursor.execute('select * from ember')
   rows = cursor.fetchall()
   listfelh.delete(0, listfelh.size())
   for row in rows:
        insertData = '{}  {}  {}  {}  {} {}'.format(row[0], row[1], row[2], row[3], row[4], row[5])
        listfelh.insert(listfelh.size() + 1, insertData)
   con.close()

def showEpulet():
    con = mysql.connect(host=dbhost, user=dbuser, password=dbpass, database=dbname)
    cursor = con.cursor()
    cursor.execute('select * from epulet')
    rows = cursor.fetchall()
    listepulet.delete(0, listepulet.size())
    for row in rows:
        insertData = '{}  {}  {}  {}  {}'.format(row[0], row[1], row[2], row[3], row[4])
        listepulet.insert(listepulet.size() + 1, insertData)
    con.close()

def showTelek():
    con = mysql.connect(host=dbhost, user=dbuser, password=dbpass, database=dbname)
    cursor = con.cursor()
    cursor.execute('select * from telek')
    rows = cursor.fetchall()
    listtelek.delete(0, listtelek.size())
    for row in rows:
        insertData = '{}  {}  {}  {}'.format(row[0], row[1], row[2], row[3])
        listtelek.insert(listtelek.size() + 1, insertData)
    con.close()

def showListazasok():
    con = mysql.connect(host=dbhost, user=dbuser, password=dbpass, database=dbname)
    cursor = con.cursor()
    cursor.execute('select * from epulet')
    rows = cursor.fetchall()
    listtelek.delete(0, listtelek.size())
    for row in rows:
        insertData = '{}  {}  {}  {}  {}'.format(row[0], row[1], row[2], row[3], row[4])
        listtelek.insert(listtelek.size() + 1, insertData)
    con.close()

def showEpuletKereskedesek():
    con = mysql.connect(host=dbhost, user=dbuser, password=dbpass, database=dbname)
    cursor = con.cursor()
    cursor.execute('select epuletkereskedes.kereskedesID,ember.nev, epulet.cim '
                   'from epulet, epuletkereskedes, ember '
                   'where epulet.epuletID in (select epuletkereskedes.epuletID from epuletkereskedes  where epuletkereskedes.kereskedesID) '
                   'and ember.emberID in (select epuletkereskedes.emberID from epuletkereskedes  where epuletkereskedes.kereskedesID) '
                   'and epulet.epuletID = epuletkereskedes.epuletID AND ember.emberID = epuletkereskedes.emberID')
    rows = cursor.fetchall()
    listev.delete(0, listev.size())
    for row in rows:
        insertData = '{}  {}  {}'.format(row[0], row[1], row[2])
        listev.insert(listev.size() + 1, insertData)
    con.close()

def showTelekKereskedesek():
    con = mysql.connect(host=dbhost, user=dbuser, password=dbpass, database=dbname)
    cursor = con.cursor()
    cursor.execute('select telekkereskedes.kereskedesID,ember.nev, telek.cim '
                   'from telek, telekkereskedes, ember '
                   'where telek.telekID in (select telekkereskedes.telekID from telekkereskedes  where telekkereskedes.kereskedesID) '
                   'and ember.emberID in (select telekkereskedes.emberID from telekkereskedes  where telekkereskedes.kereskedesID) '
                   'and telek.telekID = telekkereskedes.telekID AND ember.emberID = telekkereskedes.emberID')
    rows = cursor.fetchall()
    listtv.delete(0, listtv.size())
    for row in rows:
        insertData = '{}  {}  {}'.format(row[0], row[1], row[2])
        listtv.insert(listtv.size() + 1, insertData)
    con.close()

#######################################################################################################################
#Ember Funkciók

def getEmber():
    if idEmberEntryTabOne.get() == "":
        MessageBox.showinfo("Info", "ID mező kötelező")
    else:
        con = mysql.connect(host=dbhost, user=dbuser, password=dbpass, database=dbname)
        cursor = con.cursor()
        cursor.execute('select * from ember where emberID={}'.format(idEmberEntryTabOne.get()))
        rows = cursor.fetchmany(1)
        for row in rows:
            nevEntryTabOne.insert(0, row[1])
            szuletesiDatumEntryTabOne.insert(0, row[2])
            penzEntryTabOne.insert(0, row[3])
            emailEntryTabOne.insert(0, row[4])
            telefonEntryTabOne.insert(0, row[5])
        con.close()
        showEmber()


def insertEmber():
    if idEmberEntryTabOne.get() == "" or nevEntryTabOne.get() == "" or szuletesiDatumEntryTabOne.get() == "" or telefonEntryTabOne.get() == "":
        MessageBox.showinfo("Info", "Minden mező kötelező")
    else:
        con = mysql.connect(host=dbhost, user=dbuser, password=dbpass, database=dbname)
        cursor = con.cursor()
        cursor.execute('insert into ember values("{}","{}","{}","{}","{}","{}")'.format(idEmberEntryTabOne.get(), nevEntryTabOne.get(),
                                                                                   szuletesiDatumEntryTabOne.get(),penzEntryTabOne.get(),emailEntryTabOne.get(), telefonEntryTabOne.get(),
                                                                                   ))
        cursor.execute('commit')
        idEmberEntryTabOne.delete(0, 'end')
        nevEntryTabOne.delete(0, 'end')
        szuletesiDatumEntryTabOne.delete(0, 'end')
        penzEntryTabOne.delete(0, 'end')
        emailEntryTabOne.delete(0, 'end')
        telefonEntryTabOne.delete(0, 'end')
        MessageBox.showinfo('Info', 'Sikeres beszúrás')
        con.close()
        showEmber()


def deleteEmber():
    if idEmberEntryTabOne.get() == "":
        MessageBox.showinfo("Info", "ID mező kötelező")
    else:
        con = mysql.connect(host=dbhost, user=dbuser, password=dbpass, database=dbname)
        cursor = con.cursor()
        cursor.execute('delete from ember where emberID="{}"'.format(idEmberEntryTabOne.get()))
        cursor.execute('commit')
        idEmberEntryTabOne.delete(0, 'end')
        nevEntryTabOne.delete(0, 'end')
        szuletesiDatumEntryTabOne.delete(0, 'end')
        penzEntryTabOne.delete(0, 'end')
        emailEntryTabOne.delete(0, 'end')
        telefonEntryTabOne.delete(0, 'end')
        MessageBox.showinfo('Info', 'Törlés végrehajtva')
        con.close()
        showEmber()


def updateEmber():
    if idEmberEntryTabOne.get() == "" or nevEntryTabOne.get() == "" or szuletesiDatumEntryTabOne.get() == "" \
            or penzEntryTabOne.get() == "" or emailEntryTabOne.get() == "" or telefonEntryTabOne.get() == "":
        MessageBox.showinfo("Info", "Minden mező kötelező")
    else:
        con = mysql.connect(host=dbhost, user=dbuser, password=dbpass, database=dbname)
        cursor = con.cursor()
        cursor.execute(
            'update ember set nev="{}", szuldatum="{}", penz="{}", email="{}", telefon="{}" '
            'where emberID={}'.format(nevEntryTabOne.get(), szuletesiDatumEntryTabOne.get(), penzEntryTabOne.get(), emailEntryTabOne.get(), telefonEntryTabOne.get(),
                                       idEmberEntryTabOne.get()))
        cursor.execute('commit')
        idEmberEntryTabOne.delete(0, 'end')
        nevEntryTabOne.delete(0, 'end')
        szuletesiDatumEntryTabOne.delete(0, 'end')
        penzEntryTabOne.delete(0, 'end')
        emailEntryTabOne.delete(0, 'end')
        telefonEntryTabOne.delete(0, 'end')
        MessageBox.showinfo('Info', 'Sikeres frissítés')
        con.close()
        showEmber()

#######################################################################################################################
#Épület Funkciók

def getEpulet():
    if idEpuletEntryTabTwo.get() == "":
        MessageBox.showinfo("Info", "ID mező kötelező")
    else:
        con = mysql.connect(host=dbhost, user=dbuser, password=dbpass, database=dbname)
        cursor = con.cursor()
        cursor.execute('select * from epulet where epuletID={}'.format(idEpuletEntryTabTwo.get()))
        rows = cursor.fetchmany(1)
        for row in rows:
            teruletEntryTabTwo.insert(0, row[1])
            cimEntryTabTwo.insert(0, row[2])
            epitesEveEntryTabTwo.insert(0, row[3])
            arEntryTabTwo.insert(0, row[4])
        con.close()
        showEpulet()


def insertEpulet():
    if idEpuletEntryTabTwo.get() == "" or teruletEntryTabTwo.get() == "" or cimEntryTabTwo.get() == "" or epitesEveEntryTabTwo.get() == "" \
            or arEntryTabTwo.get() == "":
        MessageBox.showinfo("Info", "Minden mező kötelező")
    else:
        con = mysql.connect(host=dbhost, user=dbuser, password=dbpass, database=dbname)
        cursor = con.cursor()
        cursor.execute('insert into epulet values("{}","{}","{}","{}","{}")'.format(idEpuletEntryTabTwo.get(), teruletEntryTabTwo.get(),
                                                                                    cimEntryTabTwo.get(), epitesEveEntryTabTwo.get(),
                                                                                    arEntryTabTwo.get()))
        cursor.execute('commit')
        idEpuletEntryTabTwo.delete(0, 'end')
        teruletEntryTabTwo.delete(0, 'end')
        cimEntryTabTwo.delete(0, 'end')
        epitesEveEntryTabTwo.delete(0, 'end')
        arEntryTabTwo.delete(0, 'end')
        MessageBox.showinfo('Info', 'Sikeres beszúrás')
        con.close()
        showEpulet()


def deleteEpulet():
    if idEpuletEntryTabTwo.get() == "":
        MessageBox.showinfo("Info", "ID mező kötelező")
    else:
        con = mysql.connect(host=dbhost, user=dbuser, password=dbpass, database=dbname)
        cursor = con.cursor()
        cursor.execute('delete from epulet where epuletID="{}"'.format(idEpuletEntryTabTwo.get()))
        cursor.execute('commit')
        idEpuletEntryTabTwo.delete(0, 'end')
        teruletEntryTabTwo.delete(0, 'end')
        cimEntryTabTwo.delete(0, 'end')
        epitesEveEntryTabTwo.delete(0, 'end')
        arEntryTabTwo.delete(0, 'end')
        MessageBox.showinfo('Info', 'Törlés végrehajtva')
        con.close()
        showEpulet()


def updateEpulet():
    if idEpuletEntryTabTwo.get() == "" or teruletEntryTabTwo.get() == "" or cimEntryTabTwo.get() == "" or epitesEveEntryTabTwo.get() == "" \
            or arEntryTabTwo.get() == "":
        MessageBox.showinfo("Info", "Minden mező kötelező")
    else:
        con = mysql.connect(host=dbhost, user=dbuser, password=dbpass, database=dbname)
        cursor = con.cursor()
        cursor.execute(
            'update epulet set terulet="{}", cim="{}", epites_eve="{}", ar="{}" '
            'where epuletID={}'.format(teruletEntryTabTwo.get(), cimEntryTabTwo.get(), epitesEveEntryTabTwo.get(), arEntryTabTwo.get(),
                                        idEpuletEntryTabTwo.get()))
        cursor.execute('commit')
        idEpuletEntryTabTwo.delete(0, 'end')
        teruletEntryTabTwo.delete(0, 'end')
        cimEntryTabTwo .delete(0, 'end')
        epitesEveEntryTabTwo.delete(0, 'end')
        arEntryTabTwo.delete(0, 'end')
        MessageBox.showinfo('Info', 'Sikeres frissítés')
        con.close()
        showEpulet()

#######################################################################################################################
#Telek Funkciók
def getTelek():
    if idTelekEntryTabThree.get() == "":
        MessageBox.showinfo("Info", "ID mező kötelező")
    else:
        con = mysql.connect(host=dbhost, user=dbuser, password=dbpass, database=dbname)
        cursor = con.cursor()
        cursor.execute('select * from telek where telekID={}'.format(idTelekEntryTabThree.get()))
        rows = cursor.fetchmany(1)
        for row in rows:
            teruletEntryTabThree.insert(0, row[1])
            cimEntryTabThree.insert(0, row[2])
            arEntryTabThree.insert(0, row[3])
        con.close()
        showTelek()


def insertTelek():
    if idTelekEntryTabThree.get() == "" or teruletEntryTabThree.get() == "" or cimEntryTabThree.get() == "" or arEntryTabThree.get() == "":
        MessageBox.showinfo("Info", "Minden mező kötelező")
    else:
        con = mysql.connect(host=dbhost, user=dbuser, password=dbpass, database=dbname)
        cursor = con.cursor()
        cursor.execute('insert into telek values("{}","{}","{}","{}")'.format(idTelekEntryTabThree.get(), teruletEntryTabThree.get(),
                                                                              cimEntryTabThree.get(), arEntryTabThree.get()))
        cursor.execute('commit')
        idTelekEntryTabThree.delete(0, 'end')
        teruletEntryTabThree.delete(0, 'end')
        cimEntryTabThree.delete(0, 'end')
        arEntryTabThree.delete(0, 'end')
        MessageBox.showinfo('Info', 'Sikeres beszúrás')
        con.close()
        showTelek()


def deleteTelek():
    if idTelekEntryTabThree.get() == "":
        MessageBox.showinfo("Info", "ID mező kötelező")
    else:
        con = mysql.connect(host=dbhost, user=dbuser, password=dbpass, database=dbname)
        cursor = con.cursor()
        cursor.execute('delete from telek where telekID="{}"'.format(idTelekEntryTabThree.get()))
        cursor.execute('commit')
        idTelekEntryTabThree.delete(0, 'end')
        teruletEntryTabThree.delete(0, 'end')
        cimEntryTabThree.delete(0, 'end')
        arEntryTabThree.delete(0, 'end')
        MessageBox.showinfo('Info', 'Törlés végrehajtva')
        con.close()
        showTelek()


def updateTelek():
    if idTelekEntryTabThree.get() == "" or teruletEntryTabThree.get() == "" or cimEntryTabThree.get() == "" or arEntryTabThree.get() == "":
        MessageBox.showinfo("Info", "Minden mező kötelező")
    else:
        con = mysql.connect(host=dbhost, user=dbuser, password=dbpass, database=dbname)
        cursor = con.cursor()
        cursor.execute(
            'update telek set terulet="{}", cim="{}", ar="{}" '
            'where telekID={}'.format(teruletEntryTabThree.get(), cimEntryTabThree.get(), arEntryTabThree.get(), idTelekEntryTabThree.get()))
        cursor.execute('commit')
        idTelekEntryTabThree.delete(0, 'end')
        teruletEntryTabThree.delete(0, 'end')
        cimEntryTabThree.delete(0, 'end')
        arEntryTabThree.delete(0, 'end')
        MessageBox.showinfo('Info', 'Sikeres frissítés')
        con.close()
        showTelek()

#######################################################################################################################
#Listazas Funkciók
def epuletMaxArea():
    con = mysql.connect(host=dbhost, user=dbuser, password=dbpass, database=dbname)
    cursor = con.cursor()
    cursor.execute('select * from epulet order by epulet.terulet desc')
    rows = cursor.fetchall()
    listker.delete(0, listker.size())
    for row in rows:
        insertData = '{}  {}  {}  {}  {}'.format(row[0], row[1], row[2], row[3], row[4])
        listker.insert(listker.size() + 1, insertData)
    con.close()

def epuletMinArea():
    con = mysql.connect(host=dbhost, user=dbuser, password=dbpass, database=dbname)
    cursor = con.cursor()
    cursor.execute('select * from epulet order by epulet.terulet asc')
    rows = cursor.fetchall()
    listker.delete(0, listker.size())
    for row in rows:
        insertData = '{}  {}  {}  {}  {}'.format(row[0], row[1], row[2], row[3], row[4])
        listker.insert(listker.size() + 1, insertData)
    con.close()

def epuletMaxAr():
    con = mysql.connect(host=dbhost, user=dbuser, password=dbpass, database=dbname)
    cursor = con.cursor()
    cursor.execute('select * from epulet order by epulet.ar desc')
    rows = cursor.fetchall()
    listker.delete(0, listker.size())
    for row in rows:
        insertData = '{}  {}  {}  {}  {}'.format(row[0], row[1], row[2], row[3], row[4])
        listker.insert(listker.size() + 1, insertData)
    con.close()

def epuletMinAr():
    con = mysql.connect(host=dbhost, user=dbuser, password=dbpass, database=dbname)
    cursor = con.cursor()
    cursor.execute('select * from epulet order by epulet.ar asc')
    rows = cursor.fetchall()
    listker.delete(0, listker.size())
    for row in rows:
        insertData = '{}  {}  {}  {}  {}'.format(row[0], row[1], row[2], row[3], row[4])
        listker.insert(listker.size() + 1, insertData)
    con.close()

def atlagtolDragabbHaz():
    con = mysql.connect(host=dbhost, user=dbuser, password=dbpass, database=dbname)
    cursor = con.cursor()
    cursor.execute('select * from epulet where epulet.ar > (select avg(epulet.ar) from epulet)')
    rows = cursor.fetchall()
    listker.delete(0, listker.size())
    for row in rows:
        insertData = '{}  {}  {}  {}  {}'.format(row[0], row[1], row[2], row[3], row[4])
        listker.insert(listker.size() + 1, insertData)
    con.close()

def atlagtolOlcsobbHaz():
    con = mysql.connect(host=dbhost, user=dbuser, password=dbpass, database=dbname)
    cursor = con.cursor()
    cursor.execute('select * from epulet where epulet.ar < (select avg(epulet.ar) from epulet)')
    rows = cursor.fetchall()
    listker.delete(0, listker.size())
    for row in rows:
        insertData = '{}  {}  {}  {}  {}'.format(row[0], row[1], row[2], row[3], row[4])
        listker.insert(listker.size() + 1, insertData)
    con.close()

def telekMaxArea():
    con = mysql.connect(host=dbhost, user=dbuser, password=dbpass, database=dbname)
    cursor = con.cursor()
    cursor.execute('select * from telek order by telek.terulet desc')
    rows = cursor.fetchall()
    listker.delete(0, listker.size())
    for row in rows:
        insertData = '{}  {}  {}  {}'.format(row[0], row[1], row[2], row[3])
        listker.insert(listker.size() + 1, insertData)
    con.close()

def telekMinArea():
    con = mysql.connect(host=dbhost, user=dbuser, password=dbpass, database=dbname)
    cursor = con.cursor()
    cursor.execute('select * from telek order by telek.terulet asc')
    rows = cursor.fetchall()
    listker.delete(0, listker.size())
    for row in rows:
        insertData = '{}  {}  {}  {}'.format(row[0], row[1], row[2], row[3])
        listker.insert(listker.size() + 1, insertData)
    con.close()

def telekMaxAr():
    con = mysql.connect(host=dbhost, user=dbuser, password=dbpass, database=dbname)
    cursor = con.cursor()
    cursor.execute('select * from telek order by telek.ar desc')
    rows = cursor.fetchall()
    listker.delete(0, listker.size())
    for row in rows:
        insertData = '{}  {}  {}  {}'.format(row[0], row[1], row[2], row[3])
        listker.insert(listker.size() + 1, insertData)
    con.close()

def telekMinAr():
    con = mysql.connect(host=dbhost, user=dbuser, password=dbpass, database=dbname)
    cursor = con.cursor()
    cursor.execute('select * from telek order by telek.ar asc')
    rows = cursor.fetchall()
    listker.delete(0, listker.size())
    for row in rows:
        insertData = '{}  {}  {}  {}'.format(row[0], row[1], row[2], row[3])
        listker.insert(listker.size() + 1, insertData)
    con.close()

def atlagtolDragabbTelek():
    con = mysql.connect(host=dbhost, user=dbuser, password=dbpass, database=dbname)
    cursor = con.cursor()
    cursor.execute('select * from telek where telek.ar > (select avg(telek.ar) from telek)')
    rows = cursor.fetchall()
    listker.delete(0, listker.size())
    for row in rows:
        insertData = '{}  {}  {}  {}'.format(row[0], row[1], row[2], row[3])
        listker.insert(listker.size() + 1, insertData)
    con.close()

def atlagtolOlcsobbTelek():
    con = mysql.connect(host=dbhost, user=dbuser, password=dbpass, database=dbname)
    cursor = con.cursor()
    cursor.execute('select * from telek where telek.ar < (select avg(telek.ar) from telek)')
    rows = cursor.fetchall()
    listker.delete(0, listker.size())
    for row in rows:
        insertData = '{}  {}  {}  {}'.format(row[0], row[1], row[2], row[3])
        listker.insert(listker.size() + 1, insertData)
    con.close()

def legtobbPenz():
    con = mysql.connect(host=dbhost, user=dbuser, password=dbpass, database=dbname)
    cursor = con.cursor()
    cursor.execute('select * from ember order by ember.penz desc')
    rows = cursor.fetchall()
    listker.delete(0, listker.size())
    for row in rows:
        insertData = '{}  {}  {}  {}  {}  {}'.format(row[0], row[1], row[2], row[3], row[4], row[5])
        listker.insert(listker.size() + 1, insertData)
    con.close()

def legkevesebbPenz():
    con = mysql.connect(host=dbhost, user=dbuser, password=dbpass, database=dbname)
    cursor = con.cursor()
    cursor.execute('select * from ember order by ember.penz asc')
    rows = cursor.fetchall()
    listker.delete(0, listker.size())
    for row in rows:
        insertData = '{}  {}  {}  {}  {}  {}'.format(row[0], row[1], row[2], row[3], row[4], row[5])
        listker.insert(listker.size() + 1, insertData)
    con.close()

def epuletetTudEVenni():
    if idVehetEEmberEntryTabFour.get() == "":
        MessageBox.showinfo("Info", "ID mező kötelező")
    else:
        con = mysql.connect(host=dbhost, user=dbuser, password=dbpass, database=dbname)
        cursor = con.cursor()
        cursor.execute('select * from epulet where epulet.ar <= (select ember.penz from ember where emberID="{}")'.format(idVehetEEmberEntryTabFour.get()))
        rows = cursor.fetchall()
        listker.delete(0, listker.size())
        for row in rows:
            insertData = '{}  {}  {}  {}  {}'.format(row[0], row[1], row[2], row[3], row[4])
            listker.insert(listker.size() + 1, insertData)
        con.close()
        showListazasok()

def telketTudEVenni():
    if idVehetEEmberEntryTabFour.get() == "":
        MessageBox.showinfo("Info", "ID mező kötelező")
    else:
        con = mysql.connect(host=dbhost, user=dbuser, password=dbpass, database=dbname)
        cursor = con.cursor()
        cursor.execute(
            'select * from telek where telek.ar <= (select ember.penz from ember where emberID="{}")'.format(
                idVehetEEmberEntryTabFour.get()))
        rows = cursor.fetchall()
        listker.delete(0, listker.size())
        for row in rows:
            insertData = '{}  {}  {}  {}'.format(row[0], row[1], row[2], row[3])
            listker.insert(listker.size() + 1, insertData)
        con.close()
        showListazasok()

#######################################################################################################################
#Kereskedés Funkciók
def hazatVesz():
    if epuletIdEntryTabFive.get() == "" or emberIdeEntryTabFive.get() == "" or epuletIdEntryTabFive.get() == "":
        MessageBox.showinfo("Info", "Minden mező kötelező")
    else:
        con = mysql.connect(host=dbhost, user=dbuser, password=dbpass, database=dbname)
        cursor = con.cursor()
        cursor.execute('select ember.penz from ember where emberID="{}"'.format(emberIdeEntryTabFive.get()))
        rows = cursor.fetchall()

        cursor.execute('select epulet.ar from epulet where epuletID="{}"'.format(epuletIdEntryTabFive.get()))
        row = cursor.fetchall()

        if rows < row:
            MessageBox.showinfo("Info", "Kevés pénze van, keressen másik épületet!")
        else:
            cursor.execute('insert into epuletKereskedes values("{}","{}","{}")'.format(epuletkerIDEntryTabFive.get(),
                                                                                  emberIdeEntryTabFive.get(), epuletIdEntryTabFive.get()))
            cursor.execute('commit')
            epuletkerIDEntryTabFive.delete(0, 'end')
            emberIdeEntryTabFive.delete(0, 'end')
            epuletIdEntryTabFive.delete(0, 'end')
            MessageBox.showinfo('Info', 'Sikeres beszúrás')
        con.close()
        showEpuletKereskedesek()

def epuletKerTorles():
    if epuletkertorolEntryTabFive.get() == "":
        MessageBox.showinfo("Info", "ID mező kötelező")
    else:
        con = mysql.connect(host=dbhost, user=dbuser, password=dbpass, database=dbname)
        cursor = con.cursor()
        cursor.execute('delete from epuletKereskedes where kereskedesID="{}"'.format(epuletkertorolEntryTabFive.get()))
        cursor.execute('commit')
        epuletkertorolEntryTabFive.delete(0, 'end')
        emberIdeEntryTabFive.delete(0, 'end')
        epuletIdEntryTabFive.delete(0, 'end')
        MessageBox.showinfo('Info', 'Törlés végrehajtva')
        con.close()
        showEpuletKereskedesek()

def telketVesz():
    if telekIdEntryTabFive.get() == "" or emberIdtEntryTabFive.get() == "" or telekIdEntryTabFive.get() == "":
        MessageBox.showinfo("Info", "Minden mező kötelező")
    else:
        con = mysql.connect(host=dbhost, user=dbuser, password=dbpass, database=dbname)
        cursor = con.cursor()
        cursor.execute('select ember.penz from ember where emberID="{}"'.format(emberIdtEntryTabFive.get()))
        rows = cursor.fetchall()

        cursor.execute('select telek.ar from telek where telekID="{}"'.format(telekIdEntryTabFive.get()))
        row = cursor.fetchall()

        if rows < row:
            MessageBox.showinfo("Info", "Kevés pénze van, keressen másik telket!")
        else:
            cursor.execute('insert into telekKereskedes values("{}","{}","{}")'.format(telekkerIDEntryTabFive.get(),
                                                                                        emberIdtEntryTabFive.get(),
                                                                                        telekIdEntryTabFive.get()))
            cursor.execute('commit')
            telekkerIDEntryTabFive.delete(0, 'end')
            emberIdtEntryTabFive.delete(0, 'end')
            telekIdEntryTabFive.delete(0, 'end')
            MessageBox.showinfo('Info', 'Sikeres beszúrás')
        con.close()
        showTelekKereskedesek()

def telekKerTorles():
    if telekkertorolEntryTabFive.get() == "":
        MessageBox.showinfo("Info", "ID mező kötelező")
    else:
        con = mysql.connect(host=dbhost, user=dbuser, password=dbpass, database=dbname)
        cursor = con.cursor()
        cursor.execute('delete from telekKereskedes where kereskedesID="{}"'.format(telekkertorolEntryTabFive.get()))
        cursor.execute('commit')
        telekkertorolEntryTabFive.delete(0, 'end')
        emberIdtEntryTabFive.delete(0, 'end')
        telekIdEntryTabFive.delete(0, 'end')
        MessageBox.showinfo('Info', 'Törlés végrehajtva')
        con.close()
        showTelekKereskedesek()

#######################################################################################################################

if __name__ == '__main__':
    dbhost = 'localhost'
    dbuser = 'root'
    dbpass = ''
    dbname = 'ingatlan'

    root = tk.Tk()
    root.geometry("1000x600")
    root.title("Ingatlan")

    #Tabok
    tab_parent = ttk.Notebook(root)

    tab_parent.bind("<<NotebookTabChanged>>", on_tab_selected)

    style = ttk.Style()
    style.configure('TNotebook', background='red')
    style.configure('TNotebook.Tab', foreground='blue')

    tab1 = ttk.Frame(tab_parent)
    tab2 = ttk.Frame(tab_parent)
    tab3 = ttk.Frame(tab_parent)
    tab4 = ttk.Frame(tab_parent)
    tab5 = ttk.Frame(tab_parent)

    tab_parent.add(tab1, text="Emberek")
    tab_parent.add(tab2, text="Épületek")
    tab_parent.add(tab3, text="Telkek")
    tab_parent.add(tab4, text="Listázások")
    tab_parent.add(tab5, text="Kereskedések")

    tab_parent.pack(expand=1, fill='both')

#######################################################################################################################

    #TAB 1 EMBER
    #TAB 1 ID
    idEmberLabelTabOne = tk.Label(tab1, text='Azonosító', font=('bold', 10))
    idEmberLabelTabOne.grid(row=0, column=0, padx=15, pady=15)
    idEmberEntryTabOne = tk.Entry(tab1)
    idEmberEntryTabOne.grid(row=0, column=1, padx=15, pady=15)

    # TAB 1 NEV
    nevLabelTabOne = tk.Label(tab1, text='Név', font=('bold', 10))
    nevLabelTabOne.grid(row=1, column=0, padx=15, pady=15)
    nevEntryTabOne = tk.Entry(tab1)
    nevEntryTabOne.grid(row=1, column=1, padx=15, pady=15)

    # TAB 1 SZULDATUM
    szuletesiDatumLabelTabOne = tk.Label(tab1, text='Születési dátum', font=('bold', 10))
    szuletesiDatumLabelTabOne.grid(row=2, column=0, padx=15, pady=15)
    szuletesiDatumEntryTabOne = tk.Entry(tab1)
    szuletesiDatumEntryTabOne.grid(row=2, column=1, padx=15, pady=15)

    #TAB 1 PENZ
    penzLabelTabOne = tk.Label(tab1, text='Pénz', font=('bold', 10))
    penzLabelTabOne.grid(row=3, column=0, padx=15, pady=15)
    penzEntryTabOne = tk.Entry(tab1)
    penzEntryTabOne.grid(row=3, column=1, padx=15, pady=15)

    #TAB 1 EMAIL
    emailLabelTabOne = tk.Label(tab1, text='Email', font=('bold', 10))
    emailLabelTabOne.grid(row=4, column=0, padx=15, pady=15)
    emailEntryTabOne = tk.Entry(tab1)
    emailEntryTabOne.grid(row=4, column=1, padx=15, pady=15)

    #TAB 1 TELEFON
    telefonLabelTabOne = tk.Label(tab1, text='Telefon', font=('bold', 10))
    telefonLabelTabOne.grid(row=5, column=0, padx=15, pady=15)
    telefonEntryTabOne = tk.Entry(tab1)
    telefonEntryTabOne.grid(row=5, column=1, padx=15, pady=15)

    #TAB 1 GOMB
    beszurButtonTabOne = tk.Button(tab1, text="Beszúr", command=insertEmber)
    beszurButtonTabOne.place(x=30, y=335)

    frissitButtonTabOne = tk.Button(tab1, text="Frissít", command=updateEmber)
    frissitButtonTabOne.place(x=100, y=335)

    lekerButtonTabOne = tk.Button(tab1, text="Lekér", command=getEmber)
    lekerButtonTabOne.place(x=170, y=335)

    torolButtonTabOne = tk.Button(tab1, text="Töröl", command=deleteEmber)
    torolButtonTabOne.place(x=240, y=335)

    listfelh = tk.Listbox(tab1, width=70, height=20)
    listfelh.place(x=300, y=30)

#######################################################################################################################

    # TAB 2
    # TAB 2 ID
    idEpuletLabelTabTwo = tk.Label(tab2, text='Azonosító', font=('bold', 10))
    idEpuletLabelTabTwo.grid(row=0, column=0, padx=15, pady=15)
    idEpuletEntryTabTwo = tk.Entry(tab2)
    idEpuletEntryTabTwo.grid(row=0, column=1, padx=15, pady=15)

    # TAB 2 TERULET
    teruletLabelTabTwo = tk.Label(tab2, text='Terület', font=('bold', 10))
    teruletLabelTabTwo.grid(row=1, column=0, padx=15, pady=15)
    teruletEntryTabTwo = tk.Entry(tab2)
    teruletEntryTabTwo.grid(row=1, column=1, padx=15, pady=15)

    # TAB 2 CIM
    cimLabelTabTwo = tk.Label(tab2, text='Cím', font=('bold', 10))
    cimLabelTabTwo.grid(row=2, column=0, padx=15, pady=15)
    cimEntryTabTwo = tk.Entry(tab2)
    cimEntryTabTwo.grid(row=2, column=1, padx=15, pady=15)

    # TAB 2 EPITES EVE
    epitesEveLabelTabTwo = tk.Label(tab2, text='Építés éve', font=('bold', 10))
    epitesEveLabelTabTwo.grid(row=3, column=0, padx=15, pady=15)
    epitesEveEntryTabTwo = tk.Entry(tab2)
    epitesEveEntryTabTwo.grid(row=3, column=1, padx=15, pady=15)

    # TAB 2 AR
    arLabelTabTwo = tk.Label(tab2, text='Ár', font=('bold', 10))
    arLabelTabTwo.grid(row=4, column=0, padx=15, pady=15)
    arEntryTabTwo = tk.Entry(tab2)
    arEntryTabTwo.grid(row=4, column=1, padx=15, pady=15)

    # TAB 2 GOMBOK
    beszurButtonTabTwo = tk.Button(tab2, text="Beszúr", command=insertEpulet)
    beszurButtonTabTwo.place(x=30, y=335)

    frissitButtonTabTwo = tk.Button(tab2, text="Frissít", command=updateEpulet)
    frissitButtonTabTwo.place(x=100, y=335)

    lekerButtonTabTwo = tk.Button(tab2, text="Lekér", command=getEpulet)
    lekerButtonTabTwo.place(x=170, y=335)

    torolButtonTabTwo = tk.Button(tab2, text="Töröl", command=deleteEpulet)
    torolButtonTabTwo.place(x=240, y=335)

    listepulet = tk.Listbox(tab2, width=70, height=20)
    listepulet.place(x=300, y=30)

#######################################################################################################################

    # TAB 3
    # TAB 3 ID
    idTelekLabelTabThree = tk.Label(tab3, text='Azonosító', font=('bold', 10))
    idTelekLabelTabThree.grid(row=0, column=0, padx=15, pady=15)
    idTelekEntryTabThree = tk.Entry(tab3)
    idTelekEntryTabThree.grid(row=0, column=1, padx=15, pady=15)

    # TAB 3 TERULET
    teruletLabelTabThree = tk.Label(tab3, text='Terület', font=('bold', 10))
    teruletLabelTabThree.grid(row=1, column=0, padx=15, pady=15)
    teruletEntryTabThree = tk.Entry(tab3)
    teruletEntryTabThree.grid(row=1, column=1, padx=15, pady=15)

    # TAB 3 CIM
    cimLabelTabThree = tk.Label(tab3, text='Cím', font=('bold', 10))
    cimLabelTabThree.grid(row=2, column=0, padx=15, pady=15)
    cimEntryTabThree = tk.Entry(tab3)
    cimEntryTabThree.grid(row=2, column=1, padx=15, pady=15)

    # TAB 3 AR
    arLabelTabThree = tk.Label(tab3, text='Ár', font=('bold', 10))
    arLabelTabThree.grid(row=3, column=0, padx=15, pady=15)
    arEntryTabThree = tk.Entry(tab3)
    arEntryTabThree.grid(row=3, column=1, padx=15, pady=15)

    # TAB 3 GOMBOK
    beszurButtonTabThree = tk.Button(tab3, text="Beszúr", command=insertTelek)
    beszurButtonTabThree.place(x=30, y=335)

    frissitButtonTabThree = tk.Button(tab3, text="Frissít", command=updateTelek)
    frissitButtonTabThree.place(x=100, y=335)

    lekerButtonTabThree = tk.Button(tab3, text="Lekér", command=getTelek)
    lekerButtonTabThree.place(x=170, y=335)

    torolButtonTabThree = tk.Button(tab3, text="Töröl", command=deleteTelek)
    torolButtonTabThree.place(x=240, y=335)

    listtelek = tk.Listbox(tab3, width=70, height=20)
    listtelek.place(x=300, y=30)

#######################################################################################################################

    # TAB 4 GOMBOK

    epuletMaxAreaButtonTabFour = tk.Button(tab4, text="Max területű ház", command=epuletMaxArea)
    epuletMaxAreaButtonTabFour.place(x=30, y=30)

    epuletMinAreaButtonTabFour = tk.Button(tab4, text="Min területű ház", command=epuletMinArea)
    epuletMinAreaButtonTabFour.place(x=30, y=80)

    epuletMaxArButtonTabFour = tk.Button(tab4, text="Max árú ház", command=epuletMaxAr)
    epuletMaxArButtonTabFour.place(x=30, y=130)

    epuletMinArButtonTabFour = tk.Button(tab4, text="Min árú ház", command=epuletMinAr)
    epuletMinArButtonTabFour.place(x=30, y=180)

    atlagtolDragabbHazButtonTabFour = tk.Button(tab4, text="Átlagtól drágább ház", command=atlagtolDragabbHaz)
    atlagtolDragabbHazButtonTabFour.place(x=30, y=230)

    atlagtolOlcsobbHazButtonTabFour = tk.Button(tab4, text="Átlagtól olcsóbb ház", command=atlagtolOlcsobbHaz)
    atlagtolOlcsobbHazButtonTabFour.place(x=30, y=280)

    telekMaxAreaButtonTabFour = tk.Button(tab4, text="Max területű telek", command=telekMaxArea)
    telekMaxAreaButtonTabFour.place(x=250, y=30)

    telekMinAreaButtonTabFour = tk.Button(tab4, text="Min területű telek", command=telekMinArea)
    telekMinAreaButtonTabFour.place(x=250, y=80)

    telekMaxArButtonTabFour = tk.Button(tab4, text="Max árú telek", command=telekMaxAr)
    telekMaxArButtonTabFour.place(x=250, y=130)

    telekMinArButtonTabFour = tk.Button(tab4, text="Min árú telek", command=telekMinAr)
    telekMinArButtonTabFour.place(x=250, y=180)

    atlagtolDragabbTelekButtonTabFour = tk.Button(tab4, text="Átlagtól drágább telek", command=atlagtolDragabbTelek)
    atlagtolDragabbTelekButtonTabFour.place(x=250, y=230)

    atlagtolOlcsobbTelekButtonTabFour = tk.Button(tab4, text="Átlagtól olcsóbb telek", command=atlagtolOlcsobbTelek)
    atlagtolOlcsobbTelekButtonTabFour.place(x=250, y=280)

    legtobbPenzButtonTabFour = tk.Button(tab4, text="Legtöbb pénzű ember", command=legtobbPenz)
    legtobbPenzButtonTabFour.place(x=30, y=330)

    legkevesebbPenzButtonTabFour = tk.Button(tab4, text="Legkevesebb pénzű ember", command=legkevesebbPenz)
    legkevesebbPenzButtonTabFour.place(x=30, y=380)

    idVehetEEmberLabelTabFour = tk.Label(tab4, text='Azonosító', font=('bold', 10))
    idVehetEEmberLabelTabFour.place(x=30, y=450)
    idVehetEEmberEntryTabFour = tk.Entry(tab4)
    idVehetEEmberEntryTabFour.place(x=100, y=450)

    epuletetTudEVenniButtonTabFour = tk.Button(tab4, text="Megengedheti magának: épület", command=epuletetTudEVenni)
    epuletetTudEVenniButtonTabFour.place(x=250, y=445)

    telketTudEVenniButtonTabFour = tk.Button(tab4, text="Megengedheti magának: telek", command=telketTudEVenni)
    telketTudEVenniButtonTabFour.place(x=450, y=445)

    listker = tk.Listbox(tab4, width=70, height=20)
    listker.place(x=400, y=30)

#######################################################################################################################

    # TAB 5
    epuletkerIDLabelTabFive = tk.Label(tab5, text='Kereskedés azonosító', font=('bold', 10))
    epuletkerIDLabelTabFive.place(x=30, y=20)
    epuletkerIDEntryTabFive = tk.Entry(tab5)
    epuletkerIDEntryTabFive.place(x=200, y=20)

    emberIdeLabelTabFive = tk.Label(tab5, text='Ember azonosító', font=('bold', 10))
    emberIdeLabelTabFive.place(x=30, y=50)
    emberIdeEntryTabFive = tk.Entry(tab5)
    emberIdeEntryTabFive.place(x=200, y=50)

    epuletIdLabelTabFive = tk.Label(tab5, text='Épület azonosító', font=('bold', 10))
    epuletIdLabelTabFive.place(x=30, y=80)
    epuletIdEntryTabFive = tk.Entry(tab5)
    epuletIdEntryTabFive.place(x=200, y=80)

    telekkerIDLabelTabFive = tk.Label(tab5, text='Kereskedés azonosító', font=('bold', 10))
    telekkerIDLabelTabFive.place(x=500, y=20)
    telekkerIDEntryTabFive = tk.Entry(tab5)
    telekkerIDEntryTabFive.place(x=670, y=20)

    emberIdtLabelTabFive = tk.Label(tab5, text='Ember azonosító', font=('bold', 10))
    emberIdtLabelTabFive.place(x=500, y=50)
    emberIdtEntryTabFive = tk.Entry(tab5)
    emberIdtEntryTabFive.place(x=670, y=50)

    telekIdLabelTabFive = tk.Label(tab5, text='Telek azonosító', font=('bold', 10))
    telekIdLabelTabFive.place(x=500, y=80)
    telekIdEntryTabFive = tk.Entry(tab5)
    telekIdEntryTabFive.place(x=670, y=80)

    epuletkertorolLabelTabFive = tk.Label(tab5, text='Kereskedés azonosító', font=('bold', 10))
    epuletkertorolLabelTabFive.place(x=30, y=500)
    epuletkertorolEntryTabFive = tk.Entry(tab5)
    epuletkertorolEntryTabFive.place(x=200, y=500)

    telekkertorolLabelTabFive = tk.Label(tab5, text='Kereskedés azonosító', font=('bold', 10))
    telekkertorolLabelTabFive.place(x=500, y=500)
    telekkertorolEntryTabFive = tk.Entry(tab5)
    telekkertorolEntryTabFive.place(x=670, y=500)

    # TAB 5 GOMBOK

    hazatVeszButtonTabFive = tk.Button(tab5, text="Házat vesz", command=hazatVesz)
    hazatVeszButtonTabFive.place(x=30, y=110)

    telketVeszButtonTabFive = tk.Button(tab5, text="Telket vesz", command=telketVesz)
    telketVeszButtonTabFive.place(x=500, y=110)

    epuletKerTorlesButtonTabFive = tk.Button(tab5, text="Kereskedés törlése", command=epuletKerTorles)
    epuletKerTorlesButtonTabFive.place(x=30, y=540)

    telekKerTorlesButtonTabFive = tk.Button(tab5, text="Kereskedés törlése", command=telekKerTorles)
    telekKerTorlesButtonTabFive.place(x=500, y=540)

    listev = tk.Listbox(tab5, width=70, height=20)
    listev.place(x=30, y=150)

    listtv = tk.Listbox(tab5, width=70, height=20)
    listtv.place(x=500, y=150)

    root.mainloop()
