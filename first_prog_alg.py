"""Muilti line documentation string
describing module"""

class HelloWorld(object):
    """ documentaton string of class """

    # Single line comment

    @classmethod

    def main(cls, args):
        """ documentation string of method """
        print("Hello, World")

if __name__ == "__main__":
    import sys
    HelloWorld.main(sys.argv)