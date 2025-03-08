#include <stdio.h>
#include <stdlib.h>
#include <string.h>   
#include <ctype.h>
#include "newElement.h"

int main(){
	char *ptr = (char *)malloc(FILENAME_MAX);
	int q,e,token;
	int choice = -1;
	size_t size;
	double *arr = NULL;

Mark:
do{
	printf("1. Load array from file: \n");
	printf("2. Exit the program\n");
	printf("Select an item:");

	token = scanf("%d", &choice);
	if (token != 1){
		  if (getchar() == EOF){
			printf("\n");
			return 0;
		  }
		  printf("This is a symbol\n");
                  while ((q = getchar()) != '\n') 
			if(q == EOF) return 0;
		  continue;
        }

	switch (choice){
		case 1:
			 printf("Enter file name\n");
			 scanf(" ");
			 for (int i = 0; i < FILENAME_MAX; i++){
	       			 scanf("%c", &ptr[i]);
				 if (ptr[i] == '\n'){
                                        ptr[i] = 0;
					break;
				 }
			 }
		 	 FILE *file = fopen(ptr, "r");
		 	 if (file == NULL){
				perror("");
				break;
			 }
			 if ((fscanf(file, "%zu", &size) != 1)){
				printf("This is a symbol\n");
				fclose(file);
				break;
			 }
			 arr = (double *)realloc(arr, size * sizeof(double));
			 if (arr == NULL){
				perror("");
				fclose(file);
				break;
			 }
		 	 for (int i = 0; i < size; i++){
				if (fscanf(file, "%lf", &arr[i]) != 1){
					printf("This is a symbol\n");
					free(arr);
					arr = NULL;
					break;
				}
			 }
			 fclose(file);
	                 break;

		case 2:
			printf("Exiting...\n");
			free(ptr);
			return 0;
		default:
			 printf("Incorrect number\n");
			 break;

	}
}while (arr == NULL);

do{
	printf("===============MENU===============\n");
	printf("1. Load array from file\n");
	printf("2. Display the loaded array on the screen\n");
	printf("3. Find an element in an array\n");
	printf("4. Replace an element in an array\n");
	printf("5. Add an element to the end of the array\n");
	printf("6. Save the array to a file\n");
	printf("7. Exit the program\n");

	printf("Select an item:");

	token = scanf("%d", &choice);
        if (token != 1){
		 e = getchar();
		 if (e == EOF){
			printf("\n");
			return 0;
		 }
                 printf("This is a symbol\n");
                 while (getchar() != '\n');
                 continue;
            }

	switch (choice){
		case 1:
			printf("Enter file name\n");
			scanf(" ");
                        for (int i= 0; i < FILENAME_MAX; i++){
                                scanf("%c", &ptr[i]);
                                if (ptr[i] == '\n'){
					ptr[i] = 0;
                                        break;
                                }
                        }
			FILE *file = fopen(ptr, "r");
 		 	if (file == NULL){
		  	 	perror("");
		   		break;
			}
		 	if (fscanf(file, "%zu", &size) != 1){
				printf("This is a symbol\n");
				fclose(file);
				break;
			}
			size_t oldSize = size;
			double *oldarr = arr;
			arr = (double *)realloc(arr, size * sizeof(double));
			if (arr == NULL){
				perror("Error from rellocate array\n");
                                arr = oldarr;
				size = oldSize;
				fclose(file);
				break;
			}
			for (int i = 0; i < size; i++){
		 	   if (fscanf(file, "%lf", &arr[i]) != 1){
				perror("This is a symbol\n");
				free(arr);
				arr = NULL;
				fclose(file);
				goto Mark;
			   }
			}
			fclose(file);
			break;
		case 2:
		 	 for (size_t i = 0; i < size; i++){
				printf("%.2lf ", arr[i]);
		 	 }
		 	 printf("\n");
		 	 break;
		case 3:
			double n;
			printf("Enter the item you want to find:");
			if (scanf("%lf", &n) != 1){
				int c = getchar();
				if (c == EOF){
					printf("\n");
					return 0;
				}
				printf("This is a symbol\n");
       				while (getchar() != '\n');
        			continue;
			}
			searchElement(arr, size, n);
			break;
		case 4:
			size_t index;
			double tmp;
			printf("Enter the index of the element:");
			if (scanf("%zu", &index) != 1){
				int c = getchar();
				if (c == EOF){
					printf("\n");
					return 0;
				}
				printf("This is a symbol\n");
       				while (getchar() != '\n');
       				continue;
			}
			if (index > size){
				printf("Index out of array size\n");
				break;
			}
			printf("Enter the item:");
			if (scanf("%lf", &tmp) != 1){
				int c = getchar();
				if (c == EOF){
					printf("\n");
					return 0;
				}
				printf("This is a symbol\n");
       				while (c != '\n');
       				continue;
			}

			newElement(arr, size, index, tmp);
			break;
		case 5:
			double addtmp;
			printf("Enter a new element:");
			if (scanf("%lf", &addtmp) != 1){
				int c = getchar();
				if (c == EOF){
					printf("\n");
					return 0;
				}
				printf("This is a symbol\n");
    				while (getchar() != '\n');
       				continue;
			}
			addElement(&arr, &size, addtmp);
			break;
		case 6:
			FILE *file2 = fopen("newMassiv.txt", "w");
			if (file2 == NULL){
				perror("");
				break;
			}
			fprintf(file2, "%zu", size);
			for (size_t i = 0; i < size; i++){
				fprintf(file2, "%.2lf ", arr[i]);
			}
			printf("Successfully recorded\n");
			fclose(file2);

			break;
		case 7:
			printf("Exiting...\n");
			free(arr);
			free(ptr);
			break;
		default:
			printf("Incorrect number!\n");
			break;
	}

}while (choice != 7);

return 0;
}


