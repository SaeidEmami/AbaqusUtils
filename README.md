# Abaqus Utilities

These python scripts are intended to be called either interactively from inside abaqus or from the command line through abaqus cae. 

The following is a brief description for each script:


## surfUtils.py

Creates surfaces based on defined node-sets on parts in Abaqus.

For each node set defined for a part, a seperate surface containing all the nods is created. 


## igsMaker.py

Creates an igs file for every part in a model.

For each part in the model, a standard igs file is created. 
 
How to run it from command line:
  abaqus cae noGui=igsMaker.py -- filepath(.cae) desDir


