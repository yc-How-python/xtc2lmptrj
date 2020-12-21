import os
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('-i', type=str, default=r'J:\TrjData\workstation\64me_290', help="Path to input file")
parser.add_argument('-o', type=str, default=r'J:\TrjData\64me_290_', help="Path to output files")
parser.add_argument('-v', type=str, default=r'E:\vmd\vmd.exe', help="Path to VMD")
parser.add_argument('-n', type=int, default=10, help="Skip every n frames")
args = parser.parse_args()
foldersPATH = args.i
outputPATH=args.o
vmdpath=args.v
skipframes=args.n
PROJECT_DIR_PATH = os.path.dirname(os.path.abspath(os.path.abspath(__file__)))


DIR_PATH = os.path.join(PROJECT_DIR_PATH, foldersPATH)
outputPATH = os.path.join(PROJECT_DIR_PATH, outputPATH)
folders = os.listdir(DIR_PATH)
vmdscript=open('vmdscript.tcl','w')
try:
    os.mkdir(outputPATH)

except FileExistsError:
    pass
else:
    pass

for folder in folders:
    folderPATH=os.path.join(foldersPATH, folder)
    files=os.listdir(folderPATH)
    print(files)
    for eachfile in files:
        prefix, suffix = os.path.splitext(eachfile)
        if suffix == '.xtc':
            xtc = os.path.join(folderPATH, eachfile)
            continue
        elif suffix == '.gro':
            name=prefix
            gro = os.path.join(folderPATH, eachfile)
            continue
        else:
            continue
    lammpstrjPATH = os.path.join(outputPATH, name+'.lammpstrj')
    vmdscript.write(r'mol new '+repr(gro).strip('\'')+'\nanimate delete all\nmol addfile '+repr(xtc).strip('\'')+' waitfor all\n')
    vmdscript.write('animate write lammpstrj '+repr(lammpstrjPATH).strip('\'')+' skip '+str(skipframes)+'+ sel [atomselect top "name OW HW1 HW2"]  waitfor all\nmol delete top\n\n')  #write file_type filename [beg nb] [end ne ] [skip ns] [waitfor nw] [sel selection] [molecule_number]:
vmdscript.close()


os.system(repr(vmdpath).strip('\'')+' -dispdev text -e vmdscript.tcl')
