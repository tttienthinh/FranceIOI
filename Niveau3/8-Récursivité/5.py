from sys import stdin
def printer(start, end):
   print(start, end=" ")
   if start == end:
      return
   else:
      printer(start+1, end)

def main():
   start, end = stdin.readline().split()
   start, end = int(start), int(end)
   printer(start,end)
main()