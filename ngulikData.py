import pandas as pd
import matplotlib.pyplot as plt


# data
data = pd.DataFrame({
    'nama' : ['aldi', 'egel', 'purnama', 'rudi', 'toni', 'budi'],
    'usia' : [20, 21, 22, 23, 24, 25],
    'pendidikan' : ['S1', 'S2', 'S3', 'S1', 'S2', 'S3'],
    'status' : ['belum menikah', 'menikah', 'belum menikah', 'menikah', 'belum menikah', 'menikah'],
    'pendapatan' : [1000000, 2000000, 3000000, 1500000, 2500000, 3500000]
})



# visualisasi
# fig, ax = plt.subplots()
# ax.bar(data['pendidikan'], data['pendapatan'], color=color)
# ax.set_xlabel('Pendidikan')
# ax.set_ylabel('pendapatan')
# ax.set_title('Pendapatan Berdasarakan Pendidikan')
# plt.show()

# visuliasi dengan seaborn
import seaborn as sns
sns.barplot(data, x='pendidikan', y='pendapatan',hue='pendidikan')
plt.show()
