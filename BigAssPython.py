# ******************************************************************
#  This program is to input the details of an Address book        *
#  Author: A.AEDY                                                 *
#  C++ Date: 25 / 2/ 96 - Python Date:  30 / 12/ 22               *
#  Version 1.5   *******DOS  / Python VERSION*******              *
# ******************************************************************

import sys
from typing import List

# ----------------These were the C++ include files-----------------
'''
 #include <iostream.h>
 #include <iomanip.h>  # setw() etc.
 #include <string.h>
 #include <stdio.h>
 #include <stdlib.h>
 #include <fstream.h>
 '''

temp0 = 4
temp1 = 40
temp2 = 50
temp3 = 20
temp4 = 30
temp5 = 40
temp6 = 30

dummy4 = [temp0]
name1 = [temp1]
address1 = [temp2]
sex1 = [temp3]
age1 = [temp4]
phone1 = [temp5]
birthday1 = [temp6]

Width = 22
minval = 1
maxval = 5
total = 200

number_entries = 0
exit_p = 0
users_choice = 0
users_choice2 = 0

name = [temp1]
address = [temp2]
sex = [temp3]
age = [temp4]
phone = [temp5]
birthday = [temp6]

book = [str(name), str(address), str(sex), str(age), str(phone), str(birthday)]

test_entry = {"name": 0, "address": 0, "sex": 0, "age": 0, "phone": 0, "birthday": 0}

#Address_book = [total]
Address_book = [test_entry]

# **************************  FUNCTION DECLARATION'S ***********************

# ***************************  credits_f FUNC  *****************************
def credits_f():
    print(" *************************************************** ")
    print(" *              ADDRESS BOOK PROGRAM               * ")
    print(" *           ---------------------------           * ")
    print(" *                 BY AIDAN AEDY                   * ")
    print(" *           DOS REGISTERED VERSION 1.5            * ")
    print(" *            LICENSED TO - AIDAN AEDY             * ")
    print(" *************************************************** ")
    print()
    print()


# **************************************************************************
#                            START OF MAIN FUNCTION                        *
# **************************************************************************


def main(users_choice):
    #	exit
    #	filein(number_entries)
    credits_f()
    if users_choice != 5:
        print("          *** Enter Your Choice of Menu ***")
        print("            -------------------------    ")
        print("          1.| To Add An Entry.")
        print("          2.| To Delete An Entry.")
        print("          3.| To Display All Entries.")
        print("          4.| To Goto Find Menu.")
        print("          5.| To Exit From The Program. ")
        print()
        print()
        #		menu(users_choice)
        menu(users_choice, exit_p)
    else:
        print("          Thank You For Using The ADDRESS BOOK..")
        print("          You Will Now Return To DOS.")
    # fileout (number_entries)


# ***************************   END MAIN FUNC. ! **************************


'''**************************************************************************
*                            ***     NOTE'S     ***                         *
* there should be these functions included in here:                         *
* Add_f - an entry into the Address book.                                     *
* remove - an entry                                                         *
* display an entry                                                          *
* find - entry for a named person; all entries for people of same birthday  *
* all persons with age in specified range; all entries for persons of phone *
* in specified range;                                                       *
*                                                                           *
**************************************************************************'''

'''**************************************************************************
*                            START OF MAIN MENU FUNC.                       *
**************************************************************************'''


def menu(users_choice, exit_p):  # to select one of the listed func.
    print("          Your Choice of Menu is:- #")
    print()
    users_choice = int(input())

    if users_choice == 1:
        Add_f(number_entries)  # dec of Add func
    elif users_choice == 2:
        pass
        main(users_choice=0)
        #Delete()  # dec of Delete func
    elif users_choice == 3:
        Display(number_entries)  # dec of Display func
    elif users_choice == 4:
        pass
        main(users_choice=0)
        #Find(users_choice2)  # dec of Find menu
    elif users_choice == 5:
        exit_p = 1
        print("          You Will Now Exit The Program")
        credits_f()
        credits()
    else:
        print("          You Have Made An Incorrect Choice")
        exit_p = 1


# **********************  END MAIN MENU FUNC. *********************




'''****************************************************************
**********************    Add_f Function       ********************
****************************************************************'''


