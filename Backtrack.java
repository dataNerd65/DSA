//Implementing backtracking functionalitiea in java now
import java.util.*;

public class Backtrack {
    public List<List<Integer>> subsets(int[] nums){
        List<List<Integer>> res = new ArrayList<>();
        backtrack(0, nums, new ArrayList<>(), res);
        return res;
    }

    private void backtrack(int start, int[] nums, List<Integer> path, List<List<Integer>> res){
        //Appending the current subset to result
        res.add(new ArrayList<> (path));

        //Exploring further elements to add to current subset
        for(int i = start; i < nums.length; i++){
            //Include nums in current subset
            path.add(nums[i]);
            //Recurse with upadeted path and next start index
            backtrack(i+ 1, nums, path, res);

            //Bactracking by removing last element
            path.remove(path.size() - 1);
        }
    }

    public static void main(String[] args){
        Backtrack backtrack = new Backtrack();
        System.out.println(backtrack.subsets(new int[]{1, 2, 3}));
        System.out.println(backtrack.subsets(new int[]{0}));
    }
}