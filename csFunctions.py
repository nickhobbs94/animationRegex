def inString(searchString, substring):
  try:
    return searchString.find(substring) + 1
  except:
    return 0

def left(s, length):
  return s[:length]

def right(s, length):
  return s[-length:]

def mid(s, start, length):
  return s[start-1:start+length-1]

def iif(expr, branchTrue, branchFalse):
  if expr == True:
    return branchTrue
  else:
    return branchFalse

def lookup(n, *arg):
  return(arg[n-1])

if __name__ == "__main__":
  x="abcdef"
  print(left(x,2) == "ab")
  print(right(x,3) == "def")
  print(mid(x,2,3) == "bcd")
  print(inString(x,"b") == 2)
  print(iif(mid(x,2,3) == "bcd", left(x,1),right(x,1)) + '...')
  print(lookup(1, 'x', 'y', 'z'))