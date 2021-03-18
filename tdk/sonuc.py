from tdk.anlam import anlam
from tdk.atasozu import atasozu


class sonuc:

    def __init__(self, response):
        self.sozluk = response


    # Elinizdeki sonucun çoğul olup olmadığını döndürür. Dönüş türü: bool, None veya str("UnknownError")
    # Returns if your result is plural. Return type: bool, None or str("UnknownError")
    def cogulMu(self):
        try:
            cogul=self.sozluk["cogul_mu"]
        except KeyError:
            return None
        if int(cogul)==0:
            return False
        elif int(cogul)==1:
            return True
        else:
            return "UnknownError"


    # Elinizdeki sonucun özel isim olup olmadığını döndürür. Dönüş tipi: bool, None veya str("UnknownError")
    # Returns if your result is proper. Return type: bool, None or str("UnknownError")
    def ozelMi(self):
        try:
            ozel=self.sozluk["ozel_mi"]
        except KeyError:
            return None
        if int(ozel)==0:
            return False
        elif int(ozel)==1:
            return True
        else:
            return "UnknownError"


    # Sonucun içindeki anlamları anlam sınıfında objelerden bir tuple olarak döndürür. Bir şey bulamazsa None döndürür.
    # Returns the meanings in the result as a tuple of objects of class anlam. If there isn't a meaning, returns None.
    def anlamlar(self):
        try:
            rawAnlamlar=self.sozluk["anlamlarListe"]
        except KeyError:
            return None
        anlamList = []
        for birAnlam in rawAnlamlar:
            anlamList.append(anlam(birAnlam))
        if anlamList==[]:
            return None
        else:
            return tuple(anlamList)


    # Sonucun içindeki atasözlerini bulur ve atasozu objelerinden oluşan bir tuple olarak döndürür. Eğer atasözü yoksa None Döndürür.
    # Return the adages in the result as a tuple of objects of class atasozu. If there isn't, returns None.
    def atasozleri(self):
        try:
            atasoz=self.sozluk["atasozu"]
        except KeyError:
            return None
        asList = []
        for birAs in atasoz:
            asList.append(atasozu(birAs["on_taki"],birAs["madde"]))
        if asList==[]:
            return None
        else:
            return tuple(asList)


    # Sonucun köken lisanını ve köken kelimesini verir. Dönüş tipi: str veya None
    # Returns the origin language and the origin word in origin language. Return type: str or None
    def lisan(self):
        try:
            lisan = self.sozluk["lisan"]
        except KeyError:
            return None
        if lisan=="" or lisan.isspace():
            return None
        else:
            return lisan


    # Sonucun ön takısını döndürür. Dönüş tipi: str veya None
    # Returns the prefix of the word. Return type: str or None
    def ontaki(self):
        try:
            onTaki=self.sozluk["on_taki"]
        except KeyError:
            return None
        if onTaki=="" or onTaki.isspace():
            return None
        else:
            return onTaki


    # Sonucun takısını döndürür. Dönüş tipi: str veya None
    # Returns the affix of the result. Return type: str or None
    def taki(self):
        try:
            taki=self.sozluk["taki"]
        except KeyError:
            return None
        if taki=="" or taki.isspace():
            return None
        else:
            return taki
