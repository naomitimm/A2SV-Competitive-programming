# def sortPancake(arr):
#     k = [i for i in range(1,len(arr) + 1)]
    
#     copy = arr.copy()
#     copy.sort()
#     count = 0


#     if(arr != copy):

#         while count < 10 * len(arr):
#             for i in range(0, len(arr)):
#                 if arr[i] == max(arr):
#                     print(arr)
#                     sub = arr[:k[i+1]]
#                     print("\nsub:", sub)
#                     sub.reverse()
#                     print("sub reverse:",sub)
#                     arr = arr[k[i+1]:]
#                     arr = sub + arr
#                     print("arr:",arr)
#             count += 1
                

# sortPancake([3,2,4,1]) 