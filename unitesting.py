import unittest
from dnaclass import dna

class  dna_test_case(unittest.TestCase):
    def setUp(self):
        self.dna=dna("ATCG",">1")

    def tearDown(self):
        pass

    def test_char_count(self):
        result=self.dna.char_count()
        expected_result = {'A': 1, 'T': 1, 'C': 1, 'G': 1}
        self.assertDictEqual(result,expected_result)

    def test_count_nucleotide(self):
        result= self.dna.count_nucleotide("A")
        self.assertEqual(result, 1)
        
    def test_transcribe(self):
        result=self.dna.rna_transcribe()
        expected_result="AUCG"
        self.assertEqual(result,expected_result)

    def test_calculate_gc(self):
        result=self.dna.calculate_gc()
        expected_result=">1,GC=50.0%"
        self.assertEqual(result,expected_result)

    def test_reverse_complement(self):
        result=self.dna.reverse_complementV1()
        expected_result="TAGC"
        self.assertEqual(result,expected_result)

    def test_transcribe_invalid_sequence(self):
            sequence = "AUCG"
            expected_error_message = "Invalid DNA sequence. It already contains 'U'."
            try:
                self.dna.rna_transcribe(sequence,null)
            except ValueError as e:
                self.assertEqual(str(e), expected_error_message)
            else:
                self.fail("Expected ValueError was not raised.")

suite = unittest.TestLoader().loadTestsFromTestCase(dna_test_case)
unittest.TextTestRunner().run(suite)

if __name__ == '__main__':
    unittest.main()