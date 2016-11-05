from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from Image import *
from math import sqrt
# from time import sleep
from base import *

#string para identificar quando ESC for pressionado
ESCAPE = '\033'
RETURN = '\r'

angle = 45
fAspect = 0
#ID da janela GLUT
window = 0

angX, angY, angZ = 25,-10,0
control_move = False
move_count = 0

#superficies do cubo com quatro pontos
superficies = (
	 (0,1,2,3),
	 (3,2,7,6),
	 (6,7,5,4),
	 (4,5,1,0),
	 (1,5,7,2),
	 (4,0,3,6),
	 )

#vertices do cubo
vertices = (
	 (4, -0.2, -4), #0
	 (4, 0.2, -4),  #1
	 (-4, 0.2, -4), #2
	 (-4, -0.2, -4),#3
	 (4, -0.2, 4),  #4
	 (4, 0.2, 4),   #5
	 (-4, -0.2, 4), #6
	 (-4, 0.2, 4)   #7
	 )

vertices_bigger = (
	(0.2,-0.2,-0.2),
	(0.2,0.8,-0.2),
	(-0.2,0.8,-0.2),
	(-0.2,-0.2,-0.2),
	(0.2,-0.2,0.2),
	(0.2,0.8,0.2),
	(-0.2,-0.2,0.2),
	(-0.2,0.8,0.2)
	)

vertices_medium = (
	(0.2,-0.2,-0.2),
	(0.2,0.6,-0.2),
	(-0.2,0.6,-0.2),
	(-0.2,-0.2,-0.2),
	(0.2,-0.2,0.2),
	(0.2,0.6,0.2),
	(-0.2,-0.2,0.2),
	(-0.2,0.6,0.2)
	)

vertices_smaller = (
	(0.2,-0.2,-0.2),
	(0.2,0.4,-0.2),
	(-0.2,0.4,-0.2),
	(-0.2,-0.2,-0.2),
	(0.2,-0.2,0.2),
	(0.2,0.4,0.2),
	(-0.2,-0.2,0.2),
	(-0.2,0.4,0.2)
	)

square_mapper = {
	'h8': [-3.0,0.4,2.9], 'f1': [-1.3,0.4,-3.0], 'f2': [-1.3,0.4,-2.1], 'f3': [-1.3,0.4,-1.3], 'f4': [-1.3,0.4,-0.4], 'f5': [-1.3,0.4,0.4], 'f6': [-1.3,0.4,1.2], 'f7': [-1.3,0.4,2.0], 
	'h2': [-3.0,0.4,-2.1], 'h3': [-3.0,0.4,-1.3], 'h1': [-3.0,0.4,-3.0], 'h6': [-3.0,0.4,1.2], 'h7': [-3.0,0.4,2.0], 'h4': [-3.0,0.4,-0.4], 'h5': [-3.0,0.4,0.4], 'b4': [2.1,0.4,-0.4], 
	'b5': [2.1,0.4,0.4], 'b6': [2.1,0.4,1.2], 'b7': [2.1,0.4,2.0], 'b1': [2.1,0.4,-3.0], 'b2': [2.1,0.4,-2.1], 'b3': [2.1,0.4,-1.3], 'd6': [0.45,0.4,1.2], 'd7': [0.45,0.4,2.0], 
	'd4': [0.45,0.4,-0.4], 'd5': [0.45,0.4,0.4], 'd2': [0.45,0.4,-2.1], 'd3': [0.45,0.4,-1.3], 'd1': [0.45,0.4,-3.0], 'c7': [1.3,0.4,2.0], 'e5': [-0.4,0.4,0.4], 'b8': [2.1,0.4,2.9], 
	'f8': [-1.3,0.4,2.9], 'c5': [1.3,0.4,0.4], 'd8': [0.45,0.4,2.9], 'c4': [1.3,0.4,-0.4], 'g7': [-2.1,0.4,2.0], 'g6': [-2.1,0.4,1.2], 'g5': [-2.1,0.4,0.4], 'g4': [-2.1,0.4,-0.4], 
	'g3': [-2.1,0.4,-1.3], 'g2': [-2.1,0.4,-2.1], 'g1': [-2.1,0.4,-3.0], 'e4': [-0.4,0.4,-0.4], 'g8': [-2.1,0.4,2.9], 'a1': [2.9,0.4,-3.0], 'a3': [2.9,0.4,-1.3], 'a2': [2.9,0.4,-2.1], 
	'a5': [2.9,0.4,0.4], 'a4': [2.9,0.4,-0.4], 'a7': [2.9,0.4,2.0], 'a6': [2.9,0.4,1.2], 'c3': [1.3,0.4,-1.3], 'c2': [1.3,0.4,-2.1], 'c1': [1.3,0.4,-3.0], 'e6': [-0.4,0.4,1.2], 
	'e1': [-0.4,0.4,-3.0], 'c6': [1.3,0.4,1.2], 'e3': [-0.4,0.4,-1.3], 'e2': [-0.4,0.4,-2.1], 'e7': [-0.4,0.4,2.0], 'a8': [2.9,0.4,2.9], 'c8': [1.3,0.4,2.9], 'e8': [-0.4,0.4,2.9]
	}

