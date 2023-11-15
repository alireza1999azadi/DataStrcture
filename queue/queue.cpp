#include <iostream>
#define SIZE 4

using namespace std;

class Queue {
   private:
  int items[SIZE], front, rear;

   public:
  Queue() {
    front = -1;
    rear = -1;
  }

  bool isFull() {
    if (front == 0 && rear == SIZE - 1) {
      return true;
    }
    return false;
  }

  bool isEmpty() {
    if (front == -1)
      return true;
    else
      return false;
  }

  void enQueue(int element) {
    if (isFull()) {
      cout << "Queue is full";
    } else {
      if (front == -1) front = 0;
      rear++;
      items[rear] = element;
      cout << endl
         << "Inserted " << element << endl;
    }
  }

  int deQueue() {
    int element;
    if (isEmpty()) {
      cout << "Queue is empty" << endl;
      return (-1);
    } else {
      element = items[front];
      if (front >= rear) {
        front = -1;
        rear = -1;
      }
      else {
        front++;
      }
      cout << endl
         << "Deleted :" << element << endl;
      return (element);
    }
  }

  void display() {
    int i;
    if (isEmpty()) {
      cout << endl
         << "Empty Queue" << endl;
    } else {
      cout << endl
         << "Front index: " << front;
      cout << endl
         << "Items : ";
      for (i = front; i <= rear; i++)
        cout << items[i] << "  ";
      cout << endl
         << "Rear index:" << rear << endl;
    }
  }
};

int main() {
  Queue barbari;

  barbari.deQueue();

  barbari.enQueue(1);
  barbari.enQueue(2);
  barbari.enQueue(3);
  barbari.enQueue(4);

  barbari.enQueue(5);

  barbari.display();

  barbari.deQueue();

  barbari.display();

  return 0;
}