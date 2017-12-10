#!/usr/bin/python3
#-*- coding:utf-8 -*-

import math

def move(x,y,step,angle=0):
	nx = x + step*math.cos(angle)
	ny = y - step*math.sin(angle)
	return nx,ny;

if(__name__ == "__main__"):
	pass
