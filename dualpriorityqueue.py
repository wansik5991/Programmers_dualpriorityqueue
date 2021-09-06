import heapq
def solution(operations):
    heap = []

    for operation in operations :
        operation = operation.split()

        if operation[0] == 'I' :
            heapq.heappush(heap, int(operation[1]))
        else :
            if heap :
                if operation[1] == '1' :
                    heap = sorted(heap, reverse=True)[1:]
                    heapq.heapify(heap)
                else :
                    heapq.heappop(heap)
    
    if heap :
        return [max(heap), min(heap)]
    return [0,0]

#print(solution(["I 16","D 1"]))
#print(solution(["I 7","I 5","I -5","D -1"]))
print(solution(["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]))