#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Queries the Pet DB."""

import sqlite3 as lite
import sys

def querypetdata():
    """
    Function querypetdata queries data from PETS.DB and allows for the user to
    lookup person ID
    Example:
        Type the person's id in which to search. Enter -1 to end:1
        James Smith, 41 years old owned Rusty, a Dalmation, that was 4 years
        old.
        James Smith, 41 years old owned Bella, a AlaskanMalamute, that was 3
        years old.
        Type the person's id in which to search. Enter -1 to end:
    """
    con = None
    con = lite.connect('pets.db')
    personid = 1
    with con:
        personid = input('Type the person\'s id in which to search. Enter -1 to end:')
        while personid >-1:
            personid = int(personid)
            cur = con.cursor() 
            cur.execute("SELECT p.*, PET.* FROM PERSON AS p JOIN PERSON_PET "
                        "AS pp ON p.ID = pp.person_id JOIN PET ON pp.pet_id"
                        "= PET.id WHERE p.id = :pyid", {"pyid": personid})
            rows = cur.fetchall()
            if rows:
                for row in rows:
                    outp = ('%s %s, %i years old owned %s, a %s, that was %s '
                    'years old.' % (row[1], row[2], row[3], row[5], row[6], row[7]))
                    print outp
            else:
                print "\nPerson ID Not Found, Please Try Again.\n"
            personid = input('Type the person\'s id in which to search. Enter -1 to end:')
        return

if __name__ == '__main__':
    querypetdata()
