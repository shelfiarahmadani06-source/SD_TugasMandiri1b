# Tugas Mandiri 1b
## Penerapan Struktur Data Linear

### Studi Kasus

Program dibuat berdasarkan studi kasus sistem antrean layanan administrasi mahasiswa dan fitur Undo.

### Struktur Data yang Digunakan

1. **Antrean Mahasiswa**
   - Menggunakan Queue.
   - Prinsip yang digunakan adalah FIFO (First In, First Out).
   - Operasi:
     - Penambahan data
     - Penghapusan/pengambilan data
     - Melihat data terdepan
     - Memeriksa kondisi kosong

2. **Fitur Undo**
   - Menggunakan Stack.
   - Prinsip yang digunakan adalah LIFO (Last In, First Out).
   - Operasi:
     - Penambahan data
     - Penghapusan/pengambilan data
     - Melihat data terdepan
     - Memeriksa kondisi kosong

### Struktur Folder

```text
tugas mandiri 1b
│
├── structures
│   ├── __init__.py
│   ├── queue_processing.py
│   └── stack_undo.py
│
├── tests
│   ├── __init__.py
│   ├── test_queue_processing.py
│   └── test_stack_undo.py
│
├── main.py
└── README.md
