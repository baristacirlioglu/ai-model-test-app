# AI Model Test Uygulaması

Bu projede Python ile bir AI modeli (DecisionTreeClassifier) test edilip, sonuçları Node.js ile API üzerinden sunulmakta ve React frontend ile kullanıcıya gösterilmektedir.

## Klasör Yapısı
- `test_model.py`: Python model test kodu
- `results.json`: Test sonuçları (otomatik üretilir)
- `ai-api/`: Node.js backend API
- `ai-frontend/`: React frontend uygulaması

## Başlatma
1. `test_model.py` dosyasını çalıştırarak `results.json` oluştur
2. `ai-api/server.js` ile API'yi başlat (`node server.js`)
3. `ai-frontend/` klasöründe `npm start` ile frontend'i başlat
