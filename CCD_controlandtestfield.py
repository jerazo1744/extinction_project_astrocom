from sys import argv
import csv
import numpy as np
import matplotlib.pyplot as plt
from pylab import *

#BEGIN CODE FOR CONTROL FIELD
controlfile = open('351_neg14_NOMAD_BLANKS_10arcmin_box.txt', 'r')

#read all of the lines in the file
read_line = controlfile.readlines()
  
#Change line number according to the line in file, range is number of characters and placement of characters in the string
#R Magnitude
R_mag0 = read_line[0][123:129]

#define R_mag as a list
R_mag = []

for R_mag0 in read_line:
	R_mag1 = R_mag0[123:129] #read this column of specific numbers
	if R_mag1 == "      ": #if R_mag1 has these blanks
		R_mag1 = -99        #replace with -99
	R_mag.append(float(R_mag1)) #append the last number into the list	

#B Magnitude
B_mag0 = read_line[0][105:111]
B_mag = []
B_mag2 = []

for B_mag0 in read_line:
	B_mag1 = B_mag0[105:111]
	if B_mag1 == "      ":
		B_mag1 = -99
	B_mag.append(float(B_mag1))

R1 = []
B1 = []
for R_mag0 in read_line:
	R_mag1 = R_mag0[123:129] #read this column of specific numbers
	if R_mag1 == "      ": #if R_mag1 has these blanks
		R_mag1 = nan        #replace with nan
	R1.append(float(R_mag1)) #append the last number into the list	

for B_mag0 in read_line:
	B_mag1 = B_mag0[105:111]
	if B_mag1 == "      ":
		B_mag1 = nan
	B1.append(float(B_mag1))

R2 = np.array(R1) #turn into an array
B2 = np.array(B1)

fin_R = np.isfinite(R2) #to find the nans in R2

fin_B = np.isfinite(B1) #to find nans in B2

cutBR = np.logical_and(fin_R, fin_B) #create the index to exclude nans from both

R_mag_BR = R2[cutBR]
B_mag_BR = B2[cutBR]

#MEDIAN for B-R
B_R = np.subtract(B_mag_BR, R_mag_BR) #subtract R_mag from B_mag -> B-R 
okay0 = np.where((B_R < 20) & (B_R > -20)) #in B_R, find where it is less than 20 and greater than -20
okay1 = B_R[okay0]
B_Rmed = np.median(okay1)
print B_Rmed

#V Magnitude
V_mag0 = read_line[0][114:120]

V_mag = []

for V_mag0 in read_line:
	V_mag1 = V_mag0[114:120]
	if V_mag1 == "      ":
		V_mag1 = -99
	V_mag.append(float(V_mag1))

V1=[]

for V_mag0 in read_line:
	V_mag1 = V_mag0[114:120] #read this column of specific numbers
	if V_mag1 == "      ": #if V_mag1 has these blanks
		V_mag1 = nan        #replace with nan
	V1.append(float(V_mag1)) #append the last number into the list	

V2 = np.array(V1)
	
fin_V = np.isfinite(V2)

cutBV = np.logical_and(fin_V, fin_B)

V_mag_BV = V2[cutBV]
B_mag_BV = B2[cutBV]

#MEDIAN for B-V
B_V = np.subtract(B_mag_BV, V_mag_BV)
okay2 = np.where((B_V < 20) & (B_V > -20))
okay3 = B_V[okay2]
B_Vmed = np.median(okay3)
print B_Vmed

#J Magnitude
J_mag0 = read_line[0][132:138]
J_mag = []

for J_mag0 in read_line:
	J_mag1 = J_mag0[132:138]
	if J_mag1 == "      ":
		J_mag1 = -99
	J_mag.append(float(J_mag1))
	
J_mag = np.array(J_mag)

J1=[]
for J_mag0 in read_line:
	J_mag1 = J_mag0[132:138] 
	if J_mag1 == "      ": 
		J_mag1 = nan        
	J1.append(float(J_mag1)) 	

J2 = np.array(J1)
	
