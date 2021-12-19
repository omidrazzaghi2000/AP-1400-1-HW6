
<center>
<h1>
In The Name Of ALLAH
</h1>
<h2>
Advanced Programming - Homework 6
</h2>
<h2>
Dr.Amir Jahanshahi
</h2>
<h3>
Deadline: 5 , day  - 23:59
</center>


# Introduction
Hi all 🙋‍♂️

In this homework we will implement some classes and learn python more.

# MathAP Class
## PART I:
Create a Python class called ```MathAP``` that has the methods add and subtract. Have these 2 functions take at least 1 parameter.
- add
- subtract 
  
It should be able to do the following task:
```python
m_ap.add(2).add(2,5).subtract(3,2).result
```
which should perform 0+2+(2+5)-(3+2) and return 4.

## PART II:
Modify MathAP to take at least one integer(s) and/or list(s) as a parameter with any number of values passed into the list. It should now be able to perform the following tasks:
```python
m_ap.add([1], 3,4).add([3,5,7,8], [2,4.3,1.25]).subtract(2, [2,3], [1.1,2.3]).result
```
should do 0+1+3+4+(3+5+7+8)+(2+4.3+1.25)-2-(2+3)-(1.1+2.3) and return its result.

## PART III:
Make any needed changes in MathAP in order to support tuples of values in addition to lists and singletons.

# Shape Class
```Shape``` class is abstract class and then ```Rectangle``` and ```Squre``` and ```Circle``` are inherited from ```Shape```.

Override ```area``` and ```perimeter``` function for three shapes and add other needed functions.

``` python
class Shape(object):
    """
    Generic Shape object
    """
    def area(self):
        """
        Area of shape
        """
        pass

    def perimeter(self):
        """
        Perimeter of shape
        """
        pass
```

output of ```print(any_shape)``` is must be like below:

<img src="./stuff/s1.jpg">

## Shape summation
Summation is just for squres and circles and this operation return shape with summation of squares side and circles radius.

## Shape power operation
we want to implement power operation for shapes and this operation return object with area and perimeter square 2.

## Shape equality
It is so obvious.😉

## Shape compare
shapes be compared with area.

-    Circle
we need that compare circle with a number which our program compare radius of circle and number.

-    Squre
like circle we need to compare square with number by its side.