black_pawn = ['a7','b7','c7','d7','e7','f7','g7','h7']
black_rook = ['h8','a8']
black_knight = ['g8','b8']
black_bishop = ['f8','c8']
black_queen = ['d8']
black_king = ['e8']

white_pawn = ['a2','b2','c2','d2','e2','f2','g2','h2']
white_rook = ['a1','h1']
white_knight = ['b1','g1']
white_bishop = ['c1','f1']
white_queen = ['d1']
white_king = ['e1']


# steps for simulation
xeque_mate = {
	1: [white_pawn, 'e2', 'e4'],
	2: [black_pawn, 'e7', 'e5'],
	3: [white_queen, 'd1', 'h5'],
	4: [black_knight, 'b8', 'c6'],
	5: [white_bishop, 'f1', 'c4'],
	6: [black_knight, 'g8', 'f6'],
	7: [white_queen, 'h5', 'f7']
}

def draw_table():
	glBegin(GL_QUADS)
	glVertex3fv(vertices[0])
	glVertex3fv(vertices[1])
	glVertex3fv(vertices[2])
	glVertex3fv(vertices[3])

	glVertex3fv(vertices[3])
	glVertex3fv(vertices[2])
	glVertex3fv(vertices[7])
	glVertex3fv(vertices[6])

	glVertex3fv(vertices[6])
	glVertex3fv(vertices[7])
	glVertex3fv(vertices[5])
	glVertex3fv(vertices[4])

	glVertex3fv(vertices[4])
	glVertex3fv(vertices[5])
	glVertex3fv(vertices[1])
	glVertex3fv(vertices[0])

	glTexCoord2f(1, 1); glVertex3fv(vertices[1])
	glTexCoord2f(1, 0); glVertex3fv(vertices[5])
	glTexCoord2f(0, 0); glVertex3fv(vertices[7])
	glTexCoord2f(0, 1); glVertex3fv(vertices[2])

	glVertex3fv(vertices[4])
	glVertex3fv(vertices[0])
	glVertex3fv(vertices[3])
	glVertex3fv(vertices[6])
	glEnd()

def draw_small_piece(x,y,z):
	glBegin(GL_QUADS)
	glTexCoord2f(0, 0); glVertex3fv(vertices_smaller[0])
	glTexCoord2f(0, 1); glVertex3fv(vertices_smaller[1])
	glTexCoord2f(1, 1); glVertex3fv(vertices_smaller[2])
	glTexCoord2f(1, 0); glVertex3fv(vertices_smaller[3])

	glTexCoord2f(0, 0); glVertex3fv(vertices_smaller[3])
	glTexCoord2f(0, 1); glVertex3fv(vertices_smaller[2])
	glTexCoord2f(1, 1); glVertex3fv(vertices_smaller[7])
	glTexCoord2f(1, 0); glVertex3fv(vertices_smaller[6])

	glTexCoord2f(0, 0); glVertex3fv(vertices_smaller[6])
	glTexCoord2f(0, 1); glVertex3fv(vertices_smaller[7])
	glTexCoord2f(1, 1); glVertex3fv(vertices_smaller[5])
	glTexCoord2f(1, 0); glVertex3fv(vertices_smaller[4])

	glTexCoord2f(0, 0); glVertex3fv(vertices_smaller[4])
	glTexCoord2f(0, 1); glVertex3fv(vertices_smaller[5])
	glTexCoord2f(1, 1); glVertex3fv(vertices_smaller[1])
	glTexCoord2f(1, 0); glVertex3fv(vertices_smaller[0])

	glVertex3fv(vertices_smaller[1])
	glVertex3fv(vertices_smaller[5])
	glVertex3fv(vertices_smaller[7])
	glVertex3fv(vertices_smaller[2])

	glVertex3fv(vertices_smaller[4])
	glVertex3fv(vertices_smaller[0])
	glVertex3fv(vertices_smaller[3])
	glVertex3fv(vertices_smaller[6])
	glEnd()
	# pass

