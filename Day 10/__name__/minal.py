def welcome():
  print("Hey you are welcome from minal.py")


# __name__ -  determine whether the script is being run directly or being imported as a module into another script.
if __name__ == "__main__":
  welcome()

# useful because it allows you to reuse code from a script by importing it as a module into another script, without running the code in the original script
