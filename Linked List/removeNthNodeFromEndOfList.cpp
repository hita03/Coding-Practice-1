// Idea:
// With a singly linked list, the only way to find the end of the list, and thus the n'th node from the end, is to actually iterate all the way to the end. The challenge here is attemping to find the solution in only one pass. A naive approach here might be to store pointers 
// to each node in an array, allowing us 
// to calculate the n'th from the end once we reach the end, but that would take O(M) extra space, where M is the length of the linked list.

// A slightly less naive approach would be to only store only the last n+1 node pointers in the array. This could be achieved by overwriting the elements of the storage array in circlular fashion as we iterate through the list. This would lower the space complexity to O(N+1).

// In order to solve this problem in only one pass and O(1) extra space, however, we would need to find a way to both reach the end of the list with one pointer and also reach the n'th node from the end simultaneously with a second pointer.

// To do that, we can simply stagger our two pointers by n nodes by giving the first pointer (fast) a head start before starting the second pointer (slow). Doing this will cause slow to reach the n'th node from the end at the same time that fast reaches the end.

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

// Given the head of a linked list, remove the nth node from the end of the list and return its head.

// Input: head = [1,2,3,4,5], n = 2
// Output: [1,2,3,5]
// Example 2:

// Input: head = [1], n = 1
// Output: []
// Example 3:

// Input: head = [1,2], n = 1
// Output: [1]
class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        ListNode *q=head;
        ListNode *p=head;
        int count=0;
        
        while(count<n){
            p=p->next; 
            count++;
        }
        if(p==NULL) return head->next;
        
       while(p->next!=NULL){
           q=q->next;
           p=p->next;
       }
       ListNode* del=q->next;
       q->next=q->next->next;
       delete del; 
       // cout<<p->val<<q->val; 
       return head; 
    }
};


