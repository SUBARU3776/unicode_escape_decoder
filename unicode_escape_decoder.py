import codecs

def decode_unicode_escape(text):
    return codecs.decode(text, 'unicode_escape')

encoded_text = r"\u5b66\u7fd2\u9662\u5927 \u30c9\u30a4\u30c4\u30af\u30e9\u30d6\u306b\u3088\u308b\u672a\u6210\u5e74\u8005\u98f2\u9152\u7981\u6b62\u6cd5\u9055\u53cd\u4e8b\u6848\u306b\u3064\u3044\u3066\n#\u6625\u304b\u3089\u5b66\u7fd2\u9662 #\u5b66\u7fd2\u9662\u5927\u5b66 #\u30c9\u30a4\u30c4\u30af\u30e9\u30d6"

decoded_text = decode_unicode_escape(encoded_text)
print(decoded_text)