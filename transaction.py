# Import library yang dibutuhkan
from tabulate import tabulate

# Fungsi u/ membuat transaction class
""" 
  class Transaction akan kita gunakan sebagai parent class yang akan nantinya 
  menyimpan informasi (atribut) pemesanan seperti nama, jumlah, dan harga barang 
  items
  """
class Transaction:
    def __init__ (self):
        
        self.data_transc = dict()
     
    # Fungsi untuk memasukkan nama, jumlah, dan harga item (add_item)
    """
    fusngsi ini untuk menambahkan detail barang yang ingin dipesan:
    nama_item = nama barang yang ingin dipesan
    julah_item = jumlah barang yang ingin dipesan
    harga_per_item = harga barang yang ingin dipesan
    """
    def add_item (self, nama_item, jumlah_item, harga_per_item):
        
        # Menambah data ke dalam atribut dictrionary
        self.data_transc.update({nama_item : [jumlah_item, harga_per_item, (jumlah_item * harga_per_item)]})

        # Menampilkan list item
        return self.check_order()
     
        
    # Fungsi untuk memperbaharui pesanan
    """
    Fungsi ini digunakan untuk memperbaiki apabila nama, jumlah, 
    harga barang salah diinput.
    """
    def update_item_name (self, nama_item, update_nama_item):
        
        try: 
            # Update nama item
            self.data_transc[update_nama_item] = self.data_transc.pop(nama_item)

            # Menampilkan list item
            return self.check_order()
        
        except:
            raise exception ("Nama produk salah! Nama produk tidak tersedia")
    
    def update_item_qty (self, nama_item, update_jumlah_item):
        
        try: 
            # Update jumlah item
            self.data_transc[nama_item][0] = update_jumlah_item 
            
            # Update data total harga 
            self.data_transc[nama_item][2] = update_jumlah_item * self.data_transc[nama_item][1]

            #Menampilkan list item
            return self.check_order()
        
        except:
            raise exception ("Nama produk salah! Nama produk tidak tersedia")
      
    def update_item_price (self, nama_item, update_harga_item):
        
        try:
            # Update harga item
            self.data_transc[nama_item][1] = update_harga_item
            # Update data total harga
            self.data_transc[nama_item][2] = update_harga_item * self.data_transc[nama_item][0]

            #Menampilkan list item
            return self.check_order()
        
        except:
            raise exception ("Nama produk salah! Nama produk tidak tersedia")
    
    
    # Fungsi untuk menghapus item pembelian
    """
    Fungsi ini digunakan untuk menghapus salah satu item yang sudah dipesan. 
    Parameter yang dimasukkan adalah nama item (item_name).
    Outputnya semua detail terkait barang tersebut (jumlah dan harganya) akan terhapus
    """
    def delete_item (self, nama_item):
        
        try:
            # Delete item tertentu
            self.data_transc.pop(nama_item)
            
            # Menampilkan list item terbaru
            return self.check_order()
        
        except:
            raise exception ("Nama produk salah! Nama produk tidak tersedia")
    
    
    # Fungsi untuk menghapus semua pesanan
    """
    Fungsi untuk menghapus SEMUA item yang sudah dipesan. 
    Outputnya semua item dan detailnya dalam pesanan akan terhapus.
    """
    def reset_transaction (self):
        
        # Delete semua data transaksi
        self.data_transc.clear()
        
        return "Semua item berhasil di-delete!"
    
    
    # Membuat method untuk mengecek input sudah lengkap dan benar
    """
    Fungsi untuk mengecek apakah semua detail barang yang diinputkan 
    sudah lengkap dan sesuai ketentuan aplikasi
    """
    def check_order(self):
        
        try: 
            table = []
            
            # Add data dictionary transaksi ke dalam nested list table
            for key, val in self.data_transc.items():
                tmp = []
                tmp.append(key)

                for i in val:
                    tmp.append(i)

                table.append(tmp) 

            headers = ['Nama Item', 'Jumlah Item', 'Harga/Item', 'Total Harga']
            print("Transaksi Anda")
            print("")
            print(tabulate(table, headers, tablefmt='psql')) 
            
        except:
            raise exception("Terjadi kesalahan input! data nama item, jumlah item, dan harga per item tidak boleh kosong! Silahkan input ulang!")
     
    
    # Fungsi untuk menghitung total belanja yang sudah dibeli
    """
    Method ini digunakan untuk menghitung total harga yang harus dibayar oleh customer.
    Setelah dilakukan penghitungan total harga awal (sebelum diskon), 
    terlebih dahulu akan ditentukan apakah customer mendapatkan diskon. 
    Jika mendapat diskon berapa diskon yang didapatkan,
    dan setelah itu dilakukan perhitungan total harga awal dikurangi diskon,
    Lalu hasil akhirnya didapatkan harga total setelah diskon
    """
    def total_price (self):
        
        # Menampilkan list item
        self.check_order()
        print("")
        
        # Menjumlahkan total harga
        total = 0
        for key, val in self.data_transc.items():
            total += self.data_transc[key][2]
            
        # pengecekan diskon
        if total > 500_000:
            total_baru = total * 0.90
            print(f'Total belanja Anda setelah diskon 10% adalah {total_baru}')
        elif total > 300_000:
            total_baru = total * 0.92
            print(f'Total belanja Anda setelah diskon 8% adalah {total_baru}')
        elif total > 200_000:
            total_baru = total * 0.95
            print(f'Total belanja Anda setelah diskon 5% adalah {total_baru}')
        else:
            print(f'Total belanja Anda adalah Rp {total}')