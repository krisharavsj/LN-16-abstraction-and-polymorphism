class flash_cards:
    def __init__(self,word,meaning):
        self.word=word
        self.meaning=meaning
    def __str__(self):
        return self.word+'('+self.meaning+')'
flash=[]
print("welcome to flash card application")
while True:
    word=input("enter the name you want to add to the flash card")
    meaning=input("enter the meaning of the word you gave:")
    flash.append(flash_cards(word,meaning))
    option=int(input("enter 0 if you want to add another flash card otherwise enter 1"))
    if option==1:
        break
print("\n your flash cards")
for i in flash:
    print (">",i)