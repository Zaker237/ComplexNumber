# cnumber
Thid repository privide a tool to handle maths operation with complex number.

## installation

Clone this repository,  cd into it and run:
```console
python -m pip install .
```

## Usage

```python
from cnumber import ComplexNumber

number1 = ComplexNumber(1, 2)
number2 = ComplexNumber(3, 4)

number1.add(number2)

print(number1)
# this should be print 4 + 6i
```