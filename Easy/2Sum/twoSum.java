import java.util.HashMap;
class twoSum{
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> map = new HashMap<>();
        for(int i = 0; i<nums.length; i++){
            int rem = target - nums[i];
            if(map.containsKey(rem)){
                return new int[] {map.get(rem), i};
            }
            map.put(nums[i], i);
        }
        return new int[]{};
    }

    public static void main(String[] args) {
        twoSum obj = new twoSum();
        int[] nums = {2,7,11,15};
        int target = 9;
        int[] ans = obj.twoSum(nums, target);
        System.out.println(ans[0]+" "+ans[1]);
        
    }

}