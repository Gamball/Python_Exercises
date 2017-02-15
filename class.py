class Friends:
    def __init__(self, **kwargs):
        self.data = kwargs

    def Get(self):
        print(self.data['name'])
        print(self.data['age'])
        print(self.data['jop'])


def main():

    Friend1 = Friends(name=input('Name:'), age=input('Age:'), jop=input('Jop:'))
    Friend1.Get()

    Friend2 = Friends(name=input('Name:'), age=input('Age:'), jop=input('Jop:'))
    Friend2.Get()

if __name__ == '__main__': main()
