CREATE SCHEMA Manager;

CREATE DOMAIN Manager.lt_tel_nr AS VARCHAR(255)
CHECK (
	VALUE ~ '^(3706|86)\d{7}$'
);

CREATE TABLE Manager.Pirkejas (
	ID				SERIAL,	
	Vardas			VARCHAR(255)	NOT NULL,
	Pavarde 		VARCHAR(255)	NOT NULL,
	Tel_Nr			lt_tel_nr	NOT NULL, 	
	El_Pastas 		VARCHAR(320),		
	Adresas 		VARCHAR(255),
	PRIMARY KEY (ID)
);

CREATE TABLE Manager.Autorius (
	ID				SERIAL,
	Vardas 			VARCHAR(255) 	NOT NULL,
	Pavarde 		VARCHAR(255) 	NOT NULL,
	Gimimo_metai 	SMALLINT		NOT NULL,
	Mirties_metai 	SMALLINT,
	Aprasymas 		VARCHAR(1400) 	NOT NULL
					DEFAULT 'Informacija ruošiama',
	PRIMARY KEY (ID)
);

CREATE TABLE Manager.Kurinys (
	ID 				SERIAL, 
	Pavadinimas 	VARCHAR(255)	NOT NULL,
	Kaina 			MONEY	NOT NULL
					CONSTRAINT Validi_kaina
						CHECK (Kaina > 0.0::MONEY),
	Nuolaida 		MONEY	NOT NULL
					DEFAULT 0.0::MONEY
					CONSTRAINT Validi_nuolaida
						CHECK (Nuolaida < Kaina),
	Metai			SMALLINT
					CONSTRAINT Validus_metai
						CHECK (Metai <= EXTRACT(YEAR FROM CURRENT_DATE) OR Metai IS NULL),
	Aprasymas 		VARCHAR(1400)	NOT NULL
					DEFAULT 'Informacija ruošiama',
	Tipas 			VARCHAR(255) 	NOT NULL,
	Aukstis_cm 		INTEGER			NOT NULL
					CONSTRAINT Validus_aukstis
						CHECK(Aukstis_cm > 0),
	Plotis_cm 		INTEGER 		NOT NULL
					CONSTRAINT Validus_plotis
						CHECK(Plotis_cm > 0),
	Gylis_cm 		INTEGER
					CONSTRAINT Validus_gylis
						CHECK(Gylis_cm > 0 OR Gylis_cm IS NULL),
	Autorius_ID 	INTEGER			NOT NULL,
	PRIMARY KEY (ID),
	FOREIGN KEY (Autorius_ID) REFERENCES Manager.Autorius ON DELETE RESTRICT ON UPDATE CASCADE
);

CREATE TABLE Manager.Pirkimas (
	ID				SERIAL,
	Data 			DATE 			NOT NULL,
	Kaina	 		MONEY 			NOT NULL
					CONSTRAINT	Validi_kaina
						CHECK (Kaina > 0.0::MONEY),
	Pirkejas_ID 	INTEGER			NOT NULL,
	Kurinys_ID 		INTEGER 		NOT NULL,
	PRIMARY KEY (ID),
	FOREIGN KEY(Pirkejas_ID) REFERENCES Manager.Pirkejas ON DELETE RESTRICT ON UPDATE CASCADE,
	FOREIGN KEY(Kurinys_ID) REFERENCES Manager.Kurinys	ON DELETE RESTRICT ON UPDATE CASCADE
);
