
def main() -> None:    
    
    def sum_array(arr):
        return sum(list(sorted(arr)[1:-1])) if arr else 0

    
    def hero(bullets, dragons):
        return bullets >= dragons * 2


    def count_positives_sum_negatives(arr):
        return [len(list(filter(lambda x: x > 0, arr)))] + [sum(list(filter(lambda x: x < 0, arr)))] if arr else []
    

    
if __name__ == '__main__':
    main()
  