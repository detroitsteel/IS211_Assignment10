#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Inserts data into the Pet DB."""

import sqlite3 as lite
import sys

def datainsert():
    """
    Function datainsert inserts the data within the variables into the Pets.db

    """
    con = None
    person = (
        (1, 'James', 'Smith', 41),
        (2, 'Diana', 'Greene', 23),
        (3, 'Sara', 'White', 27),
        (4, 'William', 'Gibson', 23))
    pet = (
        (1,'Rusty','Dalmation',4,1),
        (2,'Bella','AlaskanMalamute',3,0),
        (3,'Max','CockerSpaniel',1,0),
        (4,'Rocky','Beagle',7,0),
        (5,'Rufus','CockerSpaniel',1,0),
        (6,'Spot','Bloodhound',2,1))
    person_pet = (
        (1,1),
        (1,2),
        (2,3),
        (2,4),
        (3,5),
        (4,6))
    #try:
    con = lite.connect('pets.db')
    with con:
        cur = con.cursor()
        cur.executemany("INSERT INTO PERSON VALUES(?, ?, ?, ?);", person)
        cur.executemany("INSERT INTO PET VALUES(?, ?, ?, ?, ?);", pet)
        cur.executemany("INSERT INTO PERSON_PET VALUES(?, ?);", person_pet)
        last_row_id = cur.lastrowid
        print "The last Id of the inserted row is {}".format(last_row_id)
        return
    
if __name__ == '__main__':
    datainsert()
