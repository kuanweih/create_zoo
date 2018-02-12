#!/bin/bash


# Make files named with the random seed (defined as a 6 digits string)
randomseed=000034
mkdir  run_10Mpc_$randomseed

cd  run_10Mpc_$randomseed
mkdir  ICs  Run_seed5e3  Run_seed5e4  Run_seed5e5

ics_runs='ICs  Run_seed5e3  Run_seed5e4  Run_seed5e5'
for i in $ics_runs; do
    mkdir  $i/Con_0  $i/Con_1  $i/Con_2
done

runs='Run_seed5e3  Run_seed5e4  Run_seed5e5'
cons='Con_0  Con_1  Con_2'
for con in $cons; do

    mkdir  ICs/$con/fastpm  ICs/$con/constrained
    python  ../writing_standard-lua.py  ICs/$con/fastpm  $randomseed  $con
    python  ../writing_submit_fastpm.py  ICs/$con/fastpm  constrain
    python  ../writing_para_con-param.py  ICs/$con/constrained  constrain
    python  ../writing_submit_constrained.py  ICs/$con/constrained

    for run in $runs; do
        python  ../writing_run-param.py  $run/$con  $run  $con
        python  ../writing_submit_mpgadget.py  $run/$con
    done
done

python  ../writing_submit_fastpm.py  ICs/Con_0/fastpm  noconstain
python  ../writing_para_con-param.py  ICs/Con_0/constrained  noconstrain
