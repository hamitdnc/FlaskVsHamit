### Yüklenecek extension'lar
- `pip install -r requirements.txt`

### Flask Migrate Komutları
- `flask db init` diyerek migration için database hazırlar
- `flask db migrate -m "Mesajiniz" ` diyerek tablo olustur.
- `flask db upgrade` diyerek models.py icindeki modelleri tabloya dönüştür.
