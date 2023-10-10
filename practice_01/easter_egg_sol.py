def decode(encoded_string, alphabet, rot):
    """
    Decode a string using the Caesar cipher method.
    This function takes a string, an alphabet, and a rotation value (rot) as input
    and decodes the string using the Caesar cipher method. It shifts each character in the
    encoded string by the specified rotation value within the provided alphabet.
    :param encoded_string: (str): The encoded string to be decoded.
    :param alphabet: (str): The alphabet used for encoding and decoding.
    :param rot: (int): The rotation value indicating how much to shift characters during decoding.
    :return: (str): The decoded string.
    """
    decode_string = []
    for char in encoded_string:
        if char in alphabet:
            rot_idx = (alphabet.index(char) + rot) % 26
            decode_string.append(alphabet[rot_idx])
        else:
            decode_string.append(char)
    return ''.join(decode_string)


if __name__ == '__main__':
    # In this exercise we will try to decode Caesar cipher
    # https://en.wikipedia.org/wiki/Caesar_cipher

    s = """Gur Mra bs Clguba, ol Gvz Crgref
    
    Ornhgvshy vf orggre guna htyl.
    Rkcyvpvg vf orggre guna vzcyvpvg.
    Fvzcyr vf orggre guna pbzcyrk.
    Pbzcyrk vf orggre guna pbzcyvpngrq.
    Syng vf orggre guna arfgrq.
    Fcnefr vf orggre guna qrafr.
    Ernqnovyvgl pbhagf.
    Fcrpvny pnfrf nera'g fcrpvny rabhtu gb oernx gur ehyrf.
    Nygubhtu cenpgvpnyvgl orngf chevgl.
    Reebef fubhyq arire cnff fvyragyl.
    Hayrff rkcyvpvgyl fvyraprq.
    Va gur snpr bs nzovthvgl, ershfr gur grzcgngvba gb thrff.
    Gurer fubhyq or bar-- naq cersrenoyl bayl bar --boivbhf jnl gb qb vg.
    Nygubhtu gung jnl znl abg or boivbhf ng svefg hayrff lbh'er Qhgpu.
    Abj vf orggre guna arire.
    Nygubhtu arire vf bsgra orggre guna *evtug* abj.
    Vs gur vzcyrzragngvba vf uneq gb rkcynva, vg'f n onq vqrn.
    Vs gur vzcyrzragngvba vf rnfl gb rkcynva, vg znl or n tbbq vqrn.
    Anzrfcnprf ner bar ubaxvat terng vqrn -- yrg'f qb zber bs gubfr!"""

    s = s.lower()
    alphabet_lower = 'abcdefghijklmnopqrstuvwxyz'

    # 1. First, let's try to search for the correct rotation, using the first line of the text
    first_line = 'Gur Mra bs Clguba, ol Gvz Crgref'.lower()

    # You may write a function that take the encoded text, the alphabet collection, and the rotation number
    for rot in range(1, 26):
        result = decode(encoded_string=first_line, alphabet=alphabet_lower, rot=rot)
        print(rot, result)
    # You will see that the correct rotation number is 13

    # 2. Then use the correct rotation to decode the whole text. You will see it is an easter egg in python!
    decode_text = decode(encoded_string=s, alphabet=alphabet_lower, rot=13)
    print(decode_text)
