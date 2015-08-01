#!/usr/bin/python

import shodan
import sys

# Configurar API Key
API_KEY = "boGy4JLA2KaTNEIZIn61qaV7Mwf3D8AC"

if len(sys.argv) == 1:
	print 'Uso: %s <Query>' % sys.argv[0] 
	sys.exit(1)
try:
	api = shodan.Shodan(API_KEY)
	# Lanza la busqueda
	query = ' '.join(sys.argv[1:])
	res = api.search(query)
	# Recorre resultados para imprimir ip's que coinciden con la busqueda
	for serv in res['matches']: 
		print  "Pais %s" % res.get('country_name')

	print "Resultados encontrados: %d" % res['total']
	print "Resultados devueltos: %d" % len(res['matches'])

except Exception, e:
	print 'Error: %s' % e
	sys.exit(1)