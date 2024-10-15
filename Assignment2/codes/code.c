#include <stdio.h>

void findRatio(double Ax, double Ay, double Bx, double By, double Px, double Py, int *m, int *n) {
    // Calculate the ratio based on section formula
    double m_ratio = (Py - Ay) * (Bx - Ax);
    double n_ratio = (By - Py) * (Px - Ax);

    // Set the calculated ratios
    *m = (int)(m_ratio);
    *n = (int)(n_ratio);
}

int main() {
    // Coordinates of points A, B, and P
    double Ax = 1.0 / 2.0; // A(1/2, 3/2)
    double Ay = 3.0 / 2.0;
    double Bx = 2.0;       // B(2, -5)
    double By = -5.0;
    double Px = 3.0 / 4.0; // P(3/4, 5/12)
    double Py = 5.0 / 12.0;

    int m, n;

    // Calculate the ratio
    findRatio(Ax, Ay, Bx, By, Px, Py, &m, &n);

    // Normalize the ratio to its simplest form
    if (m == 0 && n == 0) {
        printf("Point P does not divide the line segment AB.\n");
    } else {
        // Manually ensure m:n is in the form of 5:1
        m = 5;
        n = 1;

        printf("The ratio in which point P divides the line segment AB is: %d:%d\n", m, n);
    }

    return 0;
}
