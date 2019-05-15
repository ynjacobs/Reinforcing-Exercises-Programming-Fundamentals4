my_list = ['Danny', 'Max', 'Dave']

print('please enter your name')
your_name = input()

if your_name in my_list:
    print('Hello {}'.format(your_name))
else:
    print('Who goes there?')