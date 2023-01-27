#import matplotlib as plt
import pylab as pl
#from amuse.units.units import *
import numpy as np
import pandas as pd
import sys


'''
python code to read and plot TRES output
@20211231 NMH
'''


# Membuka dan membaca data
# ========================

filename = open(sys.argv[1],'r')
#filename = open('TRES_5e3_3_200_output','r')
data = filename.readlines()


# Menutup data (katanya biar enggak rawan error)
# ==============================================

filename.close()


# Membuat list 
# ============

age = []
triple_number = []
relative_inclination_rad = []				# Radian
relative_inclination_deg = []				# Degree
dynamical_instability = []
kozai_type = []
error_flag_secular = []

binary_type_in = []
stability_in = []
semimajoraxis_in_rsun = []					# Rsun
semimajoraxis_in_au = []					# AU
eccentricity_in = []
argument_of_pericenter_in_rad = []			# Radian
argument_of_pericenter_in_deg = []			# Degree
argument_of_pericenter_in_mod = []			# Degree, modulo
longitude_of_ascending_node_in_rad = []		# Radian
longitude_of_ascending_node_in_deg = []		# Degree
longitude_of_ascending_node_in_mod = []		# Degree, modulo

binary_type_out = []
stability_out = []
semimajoraxis_out_rsun = []					# Rsun
semimajoraxis_out_au = []					# AU
eccentricity_out = []
argument_of_pericenter_out_rad = []			# Radian
argument_of_pericenter_out_deg = []			# Degree
argument_of_pericenter_out_mod = []			# Degree, modulo
longitude_of_ascending_node_out_rad = []	# Radian
longitude_of_ascending_node_out_deg = []	# Degree
longitude_of_ascending_node_out_mod = []	# Degree, modulo

is_donor_1 = []
stellar_type_1 = []
mass_1 = []									# Msun
spin_angular_frequency_1 = []				# Myr**-1
radius_1 = []								# Rsun
core_mass_1 = []							# Msun

is_donor_2 = []
stellar_type_2 = []
mass_2 = []									# Msun
spin_angular_frequency_2 = []				# Myr**-1
radius_2 = []								# Rsun
core_mass_2 = []							# Msun

is_donor_3 = []
stellar_type_3 = []
mass_3 = []									# Msun
spin_angular_frequency_3 = []				# Myr**-1
radius_3 = []								# Rsun
core_mass_3 = []							# Msun


# Memasukkan nilai ke list
# ========================

## Bisa pakai carai ini

for i in range(len(data)):

	if i in range(15,len(data),7):
		age.append(float(data[i].split()[1]))
	if i in range(15,len(data),7):
		triple_number.append(float(data[i].split()[3]))
	if i in range(15,len(data),7):
		relative_inclination_rad.append(float(data[i].split()[4]))
	if i in range(15,len(data),7):
		dynamical_instability.append(data[i].split()[5])
	if i in range(15,len(data),7):
		kozai_type.append(data[i].split()[6])
	if i in range(15,len(data),7):
		error_flag_secular.append(float(data[i].split()[7]))

	if i in range(16,len(data),7):
		binary_type_in.append(data[i].split()[1])
	if i in range(16,len(data),7):
		stability_in.append(data[i].split()[2])
	if i in range(16,len(data),7):
		semimajoraxis_in_rsun.append(float(data[i].split()[3]))
	if i in range(16,len(data),7):
		eccentricity_in.append(float(data[i].split()[5]))
	if i in range(16,len(data),7):
		argument_of_pericenter_in_rad.append(float(data[i].split()[6]))
	if i in range(16,len(data),7):
		longitude_of_ascending_node_in_rad.append(float(data[i].split()[7]))

	if i in range(17,len(data),7):
		binary_type_out.append(data[i].split()[1])
	if i in range(17,len(data),7):
		stability_out.append(data[i].split()[2])
	if i in range(17,len(data),7):
		semimajoraxis_out_rsun.append(float(data[i].split()[3]))
	if i in range(17,len(data),7):
		eccentricity_out.append(float(data[i].split()[5]))
	if i in range(17,len(data),7):
		argument_of_pericenter_out_rad.append(float(data[i].split()[6]))
	if i in range(17,len(data),7):
		longitude_of_ascending_node_out_rad.append(float(data[i].split()[7]))

	if i in range(18,len(data),7):
		is_donor_1.append(data[i].split()[1])
	if i in range(18,len(data),7):
		stellar_type_1.append(data[i].split()[2])
	if i in range(18,len(data),7):
		mass_1.append(float(data[i].split()[3]))
	if i in range(18,len(data),7):
		spin_angular_frequency_1.append(float(data[i].split()[5]))
	if i in range(18,len(data),7):
		radius_1.append(float(data[i].split()[7]))
	if i in range(18,len(data),7):
		core_mass_1.append(float(data[i].split()[9]))

	if i in range(19,len(data),7):
		is_donor_2.append(data[i].split()[1])
	if i in range(19,len(data),7):
		stellar_type_2.append(data[i].split()[2])
	if i in range(19,len(data),7):
		mass_2.append(float(data[i].split()[3]))
	if i in range(19,len(data),7):
		spin_angular_frequency_2.append(float(data[i].split()[5]))
	if i in range(19,len(data),7):
		radius_2.append(float(data[i].split()[7]))
	if i in range(19,len(data),7):
		core_mass_2.append(float(data[i].split()[9]))

	if i in range(20,len(data),7):
		is_donor_3.append(data[i].split()[1])
	if i in range(20,len(data),7):
		stellar_type_3.append(data[i].split()[2])
	if i in range(20,len(data),7):
		mass_3.append(float(data[i].split()[3]))
	if i in range(20,len(data),7):
		spin_angular_frequency_3.append(float(data[i].split()[5]))
	if i in range(20,len(data),7):
		radius_3.append(float(data[i].split()[7]))
	if i in range(20,len(data),7):
		core_mass_3.append(float(data[i].split()[9]))


