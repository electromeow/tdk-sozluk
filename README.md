# TDK-Sözlük
En iyi TDK sözlük arama kütüphanesi.\
Best TDK dict. search library.
 
### Yükleme / Install:
```shell
$ pip install tdk-sozluk
```

### Gereksinimler / Requirements:
Python 3.3+\
pip

### Temel Kullanım / Basic Usage
```python
import tdk
sonuclar = tdk.ara("yüzmek")
for s in sonuclar:
    for i in s.anlamlar():
        print(i.anlam())
```
Output / Çıktı:
```
Kol, bacak, yüzgeç vb. organların özel hareketleriyle su yüzeyinde veya su içinde ilerlemek, durmak
Yüzme sporu yapmak
Bir sıvının yüzeyinde batmadan durmak
Herhangi bir durumun en aşırı derecesinde olmak
Dalgalanmak
Herhangi bir şeyle üzeri kaplanmak, bir şeye bulanmak
Derisini çıkarmak, derisini soymak
Çok para istemek
```
### Dokümantasyon / Documentation
Dokümanlar henüz hazır değil. Hazır olunca burada olacak.\
Docs are not ready yet. They will be here when they're completed.\
\
Ama kullanımla ilgili bilgi için kaynak kodlarındaki yorum satırlarını okuyabilirsiniz.\
But you can read the explanations in the source code.
### Katkı Yap / Contribute
Katkı yapmak için bu projeyi forklayın, geliştirin ve bir pull request ekleyin.\
To contribute this project: Fork, develop and submit a pull request.
### LICENSE
This project is distributed under MIT License.