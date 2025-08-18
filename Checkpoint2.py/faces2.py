def main():
    emoji = input("Wite a message with an emoticon: ")
    convert(emoji)

def convert(message):
    message = message.replace(":)","😀").replace(":(","🙁")
    print(message)


main()
