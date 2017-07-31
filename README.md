### Description

Tiny service to monitoring ZooKeeper nodes

### How to deploy on local machine


1. 
    Clone repo and install packages:
    ```
    cd /tmp
    git clone https://github.com/d-ganchar/zk_observer.git
    
    cd zk_observer
    mkdir env
    virtualenv --python=python3.6 env/
    source env/bin/activate
    pip install -r requirements.txt
    ```

1. 
    Run server
    ```
    python run.app
    ```
    
    open http://0.0.0.0:8000/