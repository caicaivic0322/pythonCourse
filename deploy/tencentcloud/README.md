# 腾讯云 Ubuntu 部署说明

## 1. 服务器准备

- 系统：Ubuntu 22.04+
- 安全组放行：`22`、`80`（如需 HTTPS 再放行 `443`）

## 2. 安装 Docker

```bash
sudo apt update
sudo apt install -y ca-certificates curl gnupg
sudo install -m 0755 -d /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
sudo chmod a+r /etc/apt/keyrings/docker.gpg
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
  $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt update
sudo apt install -y docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
sudo usermod -aG docker $USER
newgrp docker
```

## 3. 拉取项目

```bash
git clone https://github.com/caicaivic0322/pythonCourse.git
cd pythonCourse
```

## 4. 准备生产环境变量

```bash
cp deploy/tencentcloud/.env.prod.example deploy/tencentcloud/.env.prod
```

请编辑 `deploy/tencentcloud/.env.prod`，至少修改：

- `POSTGRES_PASSWORD`
- `SECRET_KEY`
- `DJANGO_SUPERUSER_PASSWORD`
- 如果后续绑定域名，请同步更新 `ALLOWED_HOSTS`、`CORS_ALLOWED_ORIGINS`、`CSRF_TRUSTED_ORIGINS`

## 5. 启动服务

```bash
docker compose --env-file deploy/tencentcloud/.env.prod -f deploy/tencentcloud/docker-compose.prod.yml up -d --build
```

## 6. 查看状态与日志

```bash
docker compose -f deploy/tencentcloud/docker-compose.prod.yml ps
docker compose -f deploy/tencentcloud/docker-compose.prod.yml logs -f backend
```

## 7. 访问地址

- 前端：`http://124.156.184.244`
- 后台：`http://124.156.184.244/admin/`
- API：`http://124.156.184.244/api/`

## 8. 更新发布

```bash
git pull origin main
docker compose --env-file deploy/tencentcloud/.env.prod -f deploy/tencentcloud/docker-compose.prod.yml up -d --build
```
