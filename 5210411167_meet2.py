#print string
str='aku cinta Indonesia'
print(str)
#menambah diantara string
str=str[:10]+'tanah air ku'+str[9:]
print(str)
#menghapus string
str=''
print(str)

str1='aku cinta tanah air ku Indonesia'
str1=str1[:9]+''+str1[22:]
print(str1)

kelas='praktikum pemrograman berorientasi objek'
up=kelas.upper()
lo=kelas.lower()
print(kelas)
print(up)
print(lo)

s='     python     '
print(s.strip())
print(s.lstrip())
#menghilangkan spasi akhir string
print(s.rstrip())

len(kelas)
jumlah=len(kelas)
print('panjang string =', jumlah)
#menggabungkan string
s1='python'
s2='programming'
print(s1+s2)
#menetukan indeks
print(kelas.index('a'))

#mengganti kata 
kelas2=kelas.replace('praktikum','praktik')
print(kelas2)

a='satu'
b='dua'
c='tiga'
print('saya mempunyai %s mangga' %(b))

print(kelas2)
print(kelas2.split())

#input dari keyboard
print(input('hari ini adalah : '))
data1=input('angka 1:')
data2=input('angka 2:')
hasil=int(data1)*int(data2)
print(data1,'*',data2,'=',hasil)

#tipe data list
list=[0,1,2,3,4,5,6,7,8,9]
print(list)
#akses list indeks tertentu
print(list[0])
#menampilkan 3 data pertama pada list
print(list[:3])

len(list)
print(list[10-3:])

print(list[2:9])

print(list[-10])

list.append(10)
print(list)

list.insert(1,11)
print(list)

#menggabungkan 2 list
list2=['halo']
list.extend(list2)
print(list)
list.extend('hai')
print(list)
#menghapus isi list
del list[1]
print(list)
list.remove(10)
print(list)
list.pop()
print(list)
list.pop(2) 
print(list)
#mengurutkan isi list
list3=[50,10,20,30,40]
print(list3)
urut=sorted(list3)
print(urut)
list3.sort()
print(list3)
#mengurutkan tebalik
list3.sort(reverse=True)
print(list3)
#mencari nilai terkecil dan terbesar
min(list3)
print(list3)
max(list3)
print(list3)
#dictionary
d={1:100,2:200,3:300,4:400,5:500}
print(d)
#27.mengakses dictionary
a=d[2]
print(a)
a=d.get(4)
print(a)
#mencari kunci
a=d.keys()
print(a)
#mencari nilai
a=d.values()
print(a)
#menghapus elemen tertentu
del d[1]
#copy
d.copy()

t = (100,200,300,400)
print(t[0])
print(t[3])
f = t.index(200)
print(f)
t2 = (10,20,10,30,10,40,20)
print(t2.count(10))

#set/himpunan
set={1,2,3,4}
print(set)

buah = {'nanas', 'mangga', 'apel', 'pisang'}
print(buah)

buah = set({'nanas', 'mangga','apel', 'pisang'})
print(buah)

campuran = {'pisang', 8, True}
print(campuran)

nomor = {
     (1, 2, 3),
     (4, 5, 6),
     (7, 8, 9),
}
print(nomor)

kata = {'pagi','ini', 'adalah', 'pagi', 'yang', 'sangat', 'cerah'}
print(kata)

kata = ['pagi','ini', 'adalah', 'pagi', 'yang', 'sangat', 'cerah']
print(kata)

buah = {'nanas', 'apel'}
buah.update({'semangka'})
print(buah)

nama = {'agnes', 'linda', 'sari'}
print(nama)

nama.remove('sari')
print(nama)

nama.clear()
print(nama)

nama = {'agnes', 'linda', 'sari'}
print(nama)
# menghapus nilai yang ada di sebelah kiri(cara1)
nama.pop()
print(nama)

# menghapus nilai yang ada di sebelah kiri(cara2)
Nama_dihapus = nama.pop()
print('Nama yang di hapus adalah:', Nama_dihapus)

# gabungan(union)
perempuan = {'agnes', 'linda', 'sari'}
print(perempuan)
laki_laki = {'abi', 'prayoga'}
print(laki_laki)
# cara 1
print(perempuan.union(laki_laki))
# cara2
print(perempuan|laki_laki)

# irisan(Intersection)
smp = {'kevin', "nana", 'susi', 'aisyah', 'lisa'}
smk = {'anggun','lisa', 'nanda','maman', 'kevin'}
# cara1
print(smp&smk)
# cara2
print(smp.intersection(smk))

# selisih(difference)
smp = {'kevin', "nana", 'susi', 'aisyah', 'lisa'}
smk = {'anggun','lisa', 'nanda','maman', 'kevin'}
# cara1
print(smp-smk)
# cara2
print(smp.difference(smk))

# menampilkan anggota set dengan perulangan
buah = {'nanas', 'apel', 'pepaya'}
for buah1 in buah:
     print(buah1)