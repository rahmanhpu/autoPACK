#include as follow : execfile('pathto/DPO99.py',globals(),{'recipe':recipe_variable_name})
from AutoFill.Ingredient import SingleSphereIngr, MultiSphereIngr
DPO99= MultiSphereIngr( 
packingMode = 'random',
color = [1, 0, 0],
sphereFile = 'http://autofill.googlecode.com/svn/data//Lipids/spheres/DPO99.sph',
radii = [[4.0599999999999996, 2.9399999999999999, 3.27, 3.1899999999999999, 3.1899999999999999, 2.48, 2.6200000000000001, 1.99]],
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
meshFile = 'http://autofill.googlecode.com/svn/data//Lipids/geoms/0/DPO99.c4d',
perturbAxisAmplitude = 0.1,
principalVector = [0.0, 0.0, 1.0],
name = 'DPO99',
positions = [[(1.9099999999999999, 0.25, 19.489999999999998), (-0.63, 1.1699999999999999, 8.7400000000000002), (-1.5800000000000001, -3.8999999999999999, 5.54), (1.5800000000000001, 2.7200000000000002, 14.98), (0.89000000000000001, -3.2200000000000002, 12.69), (-2.0499999999999998, 0.28000000000000003, 24.77), (-2.52, 1.3999999999999999, 2.2799999999999998), (1.3100000000000001, 1.97, 24.02)]],
placeType = 'jitter',
useRotAxis = 1,
nbMol = 0,
)
recipe.addIngredient(DPO99)
