//采用封装函数，在 main里面调用
#include<iostream>
#include <stdio.h>
#include<ctime>
#include<stdlib.h>
using namespace std;
#define MAX 1000//方便维护数据 
void showmenu(); 
//联系人结构体
struct person
{
	string name;
	int sex;//1.男 2.女 
	int age;
	string phone;
	string location;
}; 
//设计通讯录结构体（数组 
struct personfiles
{
	struct person p[MAX];
	int size=0;//记录联系人个数 
}; 
void addperson(struct personfiles *psf);
void showperson(struct personfiles *psf);
int exist(personfiles *psf,string name);
void deleteperson(personfiles *psf);
void findperson(personfiles psf);
void modifyperson(personfiles *psf); 
void deleteall(personfiles *psf);
int main()
{       struct personfiles psf;
        int select=0;
        psf.size;
		psf.size=0; 
	while(true)
	{
	    //令通讯录初始化 
		showmenu();
		cout<<"请输入你想要的功能，输入数字"<<endl;
		cin>>select;
	//	cout<<select;
		switch(select)
		{
			case 1://添加 联系人，写结构体 
				addperson(&psf);//这是一个添加函数，通过指针修改通讯录 
				break;
			case 2://显示 
			    showperson(&psf); 
				break;
			case 3://删除 
				deleteperson(&psf);						
			case 4://查找 
			    findperson(psf);
				break;
			case 5://修改
			    modifyperson(&psf) ;
				break;
			case 6://清空 
			    deleteall(&psf);
				break;
			case 0://退出
			    cout<<"thank you for next come"<<endl;
				system("pause");
				return 0; //通过return0直接结束函数 
				break;	
		 } 
	 } 
	return 0;
 } 
 
 void showmenu()//写一个菜单显示函数,通过函数封装使其模块化 
 {  cout<<"**********************"<<endl;
 	cout<<"***  1.添加联系人  ***"<<endl; 
    cout<<"***  2.显示联系人  ***"<<endl;
 	cout<<"***  3.删除联系人  ***"<<endl;
 	cout<<"***  4.查找联系人  ***"<<endl;
 	cout<<"***  5.修改联系人  ***"<<endl;			
    cout<<"***  6.清空联系人  ***"<<endl;
    cout<<"***  0.退出联系人  ***"<<endl;
    cout<<"**********************"<<endl;//通过switch分支结构，来录入不同功能 
}
 void addperson(personfiles *psf)
 {  
    if(psf->size==MAX)
    {
    	cout<<"通讯录已满，无法再添加，将退回上一级"<<endl;   
		return ; 
    }
 	cout<<"输入你要添加的人的姓名"<<endl;
	string name;
	cin>>name;
	psf->p[psf->size].name=name;//这是姓名模块 
	cout<<"输入你要添加的人的性别"<<endl;
	cout<<"1.男*****2.女"<<endl;
	int sex;
	while(1)
	{  cin>>sex;
	   if(sex==1||sex==2)
	   {
		psf->p[psf->size].sex=sex;
		break;
	   } 
	 else
	 cout<<"输入有误，重新输入" <<endl ;//这是性别模块 
	}
	cout<<"输入你要添加的人的年龄"<<endl;
	int age;
	cin>>age;
	psf->p[psf->size].age=age;//年龄模块
	cout<<"输入你要添加的人的电话号码"<<endl;
	string  phone;
	cin>>phone;
	psf->p[psf->size].phone=phone;
	cout<<"输入你要添加的人的住址"<<endl;
	string location; 
	cin>>location;
	psf->p[psf->size].location=location;
	psf->size++;
	cout<<"你录入成功"<<endl; //录入信息
	system("pause");
	system("cls"); //清屏操作 	  
  } 
  void showperson(struct personfiles *psf)//显示模块 
  {
  	if(psf->size==0)
  	{
  		cout<<"empty"<<endl;
	  }
	else
	{
			for(int i=0;i<psf->size;i++)
  	{
  		cout<<"姓名"<<psf->p[i].name<<endl;
		if(psf->p[i].sex==1)
		{cout<<"性别"<<"男"<<endl;  } 
		 else{cout<<"性别"<<"女"<<endl; }
		 cout<<"年龄"<<psf->p[i].age<<endl;
		 cout<<"电话"<<psf->p[i].phone<<endl;
		 cout<<"住址"<<psf->p[i].location<<endl; 
	  }
	}
  	system("pause");
  	system("cls");
  }
  
