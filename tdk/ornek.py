from tdk.yazar import yazar

class ornek:

    def __init__(self, response):
        self.sozluk=response

    # ornek objesinin içindeki örnek cümleyi döndürür. Yoksa None döndürür.
    # Returns the example sentence of the object itself as str. Returns None if there isn't.
    def ornek(self):
        try:
            ornek = self.sozluk["ornek"]
        except KeyError:
            return None
        if ornek == "" or ornek.isspace():
            return None
        else:
            return ornek

    # Örnek cümlenin yazarını yazar objesi olarak döndürür. Yazar yoksa None döndürür.
    # Returns the author of the example sentence as an object of class yazar. If there isn't returns None.
    def yazar(self):

        if self.sozluk["yazar_id"]==0:
            return None
        else:
            return yazar(self.sozluk["yazar"]["tam_adi"],self.sozluk["yazar"]["kisa_adi"])
