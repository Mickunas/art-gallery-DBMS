#!/usr/bin/env python3

'''
    File name: db.py
    Author: Simonas Laurinavicius
    Email: simonas.laurinavicius@mif.stud.vu.lt
    Python Version: 3.7.6
    Purpose: 
        Simple database management program using Psycopg2 database adapter.
'''

# Standard modules
import os
import re

# Third Party modules
import psycopg2

# Local modules
from myparsers import parse_config
import interface
import queries

class MyDatabase:

    def __init__(self):
        config = parse_config()
        print('Connecting to the PostgreSQL database...')
        self.conn = psycopg2.connect(**config)

    # When a connection exits the with block, if no exception has been raised by the block, 
    # the transaction is committed. In case of exception the transaction is rolled back.
    def execute_select_query(self, query, values):
        with self.conn as conn:
            with conn.cursor() as cur:
                cur.execute(query, values)
                rows = cur.fetchall()
                self.print_results(rows)

        return rows

    def execute_query(self, query, values):
        with self.conn as conn:
            with conn.cursor() as cur:
                cur.execute(query, values)
    
    def print_results(self, rows):
        print("\nGRĄŽINTI REZULTATAI: ")
        print("\n")
        if not rows:
            print("Užklausa negražino rezultatų")
        else:
            for row in rows:
                print(row)
        print("\n")

    def close(self):
        (self.conn).close()
        print("Database connection closed")
    

def main():
    db = MyDatabase()

    while True:
        interface.print_option_table()
        option = input("Pasirinkite: ")
        while not re.match(r"^[1-6]$", option):
            option = input("Galimas pasirinkimas rėžiuose [1-6], pasirinkite: ")

        interface.MainOptions[option](db)


if __name__ == "__main__":
    main()