## Atau cara ini biar lebih rapi

'''
print('age (Myr)')
for i in range(15,len(data),7):
	age.append(float(data[i].split()[1]))
	print(data[i].split()[1])
print()

print('a_in (R_sun)')
for i in range(16,len(data),7):
	a_in_rsun.append(float(data[i].split()[3]))
	print(data[i].split()[3])
print()

print('a_out (R_sun)')
for i in range(17,len(data),7):
	a_out_rsun.append(float(data[i].split()[3]))
	print(data[i].split()[3])
print()

print('m1 (M_sun)')
for i in range(18,len(data),7):
	m1.append(float(data[i].split()[3]))
	print(data[i].split()[3])
print()

print('m2 (M_sun)')
for i in range(19,len(data),7):
	m2.append(float(data[i].split()[3]))
	print(data[i].split()[3])
print()

print('m3 (M_sun)')
for i in range(20,len(data),7):
	m3.append(float(data[i].split()[3]))
	print(data[i].split()[3])
print()
'''


# Mengonversi satuan Rsun ke AU
# =============================

## 1 Sun's radius = 0.0046524726 AU, UA
## 1 AU, UA = 214.9394693836 Sun's radius

semimajoraxis_in_au = np.array(semimajoraxis_in_rsun)/214.9394693836
semimajoraxis_out_au = np.array(semimajoraxis_out_rsun)/214.9394693836

'''
print('a_in (AU)')
for i in range(len(a_in_au)):
	print(a_in_au[i])
print()

print('a_out (AU)')
for i in range(len(a_out_au)):
	print(a_out_au[i])
print()
'''


# Mengonversi satuan rad ke deg
# =============================

## np.pi rad = 180 deg
## 1 rad = 57.2958 deg

relative_inclination_deg = np.rad2deg(relative_inclination_rad)

argument_of_pericenter_in_deg = np.rad2deg(argument_of_pericenter_in_rad)
argument_of_pericenter_in_mod = argument_of_pericenter_in_deg % 360

longitude_of_ascending_node_in_deg = np.rad2deg(longitude_of_ascending_node_in_rad)
longitude_of_ascending_node_in_mod = longitude_of_ascending_node_in_deg % 360

argument_of_pericenter_out_deg = np.rad2deg(argument_of_pericenter_out_rad)
argument_of_pericenter_out_mod = argument_of_pericenter_out_deg % 360

longitude_of_ascending_node_out_deg = np.rad2deg(longitude_of_ascending_node_out_rad)
longitude_of_ascending_node_out_mod = longitude_of_ascending_node_out_deg % 360


# Membuat tabel
# =============

