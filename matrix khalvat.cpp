#include <iostream>
#include <iomanip>
#include <vector>

using namespace std;

vector<vector<double>> generateHilbertMatrix(int n) {
    vector<vector<double>> hilbertMatrix(n, vector<double>(n, 0.0));

    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            hilbertMatrix[i][j] = 1.0 / (i + j + 1);
        }
    }

    return hilbertMatrix;
}

void printMatrix(const vector<vector<double>>& matrix) {
    for (const auto& row : matrix) {
        for (double element : row) {
            cout << setw(8) << element << " ";
        }
        cout << endl;
    }
}

int main() {
    int n;

    cout << "Enter the size of the Hilbert matrix (n x n): ";
    cin >> n;

    if (n <= 0) {
        cout << "Invalid size. Please enter a positive integer." << endl;
        return 1; 
    }

    vector<vector<double>> hilbertMatrix = generateHilbertMatrix(n);
    
    cout << "Hilbert matrix of size " << n << " x " << n << " is:" << endl;
    printMatrix(hilbertMatrix);

    return 0;
}
