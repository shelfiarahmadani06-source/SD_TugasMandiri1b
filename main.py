from structures.queue_processing import QueueProcessing
from structures.stack_undo import StackUndo


def tampilkan_queue(antrean):
    print("Kondisi antrean :", list(antrean.antrian))


def tampilkan_stack(undo):
    print("Kondisi stack   :", undo.aktivitas)


def simulasi_queue():
    print("=" * 55)
    print("              SIMULASI ANTREAN MAHASISWA")
    print("=" * 55)

    antrean = QueueProcessing()

    # Langkah 1
    antrean.enqueue("Anggun")
    print("\nLangkah 1")
    print("Operasi : Penambahan data")
    print("Data    : Anggun")
    tampilkan_queue(antrean)

    # Langkah 2
    antrean.enqueue("Marisa")
    print("\nLangkah 2")
    print("Operasi : Penambahan data")
    print("Data    : Marisa")
    tampilkan_queue(antrean)

    # Langkah 3
    mahasiswa_terdepan = antrean.peek()
    print("\nLangkah 3")
    print("Operasi : Melihat data terdepan")
    print("Data    :", mahasiswa_terdepan)
    tampilkan_queue(antrean)

    # Langkah 4
    mahasiswa_dilayani = antrean.dequeue()
    print("\nLangkah 4")
    print("Operasi : Penghapusan data")
    print("Data    :", mahasiswa_dilayani)
    tampilkan_queue(antrean)

    # Langkah 5
    kondisi_kosong = antrean.is_empty()
    print("\nLangkah 5")
    print("Operasi : Memeriksa kondisi kosong")
    print("Data    :", kondisi_kosong)
    tampilkan_queue(antrean)


def simulasi_undo():
    print("\n" + "=" * 55)
    print("                 SIMULASI FITUR UNDO")
    print("=" * 55)

    undo = StackUndo()

    # Langkah 1
    undo.push("Menambahkan Anggun ke antrean")
    print("\nLangkah 1")
    print("Operasi : Penambahan data")
    print("Data    : Menambahkan Anggun ke antrean")
    tampilkan_stack(undo)

    # Langkah 2
    undo.push("Menambahkan Marisa ke antrean")
    print("\nLangkah 2")
    print("Operasi : Penambahan data")
    print("Data    : Menambahkan Marisa ke antrean")
    tampilkan_stack(undo)

    # Langkah 3
    aktivitas_terakhir = undo.peek()
    print("\nLangkah 3")
    print("Operasi : Melihat data terdepan")
    print("Data    :", aktivitas_terakhir)
    tampilkan_stack(undo)

    # Langkah 4
    aktivitas_dibatalkan = undo.pop()
    print("\nLangkah 4")
    print("Operasi : Penghapusan data / Undo")
    print("Data    :", aktivitas_dibatalkan)
    tampilkan_stack(undo)

    # Langkah 5
    kondisi_kosong = undo.is_empty()
    print("\nLangkah 5")
    print("Operasi : Memeriksa kondisi kosong")
    print("Data    :", kondisi_kosong)
    tampilkan_stack(undo)


def main():
    simulasi_queue()
    simulasi_undo()


if __name__ == "__main__":
    main()