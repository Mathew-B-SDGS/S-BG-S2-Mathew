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

    def reverse_complement(self):
        key = { "A": "T", "C": "G", "T": "A", "G": "C" }
        reversed_seq = ""
        for base in self.sequence:
            complement_base = key[base]
            reversed_seq = complement_base + reversed_seq
        return reversed_seq
    
    def calculate_gc(self):
        dict_gc = {}
        gc_count = self.sequence.count('G') + self.sequence.count('C')
        total_count = len(self.sequence)
        gc_percent = ((gc_count / total_count) * 100)
        gc_return = f"{self.sequence_id},GC={gc_percent}%"
        return gc_return 

    def count_nucleotide(self, nucleotide):
            return self.sequence.count(nucleotide)

sequence1 = dna("ATCGATCG",">1")
#print(sequence1.char_count())
#print(sequence1.calculate_gc())


class  dna_test_case(unittest.TestCase):
    def setUp(self):
        self.dna=dna("ATCG")
    def tearDown(self):
        pass
    def test_char_count(self):
        result=self.dna.char_count()
        expected_result = {'A': 1, 'T': 1, 'C': 1, 'G': 1}
        self.assertDictEqual(result,expected_result)
    def test_count_nucleotide(self):
        result= self.dna.count_nucleotide("A")
        self.assertEqual(result, 1)



# suite = unittest.TestSuite()
#suite.addTest(dna_test_case("test_count_nucleotide"))
# suite.addTest(dna_test_case("test_chat_count"))
# unittest.TextTestResult().run(suite)




suite = unittest.TestLoader().loadTestsFromTestCase(dna_test_case)
unittest.TextTestRunner().run(suite)
