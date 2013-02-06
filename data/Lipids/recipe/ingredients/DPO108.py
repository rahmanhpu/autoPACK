#include as follow : execfile('pathto/DPO108.py',globals(),{'recipe':recipe_variable_name})
from AutoFill.Ingredient import SingleSphereIngr, MultiSphereIngr
DPO108= MultiSphereIngr( 
packingMode = 'random',
color = [1, 0, 0],
sphereFile = 'http://autofill.googlecode.com/svn/data//Lipids/spheres/DPO108.sph',
radii = [[2.6000000000000001, 1.9399999999999999, 4.6399999999999997, 2.25, 2.3100000000000001, 3.5600000000000001, 4.8600000000000003, 2.7400000000000002]],
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
meshFile = 'http://autofill.googlecode.com/svn/data//Lipids/geoms/0/DPO108.c4d',
perturbAxisAmplitude = 0.1,
principalVector = [0.0, 0.0, 1.0],
name = 'DPO108',
positions = [[(1.8999999999999999, -2.1499999999999999, -16.07), (1.47, 0.34000000000000002, -19.82), (0.40000000000000002, 0.32000000000000001, -10.59), (-4.1100000000000003, 3.1899999999999999, -19.469999999999999), (-2.71, 1.1899999999999999, -22.109999999999999), (0.20000000000000001, 2.4900000000000002, -2.8100000000000001), (2.7200000000000002, -5.9199999999999999, -5.2999999999999998), (-0.62, 2.7999999999999998, -16.489999999999998)]],
placeType = 'jitter',
useRotAxis = 1,
nbMol = 0,
)
recipe.addIngredient(DPO108)
