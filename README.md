# Docker-JiebaApi-Website

用 docker 包裝"結巴中文分詞",api website 化,直接 docker build&amp;run 就能使用

```
docker build --no-cache --force-rm -t jieba-api ./

docker run --name Web-JiebaApi -p 8080:8080 -e -d jieba-api
```

Usage:Http get or post

```
http://Web-JiebaApi/textrank?message=我這句要用textrank取出關鍵字，快來試試
http://Web-JiebaApi/extract?message=我這句要用TF/IDF取出關鍵字，快來試試
```

## 一键部署到云开发

可以使用 [CloudBase Framework](https://github.com/TencentCloudBase/cloudbase-framework) 一键部署到 Serverless 云应用上

```bash
cloudbase login
cloudbase framework:deploy -e YOUR_ENV_ID
```

然后根据命令行提示访问
