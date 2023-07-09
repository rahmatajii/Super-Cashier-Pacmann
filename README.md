# Final Project - Super Cashier Pacmann
# Sistem kasir self-service yang dirancang untuk input barang pembelian secara mandiri oleh costumer. Sistem tersebut membebaskan customer untuk memasukkan item yang ingin dibeli, kuantitas item, dan harga per item yang ingin dibeli.
## 1. Requirments
   ## Membuat program kasir self service dengan requirments berikut:
   ## a. Membuat proses untuk memasukkan ID Menu Transaksi
   ## b. Membuat proses untuk menambahkan barang yang ini dibeli dan detail jumlah dan harganya
   ## c. Membuat proses untuk mengupdate detail barang yang sudah diinputkan sebelumnya jika ada kesalahan input
   ## d. Membuat proses untuk menghapus salah satu pesanan yang telah diinputkan  
   ## e. Membuat proses untuk menghapus seluruh transaksi yang telah diinputkan
   ## f. Membuat proses untuk memeriksa apakah seluruh data yang diinput sudah benar dan lengkap
   ## g. Membuat proses untuk menghitung total belanja yang harus dibayarkan dan diskon yang didapatkan (jika dapat).
 
## 2. Function dan atribut
1. `data_transc`       : Atribut yang berupa dictionary yang berfungsi untuk menyimpan data transaksi yang dilakukan oleh customer
2. `add_item`          : Method yang berfungsi untuk menambahkan list produk yang telah dimasukkan oleh customer yang berisi nama item, kuantitas item, dan harga item
3. `update_item_name`  : Method yang berguna untuk mengubah nama item yang ingin diganti
4. `update_item_qty`   : Method yang berguna untuk mengubah kuantitas item yang di-order
5. `update_item_price` : Method yang berfungsi untuk mengubah harga item yang dibeli
6. `delete_item`       : Method yang digunakan untuk menghapus item tertentu
7. `reset_transaction` : Method yang digunakan untuk menghapus seluruh data transaksi
8. `check_order`       : Method yang berfungsi untuk menampilkan seluruh data transaksi yang telah dibuat
9. `total_price`       : Method yang digunakan untuk menampilkan total harga seluruh produk

## 3. Test Case
### Test Case Menu Program
    Menampilkan menu program kasir
     ![alt text](https://github.com/rahmatajii/Super-Cashier-Pacmann/blob/main/img/testcase%20menu%20program.png?raw=true)
     
### Test Case 1
    Menambahkan item dengan method `add_item`
    <img src="img/test-case-1.png" width="700"/>
    
### Test Case 2
    Menghapus item dengan method `delete_item`
    <img src="img/test-case-2.png" width="700"/>

### Test Case 3
    Menghapus semua data transaksi dengan method `reset_transaction`
    <img src="img/test-case-3.png" width="700"/>

### Test Case 4
    Mengubah nama produk dengan method `update_item_name`
    <img src="img/test-case-4.png" width="700"/>

### Test Case 5
    Mengubah kuantitas produk dengan method `update_item_qty`
    <img src="img/test-case-5.png" width="700"/>

### Test Case 6
    Mengubah harga produk dengan method `update_item_price`
    <img src="img/test-case-6.png" width="700"/>

### Test Case 7
    Mengecek data order dengan method `check_order`
    <img src="img/test-case-7.png" width="700"/>

### Test Case 8
    Menampilkan total belanja dengan method `total_price`
    <img src="img/test-case-8.png" width="700"/>

### Test Case 9
    Keluar dari program kasir self-service
    <img src="img/test-case-9.png" width="700"/>
