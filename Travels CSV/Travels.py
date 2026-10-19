import csv
import random
from datetime import datetime,timedelta

#Output File Name
file_name="Travel_Tourism_Booking_100_Records.csv"

#Destinations
destinations=["Goa","Manali","Kashmir","Dubai","Bali","Singapore","Thailand","Maldives","Kerala","Shimla"]

#Package Types
package_types=["Family","Honeymoon","Adventure","Solo","Group"]

#Payment Modes
payment_modes=["Cash","UPI","Credit Card","Debit Card","Net Banking"]

#Booking Status
booking_status=["Confirmed","Pending","Cancelled"]

#Cities
cities=["Mumbai","Pune","Nashik","Jalgaon","Nagpur","Delhi","Ahmedabad","Surat"]

#Travel Agencies
travel_agencies=["Sky Travels","Dream Holidays","Happy Journey","Holidays Hub","Royal Tours"]

#Tour Guides
tour_guides=["Rahul","Amit","Sneha","Pooja","Rohit","Karan","Neha","Vikas"]

#First Names
first_names=["Aarav","Vivaan","Aditya","Arjun","Riya","Ananya","Sneha","Priya","Rahul","Rohan","Amit","Karan","Pooja","Neha","Meera","Ishita"]

#Last Names
last_names=["Sharma","Patel","Khan","Gupta","Joshi","Verma","Shaikh","Yadav","Pawar","Deshmukh"]

#Additional Lists
transport_types=["Flight","Train","Bus","Private Cab"]

hotel_ratings=["3 Star","4 Star","5 Star"]

meal_plans=["Breakfast","Breakfast+Dinner","All Meals"]

booking_sources=["Website","Mobile App","Agent","Office"]

insurance_options=["Yes","No"]

#Starting Date
start_date=datetime(2026,1,1)

with open(file_name,"w",newline="")as file:
    writer=csv.writer(file)

    #Header
    writer.writerow(["Booking ID","Customer Name","Destination","Package Type","Booking Date","Travel Date","Travelers","Package Cost","Discount","Final Amount","Payment Mode","Booking Status","Travel Agency","Tour Guide","City"])

    #Generate 100 Records
    for i in range(1,101):
        booking_id="BK"+str(1000+i)
        customer_name=random.choice(first_names)+""+random.choice(last_names)
        destination=random.choice(destinations)
        package=random.choice(package_types)
        booking_date=start_date+timedelta(days=random.randint(0,180))
        travel_date=booking_date+timedelta(days=random.randint(5,60))
        travelers=random.randint(1,6)
        package_cost=random.randint(15000,150000)
        discount=random.randint(1000,150000)
        final_amount=package_cost-discount
        payment=random.choice(payment_modes)
        status=random.choice(booking_status)
        agency=random.choice(travel_agencies)
        guide=random.choice(tour_guides)
        city=random.choice(cities)
        transport=random.choice(transport_types)
        hotel=random.choice(hotel_ratings)
        meal=random.choice(meal_plans)
        source=random.choice(booking_sources)
        insurance=random.choice(insurance_options)
        gst=round(final_amount*0.05,2)
        service_charge=random.randint(500,3000)
        grand_total=final_amount+gst+service_charge
        vip_customer=random.choice(["Yes","No"])
        loyalty_discount=0
        if vip_customer=="Yes":
            loyalty_discount=random.randint(500,3000)
            net_payable=grand_total-loyalty_discount
    #Write Complete Record
        writer.writerow([booking_id,customer_name,destination,package,booking_date.strftime("%d-%m-%Y"),travel_date.strftime("%d-%m-%Y"),travelers,package_cost,discount,final_amount,payment,status,agency,guide,city,transport,hotel,meal,source,insurance,gst,service_charge,grand_total,vip_customer,loyalty_discount,net_payable])

    #Program Completed
print("="*60)
print("Travel & Tourism Booking Management Systme")
print("="*60)
print("CSV File Name:",file_name)
print("Total Records:",100)
print("Status:Successfully Generated")
print("="*60)
print("CSV File Created Successfully.")
print("Thank You...")
                    
        
