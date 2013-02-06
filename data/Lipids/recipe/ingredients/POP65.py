#include as follow : execfile('pathto/POP65.py',globals(),{'recipe':recipe_variable_name})
from AutoFill.Ingredient import SingleSphereIngr, MultiSphereIngr
POP65= MultiSphereIngr( 
packingMode = 'random',
color = [1, 0, 0],
sphereFile = 'http://autofill.googlecode.com/svn/data//Lipids/spheres/POP65.sph',
radii = [[2.9300000000000002, 2.54, 2.71, 2.3300000000000001, 4.4100000000000001, 1.9399999999999999, 4.9900000000000002, 1.54]],
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
meshFile = 'http://autofill.googlecode.com/svn/data//Lipids/geoms/0/POP65.c4d',
perturbAxisAmplitude = 0.1,
principalVector = [0.0, 0.0, 1.0],
name = 'POP65',
positions = [[(3.8500000000000001, 1.24, 9.9000000000000004), (1.1299999999999999, -1.6000000000000001, 4.4500000000000002), (1.96, -0.050000000000000003, 19.260000000000002), (5.8799999999999999, 1.25, 15.300000000000001), (-7.5300000000000002, -2.4500000000000002, 5.0899999999999999), (-0.029999999999999999, 1.97, 22.34), (-2.8900000000000001, -2.5299999999999998, 14.5), (2.0800000000000001, 3.8900000000000001, 20.870000000000001)]],
placeType = 'jitter',
useRotAxis = 1,
nbMol = 0,
)
recipe.addIngredient(POP65)
