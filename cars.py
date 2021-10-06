import pandas  as pd
import numpy as np # needed for avg hp of the dataframe

class cars:
    def read_the_csv(self):
        df = pd.read_csv (r'car_input1.txt') # text file fields are seperated by ',' = csv 
        return df

    def get_cars_above_AVG(self,avg_hp,df_cars_of_origin): # return dataframe of all the cars having horsepower > avg_hp
        total_cars =  df_cars_of_origin[ (df_cars_of_origin['Horsepower'] > avg_hp)]
        return total_cars

    # get the cars of a particular origin
    # finds the avg_horse_power
    # call to get cars having horsepower > avg_hp 
    # return dataframe of all the cars having horsepower > avg_hp
    def get_car_above_AVG_hp_of_origin(self,df_all_cars,origin): 
        df_car_containg_origin_only =   df_all_cars[df_all_cars['Origin']== origin ]  # get the cars of a particular origin
        avg_hp = np.average(df_car_containg_origin_only['Horsepower']) # finds the avg_horse_power using numpy(can be removed)
        df_cars_above_avg_hp = self.get_cars_above_AVG(avg_hp,df_car_containg_origin_only) # return dataframe of all the cars having horsepower > avg_hp
        return df_cars_above_avg_hp 

    # To convert the dataframe into a list and then print top N cars based on horsepower
    def cars_to_print(self,df_total_cars,N): 
        total_cars = df_total_cars.values.tolist()  # dataframe to list 
        total_cars.sort(key = lambda x:x[2] , reverse = True) # sort in descinding order based on hp
        
        
        #prints top N cars based on horsepower
        count = 0
        for name,origin,hp in total_cars:
            print(name,hp,origin)
            count+=1
            if count == N:
                break
       

    
if __name__ == '__main__':        
    ob = cars() 
    #origin = 'US' 
    #N = 10
    origin = input()
    N = int(input())
    '''
    run below command in terminal
    python cars.py Europe 10 
    '''
    
    df_all_cars = ob.read_the_csv()
    df_car_to_print = ob.get_car_above_AVG_hp_of_origin(df_all_cars,origin)
    ob.cars_to_print(df_car_to_print,N)



'''
Without classes
N = 10
origin = 'US'
import pandas  as pd
import numpy as np

df = pd.read_csv (r'car_input1.txt')
df_car_containg_origin_only =   df[df['Origin']==origin]
avg_hp = np.average(df_car_containg_origin_only['Horsepower'])

total_cars =  df[ (df['Horsepower'] > avg_hp) & (df['Origin']==origin ) ]

total_cars =  total_cars.values.tolist()
total_cars.sort(key = lambda x:x[2] , reverse = True)
#print(list_to_print) 
for x,y,z in total_cars[:N]:
    print(x,z,y)
    
'''    