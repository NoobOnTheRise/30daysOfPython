"""
    Create a program capbale of displaying questions to the user like who wants to be a millionaire. 
    Use List data type to store the questions and their correct answers. Display the final amount the person
    """ 

listOfQuestions = []
class questions :
      def __init__(self,question,answer, answers, level, amount):
          self.question=question
          self.answer=answer
          self.answers=answers
          self.level=level
          self.amount=amount

totalPrizeAmt = 0
listOfQuestions.append(questions(
      "Who wrote the novel '1984'?",
      "George Orwell",
      ("George Orwell","J.K. Rowling","F. Scott Fitzgerald","Ernest Hemingway"), 1, 1000))
listOfQuestions.append(questions(
      "What is the capital city of Australia?",
      "Canberra",
      ("Sydney", "Melbourne", "Canberra" , "Brisbane")
       ,2,2000))
listOfQuestions.append(questions(
      "What is the chemical symbol for Gold?",
      "Au",
      ("Gd","Go","Ag","Au"), 3, 3000))
listOfQuestions.append(questions(
      "In what year was the first iPhone released?",
      "2007",
      ("2007","2008","2009","2010"), 4, 4000))
listOfQuestions.append(questions(
      "What is the tallest mountain in the world?",
      "Mount Everest",
      ("Mount Everest","K2","Kangchenjunga","Lhotse")
      , 5 , 5000))

for i in range(len(listOfQuestions)):
      print("Level",listOfQuestions[i].level,"for" ,listOfQuestions[i].amount, "USD:",listOfQuestions[i].question)
      for answer in listOfQuestions[i].answers:
        print(answer)
      ans = input("Please select an answer or e to quit: ")
      if (ans == 'e'):
        print("******************************************")
        print("GoodBye!")
        break
      else: 
        if ans == listOfQuestions[i].answer:      
            totalPrizeAmt =totalPrizeAmt + listOfQuestions[i].amount
            print("Correct Answer! You have won ",totalPrizeAmt,"USD")
        else:
          print("Incorrect! Correct answer is: ", listOfQuestions[i].answer)
          print("You take ",totalPrizeAmt,"USD home")
          break

      print("******************************************")
      print("Congratulation! You take ",totalPrizeAmt,"USD home")