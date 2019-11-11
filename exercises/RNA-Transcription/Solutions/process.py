#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: bethanygarcia
"""

import re

def process_mrna(sequence): 
    """
    Takes in an mRNA string and breaks it into codons (triplets).  
    Returns a list of codon strings, ready for translation.
    """
    #check to see if strand is evenly divisable by 3
    if len(sequence)%3 == 0:
        codons = re.findall('.{3}', sequence[sequence.find("AUG"):])
        return codons
    
    #if strand is not evenly divisable by 3, subtract the remainder from the length
    else:
        codons = re.findall('.{3}', sequence[sequence.find("AUG"):-(len(sequence)%3)])
        return codons