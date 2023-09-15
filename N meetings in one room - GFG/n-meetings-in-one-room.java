//{ Driver Code Starts
import java.io.*;
import java.util.*;
import java.lang.*;

class GFG {
    public static void main(String args[]) throws IOException {
        BufferedReader br =
            new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(br.readLine().trim());

        while (t-- > 0) {
            String inputLine[] = br.readLine().trim().split(" ");
            int n = Integer.parseInt(inputLine[0]);

            int start[] = new int[n];
            int end[] = new int[n];

            inputLine = br.readLine().trim().split(" ");
            for (int i = 0; i < n; i++)
                start[i] = Integer.parseInt(inputLine[i]);

            inputLine = br.readLine().trim().split(" ");
            for (int i = 0; i < n; i++) 
                end[i] = Integer.parseInt(inputLine[i]);
                
            int ans = new Solution().maxMeetings(start, end, n);
            System.out.println(ans);
        }
    }
}

// } Driver Code Ends


class Solution 
{
    //Function to find the maximum number of meetings that can
    //be performed in a meeting room.
    public static int maxMeetings(int start[], int end[], int n)
    {
        List<List<Integer>> meetings = new ArrayList<>();
        for(int i=0;i<start.length;i++){
            List<Integer> meeting = new ArrayList<>();
            meeting.add(start[i]);
            meeting.add(end[i]);
            meetings.add(meeting);
        }

        Collections.sort(meetings,new Comparator <List<Integer>>() {
            public int compare(List<Integer> meeting1, List<Integer> meeting2){
                // return meeting1.get(1) < meeting2.get(1); // X || wrong way
                // return meeting1.get(1).compareTo(meeting2.get(1));
                return Integer.compare(meeting1.get(1), meeting2.get(1));

            }
        });

        int ans = 1;
        int prevEndTime = meetings.get(0).get(1);

        for (int i = 1; i < meetings.size(); i++) {
            if (meetings.get(i).get(0) > prevEndTime) { // Compare start times, not end times
                ans++;
                prevEndTime = meetings.get(i).get(1);
            }
        }

        return ans;

    }
}
