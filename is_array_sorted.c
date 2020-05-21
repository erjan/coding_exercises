#this is an exercise from qwasar full stack bootcamp 2020. uploaded it cuz found a very intersting and repeating bug:

#copied 1 line of code and had i vs j in index:
  # for(int j = 0 ; j < len-1;j++){
  #          if(param_1->array[j] > param_1->array[j+1]){


#include <stdio.h>
#include <string.h>
#include <stdbool.h>

// #ifndef STRUCT_INTEGER_ARRAY
// #define STRUCT_INTEGER_ARRAY
// typedef struct s_integer_array
// {
//     int size;
//     int* array;
// } integer_array;
// #endif



bool my_is_sort(integer_array* param_1){
    int len = param_1->size;
    int i = 0;
    if(len == 0 || len == 1){
        //printf("length is short = 0 or 1\n");

        return true;
    }

    bool asc = false;
    bool desc = false;
    
    for(i = 0 ; i < len-1;i++){
        if( param_1->array[i] == param_1->array[i+1]){
            continue;
            }
        else if( param_1->array[i] > param_1->array[i+1]){
            desc = true;
            break;
            }
        else if( param_1->array[i] < param_1->array[i+1]){
            asc = true;
            break;
            }
    }

    if (asc){
        //printf("detected ascending\n");
    }
    else{
        //printf("detected descending\n");
    }
    if(asc){
        //printf("checking if its asc\n");
        for(int j = 0 ; j < len-1;j++){
            if(param_1->array[j] > param_1->array[j+1]){
                //printf("not ascending\n");
                return false;
            }
        }
    }
    else if(desc){        
        //printf("checking if its desc\n");
        for(int j = 0 ; j < len-1;j++){
            if(param_1->array[j] < param_1->array[j+1]){
                //printf("not descending\n");
                return false;
            }
        }
    }
    //printf("got here - it's sorted array\n");
    return true;
    }
    
// int main(){

//     struct s_integer_array erj;
//     int asc[4] = {4,7,0,3};
//     erj.size = 4;
//     erj.array = asc;
//     my_is_sort(&erj);
// }
