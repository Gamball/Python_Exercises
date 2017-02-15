class Car:
    def __init__(self, **kwargs):
        self.data = kwargs

    def get(self):
        print('owner name:', self.data['owner'])
        print('car name:', self.data['model'])


def main():
    omar = Car(owner='omar mohammad', model='Kia')
    omar.get()

    jana = Car(owner='khalid mohammad', model='BMW')
    jana.get()


if __name__ == '__main__': main()
