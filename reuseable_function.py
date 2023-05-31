#emojis using function

def emojis_convert(message):
    words = message.split(' ')
    emojis={
    ":)":"😀",
    ":(":"😔"
    }
    output=""
    for word in words:
        output += emojis.get(word,word) +" "
    return output


message= input(">")
result=emojis_convert(message)
print(result)


