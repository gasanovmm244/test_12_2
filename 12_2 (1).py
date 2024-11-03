import A12
import unittest

class TournamentTest(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.all_results = dict()

    def setUp(self):
        self.Usain = A12.Runner('Usain', 10)
        self.Andrey = A12.Runner('Andrey', 9)
        self.Nik = A12.Runner('Nik', 3)



    def test_Tournament_all(self):
        turna = A12.Tournament(90, self.Usain, self.Andrey, self.Nik)
        self.all_results = turna.start()
        self.assertEqual(self.all_results[len(self.all_results)], 'Nik')
        TournamentTest.all_results.update(self.all_results)

    def test_Tournament_Usain_and_Nik(self):
        turna = A12.Tournament(90, self.Usain, self.Nik)
        self.all_results = turna.start()
        self.assertEqual(self.all_results[len(self.all_results)], 'Nik')
        TournamentTest.all_results.update(self.all_results)

    def test_Tournament_Annrey_and_Nik(self):
        turna = A12.Tournament(90, self.Andrey, self.Nik)
        self.all_results = turna.start()
        self.assertEqual(self.all_results[len(self.all_results)], 'Nik')
        TournamentTest.all_results.update(self.all_results)


    def tearDown(self):
        print(self.all_results)

