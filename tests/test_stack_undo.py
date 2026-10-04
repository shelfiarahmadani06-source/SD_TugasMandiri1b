import unittest
from structures.stack_undo import StackUndo


class TestStackUndo(unittest.TestCase):

    def test_penambahan_data(self):
        undo = StackUndo()

        undo.push("Aktivitas 1")
        undo.push("Aktivitas 2")

        self.assertEqual(undo.peek(), "Aktivitas 2")

    def test_penghapusan_data(self):
        undo = StackUndo()

        undo.push("Aktivitas 1")
        undo.push("Aktivitas 2")

        aktivitas = undo.pop()

        self.assertEqual(aktivitas, "Aktivitas 2")
        self.assertEqual(undo.peek(), "Aktivitas 1")

    def test_melihat_data_terdepan(self):
        undo = StackUndo()

        undo.push("Aktivitas 3")
        undo.push("Aktivitas 4")

        aktivitas = undo.peek()

        self.assertEqual(aktivitas, "Aktivitas 4")
        self.assertEqual(undo.peek(), "Aktivitas 4")

    def test_memeriksa_kondisi_kosong(self):
        undo = StackUndo()

        self.assertTrue(undo.is_empty())

        undo.push("Aktivitas 5")

        self.assertFalse(undo.is_empty())


if __name__ == "__main__":
    unittest.main()
