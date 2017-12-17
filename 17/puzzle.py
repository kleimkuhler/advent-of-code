def spinlock(buf, N, step=3):
    cur = 0
    for i in range(1, N+1):
        cur = (cur + step) % len(buf) + 1
        buf = buf[:cur] + [i] + buf[cur:]
    return buf[cur+1]

def terminate(N, step=3):
    i, cur, val = 1, 0, 0
    while i < N+1:
        val = i-1 if cur == 1 else val
        steps = (i - cur - 1) // step 
        cur = (cur + ((steps + 1) * step)) % i + 1
        i += steps + 1
    return val

input = 356
print('1: {}'.format(spinlock([0], 2017, input)))
print('2: {}'.format(terminate(5*10**7, input)))
