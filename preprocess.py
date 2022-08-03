import joblib
import warnings
warnings.simplefilter(action='ignore')

def models(x):
    if x == '2 Series':
        return[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

    elif x == '3 Series':
        return[0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

    elif x == '4 Series':
        return[0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

    elif x == '5 Series':
        return[0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

    elif x == '6 Series':
        return[0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

    elif x == '7 Series':
        return[0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

    elif x == '8 Series':
        return[0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

    elif x == 'M2':
        return[0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

    elif x == 'M3':        
        return[0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

    elif x == 'M4':
        return[0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0]

    elif x == 'M5':
        return[0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0]

    elif x == 'M6':
        return[0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0]

    elif x == 'X1':
        return[0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0]

    elif x == 'X2':
        return[0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0]

    elif x == 'X3':
        return[0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0]

    elif x == 'X4':
        return[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0]

    elif x == 'X5':
        return[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0]

    elif x == 'X6':
        return[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0]

    elif x == 'X7':
        return[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0]

    elif x == 'Z3':
        return[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0]

    elif x == 'Z4':
        return[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0]

    elif x == 'i3':
        return[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0]

    elif x == 'i8':
        return[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1]

    else:
        return[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]



def transmissions(x):
    if x == 'Manual':
        return[1,0]
    elif x == 'Semi-Auto':
        return[0,1]
    else:
        return[0,0]



def fuelTypes(x):
    if x == 'Electric':
        return [1,0,0,0]
    elif x == 'Hybrid':
        return[0,1,0,0]
    elif x == 'Other':
        return[0,0,1,0]
    elif x == 'Petrol':
        return[0,0,0,1]
    else:
        return[0,0,0,0]




def User(data):
    
    year = data['year']
    mileage = data['mileage']
    tax = data['tax']
    mpg = data['mpg']
    engineSize = data['engineSize']
    model = models(data['model'])
    transmission = transmissions(data['transmission'])
    fuelType = fuelTypes(data['fuelType'])
    
    Final_Data= [year, mileage, tax, mpg, engineSize] + model + transmission + fuelType
    return Final_Data


# data =  {'year':2020, 'mileage':30000, 'tax':200, 'mpg':100, 'engineSize':4, 'model':'M4',
#          'transmission':'Manual', 'fuelType':'Petrol'}


# Final_Data  = User(data)
# print((Final_Data))
# print()
# print(len(Final_Data))

# model = joblib.load('Models/model.h5')
# scaler = joblib.load('Models/scaler.h5')

# Final_Data = scaler.transform([Final_Data])
# print(Final_Data)
# print(model.predict(Final_Data)[0])