fin_J = np.isfinite(J2)

cutRJ = np.logical_and(fin_J, fin_R)

J_mag_RJ = J2[cutRJ]
R_mag_RJ = R2[cutRJ]

#MEDIAN for R-J
R_J = np.subtract(R_mag_RJ, J_mag_RJ)
okay4 = np.where((R_J < 20) & (R_J > -20))
okay5 = R_J[okay4]
R_Jmed = np.median(okay5)
print R_Jmed

#H Magnitude
H_mag0 = read_line[0][139:145]
H_mag = []

for H_mag0 in read_line:
	H_mag1 = H_mag0[139:145]
	if H_mag1 == "      ":
		H_mag1 = -99
	H_mag.append(float(H_mag1))

H1=[]

for H_mag0 in read_line:
	H_mag1 = H_mag0[139:145]
	if H_mag1 == "      ":
		H_mag1 = nan
	H1.append(float(H_mag1))

H2 = np.array(H1)

fin_H = np.isfinite(H2)

cutJH = np.logical_and(fin_H, fin_J)

H_mag_JH = H2[cutJH]
J_mag_JH = J2[cutJH]
	
#MEDIAN for J-H
J_H = np.subtract(J_mag_JH, H_mag_JH)
okay6 = np.where((J_H < 20) & (J_H > -20))
okay7 = J_H[okay6]
J_Hmed = np.median(okay7)
print J_Hmed

#K Magnitude
K_mag0 = read_line[0][146:152]
K_mag = []

for K_mag0 in read_line:
	K_mag1 = K_mag0[146:152]
	if K_mag1 == "      ":
		K_mag1 = -99
	K_mag.append(float(K_mag1))

K1=[]

for K_mag0 in read_line:
	K_mag1 = K_mag0[146:152]
	if K_mag1 == "      ":
		K_mag1 = nan
	K1.append(float(K_mag1))

K2 = np.array(K1)

fin_K = np.isfinite(K2)

cutHK = np.logical_and(fin_K, fin_H)

H_mag_HK = H2[cutHK]
K_mag_HK = K2[cutHK]

#MEDIAN for H-K
H_K = np.subtract(H_mag_HK, K_mag_HK)
okay8 = np.where((H_K < 20) & (H_K > -20))
okay9 = H_K[okay8]
H_Kmed = np.median(okay9)
print H_Kmed

#MEDIAN for V-R
cutVR = np.logical_and(fin_R, fin_V)

V_mag_VR = V2[cutVR]
R_mag_VR = R2[cutVR]

V_R = np.subtract(V_mag_VR, R_mag_VR)
okay10 = np.where((V_R < 20) & (V_R > -20))
okay11 = V_R[okay10]
V_Rmed = np.median(okay11)
print V_Rmed

