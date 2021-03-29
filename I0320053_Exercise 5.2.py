#Penggunaan if untuk dua kasus
#Menginput tahun ajaran
tahun_ajaran = int(input('Masukkan tahun ajaran: '))

#memeriksa tahun
if tahun_ajaran % 4 == 0:
    print(' %d adalah tahun ajaran genap' %tahun_ajaran)
else :
    print(' %d adalah tahun ajaran ganjil' %tahun_ajaran)
print ()