def primary():
  # print("Keep it logically awesome.")

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()

  print(quotes[0], end="")
  print(quotes[4])
if __name__== "__main__":
  primary()