'''#R-J v. J-H function CONTROL FIELD
def JRH(J, R, H): #create a function: def function_name(parameters)
	list=[] #empty list
	for i in range(0,len(J)):
		if np.isfinite(J[i]) and np.isfinite(R[i]) and np.isfinite(H[i]):
			list.append(True)
		else:
			list.append(False)
	array = np.array(list)
	return array

#Create index for R-J v. J-H
index_JRH = JRH(J2, R2, H2)

J3 = J2[index_JRH]
R3 = R2[index_JRH]
H3 = H2[index_JRH]

R_J_graph = np.subtract(R3, J3)
J_H_graph = np.subtract(J3, H3)

#J-H v. H-K function CONTROL FIELD
def JHK(J, H, K): #create a function: def function_name(parameters)
	list=[] #empty list
	for i in range(0,len(H)):
		if np.isfinite(J[i]) and np.isfinite(H[i]) and np.isfinite(K[i]):
			list.append(True)
		else:
			list.append(False)
	array = np.array(list)
	return array

#Create index for J-H v. H-K
index_JHK = JHK(J2, H2, K2)

J3 = J2[index_JHK]
H3 = H2[index_JHK]
K3 = K2[index_JHK]

J_H_graph = np.subtract(J3, H3)
H_K_graph = np.subtract(H3, K3)

#B-R v. R-J function CONTROL FIELD
def BRJ(B, R, J): #create a function: def function_name(parameters)
	list=[] #empty list
	for i in range(0,len(R)):
		if np.isfinite(B[i]) and np.isfinite(R[i]) and np.isfinite(J[i]):
			list.append(True)
		else:
			list.append(False)
	array = np.array(list)
	return array

#Create index for B-R v. R-J
index_BRJ = BRJ(B2, R2, J2) 

B3 = B2[index_BRJ]
R3 = R2[index_BRJ]
J3 = J2[index_BRJ]

B_R_graph = np.subtract(B3, R3)
R_J_graph = np.subtract(R3, J3)

#B-V v. V-R function CONTROL FIELD
def BVR(B, V, R): #create a function: def function_name(parameters)
	list=[] #empty list
	for i in range(0,len(V)):
		if np.isfinite(B[i]) and np.isfinite(V[i]) and np.isfinite(R[i]):
			list.append(True)
		else:
			list.append(False)
	array = np.array(list)
	return array

#Create index for B-V v. V-R
index_BVR = BVR(B2, V2, R2)

B3 = B2[index_BVR]
V3 = V2[index_BVR]
R3 = R2[index_BVR]

B_V_graph = np.subtract(B3, V3)
V_R_graph = np.subtract(V3, R3)'''

#V-R v. R-J function CONTROL FIELD
def VRJ(V, R, J): #create a function: def function_name(parameters)
	list=[] #empty list
	for i in range(0,len(R)): #for i in the range from 0 to the length of R
		if np.isfinite(V[i]) and np.isfinite(R[i]) and np.isfinite(J[i]):
			list.append(True)
		else:
			list.append(False)
	array = np.array(list)
	return array

#Create index for V-R v. R-J 
index_VRJ = VRJ(V2, R2, J2)

V3 = V2[index_VRJ]
R3 = R2[index_VRJ]
J3 = J2[index_VRJ]

V_R_graph = np.subtract(V3, R3)
R_J_graph = np.subtract(R3, J3)

#BEGIN CODE FOR TEST FIELD
testfile = open('0_neg18_NOMAD_BLANKS_10arcmin_box.txt', 'r')
read_lines = testfile.readlines()

#R Magnitude
R_magnitude0 = read_lines[0][123:129]
R_magnitude = []

for R_magnitude0 in read_lines:
	R_magnitude1 = R_magnitude0[123:129]
	if R_magnitude1 == "      ":
		R_magnitude1 = -99
	R_magnitude.append(float(R_magnitude1))			
	
#B Magnitude
B_magnitude0 = read_lines[0][105:111]
B_magnitude = []

for B_magnitude0 in read_lines:
	B_magnitude1 = B_magnitude0[105:111]
	if B_magnitude1 == "      ":
		B_magnitude1 = -99
	B_magnitude.append(float(B_magnitude1))

#MEDIAN for B-R
Rmag1=[]
Bmag1=[]
for R_magnitude0 in read_lines:
	R_magnitude1 = R_magnitude0[123:129] #read this column of specific numbers
	if R_magnitude1 == "      ": #if R_mag1 has these blanks
		R_magnitude1 = nan        #replace with nan
	Rmag1.append(float(R_magnitude1)) #append the last number into the list	

for B_magntiude0 in read_lines:
	B_magnitude1 = B_magnitude0[105:111]
	if B_magnitude1 == "      ":
		B_magnitude1 = nan
	Bmag1.append(float(B_magnitude1))

Rmag2 = np.array(Rmag1)
Bmag2 = np.array(Bmag1)

fin_Rmag=np.isfinite(Rmag2)

fin_Bmag=np.isfinite(Bmag1)
cutRmagBmag = np.logical_and(fin_Rmag, fin_Bmag)

R_mag_RmagBmag = Rmag2[cutRmagBmag]
B_mag_RmagBmag = Bmag2[cutRmagBmag]

