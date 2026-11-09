
def solve():

    class ListNode:
        def __init__(self, val=0, next=None):
            self.val = val
            self.next = next

    def addTwoNumbers(l1, l2):

        dummy = ListNode(0)
        current = dummy
        carry = 0

        while l1 or l2 or carry:

            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            total = v1 + v2 + carry

            digit = total % 10
            carry = total // 10

            current.next = ListNode(digit)
            current = current.next

            if l1:
                l1 = l1.next

            if l2:
                l2 = l2.next

        return dummy.next

   
    def create_list(values):
        dummy = ListNode()
        current = dummy

        for value in values:
            current.next = ListNode(value)
            current = current.next

        return dummy.next

    
    def to_list(head):
        result = []

        while head:
            result.append(head.val)
            head = head.next

        return result

    
    l1 = create_list([2, 4, 3])
    l2 = create_list([5, 6, 4])

    result = addTwoNumbers(l1, l2)

    assert to_list(result) == [7, 0, 8]

    return True


if __name__ == "__main__":
    solve()
