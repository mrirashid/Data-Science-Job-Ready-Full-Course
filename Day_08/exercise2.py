## check if a value exist in a set/dict
## The hash lookup (0(1))

def set_contains(myset,target):
    ## step 1 compute mathematical signature 
    h = calculate_hash(target)
    ## step 2 calculate memory, address
    bucket_index= h % myset.total_buckets
    ## step 3 direct jump
    memory_slot=myset.buckets[bucket_index]

    if memory_slot == target:
        return True
    else:
        return False