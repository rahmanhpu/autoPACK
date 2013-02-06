#include as follow : execfile('pathto/LPO115.py',globals(),{'recipe':recipe_variable_name})
from AutoFill.Ingredient import SingleSphereIngr, MultiSphereIngr
LPO115= MultiSphereIngr( 
packingMode = 'random',
color = [1, 0, 0],
sphereFile = 'http://autofill.googlecode.com/svn/data//Lipids/spheres/LPO115.sph',
radii = [[3.5, 1.9199999999999999, 3.1899999999999999, 3.0099999999999998, 1.9299999999999999, 2.9399999999999999, 3.2599999999999998, 2.52]],
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
meshFile = 'http://autofill.googlecode.com/svn/data//Lipids/geoms/0/LPO115.c4d',
perturbAxisAmplitude = 0.1,
principalVector = [0.0, 0.0, -1.0],
name = 'LPO115',
positions = [[(0.22, 1.3500000000000001, -14.380000000000001), (-2.7599999999999998, -0.10000000000000001, -11.48), (2.5299999999999998, 0.95999999999999996, -1.49), (0.94999999999999996, 1.6399999999999999, -8.0700000000000003), (-4.1900000000000004, -0.48999999999999999, -6.6799999999999997), (1.23, -2.4700000000000002, -22.73), (0.40000000000000002, 0.47999999999999998, -18.129999999999999), (-2.79, 1.29, -2.0299999999999998)]],
placeType = 'jitter',
useRotAxis = 1,
nbMol = 0,
)
recipe.addIngredient(LPO115)
