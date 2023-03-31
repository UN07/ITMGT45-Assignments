#!/usr/bin/env python
# coding: utf-8

# In[1]:


'''
Sample data for Relationship Status below:
'''

social_graph = {
    "@bongolpoc":{"first_name":"Joselito",
                  "last_name":"Olpoc",
                  "following":[
                  ]
    },
    "@joaquin":  {"first_name":"Joaquin",
                  "last_name":"Gonzales",
                  "following":[
                      "@chums","@jobenilagan"
                  ]
    },
    "@chums" : {"first_name":"Matthew",
                "last_name":"Uy",
                "following":[
                    "@bongolpoc","@miketan","@rudyang","@joeilagan"
                ]
    },
    "@jobenilagan":{"first_name":"Joben",
                   "last_name":"Ilagan",
                   "following":[
                    "@eeebeee","@joeilagan","@chums","@joaquin"
                   ]
    },
    "@joeilagan":{"first_name":"Joe",
                  "last_name":"Ilagan",
                  "following":[
                    "@eeebeee","@jobenilagan","@chums"
                  ]
    },
    "@eeebeee":  {"first_name":"Elizabeth",
                  "last_name":"Ilagan",
                  "following":[
                    "@jobenilagan","@joeilagan"
                  ]
    },
}


# In[2]:


'''Module 4: Individual Programming Assignment 1
Parsing Data
This assignment covers your ability to manipulate data in Python.
'''

'''
Sample data for Relationship Status below:
'''


def relationship_status(from_member, to_member, social_graph):
    '''Relationship Status.
    15 points.
    Let us pretend that you are building a new app.
    Your app supports social media functionality, which means that users can have
    relationships with other users.
    There are two guidelines for describing relationships on this social media app:
    1. Any user can follow any other user.
    2. If two users follow each other, they are considered friends.
    This function describes the relationship that two users have with each other.
    Please see "assignment-4-sample-data.py" for sample data. The social graph
    will adhere to the same pattern.
    Parameters
    ----------
    from_member: str
        the subject member
    to_member: str
        the object member
    social_graph: dict
        the relationship data    
    Returns
    -------
    str
        "follower" if fromMember follows toMember,
        "followed by" if fromMember is followed by toMember,
        "friends" if fromMember and toMember follow each other,
        "no relationship" if neither fromMember nor toMember follow each other.
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    
    
       
    following = 0
    followed_by = 0
    status = ''
        
    for i in social_graph[from_member]['following']:
        if i == to_member:
            following += 1
        else:
            pass
    for i in social_graph[to_member]['following']:
        if i == from_member:
            followed_by += 1
        
    if following == 1 and followed_by == 1:
        status = 'Friends'
        
    elif following == 1 and followed_by == 0:
        status = 'Follower'
        
    elif following == 0 and followed_by == 1:
        status = 'Followed By'
        
    elif following == 0 and followed_by == 0:
        status = 'Not following each other'
        
    else:
        pass
    
    return status
    
    
relationship_status("@chums", "@jobenilagan", social_graph)


# In[3]:


'''
Sample data for Tic Tac Toe below:
'''

board1 = [
['X','X','O'],
['O','X','O'],
['O','','X'],
]

board2 = [
['X','X','O'],
['O','X','O'],
['','O','X'],
]

board3 = [
['O','X','O'],
['','O','X'],
['X','X','O'],
]

board4 = [
['X','X','X'],
['O','X','O'],
['O','','O'],
]

board5 = [
['X','X','O'],
['O','X','O'],
['X','','O'],
]

board6 = [
['X','X','O'],
['O','X','O'],
['X','',''],
]

board7 = [
['X','X','O',''],
['O','X','O','O'],
['X','','','O'],
['O','X','','']
]


# In[4]:


def tic_tac_toe(board):
    '''Tic Tac Toe. 
    15 points.
    Tic Tac Toe is a common paper-and-pencil game. 
    Players must attempt to successfully draw a straight line of their symbol across a grid.
    The player that does this first is considered the winner.
    This function evaluates a tic tac toe board and returns the winner.
    Please see "assignment-4-sample-data.py" for sample data. The board will adhere
    to the same pattern. The board may by 3x3, 4x4, 5x5, or 6x6. The board will never
    have more than one winner. The board will only ever have 2 unique symbols at the same time.
    Parameters
    ----------
    board: list
        the representation of the tic-tac-toe board as a square list of lists
    Returns
    -------
    str
        the symbol of the winner or "NO WINNER" if there is no winner
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    
    
    i = 0
    x = 0
    
    while i < 3: 
        horizontal = [j for j in board[i]]
        if len(set(horizontal)) == 1:
            winner = board[i][i]
            return winner
            break
        else:
            i += 1
            continue
    try:
        return winner
    except:
        pass
    
    while x < len(board):
        vertical = [y for y in zip(*board)]
        
        if len(set(vertical[x])) == 1:
            winner = vertical[x][0]
            return winner
            break
        else:
            x += 1
            continue
    
    try:
        return winner
    except:
        pass
    
    diagonal1 = [board[u][u] for u, v in enumerate(board)]
    diagonal2 = [board[(len(board)-1)-u][u] for u, v in enumerate(board)]
    
    if len(set(diagonal1)) == 1:
        winner = diagonal1[0][0]
    else:
        pass
    
    try:
        return winner
    except:
        pass
    
    
    if len(set(diagonal2)) == 1:
        winner = diagonal2[0][0]
        
    else:
        winner = 'NO WINNER'
    
    return winner
    

