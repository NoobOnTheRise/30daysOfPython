"""
Write a python program to translate a message into secret code language. Use the rules below to translate normal English into secret code language
Coding:
if the word contains atleast 3 characters, remove the first letter and append it at the end now append three random characters at the starting and the end else: simply reverse the string

Decoding:
if the word contains less than 3 characters, reverse it else: remove 3 random characters from start and end. Now remove the last letter and append it to the beginning

Your program should ask whether you want to code or decode
"""
import random
import string

str = input("Enter a message: ")

def encode(input):
  try:
    if len(input) > 3:
      input = input[1:] + input[0] + ''.join(
          random.choice(string.ascii_lowercase) for i in range(3))
    else:
      input = input[::-1]
  except Exception as e:
    print(e)
  return input

def decode(input):
  try:
    input = input[-4] + input[:-4] if len(input) > 3 else input[::-1]
  except Exception as e:
    print(e)
  return input

if str:
  str = ''.join(str.split(" "))
  coding = input("1 for Coding or 0 for Decoding: ")
  coding = True if (coding=="1") else False

  if coding == 1: 
    encodedMessage = encode(str)
    print("Encoded message: ", encodedMessage)
  else: 
    decodedMessage = decode(str)
    print("Decoded message: ", decodedMessage)