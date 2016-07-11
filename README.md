# Docker-JiebaApi-Website
用docker包裝"結巴中文分詞",api website化,直接docker build&amp;run就能使用


```
docker build --no-cache --force-rm -t jieba-api ./

docker run --name Web-JiebaApi -p 8080:8080 -e -d jieba-api
```

```
usage:
Http get or post

http://Web-JiebaApi/textrank?message=我這句要用textrank取出關鍵字，快來試試
http://Web-JiebaApi/extract?message=我這句要用TF/IDF取出關鍵字，快來試試
```
