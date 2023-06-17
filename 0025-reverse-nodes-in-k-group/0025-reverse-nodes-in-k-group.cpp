/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
    
    int getLength(ListNode* head){
        ListNode* curr = head;
        int cnt = 0;
        while(curr) cnt++  , curr = curr->next;
        return cnt;
    }
public:
    ListNode* th = NULL , *tt = NULL;
    void helper(ListNode* node){
        if(!th){
            th = node;
            tt = node;
        }
        else{
            node->next = th;
            th = node;
        }
    }
    ListNode* reverseKGroup(ListNode* head, int k) {
        // if(!head->next or k < 1) return head;
        
        int len = getLength(head);
        ListNode* curr = head , *originalHead = NULL , *originalTail = NULL;
        while(len >= k){
            int tempK = k;
            while(tempK-- > 0){
                ListNode* next = curr->next;
                curr->next = NULL;
                helper(curr);
                curr = next;
            }
            
            if(!originalHead){
                originalHead = th;
                originalTail = tt;
            }
            else{
                originalTail->next = th;
                originalTail = tt;
            }
            
            th = NULL;
            tt = NULL;
            len -= k;
        }
        
        originalTail->next = curr;
        return originalHead;
    }
};