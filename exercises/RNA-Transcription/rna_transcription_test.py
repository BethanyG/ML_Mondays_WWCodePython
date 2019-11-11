import unittest

from dna import to_rna


# test cases adapted from `x-common//canonical-data.json` @ version: 1.0.0

class DNATests(unittest.TestCase):
    def test_transcribes_guanine_to_cytosine(self):
        self.assertEqual(to_rna('G'), 'C')

    def test_transcribes_cytosine_to_guanine(self):
        self.assertEqual(to_rna('C'), 'G')

    def test_transcribes_thymine_to_adenine(self):
        self.assertEqual(to_rna('T'), 'A')

    def test_transcribes_adenine_to_uracil(self):
        self.assertEqual(to_rna('A'), 'U')

    def test_transcribes_all_occurences(self):
        self.assertMultiLineEqual(to_rna('ACGTGGTCTTAA'), 'UGCACCAGAAUU')

    def test_correctly_handles_single_invalid_input(self):
        self.assertEqual(to_rna('U'), '')

    def test_correctly_handles_completely_invalid_input(self):
        self.assertMultiLineEqual(to_rna('XXX'), '')

    def test_correctly_handles_partially_invalid_input(self):
        self.assertMultiLineEqual(to_rna('ACGTXXXCTTAA'), '')


if __name__ == '__main__':
    unittest.main()
