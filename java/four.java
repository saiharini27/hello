import java.util.*;
class four
{
public static void main(String[] args)
{
int c=0;
Scanner s=new Scanner(System.in);
System.out.println("enter n value");
int n=s.nextInt();
System.out.println("enter array values");
for( int i=0;i<n;i++)
int a[]=s.nextInt();
int a[]=new int[n];
for(int i=0;i<n;i++)
{
if(a[i]==4)
{
c=c+1;
}
}
System.out.println(c);
}
}


