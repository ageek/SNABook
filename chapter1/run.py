"""
This use pyplot as backend

"""


import networkx as net
import matplotlib.pyplot as plot
orgchart=net.read_pajek('ACME_orgchart.net')
net.draw(orgchart)
plot.show()

advice = net.read_pajek('ACME_advice.net')
net.draw(advice)
plot.show()
