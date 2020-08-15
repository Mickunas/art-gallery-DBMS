'''
    File name: interface.py
    Author: Simonas Laurinavicius
    Email: simonas.laurinavicius@mif.stud.vu.lt
    Python Version: 3.7.6
    Purpose: 
        Interface module defines various functions used for UI.
'''

# Standard modules
import sys
import re

# Local modules
import queries
from myparsers import parse_id_list

def print_option_table():
    print("Funkcijos: ")
    print("1 - Rasti autorių ir jo kūrinius")
    print("2 - Įvesti naują autorių")
    print("3 - Atnaujinti autoriaus aprašymą")
    print("4 - Šalinti autorių")
    print("5 - Pervesti pirkėjo pirkimus")
    print("6 - Išeiti")

def print_find_author():
    print("Pagal ką ieškosite autoriaus: ")
    print("1 - Pagal vardą ir pavardę")
    print("2 - Pagal gimimo metus")
    print("3 - Pagal mirties metus")
    print("4 - Grįžti atgal")

def option_find_author(db):
    print_find_author()
    option = input("Pasirinkite: ")
    while not re.match(r"^[1-4]$", option):
        option = input("Galimas pasirinkimas rėžiuose [1-4], pasirinkite: ")
    AuthorOptions[option](db)

def find_by_fullname(db):
    fullname = input("Įveskite vardą ir pavardę atskirtus tarpais: ")

    while not re.match(r"^[a-zA-Z]+ [a-zA-Z]+$", fullname):
        fullname = input("Įveskite vardą ir pavardę atskirtus tarpais: ")
    values = fullname.split(' ')
    query = queries.author_select_by_fullname()

    db.execute_select_query(query, values)

def find_by_birth_year(db):
    birth_year = input("Įveskite autoriaus gimimo metus: ")
    
    while not re.match(r"^[1-2][0-9]{3}$", birth_year):
        birth_year = input("Įveskite autoriaus gimimo metus: ")
    # For positional variables binding, the second argument must always be a sequence, 
    # even if it contains a single variable:
    birth_year = (birth_year, )
    query = queries.author_select_by_birth_year()

    db.execute_select_query(query, birth_year)

def find_by_death_year(db):
    death_year = input("Įveskite autoriaus mirties metus: ")
    while not re.match(r"^[1-2][0-9]{3}$", death_year):
        death_year = input("Įveskite autoriaus gimimo metus: ")
    # For positional variables binding, the second argument must always be a sequence, 
    # even if it contains a single variable:
    death_year = (death_year, )
    query = queries.author_select_by_death_year()

    db.execute_select_query(query, death_year)

def return_to_main_menu(db):
    return

def option_insert_author(db):
    firstname = input("Įveskite autoriaus vardą: ")
    while not re.match(r"^[a-zA-Z]+$", firstname):
        firstname = input("Įveskite autoriaus vardą: ")
        
    lastname = input("Įveskite autoriaus pavardę: ")
    while not re.match(r"^[a-zA-Z]+$", lastname):
        lastname = input("Įveskite autoriaus pavardę: ")

    birth_year = input("Įveskite gimimo metus: ")
    while not re.match(r"^[1-2][0-9]{3}$", birth_year):
        birth_year = input("Įveskite gimimo metus: ")
    
    death_year = input("Įveskite mirties metus (jei nėra, spauskite enter): ")
    while not re.match(r"^[1-2][0-9]{3}$", death_year) and death_year != '':
        death_year = input("Įveskite mirties metus (jei nėra, spauskite enter): ")

    if death_year == '':
        death_year = None

    description = input("Įveskite aprašymą, (jei nėra, spauskite enter): ")
    # Maximum length of a description - 1400 characters
    while not re.match(r"^.{0,1400}$", description):
        description = input("Įveskite mirties metus (jei nėra, spauskite enter): ")
    if description == '':
        description = 'Informacija ruošiama' # DEFAULT value

    values = (firstname, lastname, birth_year, death_year, description)
    query = queries.insert_author()

    db.execute_query(query, values)

def option_update_author_description(db):
    id_list = print_ID_name_table(db, "autorius")
    (min_id, max_id) = parse_id_list(id_list)
    author_id = input("Pasirinkite autoriaus ID: ")
    while not re.match(rf"^[{min_id}-{max_id}]$", author_id):
        author_id = input(f"Galimas pasirinkimas rėžiuose [{min_id}-{max_id}], pasirinkite: ")

    description = input("Įveskite autoriaus aprašymą: ")
    values = (description, author_id)
    query = queries.update_author_description()

    db.execute_query(query, values)
    
def print_ID_name_table(db, table_name):
    print("ID lentelė")
    query = queries.select_by_id_name(table_name)

    id_list = []
    rows = db.execute_select_query(query, None)
    for row in rows:
        id_list.append(row[0])

    return id_list

def option_remove_author(db):
    id_list = print_ID_name_table(db, "autorius")
    (min_id, max_id) = parse_id_list(id_list)
    author_id = input("Pasirinkite norimo pašalinti autoriaus ID: ")
    while not re.match(rf"^[{min_id}-{max_id}]$", author_id):
        author_id = input(f"Galimas pasirinkimas rėžiuose [{min_id}-{max_id}], pasirinkite: ")

    author_id = (author_id, )
    query = queries.delete_author()

    db.execute_query(query, author_id)

def option_transfer_sales(db):
    id_list = print_ID_name_table(db, "pirkejas")
    (min_id, max_id) = parse_id_list(id_list)
    remove_id = input("Pasirinkite pirkėją, kurį norite pašalinti: ")
    while not re.match(rf"^[{min_id}-{max_id}]$", remove_id):
        remove_id = input(f"Galimas pasirinkimas rėžiuose [{min_id}-{max_id}], pasirinkite: ")

    transfer_id = input("Pasirinkite pirkėją, kuriam norite pervesti pirkimus: ")
    while not re.match(rf"^[{min_id}-{max_id}]$", transfer_id) or transfer_id == remove_id:
        transfer_id = input(f"Galimas pasirinkimas rėžiuose [{min_id}-{max_id}], bei negalima pasirinkti to pačio ID!. Pasirinkite: ")

    values = (transfer_id, remove_id, remove_id)
    query = queries.transfer_sales()

    db.execute_query(query, values)

def option_exit_program(db):
    db.close()
    sys.exit()
    
MainOptions = {
    '1': option_find_author,
    '2': option_insert_author,
    '3': option_update_author_description,
    '4': option_remove_author,
    '5': option_transfer_sales,
    '6': option_exit_program
}

AuthorOptions = {
    '1': find_by_fullname,
    '2': find_by_birth_year,
    '3': find_by_death_year,
    '4': return_to_main_menu
}
