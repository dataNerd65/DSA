import java.util.ArrayList;
import java.util.List;

public class Solution{
    public List<List<String>>partition(String s){
        List<List<String>> res = new ArrayList<>();
        backtrack(s, 0, new ArrayList<>(), res);
        return res;

    }

    private void backtrack(String s, int start, List<String> path, List<List<String>> res){
        if (start == s.length()){
            res.add(new ArrayList <> (path));
            return;
        }
        for (int end = start + 1; end <= s.length(); end++){
            String substring = s.substring(start, end);
            if (isPalindrome(substring)){
                path.add(substring);
                backtrack(s, end, path, res);
                path.remove(path.size() - 1);
            }
        }
    }

    private boolean isPalindrome(String sub){
        int left = 0;
        int right = sub.length() -1;
        while(left < right){
            if(sub.charAt(left++) != sub.charAt(right--)){
                return false;
            }
        }
        return true;
    }

    public static void main(String[] args){
        Solution solution = new Solution();
        System.out.println(solution.partition("aab"));
        System.out.println(solution.partition("a"));

        
    }
}