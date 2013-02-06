#include as follow : execfile('pathto/POP73.py',globals(),{'recipe':recipe_variable_name})
from AutoFill.Ingredient import SingleSphereIngr, MultiSphereIngr
POP73= MultiSphereIngr( 
packingMode = 'random',
color = [1, 0, 0],
sphereFile = 'http://autofill.googlecode.com/svn/data//Lipids/spheres/POP73.sph',
radii = [[1.8999999999999999, 2.98, 3.3199999999999998, 3.04, 1.55, 2.8300000000000001, 3.4500000000000002, 3.0099999999999998]],
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
meshFile = 'http://autofill.googlecode.com/svn/data//Lipids/geoms/0/POP73.c4d',
perturbAxisAmplitude = 0.1,
principalVector = [0.0, 0.0, 1.0],
name = 'POP73',
positions = [[(1.1799999999999999, -0.32000000000000001, -24.18), (-0.79000000000000004, -0.93000000000000005, -17.98), (2.7599999999999998, 1.46, -5.9299999999999997), (-4.0899999999999999, -4.7699999999999996, -4.2000000000000002), (-0.5, 1.4399999999999999, -26.5), (1.6799999999999999, 2.1099999999999999, -19.609999999999999), (-1.8600000000000001, -2.5800000000000001, -11.109999999999999), (1.1799999999999999, 2.79, -12.74)]],
placeType = 'jitter',
useRotAxis = 1,
nbMol = 0,
)
recipe.addIngredient(POP73)