def draw_medium_piece(x,y,z):
	glBegin(GL_QUADS)
	glTexCoord2f(0, 0); glVertex3fv(vertices_medium[0])
	glTexCoord2f(0, 1); glVertex3fv(vertices_medium[1])
	glTexCoord2f(1, 1); glVertex3fv(vertices_medium[2])
	glTexCoord2f(1, 0); glVertex3fv(vertices_medium[3])

	glTexCoord2f(0, 0); glVertex3fv(vertices_medium[3])
	glTexCoord2f(0, 1); glVertex3fv(vertices_medium[2])
	glTexCoord2f(1, 1); glVertex3fv(vertices_medium[7])
	glTexCoord2f(1, 0); glVertex3fv(vertices_medium[6])

	glTexCoord2f(0, 0); glVertex3fv(vertices_medium[6])
	glTexCoord2f(0, 1); glVertex3fv(vertices_medium[7])
	glTexCoord2f(1, 1); glVertex3fv(vertices_medium[5])
	glTexCoord2f(1, 0); glVertex3fv(vertices_medium[4])

	glTexCoord2f(0, 0); glVertex3fv(vertices_medium[4])
	glTexCoord2f(0, 1); glVertex3fv(vertices_medium[5])
	glTexCoord2f(1, 1); glVertex3fv(vertices_medium[1])
	glTexCoord2f(1, 0); glVertex3fv(vertices_medium[0])

	glVertex3fv(vertices_medium[1])
	glVertex3fv(vertices_medium[5])
	glVertex3fv(vertices_medium[7])
	glVertex3fv(vertices_medium[2])

	glVertex3fv(vertices_medium[4])
	glVertex3fv(vertices_medium[0])
	glVertex3fv(vertices_medium[3])
	glVertex3fv(vertices_medium[6])
	glEnd()

def draw_big_piece(x,y,z):
	glBegin(GL_QUADS)
	glTexCoord2f(0, 0); glVertex3fv(vertices_bigger[0])
	glTexCoord2f(0, 1); glVertex3fv(vertices_bigger[1])
	glTexCoord2f(1, 1); glVertex3fv(vertices_bigger[2])
	glTexCoord2f(1, 0); glVertex3fv(vertices_bigger[3])

	glTexCoord2f(0, 0); glVertex3fv(vertices_bigger[3])
	glTexCoord2f(0, 1); glVertex3fv(vertices_bigger[2])
	glTexCoord2f(1, 1); glVertex3fv(vertices_bigger[7])
	glTexCoord2f(1, 0); glVertex3fv(vertices_bigger[6])

	glTexCoord2f(0, 0); glVertex3fv(vertices_bigger[6])
	glTexCoord2f(0, 1); glVertex3fv(vertices_bigger[7])
	glTexCoord2f(1, 1); glVertex3fv(vertices_bigger[5])
	glTexCoord2f(1, 0); glVertex3fv(vertices_bigger[4])

	glTexCoord2f(0, 0); glVertex3fv(vertices_bigger[4])
	glTexCoord2f(0, 1); glVertex3fv(vertices_bigger[5])
	glTexCoord2f(1, 1); glVertex3fv(vertices_bigger[1])
	glTexCoord2f(1, 0); glVertex3fv(vertices_bigger[0])

	glVertex3fv(vertices_bigger[1])
	glVertex3fv(vertices_bigger[5])
	glVertex3fv(vertices_bigger[7])
	glVertex3fv(vertices_bigger[2])

	glVertex3fv(vertices_bigger[4])
	glVertex3fv(vertices_bigger[0])
	glVertex3fv(vertices_bigger[3])
	glVertex3fv(vertices_bigger[6])
	glEnd()

