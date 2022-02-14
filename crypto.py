'''
Crypto ex sheet 4 number 3.3
'''
n = 4

# write function for sample space generation

def sampleSpaceGeneration(size):
    S = []
    if size == 0:
        raise Exception("N needs to be higher than 0")
    if size == 1:
        S = ['0','1']
        return S
    smallerSet = sampleSpaceGeneration(size-1)
    for elem in smallerSet:
        S.append(elem+'0')
        S.append(elem+'1')
    return S

#print(sampleSpaceGeneration(n))
def hardCoreBit(s,x):
    bit = 0
    for i in range(len(s)):
        X = int("" + x[i])
        S = int("" + s[i])
        b = X & S
        bit = b ^ bit
    return str(bit)

# write a function for goldreich-levin hardcore bit

# build sample space {0,1}^n+1
BiggerSet = sampleSpaceGeneration(n+1)
print("{0,1}^n+1")
print(BiggerSet)
# build sample space s = {0,1}^n
smallSSet = sampleSpaceGeneration(n)
print("s set")
print(smallSSet)

#build distribution X
def buildDistributionX(n):
    xleftDistribution = sampleSpaceGeneration(n/2)
    X = []
    for x in xleftDistribution:
        X.append(x+'1'*(int)(n/2))
    return X

D = buildDistributionX(n)
print("Distribution x")
print(D)
# build sample space S3
def buildS3(S,D):
    NewSet = []
    for s in S:
        for x in D:
            NewSet.append(s+hardCoreBit(s,x))
    return NewSet
S3 = buildS3(smallSSet,D)
print(S3)
# count the frequencies