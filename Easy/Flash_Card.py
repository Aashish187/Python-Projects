# EASY AND FUN TO PLAY FLASHCARD GAME
class FlashCard:
    def __init__(self,word,meaning):
        self.word=word
        self.meaning=meaning
    def __str__(self):
        # return a string
        return f"{self.word} : {self.meaning}"
flash=[]
print("Welcome To The FlashCard Application!")
print("Enter 0 to stop entering the flashcards")
print("Enter 1 to add another FlashCard")
while(True):
    stop=int(input("Enter Your choice: "))
    if(stop==0):
        break
    elif(stop==1):
        word=input("Please Enter the Word: ")
        meaning=input("Please Enter the Meaning: ")
        flash.append(FlashCard(word,meaning))

    else:
        print("Choose a Valid Option!")
print("\nFlashCards")
for i in flash:
    print("> ",i)
    
    
