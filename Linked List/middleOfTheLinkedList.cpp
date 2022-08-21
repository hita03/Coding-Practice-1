// Given the head of a singly linked list, return the middle node of the linked list.

// If there are two middle nodes, return the second middle node.

 

// Example 1:


// Input: head = [1,2,3,4,5]
// Output: [3,4,5]
// Explanation: The middle node of the list is node 3.
// Example 2:


// Input: head = [1,2,3,4,5,6]
// Output: [4,5,6]
// Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.

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
public:
    ListNode* middleNode(ListNode* head) {
        // ListNode* p= head;
        // vector<int> tmp;
        // int count=0;
        // while(p!=NULL){
        //     tmp.push_back(p->val);
        //     p=p->next;
        //     count+=1;
        // }
        // return tmp[(count+1)/2];
        
        ListNode *slow = head, *fast = head;
        while (fast && fast->next){
            slow = slow->next;
            fast = fast->next->next;;
        }
        return slow;
        
    }
};