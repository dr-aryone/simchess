from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import sys
import math as m

# Some api in the chain is translating the keystrokes to this octal string
# so instead of saying: ESCAPE = 27, we use the following.
ESCAPE = '\033' 

# Number of the glut window.
window = 0

test_colors = {
    "black":  (0,0,0),
	"white":  (1,1,1),
	"red":    (1,0,0),
	"green":  (0,1,0),
	"blue":   (0,0,1),
	"yellow": (1,1,0),
	"cyan":   (0,1,1),
	"magenta":(1,0,1),
	"gray":   (0.5,0.5,0.5),
	"maroon": (0.5,0,0),
	"olive":  (0.5,0.5,0),
	"purple": (0.5,0,0.5),
	"teal":   (0,0.5,0.5),
	"navy":   (0,0,0.5)
}

mapping_table = {
	0: "white",
	1: "red",
	2: "green",
	3: "blue",
	4: "yellow",
	5: "cyan",
	6: "magenta",
	7: "gray",
	8: "maroon",
	9: "olive",
	10: "purple",
	11: "teal",
	12: "navy",
}

# http://poita.org/2014/04/27/cube-vertex-numbering.html
#  cube
vertices = (
	(0,0,0), #0
	(0,0,1), #1
	(0,1,1), #3
	(0,1,0), #2

	(1,0,0), #4
	(1,0,1), #5
	(1,1,1), #7
	(1,1,0)  #6
)
extraEdges = [0,4,1,5,3,7,2,6]

# graphics primitives and extras
def point(vertex):
	glBegin(GL_POINTS)
	glVertex3fv(vertex)
	glEnd()

def line(v1,v2):
	glBegin(GL_LINES)
	glVertex3fv(v1)
	glVertex3fv(v2)
	glEnd()

def polygon(vertices):
	glBegin(GL_POLYGON)
	for vertex in vertices:
		glVertex3fv(vertex)
	glEnd()

def line_strip(vertices):
	glBegin(GL_LINE_STRIP)
	for vertex in vertices:
		glVertex3fv(vertex)
	glEnd()

def line_loop(vertices):
	glBegin(GL_LINE_LOOP)
	for vertex in vertices:
		glVertex3fv(vertex)
	glEnd()

def quad_strip(vertices):
	glBegin(GL_QUAD_STRIP)
	for vertex in vertices:
		glVertex3fv(vertex)
	glEnd()

def triangle_strip():
	pass

def triangle_fan():
	pass

# 3D models
def cube():
	pass

def pyramid():
	pass

