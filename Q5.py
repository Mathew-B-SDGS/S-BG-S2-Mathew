### Question 5 ### 
'''

Write a function which expects, as its input, a dictionary, with names as the keys and ages as the values. The function passes back an dictionary of age sums for people aged 10-20, 20-30, and over 30.

example input_dictionary:
'''
age_dict1 = {
    'Hayden Brandt': 10,
    'Lydia Weiss': 13,
    'Jadyn Faulkner': 11,
    'Tatiana Ruiz': 20,
    'Francesca Burnett': 27,
    'James Olson': 30,
    'Aedan Russo': 32,
    'Shane Key': 55,
    'Cyrus Rodgers': 60,
    'Reina Pace': 81
}



def avg_age_func(age_dict):
    '''
    function takes a dict and returns the average age within each age category in a new dict
    '''
    # all the below are just empty variables. 
    age_10_20 = 0
    sum_age_10_20 = 0
    age_20_30 = 0
    sum_age_20_30 = 0
    age_over_30 = 0
    sum_over_30 = 0

    # loop over every value in dict, seeing if age value fits into each section. age added to a variable, counter then used to calculate average. 
    for key in age_dict:
        value = age_dict[key]
        if value >= 10 and value < 20:
            age_10_20 += 1
            sum_age_10_20 += value
        elif value >= 20 and value < 30:
            age_20_30 += 1
            sum_age_20_30 += value
        elif value >= 30:
            age_over_30 += 1
            sum_over_30 += value

    return_dict = {
        'avg10_20':sum_age_10_20/age_10_20,
        'avg20_39':sum_age_20_30/age_20_30,
        'avg_30':sum_over_30/age_over_30
                   }
    
    return(return_dict)

print(avg_age_func(age_dict1))


##

