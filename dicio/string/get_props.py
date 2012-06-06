#!/usr/bin/env python
# coding: utf-8

'''
Get property names from the EcmaScript 5.1 standard.
'''

import sys
import re
import itertools

START_LINE = '''15.4 Array Objects\n'''
END_LINE = '''15.6 Boolean Objects\n'''

LEVEL_4_RE = re.compile(r'(^\d{1,2}\.\d+\.\d+\.\d+)\s*(.*)')

secao_ant = ''

with open('ecmascript_5_1.txt') as standard_text:
	section_iter = itertools.dropwhile(lambda s: s != START_LINE, standard_text)
	section_iter = itertools.takewhile(lambda s: s != END_LINE, section_iter)
	for lin in section_iter:
		lin = lin.strip()
		secao = titulo = ''
		achado = LEVEL_4_RE.match(lin)
		if achado:
			secao, titulo = achado.groups()
			if not titulo.strip():
				secao_ant = secao
				secao = ''
		elif secao_ant:
			secao = secao_ant
			secao_ant = ''
			titulo = lin.strip()
		if secao and titulo:
			print titulo
			
			
			
				
			
		
		
		
	
