#include as follow : execfile('pathto/POP56.py',globals(),{'recipe':recipe_variable_name})
from AutoFill.Ingredient import SingleSphereIngr, MultiSphereIngr
POP56= MultiSphereIngr( 
packingMode = 'random',
color = [1, 0, 0],
sphereFile = 'http://autofill.googlecode.com/svn/data//Lipids/spheres/POP56.sph',
radii = [[3.1400000000000001, 1.3, 1.79, 5.4400000000000004, 4.2699999999999996, 2.3399999999999999, 2.9500000000000002, 1.6200000000000001]],
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
meshFile = 'http://autofill.googlecode.com/svn/data//Lipids/geoms/0/POP56.c4d',
perturbAxisAmplitude = 0.1,
principalVector = [0.0, 0.0, 1.0],
name = 'POP56',
positions = [[(0.23999999999999999, -1.4099999999999999, -19.719999999999999), (7.46, -3.1499999999999999, -10.0), (3.0099999999999998, 2.8399999999999999, -21.59), (-2.4900000000000002, 0.52000000000000002, -9.8800000000000008), (-4.7599999999999998, -1.8100000000000001, -19.010000000000002), (2.0600000000000001, -0.78000000000000003, -14.4), (-0.56999999999999995, 2.9500000000000002, -22.620000000000001), (6.0300000000000002, -0.38, -11.82)]],
placeType = 'jitter',
useRotAxis = 1,
nbMol = 0,
)
recipe.addIngredient(POP56)
