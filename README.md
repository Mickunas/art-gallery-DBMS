# Database and a client interface for an Art Gallery, using PSQL, Python and psycopg2.
Made as a study project for my Databases class at Vilnius University.
Goal of the project was to put theoretical knowledge into practice by making your own database from scratch.

Development was split into several parts:
  * ER and Retalional Schema models for the database.
  * SQL sentences to create the structure of the database: tables, views, triggers and indexes.
  * Client interface for a database in a programming language of your choice.
  
Chose Art Gallery as I was familiar with this kind of bussiness and could think of more real life cases while designing the database.

It's important to note that the language used for database structures and client interface is in Lithuanian.

## Table of contents
* [Requirements](#requirements)
* [Setup](#setup)
* [Run](#run)
* [License](#license)
* [References](#references)

## Requirements
Project requires:
* Python: tested with python3 only, also shebang line specifies python3 as an interpreter.
* psycopg2
 
## Setup
To install Python go to [Python Downloads](https://www.python.org/downloads/)  
To install psycopg2 module go to [Install psycopg2](https://pypi.org/project/psycopg2/)

## Run
#### To create a database
Assuming you've navigated to **sql** folder locally and from there connected to PSQL with a user that has CREATEDB privilege, run: 
```sh
\i create_db.sql
```
#### To start a client interface
Assuming you have your PSQL server up and running, navigate to **program** folder locally and run:
```sh
python3 db.py
```
Using shebang line:
```sh
sudo chmod +x db.py
./db.py
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details

## References
* [Duomenų Bazių Valdymo Sistemos](http://klevas.mif.vu.lt/~baronas/dbvs/book/index.htm)
