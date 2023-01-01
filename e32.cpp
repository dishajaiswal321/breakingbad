#include<iostream> 
#include<cstdlib> 
using namespace std; 
class Pizzaria
{
int q[5], f, itemno, r; 
public:
Pizzaria()
{
f=r=-1;
}
void recieve(); 
void deliver(); 
void display();
void displayM();
};
void Pizzaria::recieve()//insertion in circular Q
{
cout<<"\nEnter order to be recieved: "; 
cin>>itemno;
if(((f==0)&&(r==4))||(f==r+1))//checking for overflow condition
{
}
else
{
cout<<"\n\nOverflow\n";
if(r==-1) //if R is pointing to null
{
r=f=0; //make it to point to first pos
}
else if(r==4) //if R is pointing to the end pos
{
r=0; //make R to point to first pos
}
else
{
r=r+1; //if R is pointing in the middle
} //increment R by 1 q[r]=itemno; //insert the itemno
cout<<"Order Recieved\n";
}
}
void Pizzaria:: deliver()//deletion in circular Q
{
if((f==-1)&&(r==0)) //if F is pointing to Null means no element
cout<<"\nUnderflow\n";
else
{
cout<<"Order No. "<<q[f]<<" Delivered\n"; 
if(f==4)
f=-1;
//if last element gets deleted f=-1; //then point F to the null
else if(f==r) 
f=r=-1;//else if only one element is there f=r=-1; //then make f&r to point to null
else
f=f+1;
}
}
void Pizzaria:: display()
{
if(f==-1)
cout<<"No Orders\n";
else{
if(r>=f)
{
cout<<"\nOrders are:\n"; for(int i=f;i<=r;i++)
cout<<q[i]<<"\n";
}
else
{
cout<<"\nOrders are:\n"; 
for(int i=f;i<=4;i++)
cout<<q[i]<<"\n"; 
for(int j=0;j<=r;j++)
cout<<q[j]<<"\n";
}
}
}
void Pizzaria:: displayM()
{ 
cout<<"\n\tMENU\n1.Margherita\n2.Pepperoni Pizza\n3.Mushroom Pizza\n4.Cloud\n5.Corn and Capsicum Pizza\n";
}
int main()
{
int n,i, no; 
Pizzaria p; 
do
{
cout<<"\nPress:\n1.Recieve an order\n2.Deliever an order\n3.Display Order Queue\n4.Display Menu.\n5.EXIT\n";
cin>>no; 
switch(no)
{
case 1:p.recieve(); 
break;
case 2:p.deliver(); 
break;
case 3:p.display(); 
break;
case 4:p.displayM(); 
break;
case 5:cout<<"\nEXITING. \n";
exit(1); 
break;
default:cout<<"\nINVALID CHOICE!!!!";
}
}while(1); 
return 0;
}

