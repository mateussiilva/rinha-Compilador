import sys
import json


arquivo_base = sys.argv[1]

with open(arquivo_base,"r") as file_json:
   dados_ast = json.load(file_json)


node = dados_ast["expression"]


memoria = {}


def intepretador(file):
   match file["kind"]:
      case "Print":
         valor = file.get("value").get("kind")
         if valor == "Binary":
            operacao = file["value"]["op"]
            match operacao:
               case "Add":
                  r = file["value"]["rhs"]["value"] 
                  l = file["value"]["lhs"]["value"]
                  if isinstance(r,(float,int)) and  isinstance(l,(float,int)):
                     print(r + l)
                  print(f"'{str(r) + str(l)}'")
               case "Sub":
                  r = file["value"]["rhs"]["value"]
                  l = file["value"]["lhs"]["value"]
                  print(l - r)  

               case _:
                  print("Opeaçaõ invalidade")
         else:
            print(file["value"]["value"])
      case "Let":
         print("Definir uma variavel")
         var = file["name"]["text"]
         memoria[var] = var
         ...
   # print(file)



intepretador(node)
print(memoria)