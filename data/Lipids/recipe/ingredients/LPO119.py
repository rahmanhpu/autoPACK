#include as follow : execfile('pathto/LPO119.py',globals(),{'recipe':recipe_variable_name})
from AutoFill.Ingredient import SingleSphereIngr, MultiSphereIngr
LPO119= MultiSphereIngr( 
packingMode = 'random',
color = [1, 0, 0],
sphereFile = 'http://autofill.googlecode.com/svn/data//Lipids/spheres/LPO119.sph',
radii = [[1.6299999999999999, 1.6599999999999999, 2.6800000000000002, 3.8999999999999999, 3.0800000000000001, 2.04, 3.1200000000000001, 2.73]],
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
meshFile = 'http://autofill.googlecode.com/svn/data//Lipids/geoms/0/LPO119.c4d',
perturbAxisAmplitude = 0.1,
principalVector = [0.0, 0.0, 1.0],
name = 'LPO119',
positions = [[(2.0499999999999998, -4.6200000000000001, -22.219999999999999), (-0.59999999999999998, -1.01, -15.119999999999999), (1.25, 5.54, -12.68), (2.2400000000000002, 0.71999999999999997, -18.219999999999999), (-0.60999999999999999, 6.3300000000000001, -6.2199999999999998), (0.78000000000000003, -1.79, -23.109999999999999), (-3.9900000000000002, -3.3100000000000001, -4.1299999999999999), (-2.8700000000000001, -1.48, -9.8699999999999992)]],
placeType = 'jitter',
useRotAxis = 1,
nbMol = 0,
)
recipe.addIngredient(LPO119)
