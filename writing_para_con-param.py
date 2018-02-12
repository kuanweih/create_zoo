import argparse

parser = argparse.ArgumentParser()
parser.add_argument('path')
parser.add_argument('constrain')
args = parser.parse_args()

fastpm_path = args.path
constrain_arg = args.constrain

f = open('{0}/param_Constrained.param'.format(fastpm_path),'w')

if constrain_arg == 'constrain':
    f.write('InitCondFile                    {0}/../fastpm/results-za-constrain/fastpm_0.0100 \n'.format(fastpm_path))
else:
    f.write('InitCondFile                    {0}/../fastpm/results-za/fastpm_0.0100 \n'.format(fastpm_path))

f.write('OutputDir                       {0} \n'.format(fastpm_path))
f.write('FileBase                        IC \n')
f.write('Omega0                          0.2814          % Total matter density  (at z=0) \n')
f.write('OmegaLambda                     0.7186          % Cosmological constant (at z=0) \n')
f.write('OmegaBaryon                     0.0464          % Baryon density        (at z=0) \n')
f.write('HubbleParam                     0.697           % Hubble paramater (may be used for power spec parameterization) \n')
f.write('TimeBegin                       0.01            % scale factor \n')
f.write('BoxSize                         20.0            % Mpc per side \n')
f.write('ProduceGas                      1               % 0:off, 1:on \n')
f.write('MaxMemSizePerCore               1800 \n')
f.write('NumPartPerFile                  131072 \n')
f.write('NumWriters                      16 \n')
f.write('EnableAggregatedIO              1 \n')
f.write('UnitLength_in_cm                3.085678e24     % defines length unit of output (Mpc in cm/h) \n')
f.write('UnitMass_in_g                   1.989e43        % defines mass unit of output (in g/cm) \n')
f.write('UnitVelocity_in_cm_per_s        1e5             % defines velocity unit of output (in cm/sec) \n')

f.close()
