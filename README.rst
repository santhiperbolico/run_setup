The submission script, slurm_hdf5*, uses functions from the repository 
https://github.com/galform/get_nebular_emission

run_gne_*.py
------------
Scripts with all the parameters for the spectral line model.

Parameters to change:

* outpath: Change this for different N-body simulations (SU1, SU2, UNIT1GPC_fnl0, UNIT1GPC_fnl100)
* out_endf: Change this to a name indicating the kind of run, for example, if its run with no AGN out_endf='lines_noAGN'
* For other variations, optional variables might need to be added in the call to the gne function.

slurm_hdf5_run.py
-----------------
Scripts to submit the jobs for all the intended subvolumes (there are 64 for the UNITsim suite).

* For tests reduce the number of subvolumes and redshifts.
* Check the state of your runs with: squeue --me
 
plot_gne_*.sh
------------
Scripts to make plots using the whole simulation volume.

Parameters to change to math those used for run_gne_*.py:

* outpath
* out_endf

Other parameters to change:

* subvols = 64 (or for tests set to 1 or 2)
* snapshot = (values ran with slurm_hdf5_run.py)
