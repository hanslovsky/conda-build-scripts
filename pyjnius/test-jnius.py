from __future__ import print_function

import jnius
from jnius import autoclass

AL = autoclass( 'java.util.ArrayList' )
al = AL()
for c in 'Hello World!':
	al.add( c )
print( al.toString() )
