// Problem: https://leetcode.com/problems/swap-nodes-in-pairs
// Runtime: 3 ms

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* swapPairs(struct ListNode* head) {
    int index = 0;
    struct ListNode* ret = head;
    struct ListNode* last = NULL;
    struct ListNode* prev = NULL;
    struct ListNode* curr = head;
    struct ListNode* next = NULL;
    while (curr != NULL) {
        // printf("%d\n", curr->val);
        next = curr->next;
        if (index % 2 == 1) {
            prev->next = curr->next;
            curr->next = prev;
            if (last != NULL) {
                last->next = curr;
            }
            last = prev;
            if (index == 1) {
                ret = curr;
            }
        }
        prev = curr;
        curr = next;
        index++;
    }
    return ret;
}