#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include "newElement.h"

void newElement(double *arr,size_t size, size_t index,double tmp){
     for (int i = 0; i <= size-1; i++){
	if (i == index){
		arr[index] = tmp;
	}
     }
     
     for (int i = 0; i < size; i++){
	printf("%.2lf ", arr[i]);
	}
	printf("\n");
}

void searchElement(double *arr, size_t size, double n){
	int flag = 0;
	for (size_t i = 0; i < size; i++){
		if (arr[i] == n){
			printf("%zu \n", i);
			flag = 1;
		}
	}
	if (flag == 0){
		printf("Element not found\n");
	}
}

void addElement(double **arr, size_t *size, double addtmp){
	double *oldarr = *arr;
	(*arr) = (double *)realloc(*arr, (*size+1) * sizeof(double));
	if (arr == NULL){
		perror("memory reallocated incorrectly\n");
		*arr = oldarr;
		return;
	}
	(*arr)[*size] = addtmp;
	++(*size);
	for (size_t i = 0; i < *size; i++){
		printf("%.2lf ", (*arr)[i]);
	}
	printf("\n");
}
