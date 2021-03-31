#Program untuk Grading Nilai Mahasiswa

print("Nilai Mahasiswa")

nama = input("Masukkan nama mahasiswa : ")

def CekSkorNilai (nilai):
    if nilai >= 85 :
        print("Hallo,{}".format(nama),"nilai anda setelah dikonversi adalah A")
        print("Kamu luar biasa, pertahankan prestasimu")
    elif nilai >= 80 :
        print("Hallo,{}".format(nama),"nilai anda setelah dikonversi adalah A-")
        print("Pertahankan prestasimu")
    elif nilai >= 75 :
        print("Hallo,{}".format(nama),"nilai anda setelah dikonversi adalah B+")
        print("Tetap semangat")
    elif nilai >= 70 :
        print("Hallo,{}".format(nama),"nilai anda setelah dikonversi adalah B")
        print ("Jangan pantang menyerah")
    elif nilai >= 65 :
        print("Hallo,{}".format(nama),"nilai anda setelah dikonversi adalah C+")
        print("Kamu pasti bisa")
    elif nilai >= 60 :
        print("Hallo,{}".format(nama),"nilai anda setelah dikonversi adalah C")
        print("Ayo giatkan lagi belajarmu")
    elif nilai < 60 :
        print ("Hallo,{}".format(nama),"nilai anda setelah dikonversi adalah E")
        print ("Jangan menyerah, tingkatkan lagi belajarmu")
    else:
        print ("Nilai tidak valid")

nilai_akhir = float(input("Masukkan nilai Anda : "))
CekSkorNilai(nilai_akhir)