//先封装检测联系人是否存在如果存在返回联系人在数组中的位置，不存在咋返回-1
int exist(personfiles *psf,string name)
{
	//遍历所有人名
	for(int i=0;i<psf->size;i++)
	{
		if(psf->p[i].name==name){
			return i;
		}
	
	 } 
	return -1;	
 } 
  
  
void deleteperson(personfiles *psf)//删除模块 ，按照姓名删除联系人 
{
	cout<<"输入你要删除的联系人"<<endl;
	string name;
	cin>>name;
	int ret=exist(psf,name); //这里的psf就是指一个指针，而不是一个结构体，所以不能写成&psf 
	if(ret==-1)
	{
		cout<<"查无此人"<<endl; 
	}
	else{
		//利用循环进行删除操作，再把size-1
		for(int i=ret;i<psf->size;i++)
		{   psf->p[i]=psf->p[i+1];	
		 } 
		 psf->size--;//更新通讯录中的人员数
		  cout<<"删除成功了"<<endl;
	} 	
	system("pause");
  	system("cls"); 	 
}
//封装查找联系人函数
void findperson(personfiles psf)
{
	cout<<"输出你要查找的联系人"<<endl;
	string name;
	cin>>name;
	int ret=exist(&psf,name); 
	if(ret!=-1)
	{   int i=ret;
	    cout<<"姓名"<<psf.p[i].name<<endl;
		if(psf.p[i].sex==1)
		{cout<<"性别"<<"男"<<endl;  } 
		 else{cout<<"性别"<<"女"<<endl; }
		 cout<<"年龄"<<psf.p[i].age<<endl;
		 cout<<"电话"<<psf.p[i].phone<<endl;
		 cout<<"住址"<<psf.p[i].location<<endl;	
	}
	else{cout<<"查无此人"<<endl;	
	}
	system("pause");
	system("cls");	
 } 
 //修改联系人
 void modifyperson(personfiles *psf)
 {
 	cout<<"输入你要修改的联系人"<<endl;
	  string name;
	  cin>>name;
	 int ret=exist(psf,name); //这里的psf就是指一个指针，而不是一个结构体，所以不能写成&psf 
	if(ret==-1)
	{
		cout<<"查无此人"<<endl; 
	}
	else{
	cout<<"输入新的姓名"<<endl;
	string name;
	cin>>name;
	psf->p[ret].name=name;//这是姓名模块 
	cout<<"输入新的性别"<<endl;
	cout<<"1.男*****2.女"<<endl;
	int sex;
	while(1)
	{  cin>>sex;
	   if(sex==1||sex==2)
	   {
		psf->p[ret].sex=sex;
		break;
	   } 
	 else
	 cout<<"输入有误，重新输入" <<endl ;//这是性别模块 
	}
	cout<<"输入新的年龄"<<endl;
	int age;
	cin>>age;
	psf->p[ret].age=age;//年龄模块
	cout<<"输入新的电话号码"<<endl;
	string  phone;
	cin>>phone;
	psf->p[ret].phone=phone;
	cout<<"输入新的住址"<<endl;
	string location; 
	cin>>location;
	psf->p[ret].location=location;
	cout<<"你录入成功"<<endl; //录入信息
	}system("pause");
	system("cls"); //清屏操作 
  } 
  //清空联系人模块--找不到
  void deleteall(personfiles *psf)
  {  srand((unsigned int)time(NULL));
  	psf->size=0;
  	cout<<"要输入正确三次随机数字才能完成清空选项"<<endl;
	 for (int i=1;i<4;i++)
	 {  int num=rand()%100+1; 
	 	cout<<"请输入这个数"<<num<<endl;
		 int input=0;
		 cin>>input;
		 if(input==num)
		 {
		 	cout<<"第"<<i<<"次输入正确"<<endl; 
		  } 
		  else{cout<<"清空操作撤销"<<endl;
		  system("cls");
		    return; 
		  }
	 }
  	cout<<"通讯录已清空"<<endl;
	 system("pause");
	 system("cls"); 
   } 
