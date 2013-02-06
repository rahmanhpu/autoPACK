#include as follow : execfile('pathto/POP11.py',globals(),{'recipe':recipe_variable_name})
from AutoFill.Ingredient import SingleSphereIngr, MultiSphereIngr
POP11= MultiSphereIngr( 
packingMode = 'random',
color = [1, 0, 0],
sphereFile = 'http://autofill.googlecode.com/svn/data//Lipids/spheres/POP11.sph',
radii = [[1.98, 4.1100000000000003, 3.9700000000000002, 2.9900000000000002, 2.8799999999999999, 3.0800000000000001, 1.29, 1.9299999999999999]],
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
meshFile = 'http://autofill.googlecode.com/svn/data//Lipids/geoms/0/POP11.c4d',
perturbAxisAmplitude = 0.1,
principalVector = [0.0, 0.0, -1.0],
name = 'POP11',
positions = [[(-0.040000000000000001, 3.48, -4.2999999999999998), (-1.51, -4.2699999999999996, -15.99), (0.91000000000000003, -0.28000000000000003, -17.050000000000001), (0.60999999999999999, 0.28999999999999998, -8.8800000000000008), (3.3799999999999999, -1.3400000000000001, -22.780000000000001), (-3.5, -0.23000000000000001, -9.3699999999999992), (-0.28999999999999998, 6.71, -1.97), (-4.5800000000000001, 4.5800000000000001, -5.5899999999999999)]],
placeType = 'jitter',
useRotAxis = 1,
nbMol = 0,
)
recipe.addIngredient(POP11)
