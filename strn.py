class OperationsStrn(object):
    """
      here we are creating OperationsStrn class and performing the string methods
    """
    def __init__(self):
        """

        """
        self.my_stri = "i am in bangalore"

    def count(self, a):
        """

        :param a:
        :return:
        """
        print "count of the element is: "
        return self.my_stri.count(a)

    def index(self, a):
        """

        :param a:
        :return:
        """
        return self.my_stri.index(a)

    def split(self):
        """

        :return:
        """
        return self.my_stri.split()

    def capitalize(self):
        """

        :return:
        """
        return self.my_stri.capitalize()

    def endswith(self, a):
        """

        :param a:
        :return:
        """
        return self.my_stri.endswith(a)

    def strtswith(self, a):
        """

        :param a:
        :return:
        """
        return self.my_stri.startswith(a)

    def find(self, a):
        """

        :param a:
        :return:
        """
        return self.my_stri.find(a)

    def center(self, a):
        """

        :param a:
        :return:
        """
        return self.my_stri.center(a)

    def isalnum(self):
        """

        :return:
        """
        return self.my_stri.isalnum()

    def isalpha(self):
        """

        :return:
        """
        return self.my_stri.isalpha()

    def isspace(self):
        """

        :return:
        """
        return self.my_stri.isspace()

    def isdigit(self):
        """

        :return:
        """
        return self.my_stri.isdigit()

    def isupper(self):
        """

        :return:
        """
        return self.my_stri.isupper()

    def islower(self):
        """

        :return:
        """
        return self.my_stri.islower()

    def upper(self):
        """

        :return:
        """
        return self.my_stri.upper()

    def lower(self):
        """

        :return:
        """
        return self.my_stri.lower()

    def istitle(self):
        """

        :return:
        """
        return self.my_stri.istitle()

    def title(self):
        """

        :return:
        """
        return self.my_stri.title()

    def partition(self, a):
        """

        :param a:
        :return:
        """
        return self.my_stri.partition(a)

    def ljust(self, a, b):
        """

        :param a:
        :param b:
        :return:
        """
        a = 100
        b = " "
        return self.my_stri.ljust(a, b)

    def encode(self, a):
        """

        :param a:
        :return:
        """
        return self.my_stri.endswith(a)


x = OperationsStrn()
print x

print x.capitalize()
print x.center(55)
print x.find('b')
print x.count('a')
print x.partition("am")
print x.endswith("a")
print x.istitle()
print x.islower()
print x.isupper()
print x.isdigit()
print x.isalnum()
print x.isalpha()
print x.isspace()
print x.strtswith('i')
print x.title()
print x.split()

