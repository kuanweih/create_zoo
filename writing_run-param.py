import argparse

parser = argparse.ArgumentParser()
parser.add_argument('path')
parser.add_argument('bhseed')
parser.add_argument('con')
args = parser.parse_args()

fastpm_path = args.path
bhseedmass = str(args.bhseed)
con = args.con

f = open('{0}/run-10MPC.param'.format(fastpm_path),'w')

f.write('%  Relevant files \n')
f.write('InitCondFile       ../../ICs/{0}/IC \n'.format(con))
f.write('OutputDir          ../{0} \n'.format(con))
f.write('TreeCoolFile       /home/kuanweih/CaseMP/InputMP/inputfiles/TREECOOL_fg_june11 \n')
f.write('MetalCoolFile      /home/kuanweih/CaseMP/InputMP/inputfiles/cooling_metal_UVB.hdf5 \n')
f.write(' \n')
f.write('OutputList  0.0322580645161, 0.0333333333333, 0.0344827586207, 0.0357142857143, 0.037037037037, 0.0384615384615, 0.04, 0.0416666666667, 0.0434782608696, 0.0454545454545, 0.047619047619, 0.05, 0.0526315789474, 0.0555555555556, 0.0588235294118, 0.0625, 0.0666666666667, 0.0714285714286, 0.0769230769231, 0.0833333333333, 0.0909090909091, 0.1, 0.111111111111, 0.125, 0.142857142857, 0.166666666667, 0.2, 0.25, 0.333333333333, 0.5, 1.0 \n')
f.write(' \n')
f.write('SnapshotFileBase   snapshot \n')
f.write('SnapshotWithFOF    1 \n')
f.write(' \n')
f.write('%RestartFromBlueTidesPhaseI 0 \n')
f.write(' \n')
f.write('DomainOverDecompositionFactor 8 \n')
f.write(' \n')
f.write('%EnableAggregatedIO 0 \n')
f.write(' \n')
f.write('Nmesh         176 \n')
f.write('NumWriters     16 \n')
f.write(' \n')
f.write('% CPU time -limit \n')
f.write('TimeLimitCPU     3600000 \n')
f.write(' \n')
f.write(' \n')
f.write('% Code options \n')
f.write('TypeOfTimestepCriterion  0 \n')
f.write(' \n')
f.write('%  Characteristics of run \n')
f.write('TimeBegin           0.01 \n')
f.write('TimeMax	            1.00 \n')
f.write(' \n')
f.write('Omega0              0.2814        % Total matter density  (at z=0) \n')
f.write('OmegaLambda         0.7186        % Cosmological constant (at z=0) \n')
f.write('OmegaBaryon         0.0464        % Baryon density        (at z=0) \n')
f.write('HubbleParam         0.697         % Hubble paramater (may be used for power spec parameterization) \n')
f.write('BoxSize             10.0 \n')
f.write(' \n')
f.write('CoolingOn             1 \n')
f.write('StarformationOn       1 \n')
f.write('StarformationCriterion  density,h2 \n')
f.write('HydroOn               1 \n')
f.write('BlackHoleOn           1 \n')
f.write('RadiationOn           0 \n')
f.write(' \n')
f.write('CpuTimeBetRestartFile  3600.0 \n')
f.write(' \n')
f.write(' \n')
f.write('% Accuracy of time integration \n')
f.write('MaxSizeTimestep       0.1 \n')
f.write('MinSizeTimestep       0.00 \n')
f.write(' \n')
f.write('FOFHaloLinkingLength        0.2 \n')
f.write('FOFHaloMinLength            32 \n')
f.write(' \n')
f.write('%  Further parameters of SPH \n')
f.write('DensityKernelType      quintic \n')
f.write(' \n')
f.write('DensityContrastLimit   100     % max contrast for hydro force calculation \n')
f.write('DensityResolutionEta   1.0     % for Cubic spline 1.0 = 33 \n')
f.write('MaxNumNgbDeviation     2 \n')
f.write('ArtBulkViscConst       0.75 \n')
f.write('InitGasTemp            580.0   % always ignored if set to 0 \n')
f.write('MinGasTemp             5.0 \n')
f.write(' \n')
f.write(' \n')
f.write('% Memory allocation \n')
f.write(' \n')
f.write('PartAllocFactor       2.0 \n')
f.write('BufferSize            100          % in MByte \n')
f.write('MaxMemSizePerCore     1600 \n')
f.write(' \n')
f.write(' \n')
f.write('%-----------------Softening lengths--------------------- \n')
f.write('MinGasHsmlFractional 0.00 \n')
f.write(' \n')
f.write('SofteningGas       0.0015 \n')
f.write('SofteningHalo      0.0015 \n')
f.write('SofteningDisk      0 \n')
f.write('SofteningBulge     0 \n')
f.write('SofteningStars     0.0015 \n')
f.write('SofteningBndry     0.0015 \n')
f.write(' \n')
f.write('SofteningGasMaxPhys       0.0015 \n')
f.write('SofteningHaloMaxPhys      0.0015 \n')
f.write('SofteningDiskMaxPhys      0 \n')
f.write('SofteningBulgeMaxPhys     0 \n')
f.write('SofteningStarsMaxPhys     0.0015 \n')
f.write('SofteningBndryMaxPhys     0.0015      %This is BH \n')
f.write(' \n')
f.write(' \n')
f.write('%----------------------BH Stuff------------------------- \n')
f.write('BlackHoleFeedbackFactor          0.05 \n')
f.write('BlackHoleFeedbackRadius          0. \n')
f.write('BlackHoleFeedbackRadiusMaxPhys   0. \n')
f.write('BlackHoleFeedbackMethod          spline | mass \n')

