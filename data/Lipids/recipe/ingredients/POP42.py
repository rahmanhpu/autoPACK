#include as follow : execfile('pathto/POP42.py',globals(),{'recipe':recipe_variable_name})
from AutoFill.Ingredient import SingleSphereIngr, MultiSphereIngr
POP42= MultiSphereIngr( 
packingMode = 'random',
color = [1, 0, 0],
sphereFile = 'http://autofill.googlecode.com/svn/data//Lipids/spheres/POP42.sph',
radii = [[2.8399999999999999, 2.7000000000000002, 2.5299999999999998, 4.1399999999999997, 1.26, 1.8600000000000001, 2.3599999999999999, 5.0]],
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
meshFile = 'http://autofill.googlecode.com/svn/data//Lipids/geoms/0/POP42.c4d',
perturbAxisAmplitude = 0.1,
principalVector = [0.0, 0.0, 1.0],
name = 'POP42',
positions = [[(1.9299999999999999, 0.66000000000000003, 25.609999999999999), (1.96, 0.67000000000000004, 20.93), (0.67000000000000004, -8.8000000000000007, 14.94), (-1.2, 6.1299999999999999, 17.760000000000002), (1.02, -9.0999999999999996, 10.85), (1.8400000000000001, -7.8099999999999996, 6.7400000000000002), (1.45, -4.25, 18.699999999999999), (-5.1500000000000004, 6.9699999999999998, 9.4000000000000004)]],
placeType = 'jitter',
useRotAxis = 1,
nbMol = 0,
)
recipe.addIngredient(POP42)
