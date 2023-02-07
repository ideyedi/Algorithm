import java.util.Arrays;
import java.util.stream.Stream;

class Solution {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {

        // int array merge & sorted
        int[] mergeArray = IntStream.concat(Arrays.stream(nums1), Arrays.stream(nums2)).sorted().toArray();

        // get median value
        double result = 0;
        int medianIndex = Math.floorDiv(mergeArray.length, 2);
        if (mergeArray.length % 2 == 0) {
            result = ((double) mergeArray[medianIndex - 1] + (double) mergeArray[medianIndex]) / 2;
        } else {
            result = mergeArray[medianIndex];
        }
        
        return result;
    }
}
