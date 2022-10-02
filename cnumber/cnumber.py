"""
I provide hier a class, which allow us to do several operation with Complex number
"""
import math
from .exception import DisisionByNullException


class ComplexNumber:
    """
    A Class used to represent a COmplex Number

    Attributes
    ----------
    re: float
        this represent the real part of the Complex Number.
    im : float
        it represent the imajinary part of the Complex number.

    Methods
    -------
    getImaginary():
        to access to the imaginary part of your complex number.
    getReal():
        to access to the real part of your complex number.
    conjugate():
        returns a new complex number which is the conjugate of the one the method wascalled on.
    add(other):
        returns a new complex number which is the sum of the complex number the
                method was called on and other
    subtract(other):
        returns a new complex number which is the result of subtractingother
                from the complex number the method was called on.
    multiply(other):
        returns a new complex number which is the product of the complex number the method
                was called on and other.
    divide(other):
        returns null if the real and imaginary parts of other are 0. Otherwise, it returns a
                new complex number which is the result of dividing the current complex
                number by other.
    abs():
        returns a double that is the absolute value of the complex number. (Note: The Math class
                provides a method to calculate square roots.)
    toString():
        method that returns a sensible string representation of the complex number. A complex
               number with real part 42 and imaginary part 23 could for instance be written as
               42.0 + 23.0i.
    """

    def __init__(self, real=0.0, imaginary=0.0):
        """
        initialisation of a Complex Number with 2 numbers

        """
        self.real = real
        self.imaginary = imaginary

    def __str__(self):
        return f"{self.real:.2f} + {self.imaginary:.2f}i"

    def __bool__(self):
        """
        Method for checking the existance of our complex Number.
        Return
        ------
        The Method return False when the both real and Imaginary part are egal to 0.0 and
        return True otherswise.
        """
        if self.imaginary == 0.0 and self.real == 0.0:
            return False

        return True

    def __eq__(self, other):
        if(self.real == other.real and self.imaginary == other.imaginary):
            return True

        return False

    def __add__(self, other):
        """
        this is the Method for the Classic addition von 2 Complex Number using the Signe +
        Return
        ------
        it return a Complex Number wich is the Somme of the two number.
        """
        return self.add(other)

    def __sub__(self, other):
        """
        this is the Method for the Classic Substraction for 2 Complex Number using the Signe +
        Return
        ------
        it return a Complex Number wich is the different of the two number.
        """
        return self.sub(other)

    def __mul__(self, other):
        """
        this is the Method for the Classic Multiplication for 2 Complex Number using the Signe *
        Return
        ------
        it return a Complex Number wich is the Product of the two number.
        """
        return self.multiply(other)

    def __abs__(self):
        """
        this is the Method for the Classic Abs for a Complex Number using abs function
        Return
        ------
        it return a float Number wich is the abs of the number.
        """
        return self.abs()

    # def __enter__(self):
    #     pass

    # def __exit__(self):
    #     pass

    def get_real(self):
        """This Method just return the real part of the Complex Number."""
        return self.real

    def set_real(self, real):
        """
        This is the sette for the real par
        """
        self.real = real

    def get_imaginary(self):
        """This Method just return the imaginary part of the Complex Number."""
        return self.imaginary

    def set_maginary(self, imaginary):
        """This the setter for the imaginary part"""
        self.imaginary = imaginary

    def conjugate(self):
        """
        This Method conjugate our Complex Number, that mean it change the imaginary part
        whith his opposite.
        """
        self.imaginary *= -1

    def add(self, other):
        """
        This Medthod add another Complex Number to our Complex Number by addind their real parts
        together and their imaginary parts together
        """
        new = ComplexNumber(self.get_real(), self.get_imaginary())
        new.real += other.get_real()
        new.imaginary += other.get_imaginary()
        return new

    def adds(self, c_list):
        """
        This Method shoul add a liste of Complex Numbers.

        Returns
            (ComplexNumber): it return a Complex Number which is the sum of all Complex
                             Number in the list
        """
        first = c_list[0]
        for i in range(1, len(c_list)):
            first.add(c_list[i])
        return first

    def sub(self, other):
        """
        This Medthod substract to our Complex Number another Complex Number
        to our Complex Number by subtracting their real parts together and their
        imaginary parts together
        """
        new = ComplexNumber(self.get_real(), self.get_imaginary())
        new.real -= other.get_real()
        new.imaginary -= other.get_imaginary()
        return new

    def multiply(self, other):
        """This Method multiply our Complex Number with another Complex Number"""
        new = ComplexNumber(self.get_real(), self.get_imaginary())
        real = (new.real * other.get_real()) - (new.imaginary * other.get_imaginary())
        imaginary = (new.imaginary * other.get_real()) + (new.real * other.get_imaginary())
        new.set_real(real)
        new.set_maginary(imaginary)
        return new

    def multiplys(self, c_list):
        """
            This Method shoul multiply a list of Complex Numbers
        Returns:
            (ComplexNumber): it return a Complex Number which is the multiplication of all Complex
                             Number in the list
        """
        first = c_list[0]
        for i in range(1, len(c_list)):
            first.multiply(c_list[i])
        return first

    def divide(self, other):
        """
        This Method divide our Complex Number with another Complex Number.
        The Procces are explained hier (https://de.wikipedia.org/wiki/Komplexe_Zahl#Division)
        """
        new = ComplexNumber(self.get_real(), self.get_imaginary())
        if other.get_real() == 0.0 and other.get_imaginary() == 0.0:
            raise DisisionByNullException("Devision by null Error!")

        other_bar_re = other.get_real() / ((other.get_real() **2) +
                       (other.get_imaginary() **2))
        other_bar_im = (-1 * other.get_imaginary()) / ((other.get_real() ** 2) +
                       (other.get_imaginary() ** 2))
        tmp = ComplexNumber(other_bar_re, other_bar_im)
        new.multiply(tmp)
        return new

    def abs(self):
        """
        This Method return a float Number which is the absulute Value of our Complex Number
        """
        return math.sqrt(self.get_real() **2 + self.get_imaginary() **2)

    def to_string(self):
        """For the case this Method just Print our Complex Number."""
        print(self)
