''' Generate and submit SLURM jobs for running GNE (get_nebular_emission) '''
import os
import gne.gne_slurm as sl

verbose = True

check = True   # Check slurm queues
clean = False   # Clean logs

# Options
model = 'Galform' #'Shark'
snap = 128
job_suffix = None 
  
# Check or clean
logdir =  os.path.join(os.getcwd(),'logs')
if check:
    results = sl.check_all_jobs(model,snap,logdir,
                                job_suffix=job_suffix,verbose=True)
if clean:
    sl.clean_all_jobs(model,snap,logdir,job_suffix=job_suffix,
                      only_show=False,verbose=verbose)
