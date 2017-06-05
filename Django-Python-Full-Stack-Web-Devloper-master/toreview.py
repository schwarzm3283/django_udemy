#python
    #touples
    #lambda
    #OOP


    #list comprehension vs for loop
# SUITE = 'H D S C'.split()
# RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()
#     #list comprehension example#
# mycards = [(s,r) for s in SUITE for r in RANKS]
# print(mycards)
#     #for look example#
# mycards = []
# for r in RANKS:
#     for s in SUITE:
#         mycards.append((s,r))

######django
# Virtual env

#setup urls
# 1. create template directory under main project folder
# 2. add template directory to settings.py file (create variable and insert into template directory setting)
# 3. Create Templates (html files)
# 4. Create views (functions in the app views.py file)
# 5. update app urls to include pattern for new view
# 6. if not done update project urls to include app url pattern
# 7. create static folders
# 8. create static folder variable STATIC_DIR, and STATIC_DIRS list at bottom of settings.py
# 9. add {% load staticfiles %} under html doc in html pages
#10 add static tags {%   %} where desired

# creating databases
# 1. modify models.py file to create class for each table
# 2. run python manage.py migrate
# 3. run python manage.py makemigration (app_name)
# 4. run python manage.py migrate again
#
# geting admin up and Running
# 1. import models into admin.py
# 2. add (admin.site.register(model_name))) for each model
