n = int(input())
a = list(map(int, input().split()))
k=int(input())
tong=0
max_tong=0
dem=1
for i in range(k):
    tong+=a[i]
for i in range(1,n-k+1):
    tong=tong-a[i-1]+a[i+k-1]
    if tong>max_tong:
        max_tong=tong
print(max_tong)
