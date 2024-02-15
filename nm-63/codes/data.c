#include<stdio.h>
#include<math.h>
//linspace function
double* linspace(double start, double end, int number_of_divisions);

double *return_sine(double *array, double omega);
//sine function

int main()
{
    double* x_t;
    double t_start = 0;
    double t_end = 50;
    int number_of_divs = 100;
    double omega = ;
    double* t_values = linspace(t_start,t_end,number_of_divs);
    
    double* x_o_t = return_sine()
    return 0;

}

double* linspace(double start, double end, int number_of_divisions)
{
    double difference = 1/number_of_divisions;
    double array[number_of_divisions];
    for(int i =0;i<number_of_divisions+1;i++)
    {
        *(array+i) = start + i*difference;
    }
    return array;
}

double* return_sine(double *array, double omega)
{
    int length = sizeof(array)/sizeof(*array);
    double output[length];
    for(int i=0;i<length;i++)
    {
        *(output+i) = sin(*(array+i)*omega);
    }
    return output;
}
