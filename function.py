# hildan fahlevi

# Function untuk membalik setiap kata dalam kalimat tanpa mengubah urutan kata
def reverse_per_kata(kalimat):
    """
        Membalik setiap kata dalam kalimat tanpa mengubah urutan kata.
        """
    kata_list = kalimat.split()
    hasil = [] 
    for kata in kata_list:
        hasil.append(kata[::-1])
    return ' '.join(hasil)

# Function untuk mengurutkan kata dalam kalimat sesuai urutan list indeks (mulai dari 1)
def urutkan_kalimat(kalimat, urutan):
    """
        Mengurutkan kata-kata dalam kalimat sesuai urutan yang diberikan.
        urutan: list indeks mulai dari 1.
        Contoh: urutan [5,1,4,3,2] pada "A B C D E" -> "E A D C B"
        """
    kata_list = kalimat.split()
    hasil = []
    for idx in urutan:
        hasil.append(kata_list[idx-1])
    return ' '.join(hasil)

# Function untuk mengganti huruf vokal dengan simbol tertentu sesuai opsi
def ganti_vokal(kalimat, opsi):
    """
        Mengganti huruf vokal pada kalimat dengan simbol tertentu.
        opsi 1: hanya vokal kecil yang diubah
        opsi 2: hanya vokal kapital yang diubah
        """
    vokal_kecil = {'a':'4', 'i':'1', 'u':'|_|', 'e':'3', 'o':'0'}
    vokal_besar = {'A':'4', 'I':'1', 'U':'|_|', 'E':'3', 'O':'0'}
    hasil = ''
    for huruf in kalimat:
        if opsi == 1 and huruf in vokal_kecil:
            hasil += vokal_kecil[huruf]
        elif opsi == 2 and huruf in vokal_besar:
            hasil += vokal_besar[huruf]
        else:
            hasil += huruf
    return hasil

# menggunakan input user
kalimat1 = input("Masukkan kalimat untuk reverse per kata: ")
print("Hasil reverse per kata:", reverse_per_kata(kalimat1))

kalimat2 = input("Masukkan kalimat untuk urutkan kalimat: ")
urutan_str = input("Masukkan urutannya (contoh: 5,1,4,3,2): ")
urutan = [int(x) for x in urutan_str.split(',')]
print("Hasil urutkan kalimat:", urutkan_kalimat(kalimat2, urutan))

kalimat3 = input("Masukkan kalimat untuk ganti vokal: ")
opsi = int(input("Masukkan opsi (1=vokal kecil, 2=vokal kapital): "))
print("Hasil ganti vokal:", ganti_vokal(kalimat3, opsi))