def Add_f(number_entries):
    #	system("cls")
    print("****************************************************************")
    print()
    print()

    groo = (number_entries + 1)

    print("          Please input the persons details for:-")
    print("          Name, ", "Address, ", "Sex, ", "Age, ")
    print("          Phone Numbers ", "and Birthday. ")
    print("          This Is Entry # ", groo, " In Your Address Book.")
    print()
    print()

    '''__________________________________________________________
    				 THIS IS THE MAIN INPUT SECTION
    __________________________________________________________'''



    # area to test new dictionary instead of pointers



    def bar():
        print("          Name             -  : ")
        input(str(name1))
        test_entry[groo] = name1

    def foo():
        bar()

    foo()
    test_entry["name"]
    print("test_entry = ", test_entry[groo], [name], [name1])
    print("test_entry full = ", test_entry)
    print("address_book = ", Address_book[0], [name])
    # print("address_book full = ", Address_book)


    '''

    print("          Name             -  : ")
    input(str(name1))
    Address_book[number_entries], [name].extend(name1)
    print(Address_book[number_entries], [name])
    #	_strupr(Address_book[number_entries].name)

    print()
    print("          Address          -  : ")
    input(address1)
    Address_book[number_entries], [address].extend(address1)
    #	strcpy (Address_book[number_entries].Address, Address1)
    # DO NOT CONVERT THE E-MAIL Address AS IT IS CASE SENSITIVE !

    print()
    print("          Sex              -  : ")
    input(sex1)
    Address_book[number_entries], [sex].extend(sex1)
    #	strcpy (Address_book[number_entries].sex, sex1)
    #	_strupr(Address_book[number_entries].sex)

    print()
    print("          Age              -  : ")
    input(str(age1))
    Address_book[number_entries], [age].extend(age1)
    #	strcpy (Address_book[number_entries].age, age1)
    #	_strupr(Address_book[number_entries].age)

    print()
    print("          Phone Number     -  : ")
    input(str(phone1))
    Address_book[number_entries], [phone].extend(phone1)
    #	strcpy (Address_book[number_entries].phone, phone1)
    #	_strupr(Address_book[number_entries].phone)

    print()
    print("          Date of Birth    -  : ")
    input(str(birthday1))
    Address_book[number_entries], [birthday].extend(birthday1)
    #	strcpy (Address_book[number_entries].birthday, birthday1)
    #	_strupr(Address_book[number_entries].birthday)

    '''

    print()
    print("          You will now return to the MAIN MENU. ")
    print(number_entries)
    number_entries +=1
    print(number_entries)
    main(users_choice=0)
    return number_entries



# *****        END Add_f FUNC.    *****


''' this was Added to remove all but the basic functions() and I will change as I get things working'''

'''

def Delete():
#	int s
#	int loo
	
	dummy[50]
	find[50]
	findupr[50]
		
    print()
	input("Please Enter The Person's Name,")
	print()
	input(" Of The File You Want To Delete - ")
	input(find)
			
	strcpy (findupr, find)
	_strupr(findupr)
	for  (s=0s<=totals++)

			 
		 if (!strcmp(findupr, Address_book[s].name))  

			  loo = s

 	
	  for (loo<=number_entriesloo++)		

		  strcpy (Address_book[loo].name, dummy)
		  strcpy (Address_book[loo].Address, dummy)
		  strcpy (Address_book[loo].sex, dummy)
		  strcpy (Address_book[loo].age, dummy)
		  strcpy (Address_book[loo].phone, dummy)
		  strcpy (Address_book[loo].birthday, dummy)
		  int p=loo+1

		  strcpy (Address_book[loo].name, Address_book[p].name)
		  strcpy (Address_book[loo].Address, Address_book[p].Address)
		  strcpy (Address_book[loo].sex, Address_book[p].sex)
		  strcpy (Address_book[loo].age, Address_book[p].age)
		  strcpy (Address_book[loo].phone, Address_book[p].phone)
		  strcpy (Address_book[loo].birthday, Address_book[p].birthday)

	   if (loo=s)

			number_entries--
			fputs("-- The File Is Now Erased --", stdout)


	   if (loo!=s)

			fputs( "----- There Were No Files Deleted -----", stdout) 


	fputs( "You Are Now Returning To The Main Menu.", stdout)

#     ************ end of delete func. ***************

'''

# ************************************************************************
# ********************  Display Function   *******************************
# ************************************************************************

def Display (number_entries):
    poo = 0
    dummy = "Y/N"
    print("          ***   This is the ", poo+1, " entry stored in the data base.   ***")
    while poo <= number_entries:

        print("          Name          - ", Address_book[poo], [name])
        print("          Address       - ", Address_book[poo], [address])
        print("          Sex           - ", Address_book[poo], [sex])
        print("          Age           - ", Address_book[poo], [age])
        print("          Phone         - ", Address_book[poo], [phone])
        print("          Date of Birth - ", Address_book[poo], [birthday])
        print("          .......Are you ready for Another ?.......")
        input(str(dummy))
        poo = poo + 1
    else:
        print()
        print("          That was the last Entry.......")
        print("          You will now return to the MAIN MENU. ")
        poo = 0
        print()
    main(users_choice=0)
    print()
   

