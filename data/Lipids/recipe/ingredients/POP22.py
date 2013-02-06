#include as follow : execfile('pathto/POP22.py',globals(),{'recipe':recipe_variable_name})
from AutoFill.Ingredient import SingleSphereIngr, MultiSphereIngr
POP22= MultiSphereIngr( 
packingMode = 'random',
color = [1, 0, 0],
sphereFile = 'http://autofill.googlecode.com/svn/data//Lipids/spheres/POP22.sph',
radii = [[2.3700000000000001, 3.4199999999999999, 1.97, 2.6800000000000002, 2.8399999999999999, 1.9299999999999999, 3.2999999999999998, 3.1099999999999999]],
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
meshFile = 'http://autofill.googlecode.com/svn/data//Lipids/geoms/0/POP22.c4d',
perturbAxisAmplitude = 0.1,
principalVector = [0.0, 0.0, -1.0],
name = 'POP22',
positions = [[(-5.8099999999999996, -4.1699999999999999, 4.0899999999999999), (2.46, 0.27000000000000002, 17.829999999999998), (-4.1799999999999997, -1.6100000000000001, 13.609999999999999), (4.5899999999999999, 0.23999999999999999, 10.800000000000001), (-0.75, 2.96, 23.5), (-5.4400000000000004, -2.6000000000000001, 8.8399999999999999), (6.6200000000000001, 1.02, 3.9700000000000002), (-2.0899999999999999, -1.1899999999999999, 19.170000000000002)]],
placeType = 'jitter',
useRotAxis = 1,
nbMol = 0,
)
recipe.addIngredient(POP22)
