#Program untuk menyapa pengunjung

print("Hotel Transylvania")
print("-----------------------------------")
nama_tamu = input("Masukkan nama anda : ")
gender = input ("Jenis kelamin : ")

if (gender == "perempuan"):
    print("Selamat datang,Ibu", nama_tamu,'!')
    print("Selamat datang di hotel kami, Transylvania. Adakah yang bisa kami bantu,Bu?")
elif (gender == "wanita") :
    print("Selamat datang,Ibu", nama_tamu, '!')
    print("Selamat datang di hotel kami, Transylvania. Adakah yang bisa kami bantu,Bu?")
elif (gender == "cewek") :
    print("Selamat datang,Ibu", nama_tamu, '!')
    print("Selamat datang di hotel kami, Transylvania. Adakah yang bisa kami bantu,Bu?")
else:
    print("Selamat datang,Bapak", nama_tamu,'!')
    print("Selamat datang di hotel kami, Transylvania. Adakah yang bisa kami bantu,Pak?")

