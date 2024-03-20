from bnipython.lib.bniClient import BNIClient
from bnipython.lib.api.oneGatePayment import OneGatePayment
from bnipython.lib.api.snapBI import SnapBI
from bnipython.lib.api.rdn import RDN
from bnipython.lib.api.rdl import RDL
from bnipython.lib.api.rdf import RDF
from bnipython.lib.api.bniDirect import BNIDIRECT
from bnipython.lib.api.fscm import FSCM

import sys
sys.modules['BNIClient'] = BNIClient
sys.modules['OneGatePayment'] = OneGatePayment
sys.modules['SnapBI'] = SnapBI
sys.modules['RDN'] = RDN
sys.modules['RDF'] = RDF
sys.modules['RDL'] = RDL
sys.modules['BNIDIRECT'] = BNIDIRECT
sys.modules['FSCM'] = FSCM