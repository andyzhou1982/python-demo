original_string = "你好\nworld"
decoded_string = bytes(original_string, 'utf-8').decode('unicode_escape')

print(decoded_string)
