//{ Driver Code Starts
import java.io.*;
import java.lang.*;
import java.util.*;

class Job {
    int id, profit, deadline;
    Job(int x, int y, int z){
        this.id = x;
        this.deadline = y;
        this.profit = z; 
    }
}

class GfG {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        //testcases
		int t = Integer.parseInt(br.readLine().trim());
		while(t-->0){
            String inputLine[] = br.readLine().trim().split(" ");
            
            //size of array
            int n = Integer.parseInt(inputLine[0]);
            Job[] arr = new Job[n];
            inputLine = br.readLine().trim().split(" ");
            
            //adding id, deadline, profit
            for(int i=0, k=0; i<n; i++){
                arr[i] = new Job(Integer.parseInt(inputLine[k++]), Integer.parseInt(inputLine[k++]), Integer.parseInt(inputLine[k++]));
            }
            
            Solution ob = new Solution();
            
            //function call
            int[] res = ob.JobScheduling(arr, n);
            System.out.println (res[0] + " " + res[1]);
        }
    }
}
// } Driver Code Ends


class Solution
{
    //Function to find the maximum profit and the number of jobs done.
    int[] JobScheduling(Job arr[], int n)
    {
        Arrays.sort(arr,(a,b) -> b.profit - a.profit); // sort the array in decending order . . .
        
        int maxi = 0;
        for(int i=0;i<arr.length;i++){
            maxi = Math.max(maxi , arr[i].deadline);
        }
        
        int[] deadlineArr = new int[maxi + 1];
        Arrays.fill(deadlineArr,-1);
        int noOfJobs = 0 , maxProfit = 0;
        
        for(int i=0;i<arr.length;++i){
            for(int j=arr[i].deadline;j>0;--j){
                if(deadlineArr[j] == -1){
                    deadlineArr[j] = i;
                    noOfJobs++;
                    maxProfit += arr[i].profit;
                    break;
                }
            }
        }
        
        return new int[]{noOfJobs,maxProfit};
        
    }
}

/*
class Job {
    int id, profit, deadline;
    Job(int x, int y, int z){
        this.id = x;
        this.deadline = y;
        this.profit = z; 
    }
}
*/