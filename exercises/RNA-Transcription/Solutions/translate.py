#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: bethanygarcia
"""

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



def translate (sequence):
    """Takes in a list of codons and translates them to their corresponding
       Amino acid letter.  Returns an amino acid string beginning from the start 
       codon, and ending at the stop codon.
       """
    
    seq = sequence
    
    #final product is a str, hence the call to ''.join() wrapping the generator.
    aa_rough = ''.join((RNA_Table[item] for item in seq))
    
    return aa_rough[:aa_rough.find('_')] #discard string after stop codon
