#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class RMS:
    def __init__(self,restaurant_name,menu):
        self.restaurant_name=restaurant_name
        self.menu=menu
        self.order_list=[]
        self.total_bill=0
        self.user_order=''
        self.amount_taken=0
        self.user_repeat=''
        
    def _str_(self):
        return (f'{restaurant_name} timing 11:00am - 11:00 pm')
    #coffee shop
    def welcome_user(self):
        #welcome user
        print(f'Welcome to the {restaurant_name}!')
        print('*'*30)
        
        

    def display_menu(self):
    
        #display menu
        print('Menu:')
        
        for i in self.menu:
            print(i.title(),self.menu[i])
        print('*'*30)

    def take_order(self):

        #take order
        self.user_order=input('Please place your order here:')

    def preparing_drink(self):

        #prepare drink
        import time
        print(f'Preparing your {self.user_order.title()}!')
        time.sleep(3)
        self.order_list.append(self.user_order.lower())
        self.total_bill=self.total_bill+self.menu[self.user_order.lower()]

    def serve_order(self):
        #serve order
        print(f'Here is you order: {self.user_order.title()}')
        
    def display_bill(self):
        #display bill
        #bill=menu[user_order.lower()]
        print(f'Your total bill: {self.total_bill}')


    def verify_payment(self):
        self.amount_taken=int(input(f'Please pay your bill here:'))
        while self.amount_taken<self.total_bill:
            #take money
            print('Payment failed!')
            self.total_bill=self.total_bill-self.amount_taken
            self.amount_taken=int(input(f'Please pay your remaining {self.total_bill} here:'))


        if self.amount_taken>self.total_bill:
            print(f'Here is your change {self.amount_taken-self.total_bill}')
        else:
            pass
    def thank_you(self):
        #thank you
        print(f'Thank you for visiting {restaurant_name}!')


    def repeat_order(self):
        self.take_order()
        if self.user_order.lower() in self.menu:
            self.preparing_drink()
            self.serve_order()
        else:
            print('Invalid order!')
            self.repeat_order()

    def order_process(self):
        self.display_menu()
        self.take_order()
        if self.user_order.lower() in self.menu:
            self.preparing_drink()
            self.serve_order()
            self.user_repeat=input('Do you want to order again?')
            while self.user_repeat.lower()=='yes':
                self.repeat_order()
                self.user_repeat=input('Do you want to order again?')
            self.display_bill()
            self.verify_payment()
            self.thank_you()
        else:
            print("Invalid Order")
            self.order_process()



restaurant_name='Midnight Snacks!'
menu={'pizza':700,'burger':400,'maggie':200,'french fries':350,'pasta':200}

'''
if __name__=='__main__':
    ms=RMS(restaurant_name,menu)
    ms.welcome_user()
    ms.order_process()'''

if __name__ == '__main__':
    ms_res=RMS(restaurant_name,menu)
    
    import tkinter as tk
    window=tk.Tk()
    window.geometry("500x500")
    window.title(ms_res.restaurant_name)
    window.
    #window.button(window,text='MENU',command=ms_res.menu,height=2,width=18).place(x=150,y=160)
    window.mainloop()


# In[ ]:





# In[ ]:





# In[1]:


class RMS:
    def __init__(self,restaurant_name,menu):
        self.restaurant_name=restaurant_name
        self.menu=menu
        self.order_list=[]
        self.total_bill=0
        self.user_order=''
        self.amount_taken=0
        self.user_repeat=''
        self.data_li=[]
        
    def _str_(self):
        return (f'{restaurant_name} timing 11:00am - 11:00 pm')
    #coffee shop
    def welcome_user(self):
        #welcome user
        print(f'Welcome to the {restaurant_name}!')
        print('*'*30)

    def display_menu(self):
    
        #display menu
        print('Menu:')
        
        for i in self.menu:
            print(i.title(),self.menu[i])
        print('*'*30)

    def take_order(self):

        #take order
        self.user_order=input('Please place your order here:')

    def preparing_drink(self):

        #prepare drink
        import time
        print(f'Preparing your {self.user_order.title()}!')
        time.sleep(3)
        print(self.user_order)
        self.order_list.append(self.user_order.lower())
        self.total_bill=self.total_bill+self.menu[self.user_order.lower()]

    def serve_order(self):
        #serve order
        print(f'Here is you order: {self.user_order.title()}')
        
    def display_bill(self):
        #display bill
        #bill=menu[user_order.lower()]
        print(f'Your total bill: {self.total_bill}')


    def verify_payment(self):
        self.amount_taken=int(input(f'Please pay your bill here:'))
        while self.amount_taken<self.total_bill:
            #take money
            print('Payment failed!')
            self.total_bill=self.total_bill-self.amount_taken
            self.amount_taken=int(input(f'Please pay your remaining {self.total_bill} here:'))


        if self.amount_taken>self.total_bill:
            print(f'Here is your change {self.amount_taken-self.total_bill}')
        else:
            pass
    def thank_you(self):
        #thank you
        print(f'Thank you for visiting {restaurant_name}!')
        import datetime
        import pandas as pd
        df=pd.read_excel('res_save_file.xlsx')
        current_date=(datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S'))
        self.data_li.append(self.order_list)
        self.data_li.append(self.total_bill)
        self.data_li.append(current_date)
        num=len(df)
        df.loc[num]=(self.data_li)
        df.to_excel('res_save_file.xlsx',index=False)

    def repeat_order(self):
        self.take_order()
        if self.user_order.lower() in self.menu:
            self.preparing_drink()
            self.serve_order()
        else:
            print('Invalid order!')
            self.repeat_order()

    def order_process(self):
        #zself.display_menu()
        self.take_order()
        if self.user_order.title() in self.menu:
            self.preparing_drink()
            self.serve_order()
            self.user_repeat=input('Do you want to order again?')
            while self.user_repeat.lower()=='yes':
                self.repeat_order()
                self.user_repeat=input('Do you want to order again?')
            self.display_bill()
            self.verify_payment()
            self.thank_you()
        else:
            print("Invalid Order")
            self.order_process()





if __name__=='__main__':
    user_input=open('user_input.txt','r')
    user_input_li=user_input.readlines()
    restaurant_name=user_input_li[0].replace('\n','')
    menu_items=(user_input_li[1]).replace('\n','').split(',')
    menu_prices=(user_input_li[2]).split(',')
    menu_prices=[int(i) for i in menu_prices] 
    menu=dict(zip(menu_items,menu_prices))
    ms_res=RMS(restaurant_name,menu)

    import tkinter as tk
    window=tk.Tk()
    window.geometry('500x500')
    window.title(ms_res.restaurant_name)
    tk.Label(window,text=ms_res.restaurant_name,font=('Helvetica',18)).place(x=150,y=30)
    tk.Button(window,text='Place Order Here',command=ms_res.order_process).place(x=180,y=100)
    window.mainloop()

