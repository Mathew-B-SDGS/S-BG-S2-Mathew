import unittest

class dna:
    def __init__(self, sequence, sequence_id ):
        self.sequence=sequence
        self.sequence_id=sequence_id

    def char_count(self):
        count = {"A": 0, "T": 0, "C": 0, "G": 0}
        for base in self.sequence:
            count[base] += 1
        return count
    
    def rna_transcribe(self):
        rna_string=""
        for base in self.sequence:
            if base=="T":
                rna_string+="U"
            else:
                rna_string+=base
        return rna_string

    def reverse_complementV1(self):
        key = { "A": "T", "C": "G", "T": "A", "G": "C" }
        reversed_seq = ""
        for base in self.sequence:
            complement_base = key[base]
            reversed_seq += complement_base
        return reversed_seq
    
    def calculate_gc(self):
        gc_count = self.sequence.count('G') + self.sequence.count('C')
        total_count = len(self.sequence)
        gc_percent = ((gc_count / total_count) * 100)
        gc_return = f"{self.sequence_id},GC={gc_percent}%"
        return gc_return 

    def count_nucleotide(self, nucleotide):
            return self.sequence.count(nucleotide)

sequence1 = dna("ATCG",">1")
print(sequence1.char_count(),sequence1.calculate_gc(),sequence1.reverse_complementV1())

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


suite = unittest.TestLoader().loadTestsFromTestCase(dna_test_case)
unittest.TextTestRunner().run(suite)

if __name__ == '__main__':
    unittest.main()