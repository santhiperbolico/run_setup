''' Generate and submit SLURM jobs for running GNE (get_nebular_emission) '''
import os
import gne.gne_slurm as sl

verbose = True
subvols = 64

submit_jobs = True    # False to only generate scripts (sbatch *.sh)
check_all_jobs = False # Check slurm queues
clean = False          # Clean logs

# Optional: user-defined suffix for job names
# If None, suffix is derived from cutcols/mincuts/maxcuts in param_file
job_suffix = None 

# Taurus
hpc = 'taurus'
sam = 'Galform' #'Shark'

simulations = {
    "Galform": {
        "script": "run_gne_SU1_galform.py",
        "runs": [
            ('SU1', [87]),
            #('SU1', [109, 104, 98, 90, 87, 128, 96, 78]),
            #('SU1', [128, 90, 87, 96, 78]),
            #('SU2', [90]),
            #('UNIT1GPC_fnl0', [128, 90]),
            #('UNIT1GPC_fnl100', [127, 89]),
            #('SU1', [109, 104, 98, 90, 96, 78]),
            #('SU2', [109, 104, 98, 90, 87]),
            #('UNIT1GPC_fnl0', [98, 109, 87, 90, 104]),
            #('UNIT1GPC_fnl100', [108, 103, 97, 89, 86]),
        ]
    },
    "Shark": {
        "script": "run_gne_shark.py",
        "runs": [
            ('SU1', [87]),
            #('SU1', [128, 90, 87, 96, 78]),
            #('SU2', [128, 90]),
            #('UNIT1GPC_fnl0', [128, 90]),
            #('UNIT1GPC_fnl100', [127, 89]),
        ]
    }
}


# Parameter file to use as base
# The catalogue path, subvols and snapshot will be modified
param_file = os.path.join(os.getcwd(),simulations[sam]["script"])

# Select which runs to process
runs = simulations[sam]["runs"]
if hpc=='taurus':
    root = '/data21/users/vgonzalez/Data'

logdir =  os.path.join(os.getcwd(),'logs')
    
# Submit, check or clean
if clean:
    sl.clean_all_jobs(runs,root,sam,param_file,subvols,only_show=True,
                      logdir=logdir,job_suffix=job_suffix)
elif check_all_jobs:
    results = sl.check_all_jobs(runs, root, sam, param_file, subvols,
                                logdir=logdir,job_suffix=job_suffix,verbose=True)
else:    
    job_count = 0
    for sim, snaps in runs:
        simpath = os.path.join(root,sam,sim)
        for snap in snaps:
            # Generate SLURM script
            script_path, job_name = sl.create_slurm_script(
                hpc, param_file, simpath, snap, subvols,
                logdir=logdir,job_suffix=job_suffix,
                verbose=verbose
            )
            if verbose: 
                print(f'  Created script: {script_path}')
                
            # Submit the job
            if submit_jobs:
                job_id = sl.submit_slurm_job(script_path,job_name)
                if job_id is not None:
                    job_count += 1
    
    if submit_jobs and verbose:
        print(f'Total jobs submitted: {job_count}')

