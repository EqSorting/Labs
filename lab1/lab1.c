#include <stdio.h>
#include <math.h>
#include <stdlib.h>

int main(){
	double a, b, c, x1, x2;
	printf("Enter value a:");
	if (scanf("%lf", &a) != 1){
			printf("Not only numbers have been introduced\n");
			return 1;
	}
	printf("Enter value b:");
	if (scanf("%lf", &b) != 1){
		printf("Not only numbers have been introduced\n");
		return 1;
	}
	printf("Enter value c:");
	if (scanf("%lf", &c) != 1){
		printf("Not only numbers have been introduced\n");
		return 1;
	}

	if (a == 0 && b == 0 && c == 0){
			printf("Any x\n");
			return 0;
	}
	if (a == 0){
			if (b == 0){
				printf("No solution\n");
				return 0;
			}
			x1 = -c/b;
			printf("Root of the equation x1=%.1lf\n", x1);
			return 0;
	}


        double Dis = sqrt(pow(b, 2)-(4*a*c));
        if (Dis > 0){
                x1 = (-b + Dis)/(2*a);
                x2 = (-b - Dis)/(2*a);
        }
        else if (Dis == 0){
                x1 = -b/(2*a);
		x2 = -b/(2*a);
        }
        else {
                printf("There are no solutions!\n");
		return 0;
        }

	printf("Roots of the equation: x1 = %.1lf, x2 = %.1lf\n", x1, x2);
	return 0;

}
