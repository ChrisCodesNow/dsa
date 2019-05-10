def foo(words):
    words = 
    print(f'words inside foo function = {words}')


if __name__ == '__main__':
    words = 'this is a sentence'.split()
    print(f'In main: words before function call = {words}')
    foo(words)
