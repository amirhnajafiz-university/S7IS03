<h1 align="center">
  Malware
</h1>

<br />

Third project of Data Security course at CEIT/AUT. A simple malware to get users system information and send them to our server.

## Malware

To activate malware, execute the malware script by ```malware.py```. Make sure to set the ```HOST``` and ```PORT``` correctly. Malware
will send data about victim system information to the main server.

## Server

The server manages to handle the clients that run ```malware.py``` script on their system.<br />

To start server run the following command:

```
python server.py
```

No you can get the uesers information by the following commands:

| Command       | Description                             | Parameters  |
| :-----------: | --------------------------------------- | :---------: |
| ```sysinfo``` | Gets a user system information for you. | ```index``` |
| ```close```   | Close connection for a user.            | ```index``` |
| ```stats```   | Get a list of connected users.          | ```none```  |
| ```exit```    | Terminate server.                       | ```none```  |
