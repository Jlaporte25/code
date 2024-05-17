def main():
    import sys
    import collections
    
    grocery_counts = collections.defaultdict(int)
    
    try:
        while True:
            item = input().strip().upper()
            grocery_counts[item] += 1
    except EOFError:
        pass
    
    sorted_items = sorted(grocery_counts.keys())
    
    for item in sorted_items:
        print(f"{grocery_counts[item]} {item}")        
            
main()