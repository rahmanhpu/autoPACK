#include as follow : execfile('pathto/POP78.py',globals(),{'recipe':recipe_variable_name})
from AutoFill.Ingredient import SingleSphereIngr, MultiSphereIngr
POP78= MultiSphereIngr( 
packingMode = 'random',
color = [1, 0, 0],
sphereFile = 'http://autofill.googlecode.com/svn/data//Lipids/spheres/POP78.sph',
radii = [[3.8100000000000001, 1.54, 3.8100000000000001, 4.2400000000000002, 2.8399999999999999, 1.29, 2.54, 0.76000000000000001]],
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
meshFile = 'http://autofill.googlecode.com/svn/data//Lipids/geoms/0/POP78.c4d',
perturbAxisAmplitude = 0.1,
principalVector = [0.0, 0.0, 1.0],
name = 'POP78',
positions = [[(2.75, 2.5699999999999998, -6.9199999999999999), (-2.3300000000000001, -5.2000000000000002, -5.7199999999999998), (2.5600000000000001, 2.6400000000000001, 1.74), (1.26, 2.3900000000000001, -15.93), (-2.6000000000000001, -2.1400000000000001, -14.5), (-3.2400000000000002, -3.6800000000000002, -0.92000000000000004), (-4.5099999999999998, -4.75, -10.130000000000001), (-1.3799999999999999, -5.5599999999999996, -2.6000000000000001)]],
placeType = 'jitter',
useRotAxis = 1,
nbMol = 0,
)
recipe.addIngredient(POP78)
