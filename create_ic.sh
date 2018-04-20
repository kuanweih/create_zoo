#!/bin/bash


# Create a main file named with following vars
randomseed=000000  # Random seed (6 digits string)
boxsize=10         # Mpc/h
n_particle=176     # Number of particles
con=Con_0       # Constraints in fastpm (0:no cons)
main_dir=ic-"$randomseed"-"$con"-"$boxsize"Mpc-"$n_particle"
mkdir  $main_dir

# Work under the main directory
cd  $main_dir

# Create files
mkdir  fastpm  constrained
if [ "$con" = Con_0 ]; then  # without a constraint
    python  ../writing_standard-lua.py  fastpm  $randomseed  $con  $boxsize  $n_particle
    python  ../writing_submit_fastpm.py  fastpm  noconstain
    python  ../writing_para_con-param.py  constrained  noconstrain  $boxsize
    python  ../writing_submit_constrained.py  constrained
else  # with constraints
    python  ../writing_standard-lua.py  fastpm  $randomseed  $con  $boxsize  $n_particle
    python  ../writing_submit_fastpm.py  fastpm  constrain
    python  ../writing_para_con-param.py  constrained  constrain  $boxsize
    python  ../writing_submit_constrained.py  constrained
fi
