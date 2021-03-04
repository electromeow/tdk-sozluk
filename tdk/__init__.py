import json
from sonuc import sonuc
from urllib.request import urlopen
from urllib.request import Request
from urllib.parse import quote

# Girdiğiniz kelimeyi TDK'nın sozlük parametresi olarak girdiğiniz sözlükte arar ve sonuc sınıfından değer döndürür.
# Searchs the word you entered as kelime in TDK's dictionary you entered as sozluk. Return an object of class sonuc.
def ara(kelime, sozluk="gts"):
	req=Request(f"https://sozluk.gov.tr/{sozluk.lower().strip()}?ara={quote(kelime)}",headers={"User-Agent":"Mozilla/5.0"})
	res=urlopen(req)
	resultDict=json.loads(res.read())
	donus=[]
	for rslt in resultDict:
		donus.append(sonuc(rslt))
	return tuple(donus)

