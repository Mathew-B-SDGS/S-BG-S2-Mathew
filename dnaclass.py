
from typing import Any

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
        if 'U' in self.sequence:
            raise ValueError("Invalid DNA sequence. It already contains 'U'.")    
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
    
    def calculate_gc(self) -> str:
        gc_count = self.sequence.count('G') + self.sequence.count('C')
        total_count = len(self.sequence)
        gc_percent = ((gc_count / total_count) * 100)
        gc_return = f"{self.sequence_id},GC={gc_percent}%"
        return gc_return

    def count_nucleotide(self, nucleotide):
            return self.sequence.count(nucleotide)

    @classmethod
    def from_file(cls, file_name):
        with open(file_name, "r") as file:
            sequence = file.read().strip()
        return cls(sequence,None)
    @classmethod
    def from_directory(cls, ):
        pass


class rna(dna):
    def __init__(self, *args, **kwargs):
        return super().__init__(*args, **kwargs)

if __name__ == '__main__':
    sequence_file= dna.from_file("genes.txt")

    print(sequence_file.calculate_gc())

    sequence1 = dna("ATCG",">1")

    print("I shouldn't be here!")