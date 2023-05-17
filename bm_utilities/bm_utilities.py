from Address_finder import AddressFinder as af
import geopandas as gpd
import pandas as pd
import quality_gates as qg
def address_finder(geodf,address):
    construct = af.AddressFinder(geodf)
    address = af.find_address(address)
    return address
def quality_gates_check(df,config):
    my_gate = qg.QualityGates()
    df=my_gate.run_Quality_Gates(df,config)
    return df



