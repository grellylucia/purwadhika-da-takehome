from prettytable import PrettyTable;

listMenu = ['Menampilkan Daftar Buah', 'Menambah Buah', 'Menghapus Buah', 'Membeli Buah', 'Exit Program'];

listBuah = [
    {
        'nama': 'Apel',
        'stok': 20,
        'harga': 10000
    },
    {
        'nama': 'Jeruk',
        'stok': 15,
        'harga': 15000
    },
    {
        'nama': 'Anggur',
        'stok': 25,
        'harga': 20000
    }
]

def showListBuah() :
    i = 0;
    table = PrettyTable();
    table.field_names = (['Index', 'Nama', 'Stok', 'Harga']);

    print('\nDaftar Buah\n');
        
    for buah in listBuah:
        row = [i, buah['nama'], buah['stok'], buah['harga']];
        table.add_row(row);
        i+=1;
    print(table);

def addNewBuah() :
    print('\n');
    nama = input('Masukkan Nama Buah    : ');
    stok = input('Masukkan Stok Buah    : ');
    harga = input('Masukkan Harga Buah   : ');
    newItem = {
        'nama': nama,
        'stok': int(stok),
        'harga': int(harga)
    }
    listBuah.append(newItem);
    showListBuah();

def deleteBuah() :
    delete = input('\nMasukkan index buah yang ingin dihapus : ');
    del listBuah[int(delete)];
    showListBuah();


def beliBuah(cart) :
    beli = 'ya';
    showListBuah();
    summary = [];
    total = 0;

    while beli == 'ya' :
        item = input('\nMasukkan index buah yang ingin dibeli : ');
        itemToBuy = listBuah[int(item)];

        jumlah = input('Masukkan jumlah yang ingin dibeli : ');
        if itemToBuy['stok'] < int(jumlah) :
            print('\nStok tidak cukup, stok', itemToBuy['nama'], 'tinggal ', itemToBuy['stok']);
        
        print('\n Isi Cart : ');
        addToCart(cart, itemToBuy, jumlah);

        boughtItem = [itemToBuy['nama'], jumlah, itemToBuy['harga'], totalPerItem(jumlah, itemToBuy['harga'])];
        summary.append(boughtItem);
        total += totalPerItem(jumlah, itemToBuy['harga']);
        # listBuah[int(item)['stok']] = listBuah[int(item)['stok']] - jumlah;
        # print(listBuah[int(item)]['stok']);

        beli = input('\nMau beli yang lain ? (ya/tidak) = ');
    
    print('\nDaftar Belanja : ');
    header = ['Nama', 'Qty', 'Harga', 'Total'];
    print(createTable(header, summary));

    print('Total Yang Harus Dibayar = ', total);
    paymentProcess(total);

def paymentProcess(total) :
    bayar = 0
    while int(bayar) < total:
        bayar = input('Masukkan jumlah uang : ');
        if int(bayar) >= total :
            print('\nTerima Kasih\n');
            kembalian = int(bayar) - total
            if kembalian > 0 :
                print('\nUang kembali anda : ', str(kembalian))
        else :
            kurangBayar = total - int(bayar);
            print('\nUang anda kurang sebesar ', str(kurangBayar));

def createTable(header, rows) :
    table = PrettyTable();
    table.field_names = (header);
    for row in rows :
        table.add_row(row);
    return table;

def addToCart(cart, itemToBuy, jumlah) :
    header = ['Nama', 'Qty', 'Harga'];
    item = [itemToBuy['nama'], jumlah, itemToBuy['harga']];
    cart.append(item);
    print(createTable(header, cart));

def totalPerItem(jumlah, harga):
    return int(jumlah) * harga


start = True;

while start == True :  
    no=1;
    cart = [];
    print('\n\n*** SELAMAT DATANG DI PASAR BUAH ***\n'); 
    print('\nList Menu :');
    for menu in listMenu :
        print(no, menu);
        no+=1;

    pilih = input('Masukkan angka menu yang ingin dijalankan : ');

    if pilih == '1':
        showListBuah();
    elif pilih == '2':
        addNewBuah();
    elif pilih == '3':
        showListBuah();
        deleteBuah();
    elif pilih == '4':
       beliBuah(cart);
    elif pilih == '5':
        start = False;
    else:
        print('\n*[Maaf menu tidak tersedia. Silahkan coba lagi]*')

