### 依赖

- sqlite
- redis

### 部署
在本目录的上一级目录生成*newrelic.ini*文件，然后运行

```
cd notify # NOTE: 因为super.conf中用了相对路径，所以一定要进入super.conf文件中的目录
supervisord -c super.conf
```