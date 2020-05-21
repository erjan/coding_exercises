#include <stdio.h>
#include <string.h>
#include <stdlib.h>


#ifndef STRUCT_STRING_ARRAY
#define STRUCT_STRING_ARRAY
typedef struct s_string_array
{
    int size;
    char** array;
} string_array;
#endif


void my_print_words_array(string_array* param_1)
{
    int len = param_1->size;
    char **d = param_1->array;


    for(int i = 0 ; i < len;i++){
        printf("%s\n", d[i]);
    }
}

int main(){
    struct s_string_array *d = malloc(sizeof(string_array));;
    d->size = 2;
    char *r1 = "hello";
    char *r2 = "world";
    
    char **my_arr = (char *[]){"hello", "world"};


    d->array = my_arr;
    my_print_words_array(d);

    return 0 ;

}
