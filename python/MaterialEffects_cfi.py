# The following comments couldn't be translated into the new config version:

#        pi+      pi-    K0L      K+      K-      p      pbar     n      nbar
#	0.2508, 0.2549, 0.3380, 0.2879, 0.3171, 0.3282, 0.5371, 0.3859, 0.5086 # before 170 tuning

import FWCore.ParameterSet.Config as cms

# Material effects to be simulated in the tracker material and associated cuts
MaterialEffectsBlock = cms.PSet(
    MaterialEffects = cms.PSet(
        Bremsstrahlung = cms.bool(True),
        Density = cms.double(2.329),
        # The corresponding particle masses
        pionMasses = cms.untracked.vdouble(0.13957, 0.13957, 0.497648, 0.493677, 0.493677, 
            0.93827, 0.93827, 0.939565, 0.939565),
        K0Ls = cms.untracked.vint32(130, 310),
        NuclearInteraction = cms.bool(True),
        Kplusses = cms.untracked.vint32(321),
        antiprotons = cms.untracked.vint32(-2212, -3222),
        # The energies of the pions used in the above files (same order)
        pionEnergies = cms.untracked.vdouble(1.0, 2.0, 3.0, 4.0, 5.0, 
            7.0, 9.0, 12.0, 15.0, 20.0, 
            30.0, 50.0, 100.0, 200.0, 300.0, 
            500.0, 700.0, 1000.0),
        RadiationLength = cms.double(9.36),
        PairProduction = cms.bool(True),
        # The file with the last nuclear interaction read in the previous run
        # to be put in the local running directory (if desired)
        inputFile = cms.untracked.string('NuclearInteractionInputFile.txt'),
        Piminusses = cms.untracked.vint32(-211),
        bremEnergy = cms.double(0.1),
        antineutrons = cms.untracked.vint32(-2112, -3122, -3112, -3312, -3322, 
            -3334),
        distCut = cms.double(0.02), ## Default is 0.020 for algo 1;

        photonEnergy = cms.double(0.1),
        A = cms.double(28.0855),
        bremEnergyFraction = cms.double(0.005),
        MultipleScattering = cms.bool(True),
        # The particle types simulated
        pionTypes = cms.untracked.vint32(211, -211, 130, 321, -321, 
            2212, -2212, 2112, -2112),
        # The scaling of the inelastic cross section with energy 
        ratios = cms.untracked.vdouble(0.031390573, 0.531842852, 0.819614219, 0.951251711, 0.98638275, 
            1.0, 0.985087033, 0.982996773, 0.990832192, 0.992237923, 
            0.99484158, 0.973816742, 0.967264815, 0.971714258, 0.969122824, 
            0.978681792, 0.977312732, 0.984255819, 0.035326512, 0.577356403, 
            0.857118809, 0.965683504, 0.98965936, 1.0, 0.98959924, 
            0.980665408, 0.988384816, 0.981038152, 0.975002104, 0.959996152, 
            0.953310808, 0.954705592, 0.9576154, 0.961150456, 0.965022184, 
            0.960573304, 0.0, 0.370261189, 0.649793096, 0.734342408, 
            0.749079499, 0.753360057, 0.755790543, 0.755872164, 0.751337674, 
            0.746685288, 0.747519634, 0.739357554, 0.735004444, 0.803039922, 
            0.832749896, 0.890900187, 0.936734805, 1.0, 0.0, 
            0.175571717, 0.391683394, 0.528946472, 0.572818635, 0.61421028, 
            0.644125538, 0.67030405, 0.685144573, 0.702870161, 0.714708513, 
            0.730805263, 0.777711536, 0.831090576, 0.869267129, 0.915747562, 
            0.953370523, 1.0, 0.0, 0.36535321, 0.611663677, 
            0.715315908, 0.733498956, 0.738361302, 0.745253654, 0.751459671, 
            0.750628335, 0.746442657, 0.750850669, 0.744895986, 0.73509396, 
            0.791663444, 0.828609543, 0.88999304, 0.940897842, 1.0, 
            0.0, 0.042849136, 0.459103223, 0.666165343, 0.787930873, 
            0.890397011, 0.920999533, 0.937832788, 0.950920131, 0.966595049, 
            0.97954227, 0.988061653, 0.983260159, 0.988958431, 0.991723494, 
            0.995273237, 1.0, 0.999962634, 1.0, 0.849956907, 
            0.775625988, 0.80201823, 0.816207485, 0.785899785, 0.754998487, 
            0.728977244, 0.710010673, 0.670890339, 0.665627872, 0.652682888, 
            0.613334247, 0.647534574, 0.667910938, 0.689919693, 0.709200185, 
            0.724199928, 0.0, 0.059216484, 0.437844536, 0.610370629, 
            0.702090648, 0.78007689, 0.802143073, 0.819570432, 0.825829666, 
            0.84007975, 0.838435509, 0.837529986, 0.835687165, 0.885205014, 
            0.912450156, 0.951451221, 0.973215562, 1.0, 1.0, 
            0.849573257, 0.756479495, 0.787147094, 0.804572414, 0.791806302, 
            0.760234588, 0.741109531, 0.724118186, 0.692829761, 0.688465897, 
            0.671806061, 0.636461171, 0.675314029, 0.69913446, 0.724305037, 
            0.742556115, 0.758504713),
        # and a global fudge factor for TEC Layers to make it fit
        fudgeFactor = cms.double(1.2),
        # The algorihm to detrmine the distance between the primary and the secondaries
        # 0 = no link
        # 1 = sin(theta12) - ~ ok at all momenta
        # 2 = sin(theta12) * p1/p2 - bad, should not be used
        distAlgo = cms.uint32(1),
        # The corresponding smallest momenta for which an inleatic interaction may occur
        pionMinP = cms.untracked.vdouble(0.7, 0.0, 1.0, 1.0, 0.0, 
            1.1, 0.0, 1.1, 0.0),
        Z = cms.double(14.0),
        neutrons = cms.untracked.vint32(2112, 3122, 3112, 3312, 3322, 
            3334),
        # The ratio between radiation lengths and interation lengths in the tracker at 15 GeV
        lengthRatio = cms.vdouble(0.2257, 0.2294, 0.3042, 0.2591, 0.2854, 
            0.3101, 0.5216, 0.3668, 0.4898),
        # The correspondence between long-lived hadrons/ions and the simulated hadron list
        protons = cms.untracked.vint32(2212, 3222, -101, -102, -103, 
            -104),
        #
        # The smallest pion energy for which nuclear interactions are simulated
        pionEnergy = cms.double(0.5),
        pTmin = cms.double(0.3),
        Piplusses = cms.untracked.vint32(211),
        EnergyLoss = cms.bool(True),
        Kminusses = cms.untracked.vint32(-321),
        # The corresponding particle names
        pionNames = cms.untracked.vstring('piplus', 
            'piminus', 
            'K0L', 
            'Kplus', 
            'Kminus', 
            'p', 
            'pbar', 
            'n', 
            'nbar')
    )
)
MaterialEffectsForMuonsBlock = cms.PSet(
    MaterialEffectsForMuons = cms.PSet(
        A = cms.double(55.8455),
        bremEnergyFraction = cms.double(0.005),
        Bremsstrahlung = cms.bool(False),
        bremEnergy = cms.double(0.1),
        Density = cms.double(7.87),
        MultipleScattering = cms.bool(True),
        NuclearInteraction = cms.bool(False),
        photonEnergy = cms.double(0.1),
        PairProduction = cms.bool(False),
        EnergyLoss = cms.bool(False),
        pTmin = cms.double(0.3),
        RadiationLength = cms.double(1.76),
        Z = cms.double(26.0)
    )
)

