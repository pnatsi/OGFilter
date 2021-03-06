# OGFilter
OGFilter is a script that parses the OrthoFinder output and returns only the orthogroups that meet specific criteria.  <br>
These criteria include:
- Minimum number of species present in orthogroup
- Maximum number of gene copies per species in orthogroup <br>

This feature is particularly useful in phylogenomics analysis, where a researcher is interested in obtaining genes with high species representation but low multiple copy occurences. <br>


## Arguments
Argument    |  Description             
:-------------:|:-----------------------
-g filename | file w/ gene counts (from OrthoFinder output)
-s dirname | directory that contains the orthogroups fasta files (from OrthoFinder output)
-o dirname | directory to write the output orthogroups
-min_species float | minimum proportion of the original species in the desired orthogroups 
-max_copies int | maximum number of gene copies per species in the desired orthogroups
<br>   

## Example usage

```
python OGFilter.py -g Orthogroups.GeneCount.tsv -s Orthogroup_Sequences -o output_dir -min_species 0.8 -max_copies 3 
```

This will create an output directory (-o output_dir) which will contain all orthogroups with at least 80% of the original species present (-min_species 0.8) and with maximum 3 copies per species (-max_copies 3).

<br>

======================================================================================

<br>

Who<br> 
 Mattia Giacomelli (mattia.giacomelli@bristol.ac.uk); <br>
 Paschalis Natsidis (p.natsidis@ucl.ac.uk); <br>
<br>
Where<br>
 Pisani Lab, Uni Bristol; <br>
 Telford Lab, UCL; <br>
 ITN IGNITE; 
<br>
<br>
When<br> 
 November 2019; 
