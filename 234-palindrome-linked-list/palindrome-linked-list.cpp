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
    bool isPalindrome(ListNode* head) {
        ListNode* temp = head;
        int count = 0;
        while(temp != NULL)
        {
            count++;
            temp = temp->next;
        }
        int arr[count];
        temp = head;

        for(int i = 0; i < count; i++)
        {
            arr[i] = temp->val;
            temp = temp->next;
        }

        // Compare from both ends
        for(int i = 0; i < count / 2; i++)
        {
            if(arr[i] != arr[count - 1 - i])
            {
                return false;
            }
        }
        return true;
    }
};