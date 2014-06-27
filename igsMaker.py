###################################################################################################
# Available for use under the [MIT License](http://en.wikipedia.org/wiki/MIT_License)             #
# Writer: Saeid Emami                                                                             #
###################################################################################################

'''
Creates an igs file for every part in a model.

For each part in the model, a standard igs file is created. 
 
How to run it from command line:
  abaqus cae noGui=igsMaker.py -- filepath(.cae) desDir
'''


import os
import part
import sys
          
def makeIgs(file_path, igs_dir):
    '''
    Extracts igs files out of an abaqus cae file.

    For each part in mdb, a seperate igs file is created.
    '''
    print(file_path, igs_dir)
    if not os.path.isfile(file_path):
        return
    if not os.path.isdir(igs_dir):
        os.makedirs(igs_dir)

    try:
        myMDB = openMdb(file_path)
    except:
        return

    print(file_path, igs_dir)

    for modelName in myMDB.models.keys():
        for partName in myMDB.models[modelName].parts.keys():
            aPart = myMDB.models[modelName].parts[partName]
            outputFile = igs_dir + modelName + partName + ".igs"
            aPart.writeIgesFile(outputFile, part.STANDARD)



def main():
    if len(sys.argv) < 13:
        return
    cae_file_path = sys.argv[11]
    igs_dir = sys.argv[12]

    makeIgs(cae_file_path, igs_dir)   



if __name__ == "__main__":
    main()

