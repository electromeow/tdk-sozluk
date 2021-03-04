class yazar:
    def __init__(self, tam_adi, kisa_adi):
        self.tamAdi=tam_adi
        self.kisaAdi=kisa_adi

    # Yazarın tam adını str olarak döndürür.
    # Returns the full name of the author as str.
    def tamAd(self):
        return self.tamAdi

    # Yazarın kısaltılmış ismini str olarak döndürür.
    # Returns the acronymic name of the author.
    def kisaAd(self):
        return self.kisaAdi
