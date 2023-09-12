/*
// Definition for a Node.
class Node {
    int val;
    Node next;
    Node random;

    public Node(int val) {
        this.val = val;
        this.next = null;
        this.random = null;
    }
}
*/


// class Solution {
//     public Node copyRandomList(Node head) {
//         if (head == null) {
//             return null;
//         }

//         // Create a mapping between original nodes and their corresponding copied nodes
//         Map<Node, Node> map = new HashMap<>();

//         // Create a new dummy node to serve as the new list's head
//         Node newHead = new Node(-1);
//         Node current = newHead;

//         Node original = head;

//         // First pass: Create a copy of each node and populate the mapping
//         while (original != null) {
//             Node copy = new Node(original.val);
//             map.put(original, copy);
//             current.next = copy;
//             current = current.next;
//             original = original.next;
//         }

//         // Second pass: Update random pointers
//         original = head;
//         current = newHead.next; // Start from the beginning of the copied list

//         while (original != null) {
//             current.random = map.getOrDefault(original.random, null);
//             original = original.next;
//             current = current.next;
//         }

//         return newHead.next;
//     }
// }


class Solution {
    public Node copyRandomList(Node head) {
        Node current = head;
        Node front = null;
        
        while(current != null){
            front = current.next;
            Node copiedNode = new Node(current.val);
            current.next = copiedNode;
            copiedNode.next = front;
            current = front;
        }
        
        current = head;
        
        while(current != null){
            if(current.random != null){
                current.next.random = current.random.next;
            }
            current = current.next.next;
        }
        
        current = head;
        Node dummy = new Node(-1);
        Node temp = dummy;
        
        while(current != null){
            
            front = current.next.next;
            temp.next = current.next;
            current.next = front;
            current = current.next;
            temp = temp.next;
            // temp.next = null;
        }
        return dummy.next;
    }
}

