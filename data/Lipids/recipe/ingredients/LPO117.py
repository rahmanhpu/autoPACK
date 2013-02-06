#include as follow : execfile('pathto/LPO117.py',globals(),{'recipe':recipe_variable_name})
from AutoFill.Ingredient import SingleSphereIngr, MultiSphereIngr
LPO117= MultiSphereIngr( 
packingMode = 'random',
color = [1, 0, 0],
sphereFile = 'http://autofill.googlecode.com/svn/data//Lipids/spheres/LPO117.sph',
radii = [[2.9300000000000002, 4.0800000000000001, 2.4700000000000002, 2.4399999999999999, 4.6500000000000004, 1.95, 1.8600000000000001, 3.0800000000000001]],
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
meshFile = 'http://autofill.googlecode.com/svn/data//Lipids/geoms/0/LPO117.c4d',
perturbAxisAmplitude = 0.1,
principalVector = [0.0, 0.0, 1.0],
name = 'LPO117',
positions = [[(-4.9400000000000004, -6.5, -8.9199999999999999), (3.4900000000000002, 2.5, -14.050000000000001), (0.45000000000000001, 0.54000000000000004, -19.920000000000002), (-5.7300000000000004, -4.0700000000000003, -14.09), (5.0800000000000001, 4.21, -4.75), (-1.8200000000000001, -1.53, -17.059999999999999), (-4.7400000000000002, -7.5599999999999996, -3.2599999999999998), (0.55000000000000004, 3.5499999999999998, -20.550000000000001)]],
placeType = 'jitter',
useRotAxis = 1,
nbMol = 0,
)
recipe.addIngredient(LPO117)
