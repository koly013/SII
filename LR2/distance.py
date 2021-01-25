# coding:utf-8
from typing import List, Dict
from enum import Enum

from tree import *

class DistanceType(Enum):
    EUCLIDEAN = 1
    MANHATTAN = 2
    
def distance(tree: Tree, name_a, name_b, type):
    node_a = tree.find_node(name_a)
    node_b = tree.find_node(name_b)
    
    if (node_a and node_b) and (node_a.child == None) and (node_b.child == None):
        if type == DistanceType.EUCLIDEAN:
            return euclidean_distance(node_a, node_b)
        if type == DistanceType.MANHATTAN:
            return manhattan_distance(node_a, node_b)

def euclidean_distance(node_a: Node, node_b: Node):
    p1 = pow( (node_a.params.deep[0] + node_a.params.deep[1]) / 2 - (node_b.params.deep[0] + node_b.params.deep[1]) / 2, 2)
    p2 = pow( (node_a.params.mass[0] + node_a.params.mass[1]) / 2 - (node_b.params.mass[0] + node_b.params.mass[1]) / 2, 2)
    p3 = pow( (node_a.params.size[0] + node_a.params.size[1]) / 2 - (node_b.params.size[0] + node_b.params.size[1]) / 2, 2)
    p4 = pow(node_a.params.year - node_b.params.year, 2)
    print(p1, p2, p3, p4)         
    return (p1 + p2 + p3 + p4)
    
def manhattan_distance(node_a: Node, node_b: Node):
    p1 = abs( (node_a.params.deep[0] + node_a.params.deep[1]) / 2 - (node_b.params.deep[0] + node_b.params.deep[1]) / 2)
    p2 = abs( (node_a.params.mass[0] + node_a.params.mass[1]) / 2 - (node_b.params.mass[0] + node_b.params.mass[1]) / 2)
    p3 = abs( (node_a.params.size[0] + node_a.params.size[1]) / 2 - (node_b.params.size[0] + node_b.params.size[1]) / 2)
    p4 = abs(node_a.params.year - node_b.params.year)
    print(p1, p2, p3, p4)         
    return (p1 + p2 + p3 + p4)

def main():
    json_file = open("D:\\Nik\\Desktop\\sii\\2\\tree.json",
                     "r", encoding="utf-8")
    tree = Tree(json.load(json_file))
    
    tree.find_node("Ламантиновые").print_tree_params()
    
    print(distance(tree, "Африканский ламантин", "Амазонский ламантин", DistanceType.MANHATTAN))


if __name__ == "__main__":
    main()