def bubble_sort(data):
    n = len(data)

    for i in range(n - 1):
        swapped = False

        for j in range(n - i - 1):
            if data[j] < data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
                swapped = True

        if not swapped:
            break


angka = [42, 19, 33, 8, 55]

print("Daftar angka sebelum diurutkan:", angka)

bubble_sort(angka)

print("Daftar angka setelah diurutkan secara descending:", angka)
