#include as follow : execfile('pathto/POP61.py',globals(),{'recipe':recipe_variable_name})
from AutoFill.Ingredient import SingleSphereIngr, MultiSphereIngr
POP61= MultiSphereIngr( 
packingMode = 'random',
color = [1, 0, 0],
sphereFile = 'http://autofill.googlecode.com/svn/data//Lipids/spheres/POP61.sph',
radii = [[3.3500000000000001, 3.8799999999999999, 3.1000000000000001, 1.3500000000000001, 1.8799999999999999, 4.0899999999999999, 0.70999999999999996, 3.5]],
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
meshFile = 'http://autofill.googlecode.com/svn/data//Lipids/geoms/0/POP61.c4d',
perturbAxisAmplitude = 0.1,
principalVector = [0.0, 0.0, 1.0],
name = 'POP61',
positions = [[(-1.5600000000000001, 3.0299999999999998, 6.0700000000000003), (-0.10000000000000001, 3.1299999999999999, 13.85), (-1.29, -0.20000000000000001, 18.23), (0.41999999999999998, 4.1799999999999997, 24.170000000000002), (1.9399999999999999, 1.6200000000000001, 21.66), (1.8, -6.5099999999999998, 5.96), (1.8300000000000001, 3.6299999999999999, 23.050000000000001), (-0.89000000000000001, -5.0, 13.23)]],
placeType = 'jitter',
useRotAxis = 1,
nbMol = 0,
)
recipe.addIngredient(POP61)
