#include <unistd.h>


int sastantua(int l);
void ft_putchar(char c);

void ft_putchar(char c)
{
    write(1, &c, 1);
}


int print_star(int c)
{
    char star;
    int i;

    star = '*';
    i = 1;

    while (i <= c)
    {
        ft_putchar(star);
        i++;
    }
       
}


int build_level(int row, int clm)
{
    int i;
    int j;
    int s;

    i = 0;
    j = 1;
    s = 0;
    
    while (i < row)
    {
        while(j < row - i)
        /*печатаем количество пробелов в каждой строке. пробелов будет каждый раз меньше чем в предыдущей строке
        */
        {
            ft_putchar(' ');
            j++;
        }
        s = s + 2;
        print_star(s);
        ft_putchar('\n');
        i++;
        j = 1;
        
    }
    
}


int sastantua(int level)
{
    int row;
    int clm;
    
    row = 3;
    clm = 7;
    
    while (level != 0)
    {
        build_level(row, clm);
        row++;
        level --;
    }
        
}

int main()
{
    sastantua(3);
    return 0;    
}

