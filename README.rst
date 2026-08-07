The submission script, slurm_hdf5*, uses functions from the repository 
https://github.com/galform/get_nebular_emission

The state of slurm runs can be checked with: squeue --me

run_gne_*.py
------------
Scripts with all the parameters for the spectral line model.

The only paramters that need changing in this file are those specific of the run (for example AGN=False) and the out_endf to indicate such variation. For example, if its run with no AGN out_endf='lines_noAGN'

Optional variables might need to be added in the call to the gne function.

Note that the choice of N-body simulation  (SU1, SU2, UNIT1GPC_fnl0, UNIT1GPC_fnl100) and snapshots are determined within slurm_hdf5_run.py. 

slurm_hdf5_run.py
-----------------
Scripts to submit the jobs for all the intended subvolumes (there are 64 for the UNITsim suite).

Subvolumes are given to be passes to the `SBATCH --array= <https://slurm.schedmd.com/sbatch.html>`_ command:
* subvols='0-63' for the full run
* subvols='4' for running only subvolume 4
* subvols='2,5-10' for running subvolume 2 and from 5 to 10
  
* For tests reduce the number of subvolumes and redshifts.
* The outputs and error messages by default go to the table *logs*.

clean_check.py
-----------------
For a given snapshot, this can check the logs for errors (check=True).

The script can also clean the logs (clean=True).
  
plot_gne_*.sh
------------
Scripts to make plots using the whole simulation volume.

Run this code with: sbatch plot_*.sh
 
Parameters to change to match those used for run_gne_*.py:

* outpath
* out_endf

Other parameters to change:

* subvols = 64 (or for tests set to 1 or 2)
* snapshot = (values ran with slurm_hdf5_run.py)
