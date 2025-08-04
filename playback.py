quote = input("Tell me what you want to say, but slower.")
option = input("Option 1 or 2?")


#Option 1
if option == "1" or option == "One":
    new_quote = quote.replace(" ", "...")
    print(new_quote)


#Option 2
elif option == "2" or option == "Two":
    words = quote.split()
    print(*words, sep="...")