import unittest
from structures.queue_processing import QueueProcessing


class TestQueueProcessing(unittest.TestCase):

    def test_penambahan_data(self):
        antrean = QueueProcessing()

        antrean.enqueue("Ani")
        antrean.enqueue("Budi")

        self.assertEqual(antrean.peek(), "Ani")

    def test_penghapusan_data(self):
        antrean = QueueProcessing()

        antrean.enqueue("Ani")
        antrean.enqueue("Budi")

        mahasiswa = antrean.dequeue()

        self.assertEqual(mahasiswa, "Ani")
        self.assertEqual(antrean.peek(), "Budi")

    def test_melihat_data_terdepan(self):
        antrean = QueueProcessing()

        antrean.enqueue("Citra")
        antrean.enqueue("Deni")

        mahasiswa = antrean.peek()

        self.assertEqual(mahasiswa, "Citra")
        self.assertEqual(antrean.peek(), "Citra")

    def test_memeriksa_kondisi_kosong(self):
        antrean = QueueProcessing()

        self.assertTrue(antrean.is_empty())

        antrean.enqueue("Eka")

        self.assertFalse(antrean.is_empty())


if __name__ == "__main__":
    unittest.main()