tabel = {'age (Myr)'									: age,
         'triple_number'								: triple_number,
         'relative_inclination (rad)'					: relative_inclination_rad,
         'relative_inclination (deg)'					: relative_inclination_deg,
         'dynamical_instability'						: dynamical_instability,
         'kozai_type'									: kozai_type,
         'error_flag_secular'							: error_flag_secular,

         'binary_type_in'								: binary_type_in,
         'stability_in'									: stability_in,
         'semimajoraxis_in (Rsun)'						: semimajoraxis_in_rsun,
         'semimajoraxis_in (AU)'						: semimajoraxis_in_au,
         'eccentricity_in'								: eccentricity_in,
         'argument_of_pericenter_in (rad)'				: argument_of_pericenter_in_rad,
         'argument_of_pericenter_in (deg)'				: argument_of_pericenter_in_deg,
         'argument_of_pericenter_in (deg,mod)'			: argument_of_pericenter_in_mod,
         'longitude_of_ascending_node_in (rad)'			: longitude_of_ascending_node_in_rad,
         'longitude_of_ascending_node_in (deg)'			: longitude_of_ascending_node_in_deg,
         'longitude_of_ascending_node_in (deg,mod)'		: longitude_of_ascending_node_in_mod,

         'binary_type_out'								: binary_type_out,
         'stability_out'								: stability_out,
         'semimajoraxis_out (Rsun)'						: semimajoraxis_out_rsun,
         'semimajoraxis_out (AU)'						: semimajoraxis_out_au,
         'eccentricity_out'								: eccentricity_out,
         'argument_of_pericenter_out (rad)'				: argument_of_pericenter_out_rad,
         'argument_of_pericenter_out (deg)'				: argument_of_pericenter_out_deg,
         'argument_of_pericenter_out (deg,mod)'			: argument_of_pericenter_out_mod,
         'longitude_of_ascending_node_out (rad)'		: longitude_of_ascending_node_out_rad,
         'longitude_of_ascending_node_out (deg)'		: longitude_of_ascending_node_out_deg,
         'longitude_of_ascending_node_out (deg,mod)'	: longitude_of_ascending_node_out_mod,

         'is_donor_1'									: is_donor_1,
         'stellar_type_1'								: stellar_type_1,
         'mass_1 (Msun)'								: mass_1,
         'spin_angular_frequency_1 (Myr**-1)'			: spin_angular_frequency_1,
         'radius_1 (Rsun)'								: radius_1,
         'core_mass_1 (Msun)'							: core_mass_1,

         'is_donor_2'									: is_donor_2,
         'stellar_type_2'								: stellar_type_2,
         'mass_2 (Msun)'								: mass_2,
         'spin_angular_frequency_2 (Myr**-1)'			: spin_angular_frequency_2,
         'radius_2 (Rsun)'								: radius_2,
         'core_mass_2 (Msun)'							: core_mass_2,

         'is_donor_3'									: is_donor_3,
         'stellar_type_3'								: stellar_type_3,
         'mass_3 (Msun)'								: mass_3,
         'spin_angular_frequency_3 (Myr**-1)'			: spin_angular_frequency_3,
         'radius_3 (Rsun)'								: radius_3,
         'core_mass_3 (Msun)'							: core_mass_3,
        }

#df = pd.DataFrame(tabel)
df = pd.DataFrame(tabel, columns=['age (Myr)','triple_number','relative_inclination (rad)','relative_inclination (deg)','dynamical_instability','kozai_type','error_flag_secular','binary_type_in','stability_in','semimajoraxis_in (Rsun)','semimajoraxis_in (AU)','eccentricity_in','argument_of_pericenter_in (rad)','argument_of_pericenter_in (deg)','argument_of_pericenter_in (deg,mod)','longitude_of_ascending_node_in (rad)','longitude_of_ascending_node_in (deg)','longitude_of_ascending_node_in (deg,mod)','binary_type_out','stability_out','semimajoraxis_out (Rsun)','semimajoraxis_out (AU)','eccentricity_out','argument_of_pericenter_out (rad)','argument_of_pericenter_out (deg)','argument_of_pericenter_out (deg,mod)','longitude_of_ascending_node_out (rad)','longitude_of_ascending_node_out (deg)','longitude_of_ascending_node_out (deg,mod)','is_donor_1','stellar_type_1','mass_1 (Msun)','spin_angular_frequency_1 (Myr**-1)','radius_1 (Rsun)','core_mass_1 (Msun)','is_donor_2','stellar_type_2','mass_2 (Msun)','spin_angular_frequency_2 (Myr**-1)','radius_2 (Rsun)','core_mass_2 (Msun)','is_donor_3','stellar_type_3','mass_3 (Msun)','spin_angular_frequency_3 (Myr**-1)','radius_3 (Rsun)','core_mass_3 (Msun)'])

