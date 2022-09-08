# You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

# Merge all the linked-lists into one sorted linked-list and return it.

 

# Example 1:

# Input: lists = [[1,4,5],[1,3,4],[2,6]]
# Output: [1,1,2,3,4,4,5,6]
# Explanation: The linked-lists are:
# [
#   1->4->5,
#   1->3->4,
#   2->6
# ]
# merging them into one sorted list:
# 1->1->2->3->4->4->5->6

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        li=[]
        head = ListNode(0)
        p=head
        for i in range(len(lists)):
            while lists[i]:
                li.append(lists[i].val)
                lists[i]=lists[i].next
        
        for x in sorted(li):
            p.next = ListNode(x)
            p=p.next
        return head.next    
            
# PSYCH SOLN!            
# ListNode *mergeKLists(vector<ListNode *> &lists) {
#     if(lists.empty()){
#         return nullptr;
#     }
#     while(lists.size() > 1){
#         lists.push_back(mergeTwoLists(lists[0], lists[1]));
#         lists.erase(lists.begin());
#         lists.erase(lists.begin());
#     }
#     return lists.front();
# }
# ListNode *mergeTwoLists(ListNode *l1, ListNode *l2) {
#     if(l1 == nullptr){
#         return l2;
#     }
#     if(l2 == nullptr){
#         return l1;
#     }
#     if(l1->val <= l2->val){
#         l1->next = mergeTwoLists(l1->next, l2);
#         return l1;
#     }
#     else{
#         l2->next = mergeTwoLists(l1, l2->next);
#         return l2;
#     }
# }