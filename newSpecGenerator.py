import ontospy
from ontodocs.viz.viz_html_multi import *

class SpecGenerator():
    '''
    Generates specification from an ontology
    '''

    def __init__(self, rdf_path, output_path, onto_title, onto_text):
        RDFpath = rdf_path
        outputPath = output_path

        # load current ontology from EthOn github
        g = ontospy.Ontospy(RDFpath)
        #if g.properties.__len__() == 0:
        #    exit(1)

        # invoke EthOn multi-HTML page visualizer
        #v = KompleteViz(g, onto_title, "paper", onto_text)
        v = KompleteViz(g, onto_title, "paper")

        # build HTML
        v.build(outputPath)
        
        # serialize ontology
        if '/' in outputPath:
            destination_prefix = outputPath+'/EthOn_'+outputPath.split('/')[-1]
        else:
            destination_prefix = outputPath+'/EthOn'

        g.rdflib_graph.serialize(destination=destination_prefix+'.ttl', format='turtle')
        g.rdflib_graph.serialize(destination=destination_prefix+'.xml', format='xml')
        g.rdflib_graph.serialize(destination=destination_prefix+'.nt', format='nt')

def main():
    text = "The EthOn Ethereum ontology, described using W3C RDF Schema and the Web Ontology Language. It is closely aligned with Gavin Wood's Ethereum yellow paper."
    SpecGenerator(rdf_path="https://raw.githubusercontent.com/ConsenSys/EthOn/master/EthOn.ttl", output_path="spec", onto_title="EthOn: Ethereum Ontology", onto_text=text)
    text = "The ERC20 extension of the EthOn Ethereum ontology, described using W3C RDF Schema and the Web Ontology Language. It describes the token standard suggested by Fabian Vogelsteller in Ethereum Improvement Proposal (EIP) #20 and implemented in late 2015. For more information see https://github.com/ethereum/eips/issues/20"
    SpecGenerator(rdf_path="https://raw.githubusercontent.com/ConsenSys/EthOn/master/ERC20/EthOn_ERC20.ttl", output_path="spec/ERC20", onto_title="EthOn: ERC20 Extension", onto_text=text)
    text = "The Contracts extension of the EthOn Ethereum ontology, described using W3C RDF Schema and the Web Ontology Language. It describes concepts and properties specific to smart contracts."
    SpecGenerator(rdf_path="https://raw.githubusercontent.com/ConsenSys/EthOn/master/Contracts/EthOn_Contracts.ttl", output_path="spec/Contracts", onto_title="EthOn: Contracts Extension", onto_text=text)

main()
