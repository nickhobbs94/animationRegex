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
  return s[start-1:start+length]

if __name__ == "__main__":
  x="abcdef"
  print(left(x,2000))
  print(right(x,2000))
  print(mid(x,2,1000))
  print(inString(x,"b"))