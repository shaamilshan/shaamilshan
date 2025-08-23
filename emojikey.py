def emojiReplacer(sentence):
    emoji = {"happy" : "😀", "sad" : "🥺","angry" : "😤", "dead" : "💀", "love" : "❤️", "cool" : "😎", "raining" : "⛈️",}
    
    for key,value in emoji.items():
        sentence = sentence.replace(key,value)
    return sentence

input_message = input("Enter your message : ")
input_message = input_message.lower()
output_message = emojiReplacer(input_message)
print(output_message)