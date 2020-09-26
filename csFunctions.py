# we also have the len and str functions which operate just like python's

def instring(searchString, substring):
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

availableAnimationFunctions = {
  'instring': instring,
  'left': left,
  'right': right,
  'mid': mid,
  'iif': iif,
  'lookup': lookup,

  # these two dont need to be listed I think
  'len': len,
  'str': str,
}

def evalAnimation(animationString, params={}, points={}):
  for p in params:
    animationString = animationString.replace('\"Parameter:'+p+'\"', params[p])
    print(animationString)

  for p in points:
    animationString = animationString.replace('\"'+p+'\"', points[p])
    print(animationString)

  animationString = animationString.lower()
  animationString = animationString.replace('=', '==')

  return(eval(animationString, availableAnimationFunctions))

if __name__ == "__main__":
  # example regex
  # (a|b)c
  # example animation
  print(instring(x, 'ac') + instring(x,'bc') > 0)
  # but what if we wanted to return group 1 from the above?
  # then we'd need something like
  print(iif(instring(x, 'ac')>0, 'a', iif(instring(x, 'bc')>0, 'b', '')))

  # use eval to actually evaluate animations
  print(eval("left('abc',2) + str(len('abc'))", availableAnimationFunctions))

  print(evalAnimation(
    "IIF( ( \"Parameter:AlarmCount\" = '' ), 14935011, IIF( \"Parameter:AlarmCount\" * 1 < \"..Target Alarms Per Hour\", 14935011, 7430868 ) )",
    params={'AlarmCount':'50'},
    points={'..Target Alarms Per Hour':'8'}
    ))