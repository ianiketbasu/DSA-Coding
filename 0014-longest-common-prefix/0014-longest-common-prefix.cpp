class Solution {
public:
    
//    /* int findMinLength(vector<string>& strs, int n)

//     {
// 	int min = strs[0].length();

// 	for (int i=1; i<n; i++)
// 		if (strs[i].length() < min)
// 			min = strs[i].length();

// 	return(min);
// }
    
//     string longestCommonPrefix(vector<string>& strs) 
//     {
//         int n = strs.size();
//         int min_str_len=findMinLength(strs,n);
        
//         string result;
//         char c;
        
//         for ( int i=0;i<min_str_len;i++)
//         {
//             c=strs[0][i];
//             for(int j=1;j<n;j++){
//             if(strs[j][i]!=c)
//                 return result;
            
//             result.push_back(c);
                
//             }
//         }
//         return (result);
//     }*/
// int findMinLength(vector<string>& arr, int n)
// {
// 	int min = arr[0].length();

// 	for (int i=1; i<n; i++)
// 		if (arr[i].length() < min)
// 			min = arr[i].length();

// 	return(min);
// }

// // A Function that returns the longest common prefix
// // from the array of strings
// string longestCommonPrefix(vector<string>& arr)
// {   int n = arr.size();
// 	int minlen = findMinLength(arr, n);

// 	string result; // Our resultant string
// 	char current; // The current character

// 	for (int i=0; i<minlen; i++)
// 	{
// 		// Current character (must be same
// 		// in all strings to be a part of
// 		// result)
// 		current = arr[0][i];

// 		for (int j=1 ; j<n; j++)
// 			if (arr[j][i] != current)
// 				return result;

// 		// Append to result
// 		result.push_back(current);
// 	}

// 	return (result);
// }
    
    string longestCommonPrefix(vector<string>& arr){
        string ans = "";
      
        for(int i=0;i<arr[0].size();i++){
            char current = arr[0][i];
            
            for(int j=1;j<arr.size();j++){
                if(i>= arr[j].size() || arr[j][i] != current)
                    return ans;
            }
            ans += current;
        }
        return ans;
    }
};