def reset_board():
	global black_pawn, black_rook, black_knight, black_bishop, black_queen, black_king
	global white_pawn, white_rook, white_knight, white_bishop, white_queen, white_king
	global square_mapper

	square_mapper = {
	'h8': [-3.0,0.4,2.9], 'f1': [-1.3,0.4,-3.0], 'f2': [-1.3,0.4,-2.1], 'f3': [-1.3,0.4,-1.3], 'f4': [-1.3,0.4,-0.4], 'f5': [-1.3,0.4,0.4], 'f6': [-1.3,0.4,1.2], 'f7': [-1.3,0.4,2.0], 
	'h2': [-3.0,0.4,-2.1], 'h3': [-3.0,0.4,-1.3], 'h1': [-3.0,0.4,-3.0], 'h6': [-3.0,0.4,1.2], 'h7': [-3.0,0.4,2.0], 'h4': [-3.0,0.4,-0.4], 'h5': [-3.0,0.4,0.4], 'b4': [2.1,0.4,-0.4], 
	'b5': [2.1,0.4,0.4], 'b6': [2.1,0.4,1.2], 'b7': [2.1,0.4,2.0], 'b1': [2.1,0.4,-3.0], 'b2': [2.1,0.4,-2.1], 'b3': [2.1,0.4,-1.3], 'd6': [0.45,0.4,1.2], 'd7': [0.45,0.4,2.0], 
	'd4': [0.45,0.4,-0.4], 'd5': [0.45,0.4,0.4], 'd2': [0.45,0.4,-2.1], 'd3': [0.45,0.4,-1.3], 'd1': [0.45,0.4,-3.0], 'c7': [1.3,0.4,2.0], 'e5': [-0.4,0.4,0.4], 'b8': [2.1,0.4,2.9], 
	'f8': [-1.3,0.4,2.9], 'c5': [1.3,0.4,0.4], 'd8': [0.45,0.4,2.9], 'c4': [1.3,0.4,-0.4], 'g7': [-2.1,0.4,2.0], 'g6': [-2.1,0.4,1.2], 'g5': [-2.1,0.4,0.4], 'g4': [-2.1,0.4,-0.4], 
	'g3': [-2.1,0.4,-1.3], 'g2': [-2.1,0.4,-2.1], 'g1': [-2.1,0.4,-3.0], 'e4': [-0.4,0.4,-0.4], 'g8': [-2.1,0.4,2.9], 'a1': [2.9,0.4,-3.0], 'a3': [2.9,0.4,-1.3], 'a2': [2.9,0.4,-2.1], 
	'a5': [2.9,0.4,0.4], 'a4': [2.9,0.4,-0.4], 'a7': [2.9,0.4,2.0], 'a6': [2.9,0.4,1.2], 'c3': [1.3,0.4,-1.3], 'c2': [1.3,0.4,-2.1], 'c1': [1.3,0.4,-3.0], 'e6': [-0.4,0.4,1.2], 
	'e1': [-0.4,0.4,-3.0], 'c6': [1.3,0.4,1.2], 'e3': [-0.4,0.4,-1.3], 'e2': [-0.4,0.4,-2.1], 'e7': [-0.4,0.4,2.0], 'a8': [2.9,0.4,2.9], 'c8': [1.3,0.4,2.9], 'e8': [-0.4,0.4,2.9]
	}

	black_pawn = ['a7','b7','c7','d7','e7','f7','g7','h7']
	black_rook = ['h8','a8']
	black_knight = ['g8','b8']
	black_bishop = ['f8','c8']
	black_queen = ['d8']
	black_king = ['e8']

	white_pawn = ['a2','b2','c2','d2','e2','f2','g2','h2']
	white_rook = ['a1','h1']
	white_knight = ['b1','g1']
	white_bishop = ['c1','f1']
	white_queen = ['d1']
	white_king = ['e1']

def get_distance(initialPos, finalPos):
	return sqrt(pow((finalPos[2] - initialPos[2]),2) + 
				pow((finalPos[1] - initialPos[1]),2) + 
				pow((finalPos[0] - initialPos[0]),2))

