from LJ_fetch import *
import networkx as net
import matplotlib.pyplot as plot



def main():
    g=net.Graph()
    #read_lj_friends(g,'kozel_na_sakse')
    snowball_sampling(g,'kozel_na_sakse',2)
    net.draw(g)
    plot.show()   
    net.write_pajek(g,'lj_friends.net')


if __name__ == '__main__':
    main()
