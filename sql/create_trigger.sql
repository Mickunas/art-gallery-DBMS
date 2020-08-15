CREATE FUNCTION uzpildyti_nuolaida()
    RETURNS TRIGGER AS
    $$BEGIN

    UPDATE Manager.Kurinys
        SET Nuolaida = (Kurinys.Kaina - NEW.Kaina)
        WHERE Kurinys.ID = NEW.Kurinys_ID;

    RETURN NEW;
    
    END;$$
    LANGUAGE PLPGSQL;

CREATE TRIGGER NuolaidosUzpildymas
AFTER INSERT ON Manager.Pirkimas
FOR EACH ROW
EXECUTE PROCEDURE uzpildyti_nuolaida();
