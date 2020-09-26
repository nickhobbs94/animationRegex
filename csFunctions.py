# we also have the len and str functions which operate just like python's

def inString(searchString, substring):
  return searchString.find(substring) + 1

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
  print(inString(x, 'it was the best of times it was the blurst of times') == 0)
  print(iif(mid(x,2,3) == "bcd", left(x,1),right(x,1)) + '...')
  print(lookup(1, 'x', 'y', 'z'))

  # example regex
  # (a|b)c
  # example animation
  print(inString(x, 'ac') + inString(x,'bc') > 0)
  # but what if we wanted to return group 1 from the above?
  # then we'd need something like
  print(iif(inString(x, 'ac')>0, 'a', iif(inString(x, 'bc')>0, 'b', '')))