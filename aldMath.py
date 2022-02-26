from __future__ import annotations
from multipledispatch import dispatch
from types import *
from math import sqrt
from random import random

class aldVector(object):
    
    def __init__(self, *args) -> None:
        self.x = 0.0
        self.y = 0.0
        self.z = 0.0
        if (len(args) == 2):
            try:
                self.x = float(args[0])
                self.y = float(args[1])
            except ValueError as err:
                raise err
        elif (len(args) == 3):
            try:
                self.x = float(args[0])
                self.y = float(args[1])
                self.z = float(args[2])
            except ValueError as err:
                raise err
    
    @dispatch(object, object, object) 
    def set(self, x: float, y: float, z: float) -> None:
        try:
            x = float(x)
            y = float(y)
            z = float(z)
        except ValueError as err:
            raise err
        # Setting values after try/except to prevent editing only 1 or 2 values in case of a ValueError
        self.x = x
        self.y = y
        self.z = z
    
    @dispatch(object, object)
    def set(self, x: float, y: float) -> None:
        self.set(x, y, 0)
                
    @dispatch(object, object, object)
    def add(self, x: float, y: float, z: float) -> None:
        try:
            self.x += float(x)
            self.y += float(y)
            self.z += float(z)
        except ValueError as err:
            raise err
    
    @dispatch(object, object)
    def add(self, x: float, y: float) -> None:
        self.add(x, y, 0)
        
    @dispatch(object)
    def add(self, vect: aldVector) -> None:
        if isinstance(vect, aldVector): self.add(vect.x, vect.y, vect.z)
        else: raise ValueError('aldVector expected !')
    
    # @dispatch(object, object)
    # def add(v1: aldVector, v2: aldVector) -> aldVector:
    #     return aldVector(v1.x + v2.x, v1.y + v2.y, v1.z + v2.z)
    
    @dispatch(object, object, object)
    def sub(self, x: float, y: float, z: float) -> None:
        try:
            self.x -= float(x)
            self.y -= float(y)
            self.z -= float(z)
        except ValueError as err:
            raise err
    
    @dispatch(object, object)
    def sub(self, x: float, y: float) -> None:
        self.sub(x, y, 0)
        
    @dispatch(object)
    def sub(self, vect: aldVector) -> None:
        if isinstance(vect, aldVector): self.sub(vect.x, vect.y, vect.z)
        else: raise ValueError('aldVector expected !')
        
    # @dispatch(object, object)
    # def sub(v1: aldVector, v2: aldVector) -> aldVector:
    #     return aldVector(v1.x - v2.x, v1.y - v2.y, v1.z - v2.z)
        
    @dispatch(object)
    def mult(self, a: float) -> None:
        try:
            a = float(a)
        except ValueError as err:
            raise err
        self.x *= a
        self.y *= a
        self.z *= a
    
    @dispatch(object)
    def div(self, a: float) -> None:
        try:
            a = float(a)
            a = 1/a
        except (ValueError, ZeroDivisionError) as err:
            raise err
        self.mult(a)
    
    def magnitudeSquared(self) -> float:
        return self.x * self.x + self.y * self.y + self.z * self.z
    
    def magnitude(self) -> float:
        return sqrt(self.magnitudeSquared())
    
    def normalize(self) -> None:
        mag = self.magnitude()
        if (mag == 0):
            raise ZeroDivisionError("Magnitude of vector is 0")
        self.x = self.x / mag
        self.y = self.y / mag
        self.z = self.z / mag
        
    def limit(self, maxMag: float) -> None:
        mag = self.magnitude()
        if (mag == 0 or mag <= maxMag): return # Avoid raising a ZeroDivisionError or modifying the magnitude if it is already below max
        self.normalize()
        self.mult(maxMag)
        
    def setMagnitude(self, mag: float) -> None:
        if (self.magnitude() == 0): return # Avoid raising a ZeroDivisionError
        self.normalize()
        self.mult(mag)
        
    #! Static methods
    
    @staticmethod
    def dot(v1: aldVector, v2: aldVector) -> float:
        return v1.x * v2.x + v1.y * v2.y + v1.z * v2.z
    
    @staticmethod
    def cross(v1: aldVector, v2: aldVector) -> aldVector:
        return aldVector(v1.y * v2.z - v1.z * v2.y,
                         v1.z * v2.x - v1.x * v2.z,
                         v1.x * v2.y - v1.y * v2.x)

    @staticmethod
    def dist(v1: aldVector, v2: aldVector) -> float:
        return sqrt((v1.x - v2.x) ** 2 + (v1.y - v2.y) ** 2 + (v1.z - v2.z) ** 2)

    @staticmethod
    def random3D() -> aldVector:
        vec = aldVector(random(), random(), random())
        vec.normalize()
        return vec
    
    @staticmethod
    def random2D() -> aldVector:
        vec = aldVector(random(), random(), 0)
        vec.normalize()
        return vec
    
    @staticmethod
    def linearInterpolation(v1: aldVector, v2: aldVector, t: float) -> aldVector:
        if (t < 0 or t > 1): raise ValueError('t must be between 0 and 1')
        x = (1 - t) * v1.x + t * v2.x
        y = (1 - t) * v1.y + t * v2.y
        z = (1 - t) * v1.z + t * v2.z
        return aldVector(x, y, z)

    #! Export methods

    def asArray(self) -> list[float]:
        vecList = []
        vecList.append(self.x)
        vecList.append(self.y)
        vecList.append(self.z)
        return vecList
    
    def __repr__(self) -> str:
        return f'[{self.x}, {self.y}, {self.z}]'

