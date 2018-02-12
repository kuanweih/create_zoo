import argparse

parser = argparse.ArgumentParser()
parser.add_argument('path')
parser.add_argument('constrain')
args = parser.parse_args()

fastpm_path = args.path
constrain_arg = args.constrain

f = open('{0}/submitcoma.job'.format(fastpm_path),'w')

f.write('#!/bin/bash                                                                                                                 \n')
f.write('#PBS -N FastPM \n')
f.write('#PBS -M abcd28s@gmail.com \n')
f.write('#PBS -m abe \n')
f.write('#PBS -l nodes=1:ppn=16 \n')
f.write('#PBS -l walltime=7:00:00:00 \n')

f.write('export OMP_NUM_THREADS=1 \n')

f.write('cd $PBS_O_WORKDIR \n')
f.write('#source  ~yfeng1/local/bin/setup.sh \n')
f.write('source  ~/setup.sh  \n')

if constrain_arg == 'constrain':
    f.write('mpirun  -np  96  /physics2/kuanweih/project_BH_seedmass/fastpm/src/fastpm  standard.lua  za  constrain  1>stdout  2>stderr \n')
else:
    f.write('mpirun  -np  96  /physics2/kuanweih/project_BH_seedmass/fastpm/src/fastpm  standard.lua  za  1>stdout  2>stderr \n')

f.close()
