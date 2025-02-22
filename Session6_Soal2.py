anggur = 0; jeruk = 0; apel = 0; total = 0; 
stokJeruk = 7; stokAnggur = 6;
warningMessage = 'Jumlah yang dimasukkan terlalu banyak';

apel = input('Masukkan jumlah apel : ');

while jeruk == 0 :
    j = input('Masukkan jumlah jeruk : ');
    if int(j) > stokJeruk :
        print(warningMessage);
        print('Stok jeruk tinggal : ', str(stokJeruk));
    else :
        jeruk = j;

while anggur == 0 :
    a = input('Masukkan jumlah anggur : ');
    if int(a) > stokAnggur :
        print(warningMessage);
        print('Stok jeruk tinggal : ', str(stokAnggur));
    else :
        anggur = a;

listItemTemp = [
    {
        'nama': 'Apel',
        'jumlah': apel,
        'harga': 10000
    },
    {
        'nama': 'Jeruk',
        'jumlah': jeruk,
        'harga': 15000
    },
    {
        'nama': 'Anggur',
        'jumlah': anggur,
        'harga': 20000
    }
]

def totalPerItem(jumlah, harga):
    return int(jumlah) * harga

def printItem(item, jumlah, harga) :
    print(item, ':', jumlah, 'x', str(harga), '=', str(totalPerItem(jumlah, harga)))

print('\nDetail Belanja \n');

for item in listItemTemp :
    printItem(item['nama'], item['jumlah'], item['harga']);
    total += totalPerItem(item['jumlah'],item['harga']); 

print('\nTotal : ', total, '\n');

bayar = 0
while int(bayar) < total:
    bayar = input('Masukkan jumlah uang : ');
    if int(bayar) >= total :
        print('Terima Kasih');
        kembalian = int(bayar) - total
        if kembalian > 0 :
            print('Uang kembali anda : ', str(kembalian))
    else :
        kurangBayar = total - int(bayar);
        print('Uang anda kurang sebesar ', str(kurangBayar));