Bmag_Rmag = np.subtract(B_mag_RmagBmag, R_mag_RmagBmag)
good0 = np.where((Bmag_Rmag < 20) & (Bmag_Rmag > -20))
good1 = Bmag_Rmag[good0]
Bmag_Rmagmed = np.median(good1)
print Bmag_Rmagmed
	
#V Magnitude
V_magnitude0 = read_lines[0][114:120]
V_magnitude = []

for V_magnitude0 in read_lines:
	V_magnitude1 = V_magnitude0[114:120]
	if V_magnitude1 == "      ":
		V_magnitude1 = -99
	V_magnitude.append(float(V_magnitude1))

V_magnitude = np.array(V_magnitude)

#MEDIAN for B-V
Vmag1=[]

for V_magnitude0 in read_lines:
	V_magnitude1 = V_magnitude0[114:120]
	if V_magnitude1 == "      ":
		V_magnitude1 = nan
	Vmag1.append(float(V_magnitude1))

Vmag2 = np.array(Vmag1)	

fin_Vmag = np.isfinite(Vmag2)

cutBmagVmag = np.logical_and(fin_Vmag, fin_Bmag)

V_mag_BmagVmag = Vmag2[cutBmagVmag]
B_mag_BmagVmag = Bmag2[cutBmagVmag]

Bmag_Vmag = np.subtract(B_mag_BmagVmag, V_mag_BmagVmag)
good2 = np.where((Bmag_Vmag < 20) & (Bmag_Vmag > -20))
good3 = Bmag_Vmag[good2]
Bmag_Vmagmed = np.median(good3)
print Bmag_Vmagmed

#J Magnitude
J_magnitude0 = read_lines[0][132:138]
J_magnitude = []

for J_magnitude0 in read_lines:
	J_magnitude1 = J_magnitude0[132:138]
	if J_magnitude1 == "      ":
		J_magnitude1 = -99
	J_magnitude.append(float(J_magnitude1))
	
J_magnitude = np.array(J_magnitude)

Jmag1=[]

for J_magnitude0 in read_lines:
	J_magnitude1 = J_magnitude0[132:138]
	if J_magnitude1 == "      ":
		J_magnitude1 = nan
	Jmag1.append(float(J_magnitude1))

Jmag2 = np.array(Jmag1)	

fin_Jmag=np.isfinite(Jmag2)

cutRmagJmag = np.logical_and(fin_Jmag, fin_Rmag)

R_mag_RmagJmag = Rmag2[cutRmagJmag]
J_mag_RmagJmag = Jmag2[cutRmagJmag]

#MEDIAN for R-J
Rmag_Jmag = np.subtract(R_mag_RmagJmag, J_mag_RmagJmag)
good4 = np.where((Rmag_Jmag < 20) & (Rmag_Jmag > -20))
good5 = Rmag_Jmag[good4]
Rmag_Jmagmed = np.median(good5)
print Rmag_Jmagmed

#H Magnitude
H_magnitude0 = read_lines[0][139:145]
H_magnitude = []

for H_magnitude0 in read_lines:
	H_magnitude1 = H_magnitude0[139:145]
	if H_magnitude1 == "      ":
		H_magnitude1 = -99
	H_magnitude.append(float(H_magnitude1))
	
H_magnitude = np.array(H_magnitude)

Hmag1=[]

for H_magnitude0 in read_lines:
	H_magnitude1 = H_magnitude0[139:145]
	if H_magnitude1 == "      ":
		H_magnitude1 = nan
	Hmag1.append(float(H_magnitude1))

Hmag2 = np.array(Hmag1)	

fin_Hmag = np.isfinite(Hmag2)

cutJmagHmag = np.logical_and(fin_Hmag, fin_Jmag)

J_mag_JmagHmag = Jmag2[cutJmagHmag]
H_mag_JmagHmag = Hmag2[cutJmagHmag]

#MEDIAN for J-H
Jmag_Hmag = np.subtract(J_mag_JmagHmag, H_mag_JmagHmag)
good6 = np.where((Jmag_Hmag < 20) & (Jmag_Hmag > -20))
good7 = Jmag_Hmag[good6]
Jmag_Hmagmed = np.median(good7)
print Jmag_Hmagmed

