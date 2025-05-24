import java.util.Scanner;

class treeNode{
    int val;
    treeNode left;
    treeNode right;
    treeNode(int val){
        this.val = val;
        this.left = null;
        this.right = null;
    }
}

class tree{
    treeNode add(treeNode node, int val){
        if (node == null){
            return new treeNode(val);
        }
        if (node.val > val){
            node.left = add(node.left, val);
        }
        else {
            node.right = add(node.right, val);
        }

        return node;
    }

    void inorder(treeNode node){
        if (node == null){
            return;
        }
        inorder(node.left);
        System.out.println(node.val);
        inorder(node.right);
    }

    void postOrder(treeNode node){
        if (node == null){
            return;
        }
        postOrder(node.left);
        postOrder(node.right);
        System.out.println(node.val);
    }

    void preOrder(treeNode node){
        if (node == null){
            return;
        }
        System.out.println(node.val);
        preOrder(node.left);
        preOrder(node.right);
    }

    treeNode min(treeNode node){
        if (node.left == null){
            return node;
        }
        return min(node.left);
    }

    treeNode max(treeNode node){
        if (node.right == null){
            return node;
        }
        return max(node.right);
    }
}

class BStree{
    public static void main(String[] args) {
        treeNode root = null;
        tree treeOP = new tree();
        Scanner sc = new Scanner(System.in);
        for (int i = 0; i< 3; i++){
            root = treeOP.add(root, sc.nextInt());
        }
        System.out.println("\nInOrder\n");
        treeOP.inorder(root);
        System.out.println("\nPreOrder\n");
        treeOP.preOrder(root);
        System.out.println("\nPostOrder\n");
        treeOP.postOrder(root);
        System.out.println("\nMax:\n");
        System.out.println(treeOP.max(root).val);
        System.out.println("\nMin\n");
        System.out.println(treeOP.min(root).val);
    }
}