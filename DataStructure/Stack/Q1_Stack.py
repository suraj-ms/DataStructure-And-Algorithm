from collections import Counter

def topKFrequent(nums, k):
    # Count the occurrences of each element in the list
    counts = Counter(nums)
    
    # Get the k most common elements from the Counter
    top_k = counts.most_common(k)
    
    # Extract the elements from the tuples returned by most_common method
    result = [elem for elem, _ in top_k]
    
    return result

# Example usage
nums = [1, 1, 1, 2, 2, 3]
k = 1
output = topKFrequent(nums, k)
print(output)