import sys
import json


# arquivo_base = sys.argv[1]

def ler_arvore():
   with open("exemplos/imprimir.json","r") as file_json:
      dados_ast = json.load(file_json)
   return dados_ast



arvore = ler_arvore()

def interpretador(node, memoria):

   if "expression" in node:
      return interpretador(node["expression"],memoria)
      
   if node["kind"] == "Print":
         valor = interpretador(node["value"],memoria)
         print(valor)
         return True
   
   if node["kind"] == "Binary":
      n1 = node["lhs"]["value"]
      n2 = node["rhs"]["value"]
      match node["op"]:
         case "Add":           
            if isinstance(n1,(int,float)) and isinstance(n2,(int,float)):
               print(n1 + n2)
            print(f'"{str(n1)}'+f'{str(n2)}"')
      
      return True
   
   
   
   #  TIPOS DA LINGUAGEM
   if node["kind"] == "Str":
      return str(node["value"])
   
   if node["kind"] == "Int":
      return int(node["value"])

   
   
   raise Exception("")
   
   
   
if __name__ == "__main__":
   env= {}
   interpretador(arvore,env)