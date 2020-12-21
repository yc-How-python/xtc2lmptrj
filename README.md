# Description
This program was designed for batch conversion of simulation trajectories from .gro and .xtc to .lammpstrj.
# Options for xtc2lmptrj
## -i 
The result files for each simulation including .gro and .xtc should be placed in a separate folder. 
This program requires the path to the main folder that contains all the simulated folders. 
### Example
            Main Folder -> Folder a -> .gro, .xtc, ...
                        -> Folder b -> .gro, .xtc, ...
                        -> Folder c -> .gro, .xtc, ...
            
## -o 
The path to the folder where you want to place the conversion results.
The name of each .lammpstrj will be same as the name of .gro.
## -n
The stride for writting data in .lammpstrj.
## -v 
The path to vmd.