def move(piece, pieceIndex, initialPos, finalPos, distance):
	# global white_pawn, square_mapper
	# timer(2)
	# square_mapper[piece[pieceIndex]] = finalPos
	
	finalXIsBigger = bool(square_mapper[finalPos][0] > square_mapper[initialPos][0])
	finalZIsBigger = bool(square_mapper[finalPos][2] > square_mapper[initialPos][2])

	if finalXIsBigger:
		if square_mapper[initialPos][0] < square_mapper[finalPos][0]:
			square_mapper[initialPos][0] += 0.1
	else:
		if square_mapper[initialPos][0] > square_mapper[finalPos][0]:
			square_mapper[initialPos][0] -= 0.1
	if finalZIsBigger:
		if square_mapper[initialPos][2] < square_mapper[finalPos][2]:
			square_mapper[initialPos][2] += 0.1
	else:
		if square_mapper[initialPos][2] > square_mapper[finalPos][2]:
			square_mapper[initialPos][2] -= 0.1
	
#carregar texturas das imagens salvas no array
def LoadTextures(picture_name):
	image = open(picture_name)
	ix = image.size[0]
	iy = image.size[1]
	strImage = image.tostring("raw", "RGBX", 0, -1)

	glBindTexture(GL_TEXTURE_2D, glGenTextures(1))
	glPixelStorei(GL_UNPACK_ALIGNMENT, 1)
	glTexImage2D(GL_TEXTURE_2D, 0, 3, ix, iy, 0, GL_RGBA, GL_UNSIGNED_BYTE, strImage)
	glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP)
	glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP)
	glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
	glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
	glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
	glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_DECAL)

