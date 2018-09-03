
# bash_tweet

bash script using python script to send tweet of image and or status update text.

## Getting Started
Example Status Update
```
tweet 'Your tweet here' 
```
Example Tweet Image
```
tweet 'Your image tweet here' /path/to/your/image.jpg
```

### Prerequisites

What things you need to install the software and how to install them

```
Python TwitterAPI
```

### Installing

A step by step series of examples that tell you how to get a development env running

Copy the bash and Python script to /usr/bin/

```
sudo mv ./tweet /usr/bin/tweet <br>
sudo mv ./tweet.py /usr/bin/tweet.py
```

Add folder and file for storing Twitter API key

```
mkdir ~/.tweet <br>
mv ./tweetkey.py ~/.tweet/tweetkey.py
```