if bhseedmass == 'Run_seed5e5':
    f.write('SeedBlackHoleMass                5.0e-5 \n')
elif bhseedmass == 'Run_seed5e4':
    f.write('SeedBlackHoleMass                5.0e-6 \n')
elif bhseedmass == 'Run_seed5e3':
    f.write('SeedBlackHoleMass                5.0e-7 \n')
else:
    f.write('Wrong BH seed mass!! \n')

f.write('BlackHoleAccretionFactor         100.0 \n')
f.write('BlackHoleNgbFactor               2.0 \n')
f.write('BlackHoleEddingtonFactor         3.0 \n')
f.write(' \n')

if bhseedmass == 'Run_seed5e5':
    f.write('MinFoFMassForNewSeed             5 \n')
elif bhseedmass == 'Run_seed5e4':
    f.write('MinFoFMassForNewSeed             5e-1 \n')
elif bhseedmass == 'Run_seed5e3':
    f.write('MinFoFMassForNewSeed             5e-2 \n')
else:
    f.write('Wrong BH seed mass!! \n')

f.write('TimeBetweenSeedingSearch         1.05 \n')
f.write(' \n')
f.write(' \n')
f.write('%----------------------SFR Stuff------------------------- \n')
f.write('CritPhysDensity      0        %  critical physical density for star formation \n')
f.write('                              %  in hydrogen number density in cm^(-3) \n')
f.write(' \n')
f.write('CritOverDensity      57.7     %  overdensity threshold value \n')
f.write(' \n')
f.write('QuickLymanAlphaProbability  0 % Set to 1.0 to turn dense gas directly into stars. \n')
f.write(' \n')
f.write('MaxSfrTimescale      1.5      % in internal time units \n')
f.write(' \n')
f.write('TempSupernova        1.0e8    %  in Kelvin \n')
f.write(' \n')
f.write('TempClouds           1000.0   %  in Kelvin \n')
f.write('FactorSN             0.1 \n')
f.write('FactorEVP            1000.0 \n')
f.write(' \n')
f.write('WindModel            ofjt10 | decouple % ofjt10,decouple \n')
f.write('WindEfficiency                     2.0 \n')
f.write('WindEnergyFraction                 1.0 \n')
f.write('WindSigma0             353.0  % km/s \n')
f.write('WindSpeedFactor        3.7 \n')
f.write(' \n')
f.write('WindFreeTravelLength               20 \n')
f.write('WindFreeTravelDensFac              0.1 \n')

f.close()
