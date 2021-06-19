from cryptography.fernet import Fernet


def generate_encription():
    key = Fernet.generate_key()
    return key.decode()


def basic_sum(a, b):
    return a + b


def basic_subs(a, b):
    return a - b


def basic_mult(a, b):
    return a * b


if __name__ == '__main__':
    
    test = generate_encription()
    print(test)

    print(basic_sum(1, 2))
    print(basic_subs(10, 5))
    print(basic_mult(3, 10))