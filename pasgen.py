#========================
#                       |
# pasgen v1.0           |
# Made by dserlf        |
#                       |
#========================


import  string, sys, random


class passGenerator():
    def __init__(self):
        self.list_nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
        self.list_az = []
        self.list_AZ = []
        self.list_procent = ['%', '*', ')','?', '@', '#', '$', '~']
        self.list_init = []
        self.password = ''
        self.line = '======================================================'

    def print_hello(self):
        print('Добро пожаловать в pasgen 1.0!\n'
              '[?] Как использовать: pasgen.py [аргументы]\n'
              '[?] Список аргументов: \n'
              '    - AZ: латиница верхнего регистра в пароле\n'
              '    - az: латиница нижнего регистра в пароле\n'
              '    - 09: цифры\n'
              '    -  %: использовать спецсимволы в пароле\n'
              '[?] Пример использования: pasgen.py az AZ 09\n')

    def generate_the_lists(self):
        a = string.ascii_lowercase
        for i in a:
            self.list_az.append(i)

        a = string.ascii_uppercase
        for i in a:
            self.list_AZ.append(i)

    def init_the_symbols(self):
        if 'az' in sys.argv[1:]:
            self.list_init += self.list_az
        if 'AZ' in sys.argv[1:]:
            self.list_init += self.list_AZ
        if '09' in sys.argv[1:]:
            self.list_init += self.list_nums
        if '%' in sys.argv[1:]:
            self.list_init += self.list_procent

    def generate_the_pass(self):
        self.max = int(input('Сколько символов должно быть в пароле: '))
        for i in range(1, self.max + 1):
            self.rand = random.randint(1, len(self.list_init) - 1)
            self.password += str(self.list_init[self.rand])
        print(self.line)
        print('Результат: ' + self.password)
        print(self.line)






try:
    run = passGenerator()
    run.print_hello()
    if len(sys.argv) < 2:
        sys.exit()
    run.generate_the_lists()
    run.init_the_symbols()
    run.generate_the_pass()
except:
    print('Что-то пошло не так, как планировалось.')
    sys.exit()
