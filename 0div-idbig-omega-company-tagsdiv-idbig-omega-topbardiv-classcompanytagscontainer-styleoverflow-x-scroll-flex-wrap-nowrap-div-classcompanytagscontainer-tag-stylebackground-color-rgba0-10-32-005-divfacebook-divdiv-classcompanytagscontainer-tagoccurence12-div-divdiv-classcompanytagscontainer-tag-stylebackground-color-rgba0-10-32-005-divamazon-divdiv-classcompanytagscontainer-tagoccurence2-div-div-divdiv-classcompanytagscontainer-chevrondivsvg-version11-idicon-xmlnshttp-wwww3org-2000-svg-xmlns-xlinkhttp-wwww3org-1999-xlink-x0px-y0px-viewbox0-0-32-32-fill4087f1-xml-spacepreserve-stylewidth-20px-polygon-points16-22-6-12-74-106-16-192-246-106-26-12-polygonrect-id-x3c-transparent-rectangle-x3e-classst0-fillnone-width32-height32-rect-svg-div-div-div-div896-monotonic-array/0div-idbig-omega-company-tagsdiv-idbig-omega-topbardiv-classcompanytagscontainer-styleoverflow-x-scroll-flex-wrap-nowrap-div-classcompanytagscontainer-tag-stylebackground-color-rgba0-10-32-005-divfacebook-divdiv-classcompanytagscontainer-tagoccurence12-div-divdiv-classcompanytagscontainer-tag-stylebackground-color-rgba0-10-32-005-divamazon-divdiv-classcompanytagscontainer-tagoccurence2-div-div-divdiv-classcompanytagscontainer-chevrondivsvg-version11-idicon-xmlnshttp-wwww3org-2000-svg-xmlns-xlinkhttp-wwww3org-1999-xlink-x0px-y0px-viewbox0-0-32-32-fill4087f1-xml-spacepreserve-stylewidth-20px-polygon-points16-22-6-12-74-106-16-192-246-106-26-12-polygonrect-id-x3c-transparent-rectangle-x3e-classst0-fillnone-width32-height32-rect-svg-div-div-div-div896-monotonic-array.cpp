class Solution {
public:
    bool isMonotonic(vector<int>& nums) {
        if(nums.size()==1) return true;
        vector<int>checked(nums.size(),0);
        if(nums[0]==nums[1])
        {
            int k=1,j=-1;
            for(int i=1;i<nums.size()-1;i++)
            {
                if(nums[i]==nums[i+1]) continue;
                else if(nums[i]<nums[i+1])
                {
                    k=1;
                    j=i;
                    break;
                }
                else if(nums[i]>nums[i+1])
                {
                    k=2;
                    j=i;
                    break;
                }
            }
            while(j>=0)
            {
                checked[j]=k;
                j--;
            }
        }
        for(int i=0;i<nums.size()-1;i++)
        {
            if(nums[i]<nums[i+1]) checked[i]=1;
            else if(nums[i]>nums[i+1]) checked[i]=2;
            else if(i>0&&(nums[i]==nums[i+1]))
            {
                if(checked[i-1]==1)
                {
                   // cout<<"Hello";
                    checked[i]=1;
                }
                else if(checked[i-1]==2)
                {
                    //cout<<"Hi";
                    checked[i]=2;
                }
            }
        }
        int k=checked[0];
        checked[nums.size()-1]=checked[nums.size()-2];
        for(int i=0;i<nums.size();i++)
        {
            if(k!=checked[i]) return false;
        }
        return true;
    }
};