# ***********************    END DISPLAY FUNC.   **********************


main(users_choice)

'''

/*************************************************************************
*                                                                        *
*                           START OF FIND MENU FUNC.                     *
*                                                                        *
*************************************************************************/
 void Find (int users_choice2)
 
  {
	system("cls");	
	cout << endl << endl
		 << "*** Enter The Type Of Find You Require ***" << endl 
		 << "    ----------------------------------    " << endl << endl
		 << "1.| To Find A Named Entry." << endl << endl
		 << "2.| To Find Persons with A Particular Birthday." << endl << endl
		 << "3.| To Find Persons in An Age Range." << endl << endl
		 << "4.| To Find Persons With A Phone Number." << endl << endl
		 << "5.| To Exit From The Find Menu. " << endl << endl;

	cout << endl << "Your Choice of Find Menu is:- #";
	cin  >> users_choice2;
	cout << endl << endl;

		 switch (users_choice2)
	   { 
				
		   case 1:
				Named ();     //dec of Named func
				break;
				
		   case 2:
				Birthday ();  //dec of Birthday func
				break; 
		  
		   case 3:
				Age_range (); //dec of Age func
				break;

		   case 4:
				Phone ();
				break;
				
		   case 5:
				cout << " You are now going to exit the find menu ";
				break;
				
		   default:  cout << "You Have Made An Incorrect Choice" << endl;	 
	   }
 
	  system("cls");
  }//************************  END FIND MENU. *************************




/**********************************************************************
*                         START OF NAMED PERSON FUNC.                 *
**********************************************************************/

 void Named (void) 
 {  
	int s;
	int flew;
	char dummy [1];
	char find[50];
	char findupr[50];
		
		system("cls");
		fputs("Please Enter The Persons Name To Search For -  ",stdout);
		gets(find);
			
		strcpy (findupr, find);
		_strupr(findupr);
		for  (s=0;s<=number_entries;s++)
		   {
			 
			  if (!strcmp(findupr, Address_book[s].name))  
				{
					 cout << endl 
						  << endl << Address_book[s].name 
						  << endl << Address_book[s].Address
						  << endl << Address_book[s].sex 
						  << endl << Address_book[s].age 
						  << endl << Address_book[s].phone
						  << endl << Address_book[s].birthday
						  << endl << endl;                       
					  flew = 1;
				}
		   
		  }   
	  if (flew!=1)
		{
			cout << "There Were No Files Of That Name Found " << endl;
		}
	cout << "***---------- Are You Ready To Continue ? -----------***";
	cin >> dummy[1];
			
 }/***********************  END FIND NAME FUNC.  ***********************/



/************************************************************************
*                         START OF BIRTHDAY FUNC.                       *
************************************************************************/
  
 void Birthday (void)
 {
	int s;
	char dummy [1];
	char find[50];
	char findupr[50];
		
		system("cls");	
		fputs("Please Enter The Persons Birthday To Search For -  ",stdout);
		gets(find);
			
		strcpy (findupr, find);
		_strupr(findupr);
		for  (s=0;s<=number_entries;s++)
		   {
			 
			  if (!strcmp(findupr, Address_book[s].birthday))  
				{
					 cout << endl 
						  << endl << Address_book[s].name 
						  << endl << Address_book[s].Address
						  << endl << Address_book[s].sex 
						  << endl << Address_book[s].age 
						  << endl << Address_book[s].phone
						  << endl << Address_book[s].birthday
						  << endl << endl;                       
				}
		   
		  }   
	
	cout << "***---------- Are You Ready To Continue ? -----------***";
	cin >> dummy[1];
	system("cls");
 
 
 } //**********************  END OF BIRTHDAY FUNC. **********************
 
 
 
/************************************************************************
*                           START OF AGE RANGE FUNC.                    *
************************************************************************/
 
 void Age_range (void)
 {
	int s;
	char dummy [1];
	char find1[50];
	char find2[50];
	char findupr1[50];
	char findupr2[50];	
		system("cls");
		fputs("Please Enter The Age Range To Search For -  ",stdout);
		cout << endl;
		fputs("From ( lowest  # ) - ", stdout);
		gets(find1);
		cout << endl;
		fputs("To   ( highest # ) - ", stdout);
		gets(find2);
		cout << endl;
		strcpy (findupr1, find1);
		_strupr(findupr1);
		strcpy (findupr2, find2);
		_strupr(findupr2);

		for  (s=0;s<=number_entries;s++)
		  {
			 
		   if (strcmp(findupr1, Address_book[s].age)<0) 
			{
			
			 if (strcmp(findupr2, Address_book[s].age)>0) 
				{
					cout << endl 
						 << endl << "Name    - " << Address_book[s].name 
						 << endl << "Address - " << Address_book[s].Address
						 << endl << "Sex     - " << Address_book[s].sex 
						 << endl << "Age     - " << Address_book[s].age 
						 << endl << "Phone   - " << Address_book[s].phone
						 << endl << "Birthday- " << Address_book[s].birthday
						 << endl <<  endl;                       
				}
		   
		   
			}
		  
		  }   
	
	cout << "***---------- Are You Ready To Continue ? -----------***";
	cin >> dummy[1];
	system("cls");
 
  
 }//****************      END OF AGE RANGE FUNC.     **************** 



 
 /*******************************************************************
  *                     START OF PHONE # FUNC.                 *
  *******************************************************************/
 
 void Phone (void)
 {
	int s;
	char dummy [1];
	char find1[50];
	char findupr1[50];
		system("cls");	
		fputs("Please Enter The Phone Number To Search For -  ",stdout);
		cout << endl;
		fputs(" - ", stdout);
		gets(find1);
		cout << endl;
		strcpy (findupr1, find1);
		_strupr(findupr1);

		for  (s=0;s<=number_entries;s++)
		  {
			 
		   if (!strcmp(findupr1, Address_book[s].phone)) 
			{
			
			 if (!strcmp(findupr1, Address_book[s].phone)) 
				{
					cout << endl 
						 << endl << "Name    - " << Address_book[s].name 
						 << endl << "Address - " << Address_book[s].Address
						 << endl << "Sex     - " << Address_book[s].sex 
						 << endl << "Age     - " << Address_book[s].age 
						 << endl << "Phone   - " << Address_book[s].phone
						 << endl << "Birthday- " << Address_book[s].birthday
						 << endl <<  endl;                       
				}
		   
		   
			}
		  
		  }   
	
	cout << "***---------- Are You Ready To Continue ? -----------***";
	cin >> dummy[1];
	system("cls");
 
 }    /************  END OF  HEIGHT RANGE FUNC. *****************/
 
		  
		  
  //******************************************************************       
		  
  /***********************     FILE INPUT START     *****************/        
	   
  //******************************************************************     
		  
 void filein (int &number_entries)    //ifstream&z                                                            
  {                  
	   int dummy5;	   
	   fstream z;
	   z.open("\\BIGDOS.INI",ios::in);// open file for input.
	   z >> dummy5; // to input the number of records in file.
	   if (dummy5 >1)  // if there are any entries then input them.
	   {
	   z.getline (dummy4, temp1+10); // to correct error in input.
	
		 do { 
			
			z.getline( name1, temp1);
			strcpy (Address_book[number_entries].name, name1+16);
			_strupr(Address_book[number_entries].name);
	
			
			z.getline(Address1, temp2);   
			strcpy (Address_book[number_entries].Address, Address1+16);
			//DO NOT CONVERT THE E-MAIL Address AS IT IS CASE SENSITIVE !
						
			z.getline(sex1, temp3);
			strcpy (Address_book[number_entries].sex, sex1+16);
			_strupr(Address_book[number_entries].sex);

			
			z.getline( age1, temp4);
			strcpy (Address_book[number_entries].age, age1+16);
			_strupr(Address_book[number_entries].age);

			
			z.getline( phone1, temp5);
			strcpy (Address_book[number_entries].phone, phone1+16);
			_strupr(Address_book[number_entries].phone);

			
			z.getline( birthday1, temp6);
			strcpy (Address_book[number_entries].birthday, birthday1+16);
			_strupr(Address_book[number_entries].birthday);

			number_entries++;
			
			
		}
		while (number_entries<dummy5); 
	  }
  
  } /***************************************************************
	*                                                              *
	*                      END FILE IN FUNC.                       *
	***************************************************************/
   
	
	
	
   /*****************************************************************
   *                         START OF FILE OUT FUNC                 *
   *****************************************************************/
   
  void fileout (int &number_entries) 
  
	 { 
	
	ofstream g("\\BIGDOS.INI",ios::trunc,filebuf::openprot);
   
   int poo;
		g << number_entries << "             - # of Entries.";
   
   for (poo=0;poo<number_entries;poo++)
	{	
		
		g << endl << "Name          - " << Address_book[poo].name;

		g << endl << "Address       - " << Address_book[poo].Address;

		g << endl << "Sex           - " << Address_book[poo].sex;

		g << endl << "Age           - " << Address_book[poo].age;
		
		g << endl << "Phone         - " << Address_book[poo].phone;

		g << endl << "Date of Birth - " << Address_book[poo].birthday;
		
	}
} //***********************    END File Out FUNC.   ********************** 

'''



