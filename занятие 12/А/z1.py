Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
def Solution(N):
    global X
    if N == 0:
        return 1
    return (X**N) // (Solution(N-1) * N)
X = 10
print(Solution(15))