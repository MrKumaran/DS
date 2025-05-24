import java.util.Scanner;

class Node{
    int value;
    Node next;
}



class linkedList{
    Node Head;
    void add(int num){
        Node node = new Node();
        node.value = num;
        node.next = null;

        if(Head == null){
            Head = node;
        }
        else{
            Node n = Head;
            while(n.next != null){
                n = n.next;
            }
            n.next = node;
        }
    }

    void print(){
        Node node = Head;
        while(node.next!=null){
            System.out.println(node.value);
            node = node.next;
        }
        System.out.println(node.value);
    }
}

public class test{
    public static void main(String[] args) {
        linkedList ll = new linkedList();
        Scanner sc = new Scanner(System.in);
        for(int i = 1; i< 4; i++){
            int adding = sc.nextInt();
            ll.add(adding);
        }

        ll.print();
    }
}