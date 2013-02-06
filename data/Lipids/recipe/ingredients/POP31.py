#include as follow : execfile('pathto/POP31.py',globals(),{'recipe':recipe_variable_name})
from AutoFill.Ingredient import SingleSphereIngr, MultiSphereIngr
POP31= MultiSphereIngr( 
packingMode = 'random',
color = [1, 0, 0],
sphereFile = 'http://autofill.googlecode.com/svn/data//Lipids/spheres/POP31.sph',
radii = [[1.75, 2.7400000000000002, 3.7000000000000002, 1.95, 2.5899999999999999, 3.7200000000000002, 3.0600000000000001, 3.6600000000000001]],
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
meshFile = 'http://autofill.googlecode.com/svn/data//Lipids/geoms/0/POP31.c4d',
perturbAxisAmplitude = 0.1,
principalVector = [0.0, 0.0, -1.0],
name = 'POP31',
positions = [[(-0.89000000000000001, 3.52, -24.32), (0.44, 0.029999999999999999, -21.460000000000001), (-2.0499999999999998, -0.089999999999999997, -14.32), (2.1400000000000001, 2.46, -26.010000000000002), (2.2200000000000002, -3.5, -16.059999999999999), (0.38, -2.2400000000000002, -9.0399999999999991), (4.4699999999999998, -0.90000000000000002, -21.460000000000001), (-6.04, 0.55000000000000004, -7.6399999999999997)]],
placeType = 'jitter',
useRotAxis = 1,
nbMol = 0,
)
recipe.addIngredient(POP31)
