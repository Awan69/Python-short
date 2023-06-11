def bubble_sort(data):
    n = len(data)

    for i in range(n - 1):
        swapped = False

        for j in range(n - i - 1):
            if data[j][2] > data[j + 1][2]:
                data[j], data[j + 1] = data[j + 1], data[j]
                swapped = True

        if not swapped:
            break


daftar_buku = [
    ["Harry Potter and the Sorcerer's Stone", "J.K. Rowling", 320],
    ["To Kill a Mockingbird", "Harper Lee", 281],
    ["The Great Gatsby", "F. Scott Fitzgerald", 180],
    ["Pride and Prejudice", "Jane Austen", 432],
    ["1984", "George Orwell", 328]
]

print("Daftar buku sebelum diurutkan:")
print("No.\tJudul Buku\t\t\t\tPenulis\t\t\tJumlah Halaman")
for i, buku in enumerate(daftar_buku, start=1):
    print(f"{i}\t{buku[0]}\t\t\t\t{buku[1]}\t\t\t{buku[2]}")

bubble_sort(daftar_buku)

print("\nDaftar buku setelah diurutkan berdasarkan jumlah halaman secara ascending:")
print("No.\tJudul Buku\t\t\t\tPenulis\t\t\tJumlah Halaman")
for i, buku in enumerate(daftar_buku, start=1):
    print(f"{i}\t{buku[0]}\t\t\t\t{buku[1]}\t\t\t{buku[2]}")
