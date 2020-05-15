#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import csv
import shutil
import itertools
import argparse


usage = "A script to filter OrthoFinder results and keep orthogroups with specific properties."
toolname = "OrthoFilter"
footer = "Who \n Mattia Giacomelli (mattia.giacomelli@bristol.ac.uk); \n Paschalis Natsidis (p.natsidis@ucl.ac.uk); \n \nWhere \n Pisani Lab, Uni Bristol; \n Telford Lab, UCL;\n\
 ITN IGNITE; \n  \nWhen\n November 2019; \n\n"

parser = argparse.ArgumentParser(description = usage, prog = toolname, epilog = footer, formatter_class=argparse.RawDescriptionHelpFormatter,)

parser.add_argument('-g', metavar = 'filename', dest = 'genecounts_tsv', required = True,
                    help = 'path to Orthogroups.GeneCount.tsv file')
parser.add_argument('-s', metavar = 'directory', dest = 'og_seqs_dir', required = True,
                    help = 'path to Orthgroup_Sequences directory')
parser.add_argument('-o', metavar = 'directory', dest = 'output_dir', required = True,
                    help = 'directory where the output will be written')
parser.add_argument('-max_copies', metavar = 'int', dest = 'copies', required = True,
                    help = 'Maximum number of gene copies per species in an orthogroup to be kept')
parser.add_argument('-min_species', metavar = 'float', dest = 'n_species', required = True,
                    help = 'Minimum number of species present in an orthogroup to be kept')


#parser.print_help()

args = parser.parse_args()

#READ USER INPUT
genecounts = args.genecounts_tsv
orthogroup_sequences_dir = args.og_seqs_dir
output_directory = args.output_dir
max_copies = int(args.copies)
min_species_proportion = float(args.n_species)

wdir = os.getcwd()

OGs_list = []

with open(genecounts) as tsvfile:  
    
    reader = csv.reader(tsvfile, delimiter='\t')
    row1 = next(reader)
    total_species = len(row1) - 2 
    min_species_number = total_species * min_species_proportion
    
    for og in reader:
        current_og = og[1:-1]
        current_og_ints = [int(x) for x in current_og]
        if max_copies == 1 and max(current_og_ints) == 1 and (total_species - current_og_ints.count(0)) >= min_species_number:
            OGs_list.append(og[0])
            OGs_list_ID = [item + '.fa' for item in OGs_list]
            
        if max(current_og_ints) <= max_copies and (total_species - current_og_ints.count(0)) >= min_species_number:
            counts = sorted(list(set(current_og)))
            OGs_list.append(og[0])
            OGs_list_ID = [item + '.fa' for item in OGs_list]

os.makedirs(output_directory)

for file in OGs_list_ID:
    shutil.copy(orthogroup_sequences_dir + '/' + file, output_directory)

