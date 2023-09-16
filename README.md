# Api Daria Test 

The set of written tests includes API tests written with **Python** and the **PyTest** framework.


**Installation:**

    git clone repo

    cd project
    
    create ENV and active it:
        for win: 
            python -m venv env

        for linux: 
            virtualenv --python=python3 venv
            source venv/bin/activate

    install dependencies:
        pip install -r requirements.txt

    If the packages are installed in your system:
        virtualenv venv --system-site-packages

    run tests
        run without html report file:
            pytest

        run with html report file:
            pytest --html=<path file>report.html