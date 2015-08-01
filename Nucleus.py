#!/usr/bin/python

import shodan
import GeoIP
import sys

# Configurar API Key
API_KEY = "API_Shodan"

if len(sys.argv) == 1:
	print 'Uso: %s <Query>' % sys.argv[0] 
	sys.exit(1)
try:
	api = shodan.Shodan(API_KEY)
	# Lanza la busqueda
	query = ' '.join(sys.argv[1:])
	res = api.search(query, limit=200, offset=None)
	lista_paises = []
	# Recorre resultados para imprimir ip's que coinciden con la busqueda
	for serv in res['matches']: 
		gi = GeoIP.new(GeoIP.GEOIP_MEMORY_CACHE)
		#print  serv['ip_str'] + '-' + gi.country_name_by_addr(serv['ip_str'])
		lista_paises.append(gi.country_name_by_addr(serv['ip_str']))

	lista_paises.sort()
	print lista_paises
	print "Resultados en lista: " + str(len(lista_paises))
	print "Resultados encontrados: %d" % res['total']
	print "Resultados devueltos: %d" % len(res['matches'])

except Exception, e:
	print 'Error: %s' % e
	sys.exit(1)