tic_tac_toe(board7)


# In[5]:


'''
Sample data for ETA below:
(from_stop, to_stop)
'''

legs = {
     ("upd","admu"):{
         "travel_time_mins":10
     },
     ("admu","dlsu"):{
         "travel_time_mins":35
     },
     ("dlsu","upd"):{
         "travel_time_mins":55
     }
}

legs2 = {
    ('a1', 'a2'): {
        'travel_time_mins': 10
    },
    ('a2', 'b1'): {
        'travel_time_mins': 10230
    },
    ('b1', 'a1'): {
        'travel_time_mins': 1
    }
}


# In[6]:


def eta(first_stop, second_stop, route_map):
    '''ETA. 
    20 points.
    A shuttle van service is tasked to travel along a predefined circlar route.
    This route is divided into several legs between stops.
    The route is one-way only, and it is fully connected to itself.
    This function returns how long it will take the shuttle to arrive at a stop
    after leaving another stop.
    Please see the sample data file in this same folder for sample data. The route map will
    adhere to the same pattern. The route map may contain more legs and more stops,
    but it will always be one-way and fully enclosed.
    Parameters
    ----------
    first_stop: str
        the stop that the shuttle will leave
    second_stop: str
        the stop that the shuttle will arrive at
    route_map: dict
        the data describing the routes
    Returns
    -------
    int
        the time it will take the shuttle to travel from first_stop to second_stop
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    
    estimated_minutes = 0
    
    while first_stop != second_stop:
        for i, j in legs.items():
            if i[0] == first_stop:
                estimated_minutes += j ["travel_time_mins"]
                first_stop = i [1]
                break
            else:
                pass
            
        
    return estimated_minutes
    

eta("dlsu","upd", legs)


# In[7]:


def eta(first_stop, second_stop, route_map):
    '''ETA. 
    20 points.
    A shuttle van service is tasked to travel along a predefined circlar route.
    This route is divided into several legs between stops.
    The route is one-way only, and it is fully connected to itself.
    This function returns how long it will take the shuttle to arrive at a stop
    after leaving another stop.
    Please see the sample data file in this same folder for sample data. The route map will
    adhere to the same pattern. The route map may contain more legs and more stops,
    but it will always be one-way and fully enclosed.
    Parameters
    ----------
    first_stop: str
        the stop that the shuttle will leave
    second_stop: str
        the stop that the shuttle will arrive at
    route_map: dict
        the data describing the routes
    Returns
    -------
    int
        the time it will take the shuttle to travel from first_stop to second_stop
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    
    estimated_minutes = 0
    
    while first_stop != second_stop:
        for i, j in legs2.items():
            if i[0] == first_stop:
                estimated_minutes += j ["travel_time_mins"]
                first_stop = i [1]
                break
            else:
                pass
            
        
    return estimated_minutes
    

eta("a1","b1", legs2)

