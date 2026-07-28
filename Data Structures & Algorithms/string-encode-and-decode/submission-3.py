class Solution:

    def encode(self, strs: List[str]) -> str:
        seperator = "#"
        # encoded_string = length.join(word) 
        encoded_string = ""
        for word in strs:
            print(word)
            length = str(len(word))+seperator
            encoded_string += length+word

        print(encoded_string)
        return encoded_string

    def decode(self, s: str) -> List[str]:
        decoded_string = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1

            length = int(s[i:j])
            i = j + 1  # skip '#'
            decoded_string.append(s[i:i + length])
            i += length
        return decoded_string