#include as follow : execfile('pathto/POP67.py',globals(),{'recipe':recipe_variable_name})
from AutoFill.Ingredient import SingleSphereIngr, MultiSphereIngr
POP67= MultiSphereIngr( 
packingMode = 'random',
color = [1, 0, 0],
sphereFile = 'http://autofill.googlecode.com/svn/data//Lipids/spheres/POP67.sph',
radii = [[2.3599999999999999, 3.6899999999999999, 3.8799999999999999, 2.5299999999999998, 2.8100000000000001, 0.76000000000000001, 1.9299999999999999, 2.9199999999999999]],
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
meshFile = 'http://autofill.googlecode.com/svn/data//Lipids/geoms/0/POP67.c4d',
perturbAxisAmplitude = 0.1,
principalVector = [0.0, 0.0, 1.0],
name = 'POP67',
positions = [[(-2.0, -2.6600000000000001, 4.5499999999999998), (-0.11, -0.65000000000000002, 16.280000000000001), (1.48, 4.9100000000000001, 10.82), (-1.98, -2.9300000000000002, 10.06), (1.75, -3.9700000000000002, 20.050000000000001), (-3.0299999999999998, 0.60999999999999999, -2.7799999999999998), (-1.99, -1.27, -0.32000000000000001), (0.94999999999999996, 8.1600000000000001, 3.7599999999999998)]],
placeType = 'jitter',
useRotAxis = 1,
nbMol = 0,
)
recipe.addIngredient(POP67)
