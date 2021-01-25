# coding:utf-8
from typing import List, Dict
import json


class NodeParams:
    predator = None
    deep = None
    size = None
    mass = None
    year = None
    area = None

    def __init__(self,
                 predator: bool,
                 deep: List[float],
                 size: List[float],
                 mass: List[float],
                 year: int,
                 area: List[str]):
        self.deep = deep
        self.size = size
        self.mass = mass
        self.predator = predator
        self.year = year
        self.area = area

    def print_params(self, offset=""):
        print(offset + "|--------------------")
        print(offset + "|Хищник: " + str(self.predator))
        print(offset + "|Глубина: " + str(self.deep))
        print(offset + "|Размер: " + str(self.size))
        print(offset + "|Масса: " + str(self.mass))
        print(offset + "|Год открытия: " + str(self.year))
        print(offset + "|Ареал обитания: " + str(self.area))
        print(offset + "|--------------------")


class Node:
    name = None
    parant = None
    child = None
    params = None

    def __init__(self, json: Dict, parent=None):
       # print(json)

        if "name" in json:
            self.name = json["name"]
        else:
            raise ValueError("No name field in json-object")

        self.parent = parent

        if "child" in json and "params" not in json:
            self.child = []
            for obj in json["child"]:
                self.child.append(Node(obj, self))

        elif "params" in json and "child" not in json:
            self.params = NodeParams(json["params"]["predator"],
                                     json["params"]["deep"],
                                     json["params"]["size"],
                                     json["params"]["mass"],
                                     json["params"]["year"],
                                     json["params"]["area"])
        else:
            raise ValueError()

    def print_tree(self, offset=""):
        print(offset+self.name)
        if self.child != None:
            for i in self.child:
                i.print_tree(offset+"    ")

    def print_tree_params(self, offset=""):
        print(offset+self.name)
        if self.child != None:
            for i in self.child:
                i.print_tree_params(offset+"    ")
        if self.params != None:
            self.params.print_params(offset+" ")
            
    def find_node(self, name):
        if self.name == name:
            return self
        
        if self.child == None:
            return False
        
        for i in self.child:
            res = i.find_node(name)
            if res != False:
                return res
            
        return False


class Tree:
    root: Node

    def __init__(self, json: Dict):
        if "root" in json:
            self.root = Node(json["root"])
        else:
            raise ValueError("No root in json-object")

    def print_tree(self, offset=""):
        print(offset+self.root.name)
        for i in self.root.child:
            i.print_tree(offset+"    ")

    def print_tree_params(self, offset=""):
        print(offset+self.root.name)
        for i in self.root.child:
            i.print_tree_params(offset+"    ")
            
    def find_node(self, name):
        return(self.root.find_node(name))


def main():
    json_file = open("D:\\Nik\\Desktop\\sii\\2\\tree.json",
                     "r", encoding="utf-8")
    tree = Tree(json.load(json_file))
    
    res = tree.find_node("")
    if res != False:
        res.print_tree_params()
    else: print("Не найдено")


if __name__ == "__main__":
    main()