#print (df[df.columns[::-1]])
###print (df)
#df.to_csv('TRES_output.csv')


# Membuat plot
# ============

pl.figure(1)											# Plot massa terhadap waktu
pl.plot(age,mass_1,label='m_1')							# Ini plot garis
pl.plot(age,mass_1,'o',color='blue')					# Ini plot titik, per snapshot
pl.plot(age,mass_2,label='m_2')
pl.plot(age,mass_2,'o',color='#ff7f0e')
pl.plot(age,mass_3,label='m_3')
pl.plot(age,mass_3,'o',color='green')
pl.xlabel('Age (Myr)')
pl.ylabel('Mass (M_sun)')
pl.title('Grafik Massa terhadap Waktu')
pl.legend()
pl.grid()
#pl.xlim(1450, 1500)			# TRES p1.1s0.9t2z0.02
#pl.ylim(1.8, 2)
#pl.xlim(1490, 1600)
#pl.ylim(0.6, 0.8)
#pl.xlim(1000, 2000)
#pl.xlim(1200, 1800)
#pl.xlim(1400, 1600)
#pl.xlim(1460, 1530)
#pl.xlim(1480, 1510)			# Best zoom (2)
#pl.xlim(1490, 1500)			# Best zoom (1)
#pl.xlim(2500, 4000)			# TRES p1.1s0.9t1.4z0.016
#pl.ylim(1.15, 1.45)
pl.xlim(3000, 4000)
#pl.ylim(0.4, 0.7)
#pl.xlim(3650, 3700)			# Best zoom
#pl.xlim(3500, 3700)
#pl.margins(x=-0.497, y=0.05)
#pl.savefig('Fig1_3200-3800.png')

pl.figure(2)											# Plot sumbu semi-mayor terhadap waktu
pl.plot(age,semimajoraxis_in_rsun,label='a_in')			# Satuannya Rsun
pl.plot(age,semimajoraxis_in_rsun,'o',color='blue')
pl.plot(age,semimajoraxis_out_rsun,label='a_out')
pl.plot(age,semimajoraxis_out_rsun,'o',color='#ff7f0e')
pl.xlabel('Age (Myr)')
pl.ylabel('Semi-major axis (R_sun)')
pl.title('Grafik Sumbu Semi-Mayor terhadap Waktu')
pl.legend()
pl.grid()
#pl.xlim(1100, 1600) 			# TRES p1.1s0.9t2z0.02
#pl.ylim(2400, 3900)
#pl.ylim(0, 50)
#pl.xlim(1480, 1510)
#pl.xlim(1490, 1500)
#pl.xlim(3650, 3700)			# TRES p1.1s0.9t1.4z0.016
#pl.ylim(2400, 3500)
#pl.ylim(0, 50)
#pl.savefig('Fig-2b.png')

pl.figure(3)											# Plot sumbu semi-mayor terhadap waktu
pl.plot(age,semimajoraxis_in_au,label='a_in')			# Satuannya AU
pl.plot(age,semimajoraxis_in_au,'o',color='blue')
pl.plot(age,semimajoraxis_out_au,label='a_out')
pl.plot(age,semimajoraxis_out_au,'o',color='#ff7f0e')
pl.xlabel('Age (Myr)')
pl.ylabel('Semi-major axis (AU)')
pl.title('Grafik Sumbu Semi-Mayor terhadap Waktu')
pl.legend()
pl.grid()
#pl.xlim(1100, 1600)
#pl.ylim(11.17, 18.14)
#pl.ylim(0, 0.23)
#pl.xlim(1480, 1510)
#pl.xlim(1490, 1500)
#pl.xlim(3650, 3700)			# TRES p1.1s0.9t1.4z0.016
#pl.ylim(11.17, 16.28)
#pl.ylim(0, 0.23)
#pl.savefig('Fig-3b.png')

pl.show()
