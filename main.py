import sys
import os 
import argparse 

CURRENT_DIR = os.path.dirname(__file__)

parser=argparse.ArgumentParser()
parser.add_argument("-hamilton", action="store_true" , help="Generate Hamilton graph")
parser.add_argument("-non-hamilton", action="store_true" , help="Generate non hamilton graph")
args = parser.parse_args()