def DrawGLScene():
	posicaoLuz = [-50.0, 30.0, 20.0, 1.0]
	glLightfv(GL_LIGHT0, GL_POSITION, posicaoLuz)

	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
	# glEnable(GL_TEXTURE_2D)
	LoadTextures("chess_table.jpg")
	glLoadIdentity()
	glPushMatrix()
	glColor3f(1.0, 1.0, 0.0)
	glTranslatef(0.0,-2.0,-16.0) #afastar objeto no eixo z
	glRotatef(angX,1,0,0)
	glRotatef(angY,0,1,0)
	draw_table()
	
	# glDisable(GL_TEXTURE_2D)
	# glColor3f(0.9, 0.8, 0.7)

	# DRAW WHITE PAWN
	LoadTextures("images/white_pieces/white_pawn.jpg")
	for i in range(8):
		coord = square_mapper[white_pawn[i]]
		glPushMatrix()
		glTranslatef(coord[0], coord[1], coord[2]) #afastar objeto no eixo z
		draw_small_piece(0.2, 20, 20)
		glPopMatrix()

	# DRAW WHITE ROOK
	LoadTextures("images/white_pieces/white_rook.jpg")
	coord = square_mapper[white_rook[0]]
	glPushMatrix()
	glTranslatef(coord[0],coord[1],coord[2])
	draw_medium_piece(0.2, 20, 20)
	glPopMatrix()
	coord = square_mapper[white_rook[1]]
	glPushMatrix()
	glTranslatef(coord[0],coord[1],coord[2])
	draw_medium_piece(0.2, 20, 20)
	glPopMatrix()
	
	# DRAW WHITE KNIGHT
	LoadTextures("images/white_pieces/white_knight.jpg")
	coord = square_mapper[white_knight[0]]
	glPushMatrix()
	glTranslatef(coord[0],coord[1],coord[2])
	draw_medium_piece(0.2, 20, 20)
	glPopMatrix()
	coord = square_mapper[white_knight[1]]
	glPushMatrix()
	glTranslatef(coord[0],coord[1],coord[2])
	draw_medium_piece(0.2, 20, 20)
	glPopMatrix()

	# DRAW WHITE BISHOP
	LoadTextures("images/white_pieces/white_bishop.jpg")
	coord = square_mapper[white_bishop[0]]
	glPushMatrix()
	glTranslatef(coord[0],coord[1],coord[2])
	draw_medium_piece(0.2, 20, 20)
	glPopMatrix()
	coord = square_mapper[white_bishop[1]]
	glPushMatrix()
	glTranslatef(coord[0],coord[1],coord[2])
	draw_medium_piece(0.2, 20, 20)
	glPopMatrix()

	# DRAW WHITE QUEEN
	LoadTextures("images/white_pieces/white_queen.jpg")
	coord = square_mapper[white_queen[0]]
	glPushMatrix()
	glTranslatef(coord[0],coord[1],coord[2])
	draw_big_piece(0.2, 20, 20)
	glPopMatrix()

	# DRAW WHITE KING
	LoadTextures("images/white_pieces/white_king.jpg")
	coord = square_mapper[white_king[0]]
	glPushMatrix()
	glTranslatef(coord[0],coord[1],coord[2])
	draw_big_piece(0.2, 20, 20)
	glPopMatrix()

	# DRAW BLACK PAWN
	LoadTextures("images/black_pieces/black_pawn.jpg")
	glColor3f(0.1, 0.2, 0.3)
	for i in range(8):	
		coord = square_mapper[black_pawn[i]]
		glPushMatrix()
		glTranslatef(coord[0], coord[1], coord[2]) #afastar objeto no eixo z
		draw_small_piece(0.2, 20, 20)
		glPopMatrix()

	# DRAW black ROOK
	LoadTextures("images/black_pieces/black_rook.jpg")
	coord = square_mapper[black_rook[0]]
	glPushMatrix()
	glTranslatef(coord[0],coord[1],coord[2])
	draw_medium_piece(0.2, 20, 20)
	glPopMatrix()
	coord = square_mapper[black_rook[1]]
	glPushMatrix()
	glTranslatef(coord[0],coord[1],coord[2])
	draw_medium_piece(0.2, 20, 20)
	glPopMatrix()
	
	# DRAW black KNIGHT
	LoadTextures("images/black_pieces/black_knight.jpg")
	coord = square_mapper[black_knight[0]]
	glPushMatrix()
	glTranslatef(coord[0],coord[1],coord[2])
	draw_medium_piece(0.2, 20, 20)
	glPopMatrix()
	coord = square_mapper[black_knight[1]]
	glPushMatrix()
	glTranslatef(coord[0],coord[1],coord[2])
	draw_medium_piece(0.2, 20, 20)
	glPopMatrix()

	# DRAW black BISHOP
	LoadTextures("images/black_pieces/black_bishop.jpg")
	coord = square_mapper[black_bishop[0]]
	glPushMatrix()
	glTranslatef(coord[0],coord[1],coord[2])
	draw_medium_piece(0.2, 20, 20)
	glPopMatrix()
	coord = square_mapper[black_bishop[1]]
	glPushMatrix()
	glTranslatef(coord[0],coord[1],coord[2])
	draw_medium_piece(0.2, 20, 20)
	glPopMatrix()

	# DRAW black QUEEN
	LoadTextures("images/black_pieces/black_queen.jpg")
	coord = square_mapper[black_queen[0]]
	glPushMatrix()
	glTranslatef(coord[0],coord[1],coord[2])
	draw_big_piece(0.2, 20, 20)
	glPopMatrix()

	# DRAW black KING
	LoadTextures("images/black_pieces/black_king.jpg")
	coord = square_mapper[black_king[0]]
	glPushMatrix()
	glTranslatef(coord[0],coord[1],coord[2])
	draw_big_piece(0.2, 20, 20)
	glPopMatrix()

	glPopMatrix()

	glutSwapBuffers()

	# sleep(0.033)

#Configurar parametros iniciais da janela
#chamada logo apos criar a janela
def InitGL(width, height):
	# global angle
	#carregar texturas
	LoadTextures("chess_table.jpg")
	glEnable(GL_TEXTURE_2D)
	luzAmbiente = [0.2,0.2,0.2,1.0] 
	luzDifusa = [0.7,0.7,0.7,1.0] 
	luzEspecular = [0.0, 0.0, 0.0, 1.0]

	especularidade = [1.0,1.0,1.0,1.0]
	especMaterial = 60

	#limpar o fundo com cor preta
	glClearColor(0.0,0.0,0.0,1.0)

	glShadeModel(GL_SMOOTH)
	glMaterialfv(GL_FRONT, GL_SPECULAR, especularidade)
	glMateriali(GL_FRONT, GL_SHININESS, especMaterial)
	
	glLightModelfv(GL_LIGHT_MODEL_AMBIENT, luzAmbiente)

	glLightfv(GL_LIGHT0, GL_AMBIENT, luzAmbiente)
	glLightfv(GL_LIGHT0, GL_DIFFUSE, luzDifusa)
	glLightfv(GL_LIGHT0, GL_SPECULAR, luzEspecular)

	# Habilita a definicao da cor do material a partir da cor corrente
	glEnable(GL_COLOR_MATERIAL)
	# Habilita o uso de iluminacao
	glEnable(GL_LIGHTING)
	# Habilita a luz de numero 0
	glEnable(GL_LIGHT0)
	# Habilita o depth-buffering
	glEnable(GL_DEPTH_TEST)

	# angle=45

