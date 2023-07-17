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
    ListNode* reverse(ListNode* head){
        if(!head or !head->next) return head;
        ListNode* prev = NULL;
        ListNode* curr = head;
        ListNode* next;
        
        while(curr){
            next = curr->next;
            curr->next = prev;
            
            prev = curr;
            curr = next;
        }
        
        return prev;
    }
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
      
//         ListNode* h1 = l1;
//         ListNode* h2 = l2;
        
//         h1 = reverse(h1);
//         h2 = reverse(h2);

//         ListNode* newHead = new ListNode(-1);
//         ListNode* temp = newHead;
        
//         int carry = 0;
        
//         while(h1 or h2){
//             int a = 0 , b = 0;
//             if(h1){
//                 a = h1->val;
//                 h1 = h1->next;
//             }
//             if(h2){
//                 b = h2->val;
//                 h2 = h2->next;
//             }
            
//             int sum = a + b + carry;
//             carry = sum/10;

//             ListNode* addNode = new ListNode(sum%10);
//             temp->next = addNode;
//             temp = temp->next;
//         }
        
//         if(carry)  temp->next = new ListNode(carry);
        
       
//         newHead = reverse(newHead->next);
//         return newHead;
        
        
        
        stack<int> s1;
        stack<int> s2;
        
        while(l1){
            s1.push(l1->val);
            l1 = l1->next;
        }
        
        while(l2){
            s2.push(l2->val);
            l2 = l2->next;
        }
        
        int carry = 0;
        ListNode* head = NULL;
        
        while(!s1.empty() or !s2.empty()){
            int a = 0 , b = 0;
            if(!s1.empty()){
                a = s1.top();
                s1.pop();
            }
            if(!s2.empty()){
                b = s2.top();
                s2.pop();
            }
            int sum = a + b + carry;
            carry = sum/10;
            
            ListNode* toAdd = new ListNode(sum%10);
            
            if(!head) head = toAdd;
            else{
                toAdd->next = head;
                head = toAdd;
            }
        }
        
        if(carry){
            ListNode* toAdd = new ListNode(carry);
            toAdd->next = head;
            head = toAdd;
        }
        
        return head;
        
    }
};