class Guitar:
    def play(self):
        return "Playing the guitar"


def start_playing(thing):
    return thing.play()


guitar = Guitar()
print(start_playing(guitar))