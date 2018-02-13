import argparse

parser = argparse.ArgumentParser()
parser.add_argument('path')
args = parser.parse_args()

fastpm_path = args.path

f = open('{0}/submitcoma.job'.format(fastpm_path),'w')

f.write('#!/bin/bash                                                                                                                 \n')
f.write('#PBS -N Cons-GenIC \n')
f.write('#PBS -M abcd28s@gmail.com \n')
f.write('#PBS -m abe \n')
f.write('#PBS -l nodes=1:ppn=16 \n')
f.write('#PBS -l walltime=7:00:00:00 \n')

f.write('export OMP_NUM_THREADS=1 \n')

f.write('cd $PBS_O_WORKDIR \n')
f.write('#source  ~yfeng1/local/bin/setup.sh \n')
f.write('source  ~/setup.sh  \n')

f.write('ROOT=/physics2/kuanweih/project_BH_seedmass \n')
f.write('mpirun  -np  16  $ROOT/Constrained/build/Cons-GenIC  param_Constrained.param  1>stdout  2>stderr \n')

f.close()
