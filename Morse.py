Letter = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--..",".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--..","/",".-.-.-", "--..--", "..--..", ".----.", "-.-.--", "-..-.", "-.--.", "-.--.-", ".-...", "---...", "-.-.-.", "-...-", ".-.-.", "-....-", "..--.-", ".-..-.", "...-..-", ".--.-."]
ABC = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ .,?'!()&:;=+-_\"$@"

def Encode_Text(Text):
    Morse = ""
    for Y in range(len(Text)):#go trough the text one letter at a time

        for X in range(len(ABC)):#Search for character in the Abc
            if Text[Y] == ABC[X]:
                Morse += Letter[X]+" "
                break

    return Morse


def Decode_Morse(Morse):
    Text = ""
    
    Characters = 0
    Character_Counter = -1

    for X in range(len(Morse)):#finds out how many characters are there
        if Morse[X] == " ":
            Characters += 1

    for X in range (Characters):#go trough all characters
        Current_Letter = ""
        
        for X in range (100):#decode individual letters
            Character_Counter += 1
                
            if Morse[Character_Counter] == " ":
                break
            else:    
                Current_Letter +=Morse[Character_Counter]

        for Y in range(len(ABC)):#find matching morse letter
            if Current_Letter == Letter[Y]:
                Text += ABC[Y]
                break
    
    return Text

#Examples

print(Encode_Text("YourText"))
