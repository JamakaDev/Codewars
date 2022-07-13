from string import ascii_letters as letters


def main() -> None:

  def find_missing_letter(chars):
    for i, char in enumerate(chars):
      if i and ord(char) - ord(chars[i-1]) != 1:
          return chr(ord(char)-1)
      

      



      


  print(find_missing_letter(["a","b","c","d","f"]))



if __name__ == '__main__':
  main()
