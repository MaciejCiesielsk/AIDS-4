import sys
import os 
import argparse 
import random
from hamilton import Hamilton


CURRENT_DIR = os.path.dirname(__file__)

parser=argparse.ArgumentParser()
parser.add_argument("-hamilton", action="store_true" , help="Generate Hamilton graph")
parser.add_argument("-non-hamilton", action="store_true" , help="Generate non hamilton graph")
args = parser.parse_args()



if args.hamilton:
    saturation = float(input("Enter saturation: "))
    nodes = int(input("Enter number of nodes: "))
    generation = Hamilton(nodes, saturation)
    print("Type Help for list of commands")
    while True:
        action = input('action> ').lower()
        if action == "help":
            print("Help".center(50, "-"))
            print("List of commands:")
            print("Print - print graph")
            print("Exit - exit program")
            print("-".center(50, "-"))
            continue

        if action == "print":
            generation.print_matrix()
            continue
        if action == "euler":
            print(generation.find_eulerian_cycle())
            continue
        if action=="hamilton":
            generation.find_hamilton_cycle()
            continue
        if action == "export":
            generation.export_to_tikz(os.path.join(CURRENT_DIR, f"tikzpicture.txt"))
            continue
        if action == "exit":
            break
elif args.non_hamilton:
    nodes = int(input("Enter number of nodes: "))
    saturation = 50
    generation = Hamilton(nodes, saturation)
    print("Type Help for list of commands")
    while True:
        action = input('action> ').lower()
        if action == "help":
            print("Help".center(50, "-"))
            print("List of commands:")
            print("Print - print graph")
            print("Exit - exit program")
            print("-".center(50, "-"))
            continue

        if action == "print":
            generation.print_non_hamilton_matrix()
            continue
        if action == "euler":
            print(generation.find_eulerian_cycle())
            continue
        if action=="hamilton":
            generation.find_hamilton_cycle()
            continue
        if action == "export":
            generation.export_to_tikz(os.path.join(CURRENT_DIR, f"tikzpicture.txt"))
            continue

        if action == "exit":
            break


