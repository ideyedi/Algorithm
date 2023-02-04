class RandomizedSet {

    Set s;

    public RandomizedSet() {
        this.s = new HashSet();
    }
    
    public boolean insert(int val) {
        boolean isResult = false;
        // HashSet 객체에 val가 포함되어 있지 않은 경우
        if (!this.s.contains(val)){
            this.s.add(val);
            isResult = true;
        } 
        return isResult;
    }
    
    public boolean remove(int val) {
        boolean isResult = false;
        // HashSet 객체에 val가 포함되어 있는 경우
        if (this.s.contains(val)){
            this.s.remove(val);
            isResult = true;
        } 
        return isResult;
    }
    
    public int getRandom() {
        int i = 0;
        int resultvalue = 0;
        int randomValue = (int) (Math.random() * this.s.size());

        Iterator sIter = this.s.iterator();
        while (sIter.hasNext()) {
            resultvalue = (Integer) sIter.next();
            // 반복 횟수가 randomValue와 일치하는 경우
            if (i == randomValue) {
                break;
            }
            i++;
        }
        return resultvalue;
    }
}

/**
 * Your RandomizedSet object will be instantiated and called as such:
 * RandomizedSet obj = new RandomizedSet();
 * boolean param_1 = obj.insert(val);
 * boolean param_2 = obj.remove(val);
 * int param_3 = obj.getRandom();
 */