#K Magnitude
K_magnitude0 = read_lines[0][146:152]
K_magnitude = []


for K_magnitude0 in read_lines:
	K_magnitude1 = K_magnitude0[146:152]
	if K_magnitude1 == "      ":
		K_magnitude1 = -99
	K_magnitude.append(float(K_magnitude1))
	
K_magnitude = np.array(K_magnitude)

Kmag1=[]

for K_magnitude0 in read_lines:
	K_magnitude1 = K_magnitude0[146:152]
	if K_magnitude1 == "      ":
		K_magnitude1 = nan
	Kmag1.append(float(K_magnitude1))

Kmag2 = np.array(Kmag1)	

fin_Kmag = np.isfinite(Kmag2)

cutHmagKmag = np.logical_and(fin_Kmag, fin_Hmag)

H_mag_HmagKmag = Hmag2[cutHmagKmag]
K_mag_HmagKmag = Kmag2[cutHmagKmag]

#MEDIAN for H-K
Hmag_Kmag = np.subtract(H_mag_HmagKmag, K_mag_HmagKmag)
good8 = np.where((Hmag_Kmag < 20) & (Hmag_Kmag > -20))
good9 = Hmag_Kmag[good8]
Hmag_Kmagmed = np.median(good9)	
print Hmag_Kmagmed	

#MEDIAN for V-R
cutVmagRmag = np.logical_and(fin_Rmag, fin_Vmag)

V_mag_VmagRmag = Vmag2[cutVmagRmag]
R_mag_VmagRmag = Rmag2[cutVmagRmag]

Vmag_Rmag = np.subtract(V_mag_VmagRmag, R_mag_VmagRmag)
good12 = np.where((Vmag_Rmag < 20) & (Vmag_Rmag > -20))
good13 = Vmag_Rmag[good12]
Vmag_Rmagmed = np.median(good13)
print Vmag_Rmagmed

#V-R v. R-J function TEST FIELD
def testVRJ(Vmag, Rmag, Jmag): #create a function: def function_name(parameters)
	test_list=[] #empty list
	for i in range(0,len(Rmag)): #for i in the range from 0 to the length of R
		if np.isfinite(Vmag[i]) and np.isfinite(Rmag[i]) and np.isfinite(Jmag[i]):
			test_list.append(True)
		else:
			test_list.append(False)
	test_array = np.array(test_list)
	return test_array

#Create index for V-R v. R-J 
index_testVRJ = testVRJ(Vmag2, Rmag2, Jmag2)

test_V3 = Vmag2[index_testVRJ]
test_R3 = Rmag2[index_testVRJ]
test_J3 = Jmag2[index_testVRJ]

Vmag_Rmag_graph = np.subtract(test_V3, test_R3)
Rmag_Jmag_graph = np.subtract(test_R3, test_J3)

