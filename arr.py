def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[:mid]
        
        merge_sort(left_half)
        merge_sort(right_half)
        
        i,j,k = 0,0,0
        
        # merge the two halves back togather
        while i < len(left_half) and j < len(right_half):
            if left_half [i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
               arr[k]  = right_half[j]
               j+=1
               k+=1     
                
        while i < len(left_half):
             arr [k] = right_half[i]
             i +=1
             k+=1
        while j < len(right_half):
            arr[k] = right_half[j]
            j+=1
            k+=1
my_list = [12,11,13,5,6,7,9]
merge_sort(my_list)
print("sorted array is:", my_list)

# def sort_array(arr):
#     sorted_arr =sorted(arr)
#     return sorted_arr