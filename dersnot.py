def functioner(emoji = None):
    return lambda message: print(message, emoji)
(lambda message: print(message, ":)"))(66)
(lambda message: print(message, ":)"))([66])
print_smile = functioner(":)")
print_sad = functioner(":(")
print_neutral = functioner(":|")
print(print_smile("Hello"))
print(print_sad("bugünkü dersteki yüz ifadem -->"))
print(print_neutral("Hello"))  

