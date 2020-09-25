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

if __name__ == "__main__":
  x="abcdef"
  print(left(x,2) == "ab")
  print(right(x,3) == "def")
  print(mid(x,2,3) == "bcd")
  print(inString(x,"b") == 2)