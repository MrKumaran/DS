#include<stdio.h>
#include<stdlib.h>

struct Node{
  int val;
  struct Node *next;
};

struct Node *front,*rear = NULL;

void insert(int value);
int removeRear();

int main(void){
 int n = 4;
 for (size_t i = 0; i < n; i++) {
    int input;
    scanf("%d ",&input);
    insert(input);
  }
  for (size_t i = 0; i < n; i++) {
     int output = removeRear();
     printf("%d ",output);
   }
   printf("\n%d", removeRear());
  return 0;
}

void insert(int value){
  struct Node *ptr = malloc(sizeof(struct Node *));
  ptr->val = value;
  if(rear == NULL){
    rear = ptr;
    front = rear;
  }
  else{
    rear -> next = ptr;
    rear = ptr;
  }
}

int removeRear(){
  if(front == NULL){
    return -1;
  }
  struct Node *ptr = front;
  front = front->next;
  int op = ptr->val;
  free(ptr);
  return op;
}
