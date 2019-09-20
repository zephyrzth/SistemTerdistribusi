## Tugas 2 Sistem Terdistribusi - Anargya Widyadhana - 05111740000047

### Aktifasi virtualenv
jika menggunakan ubuntu
install python3-venv
apt-get install python3-venv

python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

### Tutorial
Di sini akan digunakan remote object menggunakan nameserver. Untuk penggunaannya, jika dijalankan client dan server pada mesin yang berbeda,
1. Pertama, buka koneksi port dengan menambah Inbound Rules dan Outbound Rules pada Windows Firewall pada port yang diinginkan (di sini digunakan port 7777).
2. Start nameserver dengan command `pyro4-ns -n [IP Server] -p 7777`.
3. Ubah variabel `daemon` dan `ns` pada `greet_server.py` menjadi sesuai IP dan port, menjadi
   ```
   daemon = Pyro4.Daemon(host="[IP Server]")
   ns = Pyro4.locateNS("[IP Server]",7777)
   ```
4. Pada `greet_client.py` ubah variabel `uri` pada fungsi `test_with_ns()` sesuai IP server, menjadi
   ```
   uri = "PYRONAME:greetserver@[IP Server]:7777"
   ```
5. Jalankan `greet_server.py` terlebih dahulu, kemudian jalankan `greet_client.py`.
