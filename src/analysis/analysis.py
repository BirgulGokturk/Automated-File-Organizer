import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Analiz edilecek örnek veriler
data = {
    'Tur': ['Film', 'Film', 'Dizi', 'Film', 'Dizi', 'Film', 'Dizi', 'Film', 'Dizi', 'Film'],
    'Yil': [2020, 2019, 2021, 2020, 2018, 2021, 2020, 2019, 2022, 2021]
}

df = pd.DataFrame(data)

# Grafik oluşturma
plt.figure(figsize=(10,6))
sns.set_theme(style="darkgrid")
ax = sns.countplot(x='Tur', data=df, palette='magma')

plt.title('İçerik Türü Dağılım Analizi')
plt.xlabel('Kategori')
plt.ylabel('Adet')

print("Grafik hazırlanıyor... Lütfen bekleyin.")
plt.show()