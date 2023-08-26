public class main{
    public static void main(String[] args){
        int[] nums = [10,10,5,3,2,14];
        int total = sum(nums);
        System.out.println(total)
    }
    private static int sum(int[] nums){
        int total = 0;
        for i : nums{
            total+=i
        }
        return total
    }
}