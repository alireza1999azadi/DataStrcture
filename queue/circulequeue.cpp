#include <iostream>
using namespace std;

#define SIZE 4

class CircularQueue {
private:
    int items[SIZE];
    int front, rear;

public:
    CircularQueue() {
        front = -1;
        rear = -1;
    }

    bool isFull() {
        if (front == 0 && rear == SIZE - 1)
            return true;
        if (front == rear + 1)
            return true;
        return false;
    }

    bool isEmpty() {
        if (front == -1)
            return true;
        return false;
    }

    void enQueue(int element) {
        if (isFull()) {
            cout << "Queue is full" << endl;
        } else {
            if (front == -1)
                front = 0;
            rear = (rear + 1) % SIZE;
            items[rear] = element;
            cout << "Inserted " << element << endl;
        }
    }

    int deQueue() {
        int element;
        if (isEmpty()) {
            cout << "Queue is empty" << endl;
            return -1;
        } else {
            element = items[front];
            if (front == rear) {
                front = -1;
                rear = -1;
            } else {
                front = (front + 1) % SIZE;
            }
            cout << "Deleted: " << element << endl;
            return element;
        }
    }

    void display() {
        int i;
        if (isEmpty()) {
            cout << "Empty Queue" << endl;
        } else {
            cout << "Front index: " << front << endl;
            cout << "Items : ";
            for (i = front; i != rear; i = (i + 1) % SIZE)
                cout << items[i] << " ";
            cout << items[i] << endl;  
            cout << "Rear index: " << rear << endl;
        }
    }
};

int main() {
    CircularQueue cq;

    cq.deQueue();  

    cq.enQueue(5);
    cq.enQueue(7);
    cq.enQueue(6);
    cq.enQueue(1);
   

    cq.enQueue(8);

    cq.display();

    cq.deQueue();
    cq.display();

    cq.enQueue(2);
    cq.display();

    return 0;
}
