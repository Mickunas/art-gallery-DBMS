CREATE VIEW Grafika
    AS SELECT * FROM Manager.Kurinys
        WHERE Kurinys.Tipas = 'Grafika';

CREATE VIEW Pirkimai_svarbi_info
    AS SELECT Pirkejas.Vardas || ' ' || Pirkejas.Pavarde AS "Pirkėjas", Pirkimas.data AS "Pirkimo data", Pirkimas.kaina AS "Pirkimo kaina", Kurinys.Pavadinimas AS "Kūrinio pavadinimas"
        FROM (Manager.Pirkimas JOIN Manager.Kurinys ON Pirkimas.Kurinys_ID = Kurinys.ID)
                                JOIN Manager.Pirkejas ON Pirkimas.Pirkejas_ID = Pirkejas.ID;

CREATE MATERIALIZED VIEW Vasario_pirkimai
    AS SELECT *
        FROM Manager.Pirkimas
            WHERE EXTRACT(MONTH FROM Pirkimas.Data) = 2
    WITH NO DATA;