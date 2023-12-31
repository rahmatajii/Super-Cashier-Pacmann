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

https://github.com/rahmatajii/Super-Cashier-Pacmann/issues/1#issue-1795457824
     
### Test Case 1
    Menambahkan item dengan method `add_item`
   https://github.com/rahmatajii/Super-Cashier-Pacmann/blob/main/img/testcase_1.jpg
    
### Test Case 2
    Menghapus item dengan method `delete_item`
   https://github.com/rahmatajii/Super-Cashier-Pacmann/blob/main/img/testcase_2.png

### Test Case 3
    Menghapus semua data transaksi dengan method `reset_transaction`
   https://github.com/rahmatajii/Super-Cashier-Pacmann/blob/main/img/testcase_3a.png
   https://github.com/rahmatajii/Super-Cashier-Pacmann/blob/main/img/testcase_3b.png

### Test Case 4
    Mengubah nama produk dengan method `update_item_name`
   https://github.com/rahmatajii/Super-Cashier-Pacmann/blob/main/img/testcase_4.png

### Test Case 5
    Mengubah kuantitas produk dengan method `update_item_qty`
   https://github.com/rahmatajii/Super-Cashier-Pacmann/blob/main/img/testcase_5.png

### Test Case 6
    Mengubah harga produk dengan method `update_item_price`
   https://github.com/rahmatajii/Super-Cashier-Pacmann/blob/main/img/testcase_6.png

### Test Case 7
    Mengecek data order dengan method `check_order`
   https://github.com/rahmatajii/Super-Cashier-Pacmann/blob/main/img/testcase_7.png

### Test Case 8
    Menampilkan total belanja dengan method `total_price`
   https://github.com/rahmatajii/Super-Cashier-Pacmann/blob/main/img/testcase_8a.png
   https://github.com/rahmatajii/Super-Cashier-Pacmann/blob/main/img/testcase_8b.png

### Test Case 9
    Keluar dari program kasir self-service
   https://github.com/rahmatajii/Super-Cashier-Pacmann/blob/main/img/testcase_9.png
