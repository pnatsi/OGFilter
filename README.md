# OGFilter
OGFilter is a script that parsees the OrthoFinder output and returns only the orthogroups that meet specific criteria.
These criteria include:
- Minimum number of species present in orthogroup
- Maximum number of gene copies per species in orthogroup

For example:

```
python OGFilter.py -g Orthogroups.GeneCount.tsv -s Orthogroup_Sequences -o output_dir -min_species 0.8 -max_dupl 3 
```

This will create an output directory (-o output_dir) which will contain all orthogroups with at least 80% of the original species present (-min_species 0.8) and with maximum 3 copies per species (-max_copies 3).
