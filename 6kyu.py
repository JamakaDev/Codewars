from string import ascii_letters as letters


def main() -> None:

  def find_missing_letter(chars):
    for i, char in enumerate(chars):
      if i and ord(char) - ord(chars[i-1]) != 1:
          return chr(ord(char)-1)
      

  def dot(n,m):    
    # return ("+---" * n + "+\n" + "| o " * n + "|\n") * m + ("+---" * n + "+")
    res = ''
    x = 0
    while x < m:
      if x == 0:
        for i in range(3):
          if i % 2: res += f"\n|{' o |' * n}\n"
          else: res += f"+{'---+' * n}"
      else:
        for i in range(2):
          if not i % 2: res += f"\n|{' o |' * n}\n"
          else: res += f"+{'---+' * n}"
      x += 1
    return res


  def sum_dig_pow(a, b):
    res = []
    for i in range(a, b+1):
        temp = 0
        for j, char in enumerate(str(i)): temp += int(char)**(j+1)
        if temp == i: res.append(i)
    return res

      
  print(sum_dig_pow(1, 100))
  # print(dot(15,7))
  # print(find_missing_letter(["a","b","c","d","f"]))



if __name__ == '__main__':
  main()
