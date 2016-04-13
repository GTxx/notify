### 依赖

- sqlite
- redis

### 部署
在本目录的上一级目录生成*newrelic.ini*文件，然后运行

```
supervisord -c super.conf
```