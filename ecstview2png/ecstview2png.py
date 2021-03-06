'''
This script converts an Ecstatica view file into a PNG image

Author: Fabian Hachenberg
'''

import Ecstatica
import Ecstatica.View
import Ecstatica.Camera
import Ecstatica.Graphic

import pygame.image

import argparse

def convertView(view_filename, output_filename, palette_filename=None):
	if palette_filename != None:
		graphic = Ecstatica.Graphic.loadGraphic(palette_filename)
		palette = graphic.palette
	else:
		palette = default_palette
	
	cam = Ecstatica.Camera.Camera((0,0,0),(0,0,1),1.0)
	
	f = open(view_filename, "rb")
	view = Ecstatica.View.loadView(cam, f)
	f.close()	
		
	pygame.display.init()
	surf = pygame.image.fromstring("".join(map(chr, view.colordata)), (320,200), "P")
	surf.set_palette(palette)
	pygame.image.save(surf, output_filename)
	
	return output_filename

default_palette = [(0, 0, 0), (255, 255, 255), (255, 0, 0), (255, 255, 0), (79, 79, 79), (143, 143, 143), (0, 0, 191), (127, 191, 255), (243, 243, 243), (255, 255, 255), (255, 255, 255), (255, 255, 255), (255, 255, 255), (255, 255, 255), (255, 255, 255), (255, 255, 255), (51, 19, 11), (55, 19, 11), (63, 23, 11), (67, 23, 11), (75, 27, 15), (79, 27, 15), (87, 31, 15), (91, 31, 15), (99, 35, 19), (103, 35, 19), (111, 39, 19), (115, 39, 19), (123, 43, 23), (127, 43, 23), (135, 47, 23), (139, 47, 23), (31, 15, 0), (39, 19, 0), (51, 23, 0), (59, 31, 0), (71, 35, 0), (79, 39, 7), (91, 47, 7), (99, 51, 7), (111, 55, 11), (119, 63, 15), (131, 67, 19), (139, 75, 23), (151, 79, 27), (159, 87, 31), (171, 91, 35), (179, 99, 39), (191, 107, 47), (195, 115, 51), (199, 123, 59), (203, 131, 63), (207, 139, 71), (211, 147, 79), (215, 155, 83), (219, 163, 91), (223, 171, 99), (227, 179, 107), (231, 187, 115), (235, 195, 123), (239, 203, 131), (243, 211, 139), (251, 219, 151), (255, 227, 159), (0, 31, 0), (0, 35, 0), (0, 43, 0), (0, 51, 0), (0, 59, 0), (0, 67, 0), (0, 71, 0), (0, 79, 0), (0, 87, 0), (0, 95, 0), (0, 103, 0), (0, 111, 0), (0, 115, 0), (0, 123, 0), (0, 131, 0), (0, 139, 0), (0, 147, 0), (7, 151, 7), (15, 159, 15), (23, 167, 23), (31, 175, 31), (43, 183, 43), (55, 187, 55), (67, 195, 67), (79, 203, 79), (91, 211, 91), (103, 219, 103), (119, 223, 119), (135, 231, 135), (151, 239, 151), (167, 247, 167), (187, 255, 187), (15, 15, 15), (23, 23, 23), (27, 27, 27), (35, 35, 35), (43, 43, 43), (51, 51, 51), (59, 59, 59), (67, 67, 67), (75, 75, 75), (83, 83, 83), (91, 91, 91), (99, 99, 99), (107, 107, 107), (115, 115, 115), (123, 123, 123), (131, 131, 131), (139, 139, 139), (147, 147, 147), (151, 151, 151), (159, 159, 159), (167, 167, 167), (175, 175, 175), (183, 183, 183), (191, 191, 191), (199, 199, 199), (207, 207, 207), (215, 215, 215), (223, 223, 223), (231, 231, 231), (239, 239, 239), (247, 247, 247), (255, 255, 255), (0, 0, 31), (0, 0, 35), (0, 0, 43), (0, 0, 51), (0, 0, 59), (0, 0, 67), (0, 0, 75), (0, 0, 79), (0, 0, 87), (0, 0, 95), (0, 0, 103), (0, 0, 111), (0, 0, 115), (0, 0, 123), (0, 0, 131), (0, 0, 139), (0, 0, 147), (7, 7, 151), (15, 15, 159), (23, 23, 167), (31, 31, 175), (43, 43, 183), (55, 55, 187), (67, 67, 195), (79, 79, 203), (91, 91, 211), (103, 103, 219), (119, 119, 223), (135, 135, 231), (151, 151, 239), (167, 167, 247), (187, 187, 255), (23, 23, 0), (27, 27, 0), (35, 35, 0), (43, 43, 0), (51, 51, 0), (59, 59, 0), (67, 67, 0), (75, 75, 0), (83, 83, 0), (87, 87, 0), (95, 95, 0), (103, 103, 0), (111, 111, 0), (119, 119, 0), (127, 127, 0), (135, 135, 0), (143, 143, 0), (147, 147, 0), (155, 155, 7), (163, 163, 11), (171, 171, 15), (179, 179, 19), (187, 187, 27), (195, 195, 31), (203, 203, 39), (207, 207, 47), (215, 215, 51), (223, 223, 59), (231, 231, 67), (239, 239, 75), (247, 247, 87), (255, 255, 95), (31, 0, 0), (35, 0, 0), (43, 0, 0), (51, 0, 0), (59, 0, 0), (67, 0, 0), (71, 0, 0), (79, 0, 0), (87, 0, 0), (95, 0, 0), (103, 0, 0), (111, 0, 0), (115, 0, 0), (123, 0, 0), (131, 0, 0), (139, 0, 0), (147, 0, 0), (151, 0, 0), (159, 7, 7), (167, 11, 11), (175, 15, 15), (183, 19, 19), (187, 27, 27), (195, 31, 31), (203, 35, 35), (211, 43, 43), (219, 51, 51), (223, 55, 55), (231, 67, 67), (239, 75, 75), (247, 83, 83), (255, 91, 91), (23, 0, 23), (27, 0, 27), (35, 0, 35), (43, 0, 43), (51, 0, 51), (59, 0, 59), (67, 0, 67), (75, 7, 75), (83, 7, 83), (87, 7, 87), (95, 7, 95), (103, 11, 103), (111, 11, 111), (119, 15, 119), (127, 15, 127), (135, 19, 135), (143, 23, 143), (147, 27, 147), (155, 35, 155), (163, 43, 163), (171, 55, 171), (179, 63, 179), (187, 71, 187), (195, 83, 195), (203, 95, 203), (207, 103, 207), (215, 119, 215), (223, 131, 223), (231, 143, 231), (239, 155, 239), (247, 171, 247), (255, 187, 255)]

if __name__ == "__main__":
	
	parser = argparse.ArgumentParser(description='Convert Ecstatica View file into PNG image')
	parser.add_argument('--view', dest="view_filename", type=str, action="store", help='view file to convert')
	parser.add_argument('--output', dest='output_filename', type=str, action='store', default="output.png", help='output filename')
	parser.add_argument('--palette', dest='palette_filename', type=str, action='store', help='the image file in which the palette is saved')
	
	args = parser.parse_args()
	
	if args.view_filename == None:
		print("Error -- View filename required")
		raise SystemExit(255)

	convertView(args.view_filename, args.output_filename, args.palette_filename)	
