-- Data for Pirkejas table
INSERT INTO Manager.Pirkejas VALUES(DEFAULT, 'Vytautas', 'Rinkevičius', '868796447', 'vytautas@gmail.com', 'Gedimino Pr. 15-4');
INSERT INTO Manager.Pirkejas VALUES(DEFAULT, 'Ričardas', 'Gausas', '37069745915', 'ricardas@gmail.com', 'Didžioji g. 6');
INSERT INTO Manager.Pirkejas VALUES(DEFAULT, 'Joana', 'Kepler', '868687901', 'joana@hotmail.com', 'Miesto g. 13-7');
INSERT INTO Manager.Pirkejas VALUES(DEFAULT, 'Martynas', 'Kvazevičius', '861234567', 'martynas@home.lt', 'Užusienio g. 34');

-- Data for Autorius table
INSERT INTO Manager.Autorius VALUES(DEFAULT, 'Samuel', 'Bak', '1933', NULL, DEFAULT);
INSERT INTO Manager.Autorius VALUES(DEFAULT, 'Vytautas', 'Kasiulis', '1918', '1995', DEFAULT);
INSERT INTO Manager.Autorius VALUES(DEFAULT, 'Pranas', 'Gailius', '1928', '2015', DEFAULT);

-- Data for Kurinys table
INSERT INTO Manager.Kurinys VALUES(DEFAULT, 'Grupinė nuotrauka su Mėlynu Angelu', 399.00, DEFAULT, 1973, DEFAULT, 'Grafika', 65, 50, NULL, 1);
INSERT INTO Manager.Kurinys VALUES(DEFAULT, 'Still Life With Pears and bottle', 6000.00, 350.00, 1978, DEFAULT, 'Tapyba', 60, 60, NULL, 1);

INSERT INTO Manager.Kurinys VALUES(DEFAULT, 'Jaunuolis su gitara', 6000.00, DEFAULT, NULL, DEFAULT, 'Tapyba', 73, 60, NULL, 2);
INSERT INTO Manager.Kurinys VALUES(DEFAULT, 'Mulen Ružas', 3500.00, DEFAULT, NULL, DEFAULT, 'Grafika', 50, 65, NULL, 2);

INSERT INTO Manager.Kurinys VALUES(DEFAULT, 'ADRET II', 4500.00, DEFAULT, 1995, DEFAULT, 'Tapyba', 120, 111, NULL, 3);
INSERT INTO Manager.Kurinys VALUES(DEFAULT, 'Dvi Nuogalės', 4000.00, 200.00, 1998, DEFAULT, 'Tapyba', 77, 97, NULL, 3);

-- Data for Pirkimas table
INSERT INTO Manager.Pirkimas VALUES(DEFAULT, '2020-02-05', 5650.00, 1, 2);
INSERT INTO Manager.Pirkimas VALUES(DEFAULT, '2020-02-21', 3800.00, 3, 6);
