###################################################################################################
# Available for use under the [MIT License](http://en.wikipedia.org/wiki/MIT_License)             #
# Writer: Saeid Emami                                                                             #
###################################################################################################


'''
Creates surfaces based on defined node-sets on parts in Abaqus.

For each node set defined for a part, a seperate surface containing all the nods is created. 
'''


from abaqus import *
import mesh


def defineAllPartSurfaces(model):
    '''
    Define all surfaces for all parts.
    For each node set, a surface that covers all the nodes is defined.
    '''
    parts = (p for p in mdb.models[model].parts.values())
    for part in parts:
        sets = part.sets
        setNames = sets.keys()
        for setName in setNames:
            if (len(sets[setName].nodes) > 0) and (len(sets[setName].elements) == 0): # Checks if a set is nodeset
                f1, f2, f3, f4, f5, f6 = detectElementSidesOnPart(model, part, sets[setName])
                part.Surface(face1Elements = f1, face2Elements = f2, face3Elements = f3, 
                             face4Elements = f4, face5Elements = f5, face6Elements = f6, name = setName)



def detectElementSidesOnPart(model, part, nset):
    '''
    Returns a tuple of element numbers arry (a1, a2, a3, a4, a5, a6) to define a surface for a part.
    a1 is the array of all elements with all nodes on side 1 in nset, and so on.
    '''
    allElements = part.elements
    allNodes = part.nodes
    Nset = nset.nodes
    NsetLabels = set(n.label for n in Nset)
    face1 = []
    face2 = []
    face3 = []
    face4 = []
    face5 = []
    face6 = []

    surfElementLabels = set()  
    for node in Nset: 
        surfElementLabels.update(set([e.label for e in node.getElements()]))

    for anElementLabel in surfElementLabels: 
        anElement = allElements.getFromLabel(anElementLabel)
        n0 = allNodes[anElement.connectivity[ 0 ]].label in NsetLabels
        n1 = allNodes[anElement.connectivity[ 1 ]].label in NsetLabels
        n2 = allNodes[anElement.connectivity[ 2 ]].label in NsetLabels
        n3 = allNodes[anElement.connectivity[ 3 ]].label in NsetLabels
        n4 = allNodes[anElement.connectivity[ 4 ]].label in NsetLabels
        n5 = allNodes[anElement.connectivity[ 5 ]].label in NsetLabels
        n6 = allNodes[anElement.connectivity[ 6 ]].label in NsetLabels
        n7 = allNodes[anElement.connectivity[ 7 ]].label in NsetLabels
        if n0 and n1 and n2 and n3: face1.append(anElement)
        if n4 and n5 and n6 and n7: face2.append(anElement)
        if n0 and n1 and n5 and n4: face3.append(anElement)
        if n1 and n2 and n6 and n5: face4.append(anElement)
        if n2 and n3 and n7 and n6: face5.append(anElement)
        if n0 and n3 and n7 and n4: face6.append(anElement)

    f1 = mesh.MeshElementArray(face1)
    f2 = mesh.MeshElementArray(face2)
    f3 = mesh.MeshElementArray(face3)
    f4 = mesh.MeshElementArray(face4)
    f5 = mesh.MeshElementArray(face5)
    f6 = mesh.MeshElementArray(face6)

    if not f1: f1 = ()
    if not f2: f2 = ()
    if not f3: f3 = ()
    if not f4: f4 = ()
    if not f5: f5 = ()
    if not f6: f6 = ()

    return f1, f2, f3, f4, f5, f6



if __name__ == "__main__":
    modelNames = mdb.models.keys()
    for modelName in modelNames:
        defineAllPartSurfaces(modelName)


