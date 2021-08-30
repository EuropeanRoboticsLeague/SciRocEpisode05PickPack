import sciroc_episode05_logging

#Initialize the logger with team name 
sciroc_log = sciroc_episode05_logging.LogStatusSciRoc(team_name='AutonOHM')

#Logging start of run
sciroc_log.log_run_started()

#Logging object picked
sciroc_log.log_object_picked(object_name='Ocado Toasted Sesame Oil')

#Logging object placed
sciroc_log.log_object_placed(object_name='Ocado Toasted Sesame Oil')

#logging object dropped
sciroc_log.log_object_placed(object_name='DROPPED')

#logging run stopped
sciroc_log.log_run_stopped()


#object names:
'''
Ocado Bulgur Wheat & Couscous
Ocado Chick Peas in Water
Ocado Toasted Sesame Oil
Ocado Original Breadsticks
Ocado Ground Paprika
Ocado Sunflower Seeds
Ocado South American Roast & Ground Coffee
Ocado Antibacterial Multi Surface Cleaner Spray
Baby Ocado Ultra Soft Fragrance Free Wipes
Ocado Regular Soft Tissues
Ocado Plain Naan
'''
