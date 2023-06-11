def selection_sort(data):
    n = len(data)

    for i in range(n - 1):
        min_index = i

        for j in range(i + 1, n):
            if data[j] < data[min_index]:
                min_index = j

        data[i], data[min_index] = data[min_index], data[i]


angka = [9, 5, 3, 8, 2]

print("Daftar angka sebelum diurutkan:", angka)

selection_sort(angka)

print("Daftar angka setelah diurutkan:", angka)
