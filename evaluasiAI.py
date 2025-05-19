import pandas as pd
import re

# Fungsi normalisasi teks
def normalize(text):
    text = text.lower()
    text = re.sub(r'\b(a|an|the)\b', ' ', text)
    text = re.sub(r'[^\w\s]', '', text)
    text = ' '.join(text.split())
    return text

# Fungsi evaluasi exact match
def exact_match(pred, ref):
    return int(normalize(pred) == normalize(ref))

# Baca CSV
df = pd.read_csv("data_jawaban - Sheet1.csv")

# Normalisasi nama kolom
df.columns = [col.strip().lower().replace(' ', '_') for col in df.columns]
print(df.columns.tolist())  # pastikan ini muncul: 'jawaban_ai', 'jawaban_referensi'

# Hitung exact match
df["exact_match"] = df.apply(
    lambda row: exact_match(row["jawaban_ai"], row["jawaban_referensi"]),
    axis=1
)

# Hitung akurasi
em_accuracy = df["exact_match"].mean() * 100

# Tampilkan hasil
print(df[["id", "tipe_skenario", "pertanyaan", "jawaban_ai", "jawaban_referensi", "exact_match"]])
print(f"\nExact Match Accuracy: {em_accuracy:.2f}%")
