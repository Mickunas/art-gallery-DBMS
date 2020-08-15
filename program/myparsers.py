'''
    File name: myparsers.py
    Author: Simonas Laurinavicius
    Email: simonas.laurinavicius@mif.stud.vu.lt
    Python Version: 3.7.6
    Purpose: 
        Myparsers module defines various parsers used throughout the program.
'''

# Standard modules
from configparser import ConfigParser


# Source [https://www.postgresqltutorial.com/postgresql-python/connect/]
def parse_config(filename='database.conf', section='postgresql'):
    # create a parser
    parser = ConfigParser()
    # read config file
    parser.read(filename)

    # get section, default to postgresql
    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception('Section {0} not found in the {1} file'.format(section, filename))

    return db

def parse_id_list(id_list):
    _min = min(id_list)
    _max = max(id_list)
    
    return (_min, _max)