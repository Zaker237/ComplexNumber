import math
import argparse

"""
I provide hier a class, which allow us to do several operation with Complex number
"""


class ComplexNumber(object):
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
        returns a new complex number which is the sum of the complex number the method was called on and other
    subtract(other):
        returns a new complex number which is the result of subtractingother from the complex number the method was called on.
    multiply(other):
        returns a new complex number which is the product of the complex number the method was called on and other.
    divide(other):
        returns null if the real and imaginary parts of other are 0. Otherwise, it returns a new complex number which is the result of dividing the current complex number by other.  
    abs():
        returns a double that is the absolute value of the complex number. (Note: The Math class provides a method to calculate square roots.)
    toString():
        method that returns a sensible string representation of the complex number. A complex  number with real part 42 and imaginary part 23 could for instance be written as 42.0 + 23.0i.
    """

    def __init__(self, real = 0.0, imaginary = 0.0):
        """
        initialisation of a Complex Number with 2 numbers

        """
        self.re = real
        self.im = imaginary
    
    def __str__(self):
        return f"{self.re:.2f} + {self.im:.2f}i"
    
    def __bool__(self):
        """
        Method for checking the existance of our complex Number.
        Return
        ------
        The Method return False when the both real and Imaginary part are egal to 0.0 and return True otherswise.
        """
        if self.im == 0.0 and self.im == 0.0:
            return False
        else:
            return True

        def __add__(self, other):
            """
            this is the Method for the Classic addition von 2 COmplex Number using the Signe +
            Return
            ------
            it return a Complex Number wich ist the Somme of the tu number.
            """
            return self.add(other)
    
    def getReal(self):
        """
        This Method just return the real part of the Complex Number.
        """
        return self.re

    def setReal(self, real):
        """
        This is the sette for the real par
        """
        self.re = real

    def getImaginary(self):
        """
        This Method just return the imaginary part of the Complex Number.
        """
        return self.im
    
    def setImaginary(self, imaginary):
        """
        this the setter for the imaginary part
        """
        self.im = imaginary

    def conjugate(self):
        """
        This Method conjugate our Complex Number, that mean it change the imaginary part whith his opposite.
        """
        self.im *= -1

    def add(self, other):
        """
        This Medthod add another Complex Number to our Complex Number by addind their real parts together and their imaginary parts together
        """
        new = ComplexNumber(self.getReal(), self.getImaginary())
        new.re += other.getReal()
        new.im += other.getImaginary()
        return new
    
    def sub(self, other):
        """
        This Medthod substract to our Complex Number another Complex Number to our Complex Number by subtracting their real parts together and their imaginary parts together
        """
        new = ComplexNumber(self.getReal(), self.getImaginary())
        new.re -= other.getReal()
        new.im -= other.getImaginary()
        return new
    
    def multiply(self, other):
        """
        This Method multiply our Complex Number with another Complex Number
        """
        new = ComplexNumber(self.getReal(), self.getImaginary())
        new.re = (new.re*other.getReal()) - (new.im*other.getImaginary())
        new.im = (new.im*other.getReal()) + (new.re*other.getImaginary())
        return new
    
    def divide(self, other):
        """
        This Method divide our Complex Number with another Complex Number.
        The Procces are explained hier (https://de.wikipedia.org/wiki/Komplexe_Zahl#Division)
        """
        new = ComplexNumber(self.getReal(), self.getImaginary())
        if other.getReal() == 0.0 and other.getImaginary() == 0.0:
            return 0.0
        else:
            other_bar_re = other.getReal()/((other.getReal()**2) + (other.getImaginary()**2))
            other_bar_im = (-1*other.getImaginary())/((other.getReal()**2) + (other.getImaginary()**2))
            tmp = ComplexNumber(other_bar_re, other_bar_im)
            new.multiply(tmp)
        return new
        
    def abs(self):
        """
        This Method return a float Number which is the absulute Value of our Complex Number
        """
        return math.sqrt(self.getReal()**2 + self.getImaginary()**2)
    
    def toString(self):
        """
        For the case this Method just Print our Complex Number
        """
        print(self)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-r1', type=float, default=0, help='the real part of the first Complex NUmber')
    parser.add_argument('-i1', type=float, default=0, help='the imaginary part of the first Complex Number')
    parser.add_argument('-r2', type=float, default=0, help='the real part of the seconf Complex Number')
    parser.add_argument('-i2', type=float, default=0, help='the imaginary part of the second Complex Number')

    args = parser.parse_args()
    print(f"({args.r1} + {args.i1}i) x ({args.r2} + {args.i2}i) = {ComplexNumber(args.r1, args.i1).multiply(ComplexNumber(args.r2, args.i2))}")
    print(f"({args.r1} + {args.i1}i) + ({args.r2} + {args.i2}i) = {ComplexNumber(args.r1, args.i1).add(ComplexNumber(args.r2, args.i2))}")
    print(f"({args.r1} + {args.i1}i) - ({args.r2} + {args.i2}i) = {ComplexNumber(args.r1, args.i1).sub(ComplexNumber(args.r2, args.i2))}")

if __name__ == '__main__':
    main()