#include <stdio.h>
#include <stdlib.h>

int main ()
{
    //char *x = new char[100];
    int *a;
    int *c;
    int b[10];
    a  = new int[2];
    //c = new int[2];
    //int a[2]; // even this is not giving error
    //c = a;
    a[0] = 1000;
    // a[100] = 4;
    b[100] = 10;
    b[4] = 15;
    b[3] = 25;
printf ("Hello World\n");
printf("%d %d\n", a[0],b[5]); //the value for b[5] has never been assigned before
printf("%d\n",b[100]);

if (b[5]<2) b[4] = 5;
   delete [] a;
   //delete[] c;  
   return 0;
}
