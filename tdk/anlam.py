from ornek import ornek

class anlam:

    def __init__(self, response):
        self.sozluk=response

    # Anlamın fiil olup olmadığını döndürür. Dönüş tipi: bool, None veya str("UnknownError")
    # Returns the meaning is a verb. Return type: bool, None or str("UnknownError")
    def fiilMi(self):
        try:
            fiilmi=self.sozluk["fiil"]
        except KeyError:
            return None
        if fiilmi==0:
            return False
        elif fiilmi==1:
            return True
        else:
            return "UnknownError"

    # Anlam onjesinin içindeki anlamı str olarak döndürür.
    # Returns the meaning of the anlam object itself as str.
    def anlam(self):
        return self.sozluk["anlam"]

    # Anlama ait örnekleri ornek sınıfından objelerden oluşan bir tuple olarak veya None olarak döndürür.
    # Returns the examples of the meaning as a tuple of objects of class ornek. Returns None if there isn't.
    def ornekler(self):
        ornklist=[]
        try:
            ornkler=self.sozluk["orneklerListe"]
        except KeyError:
            return None
        for ornk in ornkler:
            ornklist.append(ornek(ornk))
        if ornklist==[]:
            return None
        else:
            return tuple(ornklist)

    # Anlamın türünü str olarak döndürür.
    # Returns the type of the word as str.
    def tur(self):
        return self.sozluk["ozelliklerListe"]["tam_adi"]

    # Anlamın türünün kısaltılmış adını str olarak döndürür.
    # Returns the acronymic name of the type of the word as str.
    def tur_kisaltmasi(self):
        return self.sozluk["ozelliklerListe"]["kisa_adi"]

