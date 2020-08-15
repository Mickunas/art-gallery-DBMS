'''
    File name: queries.py
    Author: Simonas Laurinavicius
    Email: simonas.laurinavicius@mif.stud.vu.lt
    Python Version: 3.7.6
    Purpose: 
        Queries module defines various SQL statements as functions, which are used for database management.
'''

# Third Party Modules
from psycopg2 import sql

# SELECT QUERIES

def author_select_by_fullname():
    query = """ SELECT Vardas || ' ' || Pavarde AS "Autorius", Pavadinimas, Kaina, Metai 
                    FROM Autorius JOIN Kurinys
                    ON Autorius.ID = Kurinys.Autorius_ID
                    WHERE Vardas = %s AND Pavarde = %s; """
    return query

def author_select_by_birth_year():
    query = """ SELECT Vardas || ' ' || Pavarde AS "Autorius", Gimimo_metai, Pavadinimas, Kaina, Metai 
                    FROM Autorius JOIN Kurinys
                    ON Autorius.ID = Kurinys.Autorius_ID
                    WHERE Gimimo_metai = %s; """
    return query

def author_select_by_death_year():
    query = """ SELECT Vardas || ' ' || Pavarde AS "Autorius", Mirties_metai, Pavadinimas, Kaina, Metai 
                    FROM Autorius JOIN Kurinys
                    ON Autorius.ID = Kurinys.Autorius_ID
                    WHERE Mirties_metai = %s; """
    return query

def select_by_id_name(table_name):
    query = sql.SQL(""" SELECT ID, Vardas || ' ' || Pavarde AS "Autorius" 
                        FROM {} 
                        ORDER BY ID; """).format(sql.Identifier(table_name))
    return query
    
# INSERT QUERIES
def insert_author():
    query = """ INSERT INTO Autorius(Vardas, Pavarde, Gimimo_metai, Mirties_metai, Aprasymas)
                    VALUES(%s, %s, %s, %s, %s);"""
    return query

# UPDATE QUERIES
def update_author_description():
    query = """ UPDATE Autorius
                    SET Aprasymas = %s
                    WHERE ID = %s; """
    return query

# DELETE QUERIES
def delete_author():
    query = """ DELETE FROM Autorius
                    WHERE ID = %s; """
    return query

# TRANSACTION QUERIES

def transfer_sales():
    query = """ UPDATE Pirkimas
                    SET Pirkejas_ID = %s
                    WHERE ID = %s; 

                DELETE FROM Pirkejas
                    WHERE ID2 = %s; """ 
    
    return query