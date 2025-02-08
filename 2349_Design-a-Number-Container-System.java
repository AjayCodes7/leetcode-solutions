class NumberContainers {
    HashMap<Integer, SortedSet<Integer>> numbers;
    HashMap<Integer, Integer> map;
    public NumberContainers() {
        numbers = new HashMap<>();
        map = new HashMap<>();
    }
    
    public void change(int index, int number) {
        if(map.containsKey(index)){
            int oldVal = map.get(index);
            if(numbers.get(oldVal).size() == 1){
                numbers.remove(oldVal);
            } else{
                numbers.get(oldVal).remove(index);
            }
        }
        map.put(index,number);
        numbers.putIfAbsent(number,new TreeSet<>());
        numbers.get(number).add(index);
    }
    
    public int find(int number) {
        if(numbers.containsKey(number)){
            return (int)numbers.get(number).first();
        }
        return -1;
    }
}

/**
 * Your NumberContainers object will be instantiated and called as such:
 * NumberContainers obj = new NumberContainers();
 * obj.change(index,number);
 * int param_2 = obj.find(number);
 */