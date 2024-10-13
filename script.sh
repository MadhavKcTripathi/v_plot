#!/bin/bash

zcat mapped.bed.gz | awk '{print int(((($9 + $10) / 2) - $3) * 1000 / ($4 - $3)),"\t",$12}' > coordinates.tsv

cat coordinates.tsv | python make_matrix.py > matrix.csv

tr -d '[,]' < matrix.csv > cleaned_matrix.dat

gnuplot GNU_plot.gp
