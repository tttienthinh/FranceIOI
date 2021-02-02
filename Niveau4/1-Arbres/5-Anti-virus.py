from queue import Queue
nbContainers = int(input())
fils = [[] for _ in range(nbContainers + 1)]
for carton,container in enumerate(input().split(),1):
  fils[ int(container) ].append(carton)
masque = input()

def compatible(carton,masque):
  carton = str(carton)
  if len(masque) != len(carton):
     return False
  for chiffreC,chiffreM in zip(carton,masque):
     if chiffreC != chiffreM and chiffreM != "?":
        return False
  return True

enAttente = Queue(nbContainers)
for carton in fils[0]:
  enAttente.put(carton)

while not enAttente.empty():
  container = enAttente.get()
  for carton in fils[ container ]:
     enAttente.put(carton)
  if compatible(container,masque):
     print(container,end=" ")

while not enAttente.empty():
    print(enAttente.get())