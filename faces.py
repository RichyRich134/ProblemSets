str = input("Welcome to the Emoticon to Emoji converter. Please tell me your message.")

replacement_dictionary = {
":)":"🙂",
":(":"🙁"
}

for key, value in replacement_dictionary.items():
    if key in str:
        str = str.replace(key, value)

print(str)

#def main():
    #message = input("Welcome to the Emoticon to Emoji converter. Please tell me your message.")
    #convert(message)
 
# def convert(message):
    #new_message = message.replace(":)", "🙂").replace(":(", "🙁")
    #print(new_message)
#main()

#1)Replace function
#2)Manually strip when recognized with if. 
#3)

     


    

    