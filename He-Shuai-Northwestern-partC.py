from __future__ import division
import Image
from math import cos, sin, pi

f = open('code.in', 'rb')

points, faces = [],[]
# creates list of points and faces
for x in f.readlines():
	if x[0] == 'p':
		x = x[6:]
		points.append([float(k) for k in x.split(' ')])
	else:
		x = x[5:]
		faces.append([int(k) for k in x.split(' ')])

#2D projection of points
flat_points = []
for p in points:
	x = 5*p[0]/(1/(p[2]-2))
	y = 5*p[1]/(1/(p[2]-2))
	flat_points.append([int(x*512+512), int(-y*512+512)])

#see if point is inside of boundary
def check_point(point):
	return (point[0] >= 0 and point[0] <= 1024) and (point[1] >= 0 and point[1] <= 1024)

# creates the image Part A
img = Image.new('RGB',(1024,1024),"black")
pixels = img.load()
for i in flat_points:
	if check_point(i):
		pixels[i[0], i[1]] = (255, 255, 0)

img.save('He-Shuai-Northwestern-imageA.png')

#3D rotation