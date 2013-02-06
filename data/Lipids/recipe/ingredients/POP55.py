#include as follow : execfile('pathto/POP55.py',globals(),{'recipe':recipe_variable_name})
from AutoFill.Ingredient import SingleSphereIngr, MultiSphereIngr
POP55= MultiSphereIngr( 
packingMode = 'random',
color = [1, 0, 0],
sphereFile = 'http://autofill.googlecode.com/svn/data//Lipids/spheres/POP55.sph',
radii = [[2.9900000000000002, 2.54, 2.7200000000000002, 3.46, 2.6800000000000002, 2.4700000000000002, 1.9099999999999999, 4.1500000000000004]],
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
meshFile = 'http://autofill.googlecode.com/svn/data//Lipids/geoms/0/POP55.c4d',
perturbAxisAmplitude = 0.1,
principalVector = [0.0, 0.0, 1.0],
name = 'POP55',
positions = [[(-0.38, -2.7400000000000002, -15.390000000000001), (-2.6800000000000002, 6.1399999999999997, -4.3899999999999997), (1.6899999999999999, -1.75, -6.8200000000000003), (-0.77000000000000002, 4.1399999999999997, -10.01), (-0.41999999999999998, 0.48999999999999999, -21.920000000000002), (2.0899999999999999, 0.53000000000000003, -19.890000000000001), (-1.79, -3.4500000000000002, -18.829999999999998), (0.56999999999999995, -3.3900000000000001, -11.74)]],
placeType = 'jitter',
useRotAxis = 1,
nbMol = 0,
)
recipe.addIngredient(POP55)
