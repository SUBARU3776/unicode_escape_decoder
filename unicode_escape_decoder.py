import codecs

def decode_unicode_escape(text):
    return codecs.decode(text, 'unicode_escape')

encoded_text = r""

decoded_text = decode_unicode_escape(encoded_text)
print(decoded_text)
