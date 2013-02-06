#include as follow : execfile('pathto/POP84.py',globals(),{'recipe':recipe_variable_name})
from AutoFill.Ingredient import SingleSphereIngr, MultiSphereIngr
POP84= MultiSphereIngr( 
packingMode = 'random',
color = [1, 0, 0],
sphereFile = 'http://autofill.googlecode.com/svn/data//Lipids/spheres/POP84.sph',
radii = [[2.46, 2.3599999999999999, 3.0499999999999998, 2.6600000000000001, 2.3199999999999998, 4.2599999999999998, 1.8899999999999999, 1.9299999999999999]],
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
meshFile = 'http://autofill.googlecode.com/svn/data//Lipids/geoms/0/POP84.c4d',
perturbAxisAmplitude = 0.1,
principalVector = [0.0, 0.0, 1.0],
name = 'POP84',
positions = [[(0.76000000000000001, 2.7400000000000002, 14.91), (2.8700000000000001, -8.1099999999999994, 2.3999999999999999), (-0.81000000000000005, 4.4100000000000001, 8.8900000000000006), (-1.29, 0.56999999999999995, 19.460000000000001), (3.0099999999999998, -7.2000000000000002, 7.5), (-4.0800000000000001, 6.2300000000000004, 1.97), (2.2599999999999998, -1.8799999999999999, 15.49), (2.9399999999999999, -4.9299999999999997, 11.789999999999999)]],
placeType = 'jitter',
useRotAxis = 1,
nbMol = 0,
)
recipe.addIngredient(POP84)
