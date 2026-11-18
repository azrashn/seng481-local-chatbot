# SENG 481 – P02: Yerel LLM Chatbot

Açık kaynak bir büyük dil modelini (LLM) **tamamen kendi bilgisayarımızda** çalıştıran basit bir sohbet uygulaması. Model [Ollama](https://ollama.com) ile yerelde çalışır; internet bağlantısı veya ücretli API gerekmez, veriler bilgisayardan dışarı çıkmaz.

## Ekip

| Üye | Sorumluluk |
|---|---|
| Esma Azra Şahin | LLM entegrasyonu, model seçimi ve karşılaştırma, prompt tasarımı |
| Sıla Yıldırım | Backend: sohbet geçmişi, veritabanı |
| Fatih Oğuz Kaya | Frontend: arayüz tasarımı |
| Belis Özçelik | RAG (belge tabanlı soru-cevap), test, dokümantasyon |

## Mimari

```
[Streamlit arayüzü]  →  [Python uygulama katmanı]  →  [Ollama + yerel LLM]
                         sohbet geçmişi, prompt        localhost:11434
```

## Kurulum

1. **Ollama'yı kurun:** https://ollama.com/download
2. **Bir model indirin** (8 GB RAM için önerilen):
   ```bash
   ollama pull llama3.2:3b
   ```
   Daha güçlü bilgisayarlar için `qwen3:8b` veya `gemma3:4b` de denenebilir.
3. **Python bağımlılıklarını kurun** (Python 3.10+):
   ```bash
   python -m venv .venv
   # Windows: .venv\Scripts\activate   |   macOS/Linux: source .venv/bin/activate
   pip install -r requirements.txt
   ```
4. **Uygulamayı çalıştırın:**
   ```bash
   streamlit run app.py
   ```
   Tarayıcıda `http://localhost:8501` açılır.

## Özellikler

- [x] Yerel model ile sohbet
- [x] Sohbet geçmişi (bağlamı hatırlama)
- [x] Cevabın akarak gelmesi (streaming)
- [x] Model seçimi ve düzenlenebilir sistem promptu
- [ ] Sohbetleri kaydetme (SQLite)
- [ ] PDF yükleyip belgeye göre soru sorma (RAG)
- [ ] Model karşılaştırma raporu

## Çalışma düzeni

- Her iş için bir **issue** açılır ve kişiye atanır.
- `main` dalına doğrudan push yapılmaz; her issue için ayrı dal açılır:
  `feature/<issue-no>-kisa-aciklama` (ör. `feature/7-sqlite-kayit`)
- İş bitince **Pull Request** açılır, en az bir ekip arkadaşı inceler, sonra birleştirilir.
- Commit mesajlarında issue numarası geçer: `Sohbet kaydı eklendi (#7)`

## Lisans

MIT
