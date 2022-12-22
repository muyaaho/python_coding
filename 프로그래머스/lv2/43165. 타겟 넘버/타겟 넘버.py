def solution(numbers, target):
    arr = []
    answer = 0
    
    def fun(now, a):
        global answer
        if len(a) == 0:
            if now==target:
                arr.append(now)
            return
        
        fun(now + a[0], a[1:])
        fun(now - a[0], a[1:])
    
    fun(numbers[0], numbers[1:])
    fun(-numbers[0], numbers[1:])
    
    
    return len(arr)