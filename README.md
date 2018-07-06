# Rapid-ChatXChannels
A rapid fire tutorial and introduction of Django Channels. To get more in-depth check out the full course https://kirr.co/badl8e


YouTube Video: __coming soon__



### Recommended Start
```

$ cd path/to/your/dev/folder
$ mkdir channels-rapid
$ cd channels-rapid
$ git clone https://github.com/codingforentrepreneurs/Rapid-ChatXChannels .
$ git reset 2a3f180b94d682efd30fd1d2a394a16bab1008a3 --hard
$ git remote remove origin
$ virtualenv -p python3 .
$ source bin/activate
(channels-rapid) $ cd src
(channels-rapid) $ pip install -r requirements.txt
(channels-rapid) $ python manage.py createsuperuser
... do the creation
(channels-rapid) $ python manage.py createsuperuser
... create second super user 
```


### Install Redis
1. Download Redis
    - Using [Homebrew](http://brew.sh):
        ```
        brew install redis

        brew services start redis
        ```
        Brew permission errors? Try `sudo chown -R "$USER":admin /usr/local`

    - Direct [Download](http://redis.io/download)

2. Open & Test Redis:
    - open Terminal

    - **redis-cli ping**
        ```
        $ redis-cli ping
        PONG
        ```

    - **redis-server**
        ```
        $ redis-server
        86750:C 08 Nov 08:17:21.431 # Warning: no config file specified, using the default config. In order to specify a config file use redis-server /path/to/redis.conf
        86750:M 08 Nov 08:17:21.433 * Increased maximum number of open files to 10032 (it was originally set to 256).
                        _._                                                  
                   _.-``__ ''-._                                             
              _.-``    `.  `_.  ''-._           Redis 3.2.5 (00000000/0) 64 bit
          .-`` .-```.  ```\/    _.,_ ''-._                                   
         (    '      ,       .-`  | `,    )     Running in standalone mode
         |`-._`-...-` __...-.``-._|'` _.-'|     Port: 6379
         |    `-._   `._    /     _.-'    |     PID: 86750
          `-._    `-._  `-./  _.-'    _.-'                                   
         |`-._`-._    `-.__.-'    _.-'_.-'|                                  
         |    `-._`-._        _.-'_.-'    |           http://redis.io        
          `-._    `-._`-.__.-'_.-'    _.-'                                   
         |`-._`-._    `-.__.-'    _.-'_.-'|                                  
         |    `-._`-._        _.-'_.-'    |                                  
          `-._    `-._`-.__.-'_.-'    _.-'                                   
              `-._    `-.__.-'    _.-'                                       
                  `-._        _.-'                                           
                      `-.__.-'                                               

        86750:M 08 Nov 08:17:21.434 # Server started, Redis version 3.2.5
        86750:M 08 Nov 08:17:21.434 * The server is now ready to accept connections on port 6379

        ```
        **Close Redis** with `control` + `c` to quit