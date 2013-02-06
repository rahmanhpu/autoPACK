#include as follow : execfile('pathto/POP28.py',globals(),{'recipe':recipe_variable_name})
from AutoFill.Ingredient import SingleSphereIngr, MultiSphereIngr
POP28= MultiSphereIngr( 
packingMode = 'random',
color = [1, 0, 0],
sphereFile = 'http://autofill.googlecode.com/svn/data//Lipids/spheres/POP28.sph',
radii = [[2.5600000000000001, 2.6299999999999999, 4.46, 3.2000000000000002, 3.1800000000000002, 3.6299999999999999, 1.5700000000000001, 1.6599999999999999]],
cutoff_boundary = 0,
Type = 'MultiSphere',
cutoff_surface = 0,
gradient = '',
jitterMax = [0.5, 0.5, 0.10000000000000001],
packingPriority = 0,
rotAxis = [0.0, 2.0, 1.0],
nbJitter = 5,
molarity = 1.0,
rotRange = 6.2831,
meshFile = 'http://autofill.googlecode.com/svn/data//Lipids/geoms/0/POP28.c4d',
perturbAxisAmplitude = 0.1,
principalVector = [0.0, 0.0, 1.0],
name = 'POP28',
positions = [[(-5.0300000000000002, 4.2800000000000002, -4.9699999999999998), (0.45000000000000001, -0.42999999999999999, -19.77), (5.7000000000000002, -3.73, -5.4199999999999999), (-6.4400000000000004, 3.73, -11.699999999999999), (-4.04, 2.6600000000000001, -17.59), (4.1399999999999997, -2.6600000000000001, -14.1), (-0.92000000000000004, -0.14999999999999999, -24.010000000000002), (2.21, -1.0900000000000001, -24.359999999999999)]],
placeType = 'jitter',
useRotAxis = 1,
nbMol = 0,
)
recipe.addIngredient(POP28)