'''#J-H v. H-K function TEST FIELD
def testJHK(Jmag, Hmag, Kmag): #create a function: def function_name(parameters)
	test_list=[] #empty list
	for i in range(0,len(Hmag)): #for i in the range from 0 to the length of R
		if np.isfinite(Jmag[i]) and np.isfinite(Hmag[i]) and np.isfinite(Kmag[i]):
			test_list.append(True)
		else:
			test_list.append(False)
	test_array = np.array(test_list)
	return test_array

#Create index for J-H v. H-K 
index_testJHK = testJHK(Jmag2, Hmag2, Kmag2)

test_J3 = Jmag2[index_testJHK]
test_H3 = Hmag2[index_testJHK]
test_K3 = Kmag2[index_testJHK]

Jmag_Hmag_graph = np.subtract(test_J3, test_H3)
Hmag_Kmag_graph = np.subtract(test_H3, test_K3)

#R-J v. J-H function TEST FIELD
def testRJH(Rmag, Jmag, Hmag): #create a function: def function_name(parameters)
	test_list=[] #empty list
	for i in range(0,len(Jmag)): #for i in the range from 0 to the length of R
		if np.isfinite(Rmag[i]) and np.isfinite(Jmag[i]) and np.isfinite(Hmag[i]):
			test_list.append(True)
		else:
			test_list.append(False)
	test_array = np.array(test_list)
	return test_array

#Create index for R-J v. J-H 
index_testRJH = testRJH(Rmag2, Jmag2, Hmag2)

test_R3 = Rmag2[index_testRJH]
test_J3 = Jmag2[index_testRJH]
test_H3 = Hmag2[index_testRJH]

Rmag_Jmag_graph = np.subtract(test_R3, test_J3)
Jmag_Hmag_graph = np.subtract(test_J3, test_H3)

#B-R v. R-J function TEST FIELD
def testBRJ(Bmag, Rmag, Jmag): #create a function: def function_name(parameters)
	test_list=[] #empty list
	for i in range(0,len(Rmag)): #for i in the range from 0 to the length of R
		if np.isfinite(Bmag[i]) and np.isfinite(Rmag[i]) and np.isfinite(Jmag[i]):
			test_list.append(True)
		else:
			test_list.append(False)
	test_array = np.array(test_list)
	return test_array

#Create index for B-R v. R-J 
index_testBRJ = testBRJ(Bmag2, Rmag2, Jmag2)

test_B3 = Bmag2[index_testBRJ]
test_R3 = Rmag2[index_testBRJ]
test_J3 = Jmag2[index_testBRJ]

Bmag_Rmag_graph = np.subtract(test_B3, test_R3)
Rmag_Jmag_graph = np.subtract(test_R3, test_J3)

#B-V v. V-R function TEST FIELD
def testBVR(Bmag, Vmag, Rmag): #create a function: def function_name(parameters)
	test_list=[] #empty list
	for i in range(0,len(Vmag)): #for i in the range from 0 to the length of R
		if np.isfinite(Bmag[i]) and np.isfinite(Vmag[i]) and np.isfinite(Rmag[i]):
			test_list.append(True)
		else:
			test_list.append(False)
	test_array = np.array(test_list)
	return test_array

#Create index for B-V v. V-R 
index_testBVR = testBVR(Bmag2, Vmag2, Rmag2)

test_B3 = Bmag2[index_testBVR]
test_V3 = Vmag2[index_testBVR]
test_R3 = Rmag2[index_testBVR]

Bmag_Vmag_graph = np.subtract(test_B3, test_V3)
Vmag_Rmag_graph = np.subtract(test_V3, test_R3)'''

# For SLOPE
x = arange(-1, 10, 0.01)

#J-H v. H-K Tick Coordinates for 5 mag
x1 = [0, 0.315, .63, .945] 
y1 = [0, .535, 1.07, 1.605] 
#y = 1.698*x #slope for J-H v H-K

#R-J v. J-H Tick Coordinates for 2 mag
x2 = [0, .214, .428, .642, 0.856, 1.07, 1.284]
y2 = [0 - 1, .932 - 1 , 1.864 - 1, 2.796 - 1, 3.728 - 1, 4.66 - 1, 5.592 - 1]
#y = 4.355*x - 1 #slope for R-J v J-H

#B-R v. R-J for 2 mag
x3 = [-0.932, 0, 0.932, 1.864, 2.796, 3.728]
y3 = [-1.152, 0, 1.152, 2.304, 3.456, 4.608]
#y = 1.236*x #slope for B-R v R-J

#B-V v. V-R Tick Coordinates for 3 mag
x4 = [-0.756, 0, 0.756, 1.512, 2.268]
y4 = [-0.972, 0, 0.972, 1.944, 2.916]
#y = 1.286*x #slope for B-V v V-R

#V-R v. R-J Tick Coordinates for 2 mag
x5 = [0, 0.932, 1.864, 2.796]
y5 = [0, 0.504, 1.008, 1.512]
y = 0.541*x #slope for V-R v R-J

