#include as follow : execfile('pathto/POP7.py',globals(),{'recipe':recipe_variable_name})
from AutoFill.Ingredient import SingleSphereIngr, MultiSphereIngr
POP7= MultiSphereIngr( 
packingMode = 'random',
color = [1, 0, 0],
sphereFile = 'http://autofill.googlecode.com/svn/data//Lipids/spheres/POP7.sph',
radii = [[2.9700000000000002, 3.8100000000000001, 2.9700000000000002, 3.21, 1.8999999999999999, 3.8100000000000001, 1.5800000000000001, 2.8999999999999999]],
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
meshFile = 'http://autofill.googlecode.com/svn/data//Lipids/geoms/0/POP7.c4d',
perturbAxisAmplitude = 0.1,
principalVector = [0.0, 0.0, -1.0],
name = 'POP7',
positions = [[(-3.1699999999999999, 3.2999999999999998, -11.41), (-6.29, 2.0499999999999998, -4.5700000000000003), (2.1499999999999999, -1.1399999999999999, -20.489999999999998), (2.8199999999999998, -3.1200000000000001, -13.85), (0.89000000000000001, 1.4299999999999999, -24.600000000000001), (1.21, -3.73, -5.8499999999999996), (3.9300000000000002, 0.02, -26.010000000000002), (-1.9299999999999999, 2.1000000000000001, -18.050000000000001)]],
placeType = 'jitter',
useRotAxis = 1,
nbMol = 0,
)
recipe.addIngredient(POP7)
