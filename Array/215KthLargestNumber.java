class Solution {
    public int findKthLargest(int[] nums, int k) {
        if (k == 0) {
            return 0;
        }
        //PriorityQueue<Integer> queue = new PriorityQueue<>(10, Collections.reverseOrder());
        PriorityQueue<Integer> pq = new PriorityQueue<>(nums.length, 
            new Comparator<Integer>() {
                public int compare(Integer int1, Integer int2) {
                    return int2 - int1;
                }
            });
        for (int i : nums) {
            pq.add(i);
        }
        int toReturn = 0;
        for (int i = 0; i < k; i++) {
            toReturn = pq.remove();
        }
        return toReturn;
    }
}
