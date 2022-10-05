# Test_task_Prodly

How To Run Tests
----------------

1) Install all requirements:

    ```bash
    pip3 install -r requirements
    ```


2) Run tests:

    ```bash
    python3 -m pytest -v --driver Chrome --driver-path ~/chrome tests/*
   
   or
   
    pytest {path_test} -v --html=Reports/reports.html 
    
    or
    
    Run Tests in parallel
    pytest {path_test} -v -n 4 --html=Reports/reports.html 
    ```
