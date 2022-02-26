from aldMath import aldVector

def main():
    vec1 = aldVector(0, 0)
    vec2 = aldVector(100, 100)
    print(aldVector.linearInterpolation(vec1, vec2, 0.1))


if __name__=='__main__':
    main()