#include as follow : execfile('pathto/DPO109.py',globals(),{'recipe':recipe_variable_name})
from AutoFill.Ingredient import SingleSphereIngr, MultiSphereIngr
DPO109= MultiSphereIngr( 
packingMode = 'random',
color = [1, 0, 0],
sphereFile = 'http://autofill.googlecode.com/svn/data//Lipids/spheres/DPO109.sph',
radii = [[3.6699999999999999, 3.2799999999999998, 4.0700000000000003, 2.5299999999999998, 2.8300000000000001, 3.0099999999999998, 1.6299999999999999, 1.3]],
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
meshFile = 'http://autofill.googlecode.com/svn/data//Lipids/geoms/0/DPO109.c4d',
perturbAxisAmplitude = 0.1,
principalVector = [0.0, 0.0, 1.0],
name = 'DPO109',
positions = [[(6.1200000000000001, -0.80000000000000004, 5.0700000000000003), (1.0600000000000001, 2.2999999999999998, 18.18), (2.4700000000000002, 1.1399999999999999, 22.100000000000001), (-5.6900000000000004, -2.1200000000000001, 10.67), (-3.3399999999999999, -0.28000000000000003, 16.68), (5.29, 2.0600000000000001, 12.369999999999999), (-7.1200000000000001, -3.9300000000000002, 5.9800000000000004), (-8.9100000000000001, -2.7999999999999998, 2.4300000000000002)]],
placeType = 'jitter',
useRotAxis = 1,
nbMol = 0,
)
recipe.addIngredient(DPO109)
