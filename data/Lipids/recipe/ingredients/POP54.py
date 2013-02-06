#include as follow : execfile('pathto/POP54.py',globals(),{'recipe':recipe_variable_name})
from AutoFill.Ingredient import SingleSphereIngr, MultiSphereIngr
POP54= MultiSphereIngr( 
packingMode = 'random',
color = [1, 0, 0],
sphereFile = 'http://autofill.googlecode.com/svn/data//Lipids/spheres/POP54.sph',
radii = [[1.9299999999999999, 1.3, 2.9399999999999999, 1.3300000000000001, 4.4100000000000001, 2.4700000000000002, 3.1699999999999999, 2.6299999999999999]],
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
meshFile = 'http://autofill.googlecode.com/svn/data//Lipids/geoms/0/POP54.c4d',
perturbAxisAmplitude = 0.1,
principalVector = [0.0, 0.0, 1.0],
name = 'POP54',
positions = [[(-1.51, -5.1500000000000004, -9.8399999999999999), (-1.77, -5.3099999999999996, -5.7999999999999998), (3.2200000000000002, 6.7400000000000002, -9.4499999999999993), (-0.60999999999999999, -6.6500000000000004, -3.0899999999999999), (-1.3899999999999999, -1.23, -20.719999999999999), (4.1399999999999997, 8.2899999999999991, -3.04), (0.46000000000000002, 4.2199999999999998, -15.15), (-0.65000000000000002, -4.0999999999999996, -15.32)]],
placeType = 'jitter',
useRotAxis = 1,
nbMol = 0,
)
recipe.addIngredient(POP54)
