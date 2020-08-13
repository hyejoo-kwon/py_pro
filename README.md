# py_pro

- ## tooltips
    - POSITIVE_INTEGER is 0~2147483647
    - delete db and reset? delet all migrations/*.py and *.pyc except __init__.py.
    - POSTIVE_INTEGER default null ? means not in a stock

- ## commands
    - ``./manage.py graph_models -a -g -o my_project_visualized.png``

- ## model_story_relation
    - AS:ANONUMOUS_USER
        1. visit index, see list of representational products,
            - ack: login and register button somewhere
            - ack: list of drinks is represtational not listing in detail.
            - dev_todo: show posts those likes aheads above them
            - user_todo
                - signin, signup
                - press single respresentational drink
                - press list-menu of drinks to filter or find something.
                - press post-menu to see how much these users are on active

        2. Press listpage of drinks
            - ack: default list is based on filter; a filter ``updated_at`` based.
            - ack: category_filter [default = all] select panel exists, ie) liqur, vodka, beer?
            - ack: ordering_filter [default = updated_at in descending] ie) price, likes, postscount, selling, updated_at
            - ack: keyword_seach_filter, [brand, product_name]
            - user_todo
                - find exact he likes to drink or for present to other,
                - 
            

