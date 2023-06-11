def selection_sort(data):
    n = len(data)

    for i in range(n - 1):
        max_index = i

        for j in range(i + 1, n):
            if data[j][2] > data[max_index][2]:
                max_index = j

        data[i], data[max_index] = data[max_index], data[i]


daftar_pemain = [
    ["Kylian Mbappe", "Paris Saint Germain", 40],
    ["Victor Osimhen", "Napoli", 28],
    ["Robert Lewandowski", "Barcelona", 33],
    ["Erling Haaland", "Manchester City", 52],
    ["Christopher Nkunku", "RB Leipzig", 22]
]

print("Daftar pemain sebelum diurutkan:")
print("No.\tNama Pemain\t\tKlub\t\tJumlah Gol")
for i, pemain in enumerate(daftar_pemain, start=1):
    print(f"{i}\t{pemain[0]}\t\t{pemain[1]}\t\t{pemain[2]}")

selection_sort(daftar_pemain)

print("\nDaftar pemain setelah diurutkan berdasarkan jumlah gol secara descending:")
print("No.\tNama Pemain\t\tKlub\t\tJumlah Gol")
for i, pemain in enumerate(daftar_pemain, start=1):
    print(f"{i}\t{pemain[0]}\t\t{pemain[1]}\t\t{pemain[2]}")
