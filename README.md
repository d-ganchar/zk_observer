## ZooKeeper observer

[![Build Status](https://api.travis-ci.org/d-ganchar/zk_observer.svg?branch=master)](https://travis-ci.org/d-ganchar/zk_observer.svg?branch=master)

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
    Run ZooKeeper and prepare demo data:
    
    ```
    docker run -d -p 2181:2181 zookeeper:3.4
    python prepare_data.py
    ```

1. 
    Run server
    ```
    python run.app
    ```
    
    open http://0.0.0.0:8000/
    
### You can run zk_observer in container

```
docker run -e "ZK_HOST=zk_host1:port,zk_host2:port" -e "ZK_ACL=path_r:password" -p 8000:8000 zk_observer
```