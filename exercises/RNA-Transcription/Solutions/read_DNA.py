#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 17 03:22:56 2016

@author: bethanygarcia
"""

import re
from itertools import takewhile


def read_seq(inputfile):
    """Reads and returns input sequence with special characters removed."""
    with open(inputfile, "r") as input_file:
        sequence = input_file.read()
    sequence = sequence.replace("\n", '')
    sequence = sequence.replace("\r", '')
    sequence = sequence.replace(" ", '')
    
    
    return sequence
    

DNA_table = {
'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',
'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W',
}

RNA_Table = {
"UUU":"F", "UUC":"F", "UUA":"L", "UUG":"L",
"UCU":"S", "UCC":"S", "UCA":"S", "UCG":"S",
"UAU":"Y", "UAC":"Y", "UAA":"_", "UAG":"_",
"UGU":"C", "UGC":"C", "UGA":"_", "UGG":"W",
"CUU":"L", "CUC":"L", "CUA":"L", "CUG":"L",
"CCU":"P", "CCC":"P", "CCA":"P", "CCG":"P",
"CAU":"H", "CAC":"H", "CAA":"Q", "CAG":"Q",
"CGU":"R", "CGC":"R", "CGA":"R", "CGG":"R",
"AUU":"I", "AUC":"I", "AUA":"I", "AUG":"M",
"ACU":"T", "ACC":"T", "ACA":"T", "ACG":"T",
"AAU":"N", "AAC":"N", "AAA":"K", "AAG":"K",
"AGU":"S", "AGC":"S", "AGA":"R", "AGG":"R",
"GUU":"V", "GUC":"V", "GUA":"V", "GUG":"V",
"GCU":"A", "GCC":"A", "GCA":"A", "GCG":"A",
"GAU":"D", "GAC":"D", "GAA":"E", "GAG":"E",
"GGU":"G", "GGC":"G", "GGA":"G", "GGG":"G",
}


def to_rna(sequence):
    '''Transcribe a string containing a DNA 
       nucleotide sequence into a string containing
       the corresponding sequence of amino acids.'''
    
    for item in sequence:
        if item not in "GCTA":
            return ""
    
    transcription = str.maketrans("GCTA", "CGAU")
    
    return str.translate(sequence, transcription)


def translate_seq_takewhile(sequence):
    """Solution using itertools.takewhile()  
       Timed at 121 µs ± 976 ns per loop 
       (mean ± std. dev. of 7 runs, 10000 loops each)
       """
    
    seq = sequence
    
    #final product is a str, hence the call to ''.join() wrapping the generator.
    
    return  ''.join(takewhile(lambda x: x != '_',   #only take the string until '_' is reached
                      (RNA_Table[item] for item in  #lookup each codon in dict
                      (seq[i:i+3] for i in          #split into codons from AUG to end
                       range(seq.find('AUG'),(len(seq) - len(seq)%3),3)
                      ))))                
 

def translate_seq_slice(seq):
    """Solution using string slices 
       Timed at 116 µs ± 808 ns per loop 
       (mean ± std. dev. of 7 runs, 10000 loops each)
    """
    #final product is a str, hence the call to ''.join()
    mRNA2 = ''.join(
                    RNA_Table[item] for item in  #lookup each codon in dict
                    (seq[i:i+3] for i in         #split into codons from AUG to end
                     range(seq.find('AUG'),(len(seq) - len(seq)%3),3))
                    )
    
    return mRNA2[:mRNA2.find('_')] #trunkate the string at first '_'

    
def translate_long_way(seq):
    """
    Attempt to do this without any list comprehnsions or fanciness.
    Timed at 120 µs ± 773 ns per loop 
    (mean ± std. dev. of 7 runs, 10000 loops each)
    """
    
    codons = []
    aminos = []
    for i in range(seq.find('AUG'),(len(seq) - len(seq)%3),3):
        codons.append(seq[i:i+3])
    
    for item in codons:
        aminos.append(RNA_Table[item]) 
    
    
    protein = ''.join(aminos)
    
    return protein[:protein.find('_')]


def translate_seq_regex(sequence): 
    """
    Solution using an uncompiled regex.
    Timed at 95.2 µs ± 2.47 µs per loop 
    (mean ± std. dev. of 7 runs, 10000 loops each)
    """
    #check to see if strand is evenly divisable by 3
    if len(sequence)%3 == 0:
        #''.join() around looking up the protein code for every item returned by the regex.findall()
        mRNA = ''.join((RNA_Table[item] for item in re.findall('.{3}', sequence[sequence.find("AUG"):])))
        return (mRNA[:mRNA.find('_')])

    else:
        #''.join() around looking up the protein code for every item returned by the regex.findall()
        # this condition kicks in if the strand is not evenly divisable by 3
        mRNA = ''.join((RNA_Table[item] for item in re.findall('.{3}', sequence[sequence.find("AUG"):-(len(sequence)%3)])))
        return (mRNA[:mRNA.find('_')])

    
prt = read_seq('protein.txt')
dna = read_seq('dna.txt')
mrna = read_seq('mrna.txt')
s=to_rna(dna)

print('\n\n')
print(translate_seq_takewhile(s) == translate_seq_slice(s) == translate_seq_regex(s) == translate_long_way(s) == prt)