def EspecificaParametrosVisualizacao():
	global angle, fAspect

	glMatrixMode(GL_PROJECTION)
	glLoadIdentity()
	gluPerspective(angle, fAspect, 0.4, 500)
	glMatrixMode(GL_MODELVIEW)
	glLoadIdentity()
	gluLookAt(0,80,500, 0,0,0, 0,1,0)

#Redesenhar janela quando ela for redimensionada
def ReSizeGLScene(width, height):
	global fAspect
	#prevenir que tamanho seja igual a zero
	if height == 0:
		height = 1

	fAspect = width/height

	EspecificaParametrosVisualizacao()

#Gerenciar teclas pressionadas
def keyPressed(*args):
	global angY, angX, control_move, move_count, white_pawn

	#ESCAPE
	if args[0] == ESCAPE:
		sys.exit()
	if args[0] == RETURN:
		print move_count
		if move_count < 7:
			move_count += 1
			square_mapper['temp'] = square_mapper[xeque_mate[move_count][1]]
			control_move = True
		else:
			move_count = 0
			control_move = False
			reset_board()
			print square_mapper['d8']
			# print white_pawn
	if args[0] == GLUT_KEY_UP:
		angX -= 10
	if args[0] == GLUT_KEY_DOWN:
		angX += 10
	if args[0] == GLUT_KEY_LEFT:
		angY += 10
	if args[0] == GLUT_KEY_RIGHT:
		angY -= 10

def mouse(button, state, x, y):
	global angle

	if (button == GLUT_LEFT_BUTTON):
		angle -= 10
		EspecificaParametrosVisualizacao()
	if (button == GLUT_RIGHT_BUTTON):
		angle += 10
		EspecificaParametrosVisualizacao()

	glutPostRedisplay()

def timer(value):
	global control_move, move_count

	if control_move:
		# print "control_move ", control_move
		# print "white_pawn ", xeque_mate[move_count][0]
		move(xeque_mate[move_count][0], 
			 xeque_mate[move_count][0].index(xeque_mate[move_count][1]),
			 'temp',xeque_mate[move_count][2],0)

		initialPos = [ float(str(round(elem,4))[:-2]) for elem in square_mapper['temp'] ]
		finalPos = [ float(str(round(elem,4))[:-2]) for elem in square_mapper[xeque_mate[move_count][2]] ]
		# print "initial: ", initialPos
		# print "final: ", finalPos
		if initialPos == finalPos:
			control_move = False
			xeque_mate[move_count][0][xeque_mate[move_count][0].index(xeque_mate[move_count][1])] = xeque_mate[move_count][2]
			# print xeque_mate[move_count][0]
			
	glutPostRedisplay()
	glutTimerFunc(25, timer, control_move)

def main(*args):
	global window, control_move

	#passar argumentos para funcao init
	#deve ser chamada antes de glutCreateWindow
	glutInit(sys.argv)

	#configurar modo de display inicial
	glutInitDisplayMode(GLUT_RGB | GLUT_DOUBLE | GLUT_DEPTH)

	#dimensoes da janela
	glutInitWindowSize(900, 900)

	#posicao inicial da janela
	glutInitWindowPosition(600,0)

	#criar janela, recuperar ID e configurar titulo da janela
	window = glutCreateWindow("Chess Simulator")

	#registrar qual funcao ira desenhar
	glutDisplayFunc(DrawGLScene)

	#Funciona como um while loop pra redesenhar o objeto constantemente
	glutIdleFunc(DrawGLScene)

	# Funcao a ser chamada quando janela for redimensionada
	glutReshapeFunc(ReSizeGLScene)

	#Funcao a ser chamada quando alguma tecla for pressionada
	glutKeyboardFunc(keyPressed)
	glutSpecialFunc(keyPressed)
	glutMouseFunc(mouse)

	# timer
	glutTimerFunc(25, timer, control_move)

	#inicializar janela
	InitGL(900,900)

	#iniciar evento
	glutMainLoop()

if __name__ == '__main__':
	main()