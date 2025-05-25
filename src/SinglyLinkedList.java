class Node {
    int data;
    Node next;

    Node(int data) {
        this.data = data;
        this.next = null;
    }
}

class SinglyLinkedList {
    Node head;

    void insertAtBegin(int data) {
        Node newNode = new Node(data);
        newNode.next = head;
        head = newNode;
    }

    void insertAtEnd(int data) {
        Node newNode = new Node(data);
        if (head == null) {
            head = newNode;
            return;
        }
        Node current = head;
        while (current.next != null) {
            current = current.next;
        }
        current.next = newNode;
    }

    void insertAtIndex(int index, int data) {
        if (index < 0) return;
        if (index == 0) {
            insertAtBegin(data);
            return;
        }
        Node newNode = new Node(data);
        Node current = head;
        for (int i = 0; current != null && i < index - 1; i++) {
            current = current.next;
        }
        if (current == null) return;
        newNode.next = current.next;
        current.next = newNode;
    }

    void deleteAtBegin() {
        if (head == null) return;
        head = head.next;
    }

    void deleteAtEnd() {
        if (head == null) return;
        if (head.next == null) {
            head = null;
            return;
        }
        Node current = head;
        while (current.next.next != null) {
            current = current.next;
        }
        current.next = null;
    }

    void deleteAtIndex(int index) {
        if (index < 0 || head == null) return;
        if (index == 0) {
            deleteAtBegin();
            return;
        }
        Node current = head;
        for (int i = 0; current.next != null && i < index - 1; i++) {
            current = current.next;
        }
        if (current.next == null) return;
        current.next = current.next.next;
    }

    void printList() {
        Node current = head;
        while (current != null) {
            System.out.print(current.data + " -> ");
            current = current.next;
        }
        System.out.println("null");
    }

    public static void main(String[] args) {
        SinglyLinkedList sll = new SinglyLinkedList();
        sll.insertAtBegin(2);
        sll.insertAtBegin(22);
        sll.insertAtBegin(222);
        sll.insertAtBegin(2222);
        sll.printList();
    }
}
