#include as follow : execfile('pathto/DPO98.py',globals(),{'recipe':recipe_variable_name})
from AutoFill.Ingredient import SingleSphereIngr, MultiSphereIngr
DPO98= MultiSphereIngr( 
packingMode = 'random',
color = [1, 0, 0],
sphereFile = 'http://autofill.googlecode.com/svn/data//Lipids/spheres/DPO98.sph',
radii = [[3.1099999999999999, 3.0600000000000001, 3.4300000000000002, 3.7599999999999998, 1.95, 2.1899999999999999, 2.7799999999999998, 3.3599999999999999]],
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
meshFile = 'http://autofill.googlecode.com/svn/data//Lipids/geoms/0/DPO98.c4d',
perturbAxisAmplitude = 0.1,
principalVector = [0.0, 0.0, -1.0],
name = 'DPO98',
positions = [[(-4.4900000000000002, 1.4099999999999999, 9.0600000000000005), (2.8100000000000001, 2.29, 10.720000000000001), (1.6599999999999999, 3.0, 3.6499999999999999), (1.0800000000000001, -1.47, 19.300000000000001), (-2.3199999999999998, 0.64000000000000001, 14.890000000000001), (3.0600000000000001, 0.81999999999999995, 16.41), (2.96, -4.0599999999999996, 17.23), (-6.2699999999999996, -0.70999999999999996, 2.27)]],
placeType = 'jitter',
useRotAxis = 1,
nbMol = 0,
)
recipe.addIngredient(DPO98)
