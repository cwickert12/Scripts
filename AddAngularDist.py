#!/usr/bin/env python
# coding: utf-8

# Import system-level operations and add custom module path
import sys
sys.path.append('/home/cwickert/ENDFtk/build/')  # Add ENDFtk build path to import the module

# Import the ENDFtk library for ENDF file parsing and matplotlib for plotting (though not used in this script)
import ENDFtk
import matplotlib.pyplot as plt

# Load two ENDF tapes: one with existing data (tape20), and one with updated angular distributions (tape21)
tape20 = ENDFtk.tree.Tape.from_file('tape20')
tape21 = ENDFtk.tree.Tape.from_file('tape21')

# Extract MF4 (angular distributions) from the first material in each tape
file40 = tape20.material(tape20.material_numbers[0]).file(4).parse()
sections40 = file40.sections.to_list()

file41 = tape21.material(tape21.material_numbers[0]).file(4).parse()
sections41 = file41.sections.to_list()

# Extract angular distribution data (could be Legendre or Tabulated)
distribution1 = sections41[0].angular_distributions[:]  # Updated data
distribution0 = sections40[0].angular_distributions[:]  # Original data

# Store interpolation information from the updated file
main = sections41[0].distributions

# Find the maximum energy in the updated data
Emax = float(distribution1[-1].E)

# Identify the index in the original data where energy exceeds the maximum of updated data
for i, d in enumerate(distribution0):
    if float(d.E) > Emax:
        istart = i
        break

# Merge updated and original distributions, but only those with energies above Emax from original
# Separate them into Legendre and Tabulated distributions
legendre_distributions = [
    d for d in (distribution1 + distribution0[i:]) if isinstance(d, ENDFtk.MF4.LegendreCoefficients)
]
tabulated_distributions = [
    d for d in (distribution1 + distribution0[i:]) if isinstance(d, ENDFtk.MF4.TabulatedDistribution)
]

# Reconstruct the Legendre part of the MF4 section
new_legendre = ENDFtk.MF4.LegendreDistributions(
    [len(legendre_distributions)], 
    main.interpolants.to_list(), 
    legendre_distributions
)

# Initialize Tabulated container (only if present)
new_tabulated = []
if len(tabulated_distributions) != 0:
    new_tabulated = ENDFtk.MF4.TabulatedDistributions(
        [len(tabulated_distributions)], 
        main.interpolants.to_list(), 
        tabulated_distributions
    )
    # Combine both Legendre and Tabulated distributions
    combined = ENDFtk.MF4.MixedDistributions(new_legendre, new_tabulated)
else: 
    # Use only Legendre distributions if no tabulated data exists
    combined = new_legendre

# Create a new MF4 section with the merged distribution data
sections_new = ENDFtk.MF4.Section(
    sections41[0].MT, 
    sections41[0].ZA, 
    sections41[0].AWR, 
    sections41[0].LCT, 
    combined
)

# Replace the original MF4 section in tape20 with the new merged section
tape20.material(tape20.material_numbers[0]).file(4).insert_or_replace(sections_new)

# Write the updated tape to a new file
tape20.to_file('tape22')
