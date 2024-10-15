from hashlib import sha256



class Hash:
    def __init__(self, message):
        self.message = message
    def rotate(self, input):
        return [(b << 4 | b >> 3) & 0xff for b in input]
    
    def encrypt(self):
        return sha256(self.rotate(self.message))
    


def main():
    txt = b'ready_player_one!'
    encoded_txt = Hash(txt).encrypt()
    while True:
        i = input(f'Input the sha that matches {encoded_txt}')
        hex = bytes.fromhex(i)
        if (Hash(hex).encrypt() == encoded_txt and i != txt):
            print('Success!')
            return
        else:
            print('Didnt work!')