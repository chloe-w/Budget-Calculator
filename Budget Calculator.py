# template for "Stopwatch: The Game"
import simplegui

# define global variables
money = 0
city = 0
customer = 0
customer_population_level = 0

# number of employees
n_frontend_developer = 2
n_backend_developer = 2
n_app_devoper = 2
n_social_coordinator = 1
n_social_coordinator_assitant = 2
n_customer_service = 1
n_driver = 1
n_cofounder = 3

# salaries
s_frontend_developer = 4000
s_backend_developer = 4000
s_app_devoper = 4000
s_social_coordinator = 3200
s_social_coordinator_assitant = 2250
s_customer_service = 2250
s_driver = 3000
s_cofounder = 1000

# operating expenses
marketing = 0
delivery_compensation = 0
insurance = 0
rental = 2500

    
# event handlers for calculator with a store and operand
def output():
    """prints contents of store and operand"""
    print money

def clear():
    global money, city, customer,customer_population_level, n_frontend_developer,n_backend_developer
    global n_app_devoper, n_social_coordinator, n_social_coordinator_assitant, n_customer_service
    global n_driver, n_cofounder,s_frontend_developer,s_backend_developer, s_app_devoper, s_social_coordinator
    global s_social_coordinator_assitant, s_customer_service, s_driver, s_cofounder
    global marketing, insurance, rental, delivery_compensation
    money = 0
    city = 0
    customer = 0
    customer_population_level = 0
    n_frontend_developer = 2
    n_backend_developer = 2
    n_app_devoper = 2
    n_social_coordinator = 1
    n_social_coordinator_assitant = 2
    n_customer_service = 1
    n_driver = 1
    n_cofounder = 3
    s_cofounder = 1000
    marketing = 0
    delivery_compensation = 0
    insurance = 0
    rental = 2500

    
    
# define input handlers
def n_cities(t):
    global city, n_social_coordinator, n_social_coordinator_assitant, n_driver, rental, customer
    city = int(t)
    # change in number of employees
    n_social_coordinator = n_social_coordinator * city
    n_social_coordinator_assitant = n_social_coordinator * 2
    n_driver = n_driver * city
    rental = rental * city
    if customer <= 1000:
        n_driver = n_driver * city
    else:
        n_driver = 0
    
def customer(t):
    global customer_population_level, n_frontend_developer,n_backend_developer, n_app_devoper, n_customer_service
    global s_cofounder, marketing, insurance, delivery_compensation, customer
    customer = int(t)
    
    # change in customer population level
    if customer <= 300:
        customer_population_level = 1
    elif 300 < customer <= 1000:
        customer_population_level = 2
    elif 1000 < customer <= 5000:
        customer_population_level = 3
    elif 5000 < customer <= 10000:
        customer_population_level = 4
    elif 10000 < customer:
        customer_population_level = 5

    # change in number of employees
    n_frontend_developer = n_frontend_developer + (customer_population_level-1)/2
    n_backend_developer = n_backend_developer + customer_population_level-1
    n_app_devoper = n_app_devoper + customer_population_level-1
    if customer <= 1000:
        n_customer_service = n_customer_service
    else:
        n_customer_service = customer/1000 
    
    
    # change in salary of co_founder
    s_cofounder = s_cofounder * customer_population_level
    
    # change in marketing expenses
    if customer_population_level == 1:
        marketing = 8000
    elif customer_population_level == 2:
        marketing = 6000
    elif customer_population_level == 3:
        marketing = 4000
    elif customer_population_level >= 4:
        marketing = 1000

    
    # change in insurance expenses
    if customer_population_level == 1:
        insurance = 5000
    elif customer_population_level == 2:
        insurance = 5000
    elif customer_population_level == 3:
        insurance = 10000
    elif customer_population_level == 4:
        insurance = 10000
    elif customer_population_level == 5:
        insurance = 15000
        
    # change in delivery compensation
    delivery_compensation = 0.5 * customer
        
                
def total_money():
    global money, city, customer_population_level, n_frontend_developer,n_backend_developer 
    global n_app_devoper, n_social_coordinator, n_social_coordinator_assitant, n_customer_service
    global n_driver, n_cofounder,s_frontend_developer,s_backend_developer, s_app_devoper, s_social_coordinator
    global s_social_coordinator_assitant, s_customer_service, s_driver, s_cofounder
    global marketing, insurance, rental, delivery_compensation
    money = (n_frontend_developer * s_frontend_developer + 
            n_backend_developer * s_backend_developer +
            n_app_devoper * s_app_devoper +
            n_social_coordinator * s_social_coordinator +
            n_social_coordinator_assitant * s_social_coordinator_assitant +
            n_customer_service * s_customer_service +
            n_driver * s_driver +
            n_cofounder * s_cofounder +
            marketing + insurance + rental + delivery_compensation)
                
    output()


# define draw handler
def draw_handler(canvas):
    canvas.draw_text("The Estimated Budget is = $ "
                     + str(money),
                     [10,30], 12, "White")

# create frame
f = simplegui.create_frame("Budget Calculator", 200,200)

# register event handlers
f.add_input('Customer Population', 
                      customer, 50)
f.add_input('Number of Cities', n_cities, 50)
f.add_button("Calculate", total_money, 100)
f.add_button("Clear", clear, 100)
f.set_draw_handler(draw_handler)


# start frame
f.start()





