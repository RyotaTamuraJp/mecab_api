# Docker MeCab API

You can easily build the environment of MeCab + Neologd dictionary with Docker.  
In this Docker container there is a morphological analysis API written in Python's Flask.

## Description

You can build that environment with the following steps.

    $ docker build ./ -t [image name]
    $ docker run --name [container name] -p 5000:5000 -d [image name]


## Features

- This morphological analyzer can extract proper noun well.
- Refer to "request.py" in order to obtain the result of morphological analysis.

## Requirement

- RAM >= 8GB
- docker
- python >= 3.6

## Usage

1. Import the function from request.py
```python
from request import get_docker_mecab_result
```

2. The sentence to be analyzed is defined.
```python
text = "きゃりーぱみゅぱみゅ"
```

3. The URL is defined. The port was specified when I ran the Docker container.
```python
url = "http://localhost:5000/mecab_reply"
```

4. Get results.
```python
result = get_docker_mecab_result(text, url)
```

5. Print the result.
```python
print(result)
['きゃりーぱみゅぱみゅ\t名詞,固有名詞,人名,一般,*,*,きゃりーぱみゅぱみゅ,キャリーパミュパミュ,キャリーパミュパミュ']
# ['表層形\t品詞,品詞細分類1,品詞細分類2,品詞細分類3,活用型,活用形,原形,読み,発音']
```
