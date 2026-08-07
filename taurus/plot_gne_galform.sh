#!/bin/sh
# Run this code with sbatch plot_gne_galform.sh
#SBATCH -A 16cores
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --job-name=plot_galform
#SBATCH --error=/home2/vgonzalez/buds/run_setups/taurus/logs/%x_%j.err
#SBATCH --output=/home2/vgonzalez/buds/run_setups/taurus/logs/%x_%j.out
#SBATCH --partition=all
#SBATCH --exclude=epi
#SBATCH --time=00:30:00
#
srun python << 'EOF_PYTHON_SCRIPT'
###############################################################
from gne.gne import gne
from gne.gne_plots import make_testplots
import os, h5py

verbose = True

outpath = '/data21/users/vgonzalez/Data/Galform/SU1'
#outpath = '/data21/users/vgonzalez/Data/Shark/SU1'
subvols = 64
snapshot = 96 #128 96 87

#out_endf = "lines_noAGN"
out_endf = "var_alpha_NLR_1_2"

### Make plots
list_subvols = subvols
if isinstance(subvols, int):
    list_subvols = list(range(subvols))

make_testplots(snapshot,out_endf,outpath=outpath,
               subvols=list_subvols,
               gridplots=False,verbose=verbose)
###############################################################
EOF_PYTHON_SCRIPT
