class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        old_node = head
        new_node = []

        while old_node:
            new_node.append(Node(old_node.val))
            old_node = old_node.next

        for i in range(len(new_node)-1):
            new_node[i].next = new_node[i + 1]
        
        old_node = head
        for i in range(len(new_node)):
            if old_node.random:
                index = 0
                temp = head
                while temp != old_node.random:
                    temp = temp.next
                    index += 1
                new_node[i].random = new_node[index]
            old_node = old_node.next
        return new_node[0]
        