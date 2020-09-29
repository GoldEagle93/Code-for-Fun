import fileinput
import sys
count=0
mid=0.000
trylist=[]
litMin=[]
litMax=[]
i=0
PhosList=['DOPE', 'DOPC', 'POPE', 'POPC', 'SOPS', 'DPPC', 'DMPC', 'DLPC', 'PLPC', 'DLPE']

file=fileinput.input(sys.argv[1:])
for line in file:
	for i in PhosList:
		if i in line and "   P" in line: 
			Phos=float(line[39:45])
			trylist.append(Phos)

trylist.sort()
mid=(trylist[-1]+trylist[0])/2

for i in trylist:
	if i<(mid-1.5) :
		litMin.append(i)
	elif i>=(mid+1.5):
		litMax.append(i)
litMin.sort()
litMax.sort()

file.seek(0)
for line in file:
	if "TIP3   OH" in line:
		water=float(line[39:45])
		if water > litMin[-1] and water < litMax[0]:
			count+=1

finalfile=open('finalfile.txt','a+')
finalfile.write(str(count))
finalfile.write('\n')
print(count)
file.close()
