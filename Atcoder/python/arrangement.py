def listExcludedIndices(data, indices=[]):
    return [x for i, x in enumerate(data) if i not in indices]

data = list(map(int, input().split()))

result = []
for i in range(len(data)):
    for j in range(len(data) - 1):
        for k in range(len(data) - 2):
            jData = listExcludedIndices(data, [i])
            kData = listExcludedIndices(jData, [j])
            result.append([data[i], jData[j], kData[k]])