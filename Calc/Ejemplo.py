import sys
import os
lib_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

sys.path.append(lib_path)
print(sys.path)

from FundamentosPython import nuevoTema

nuevoTema("Acceder a módulos superiores")