#!/bin/sh
#SBATCH -A 16cores
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=16
#SBATCH --job-name=test_hello_world
#SBATCH --error=test_hello_world.err
#SBATCH --output=test_hello_world.out
##SBATCH --mem=600000
#SBATCH --partition=all
#SBATCH --time=30-00:00:00
#
export OMP_NUM_THREADS=16
srun python hello.py

# usage : sbatch test.sh
# description: submits hello.py to SLURM with 16 cores, using sbatch
