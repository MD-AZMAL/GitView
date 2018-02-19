from script import * # import the class User


Az = User('MD-AZMAL') # User object
Az.user_details() # display user details
Az.user_repos() # display repository details


# Testing on other users

Dan = User('shiffman')
Dan.user_details()
Dan.user_repos()
