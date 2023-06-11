def bubble_sort(data):
    n = len(data)

    for i in range(n - 1):
        swapped = False

        for j in range(n - i - 1):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
                swapped = True

        if not swapped:
            break


nilai_ujian = [78, 65, 90, 82, 70]

print("Daftar nilai sebelum diurutkan:", nilai_ujian)

bubble_sort(nilai_ujian)

print("Daftar nilai setelah diurutkan:", nilai_ujian)