plt.plot(R_J_graph, V_R_graph, 'ko', label='Control Field', markersize=5.0, alpha=0.7) #plot on the x axis B_R and on the y B_mag, 'ko' is the color black, markersize is the size of the dots
plt.plot(Rmag_Jmag_graph, Vmag_Rmag_graph, 'm^', label='Test Field', markersize=5.0, alpha=0.7) #plot for test field
plt.plot(x, y, color = 'g') #plot for slope
plt.plot(x5, y5, marker = 'x', color = 'g', markeredgewidth = 3.0, markersize =10.0) #plot for tick marks
plt.plot(R_Jmed, V_Rmed, marker = 'd', color = 'c', markeredgewidth = 2.0, markersize = 10.0) #plot for median for control field
plt.plot(Rmag_Jmagmed, Vmag_Rmagmed, marker = 'd', color = 'c', markeredgewidth = 2.0, markersize = 10.0) #plot for test field
#R-J v J-H ARROW AND TEXT PLOTTING AND AXIS
#plt.arrow(0.0, 2.0, 0.214, .864, head_width = 0.05, head_length = 0.05, fc= 'g', ec = 'g') #plot an arrow, location in x and y, addition to x and y, head width and length, color
#plt.text(-0.1, 2.9, '2 magnitudes', color = 'r', rotation = 52) #add text on the figure, x, y, 'string', color... add any more kwargs
#plt.axis([-0.5, 2.0, -1.0, 5.0]) #axis number label [x1, x2, y1, y2]
#B-V v V-R ARROW AND TEXT PLOTTING AND AXIS
#plt.arrow(-1.0, 1.0, 0.756, 0.972, head_width = 0.05, head_length = 0.05, fc= 'g', ec = 'g') #plot an arrow, location in x and y, addition to x and y, head width and length, color
#plt.text(-1.1, 2.0, '3 magnitudes', color = 'r', rotation = 38) #add text on the figure, x, y, 'string', color... add any more kwargs
#plt.axis([-2, 3.0, -1.0, 6.0]) #axis number label [x1, x2, y1, y2]
#J-H H-K ARROW AND TEXT PLOTTING AND AXIS
#plt.arrow(-1.0, 1.0, 0.315, 0.535, head_width = 0.05, head_length = 0.05, fc= 'g', ec = 'g') #plot an arrow, location in x and y, addition to x and y, head width and length, color
#plt.text(-1.1, 1.5, '5 magnitudes', color = 'r', rotation = 56) #add text on the figure, x, y, 'string', color... add any more kwargs
#plt.axis([-1.5, 1.5, -0.5, 2.0]) #axis number label [x1, x2, y1, y2]
#B-R v R-J ARROW AND TEXT PLOTTING AND AXIS
#plt.arrow(-0.5, 2.0, 0.932, 1.152, head_width = 0.05, head_length = 0.05, fc= 'g', ec = 'g') #plot an arrow, location in x and y, addition to x and y, head width and length, color
#plt.text(-0.6, 3.2, '2 magnitudes', color = 'r', rotation = 36) #add text on the figure, x, y, 'string', color... add any more kwargs
#plt.axis([-1.0, 5.0, -2.0, 6.0]) #axis number label [x1, x2, y1, y2]
#V-R v R-J ARROW AND TEXT PLOTTING AND AXIS
plt.arrow(0.0, 1.0, 0.932, 0.504, head_width = 0.05, head_length = 0.05, fc= 'g', ec = 'g') #plot an arrow, location in x and y, addition to x and y, head width and length, color
plt.text(-0.04, 1.5, '2 magnitudes', color = 'r', rotation = 36) #add text on the figure, x, y, 'string', color... add any more kwargs
plt.axis([-1.0, 4.0, -1.0, 2.0]) #axis number label [x1, x2, y1, y2]
plt.legend(loc='lower left', labelspacing = 0.2, prop={'size':10})
plt.xlabel('R-J') #label x
plt.ylabel('V-R') #label y
plt.title('(351,-14) and (0,-18) NOMAD 4 arcmin box') #title


plt.show()

controlfile.close()
testfile.close()

