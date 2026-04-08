# PyMaster 线上更新 SOP

## 适用范围

适用于以下线上更新场景：

- 后端代码更新
- 前端页面更新
- 课程种子数据更新
- 课程去重、课程结构调整

---

## 0. 更新前原则

### 原则 1：先拉代码，再执行脚本

永远先执行：

```bash
cd /root/Python_Course
git pull origin main
```

不要在旧代码版本上执行 `seed_gesp_courses.py` 或 `dedupe_courses.py`。

### 原则 2：所有后端脚本都必须加载生产环境

生产环境使用 Postgres，不要让脚本回退到本地 sqlite。

所有后端脚本执行前固定使用：

```bash
cd /root/Python_Course/backend
source venv/bin/activate
set -a
source /root/Python_Course/backend/.env.prod
set +a
```

然后再执行：

- `python seed_gesp_courses.py`
- `python dedupe_courses.py ...`
- `python manage.py ...`

### 原则 3：后端改动和前端改动分开看

- 只有后端接口、解锁逻辑、课程数据变化：重启 `pymaster`
- 有前端页面、练习区、样式改动：重新构建并发布前端

---

## 1. 标准更新流程

### 1.1 只更新后端逻辑

例如：

- 解锁逻辑优化
- API 修复
- Django 配置修复

执行：

```bash
cd /root/Python_Course
git pull origin main

cd /root/Python_Course/backend
source venv/bin/activate
set -a
source /root/Python_Course/backend/.env.prod
set +a

sudo systemctl restart pymaster
sudo systemctl status pymaster --no-pager -l | head -n 30
```

### 1.2 更新课程种子数据

例如：

- 新增课程
- 新增章节
- 调整课程描述
- 增加题目

执行：

```bash
cd /root/Python_Course
git pull origin main

cd /root/Python_Course/backend
source venv/bin/activate
set -a
source /root/Python_Course/backend/.env.prod
set +a

python seed_gesp_courses.py
sudo systemctl restart pymaster
```

执行后建议验证：

```bash
python - <<'PY'
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
import django
django.setup()
from courses.models import Course

for c in Course.objects.order_by('order', 'id'):
    print(c.id, c.order, c.title)
PY
```

### 1.3 更新前端页面

例如：

- 课程详情页
- 课程中心
- 练习区
- 样式和交互

执行：

```bash
cd /root/Python_Course
git pull origin main

cd /root/Python_Course/frontend
npm install
npm run build
rm -rf /var/www/pymaster/frontend
cp -r dist /var/www/pymaster/frontend
chown -R www-data:www-data /var/www/pymaster/frontend
sudo systemctl restart nginx
```

### 1.4 同时更新后端课程与前端页面

这是最常见的完整流程：

```bash
cd /root/Python_Course
git pull origin main

cd /root/Python_Course/backend
source venv/bin/activate
set -a
source /root/Python_Course/backend/.env.prod
set +a
python seed_gesp_courses.py
sudo systemctl restart pymaster

cd /root/Python_Course/frontend
npm install
npm run build
rm -rf /var/www/pymaster/frontend
cp -r dist /var/www/pymaster/frontend
chown -R www-data:www-data /var/www/pymaster/frontend
sudo systemctl restart nginx
```

---

## 2. 重复课程清理 SOP

### 2.1 先查重复课程

```bash
cd /root/Python_Course/backend
source venv/bin/activate
set -a
source /root/Python_Course/backend/.env.prod
set +a

python - <<'PY'
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
import django
django.setup()
from courses.models import Course

qs = Course.objects.filter(title='GESP 2级：逻辑进阶').order_by('id')
print('count =', qs.count())
for c in qs:
    print('id=', c.id, 'order=', c.order, 'desc=', c.description[:80])
    print('chapters=', c.chapters.count())
    print('---')
PY
```

### 2.2 先预览，再执行

假设保留课程 `id=8`：

预览：

```bash
python dedupe_courses.py --title "GESP 2级：逻辑进阶" --keep-id 8
```

正式执行：

```bash
python dedupe_courses.py --title "GESP 2级：逻辑进阶" --keep-id 8 --apply
sudo systemctl restart pymaster
```

### 2.3 清理后验证

```bash
python - <<'PY'
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
import django
django.setup()
from courses.models import Course

qs = Course.objects.filter(title='GESP 2级：逻辑进阶').order_by('id')
print('count =', qs.count())
for c in qs:
    print('id=', c.id, 'order=', c.order, 'chapters=', c.chapters.count())
PY
```

---

## 3. 故障排查 SOP

### 3.1 网站看不到新增课程

按顺序检查：

1. 是否已经 `git pull`
2. 是否执行了 `python seed_gesp_courses.py`
3. 执行脚本前是否加载了 `.env.prod`
4. 数据是否真的进了生产库

验证命令：

```bash
cd /root/Python_Course/backend
source venv/bin/activate
set -a
source /root/Python_Course/backend/.env.prod
set +a

python - <<'PY'
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
import django
django.setup()
from courses.models import Course

for c in Course.objects.order_by('order', 'id'):
    print(c.id, c.order, c.title)
PY
```

### 3.2 页面显示“未找到该课程”

先不要立刻判断为课程不存在。现在前端已经区分错误状态，但仍建议按顺序检查：

1. 是否已登录
2. 后端接口是否返回 401 / 403 / 404 / 500
3. 数据库中该课程 id 是否存在
4. 前端是否重新构建部署

### 3.3 API 返回 400

优先检查：

- `ALLOWED_HOSTS`
- `CORS_ALLOWED_ORIGINS`
- `CSRF_TRUSTED_ORIGINS`
- `pymaster.service`
- `.env.prod`

### 3.4 后端脚本更新错库

如果你执行：

```bash
echo "DATABASE_URL=$DATABASE_URL"
```

发现是空值，说明脚本会回退到 sqlite。  
这时不要继续执行任何种子脚本，必须先：

```bash
set -a
source /root/Python_Course/backend/.env.prod
set +a
```

---

## 4. 生产环境固定约定

### 4.1 后端环境文件

固定使用：

```bash
/root/Python_Course/backend/.env.prod
```

### 4.2 systemd 服务

`pymaster.service` 应使用：

```ini
EnvironmentFile=/root/Python_Course/backend/.env.prod
```

### 4.3 不再手动裸跑生产脚本

以后不要在没加载环境的情况下直接执行：

```bash
python seed_gesp_courses.py
python dedupe_courses.py
python manage.py ...
```

---

## 5. 每次上线前的最小检查清单

### 后端

- 已执行 `git pull origin main`
- 已进入 `backend`
- 已激活 `venv`
- 已加载 `.env.prod`
- 已确认需要不要执行 `seed_gesp_courses.py`
- 已确认需要不要执行 `dedupe_courses.py`
- 已重启 `pymaster`

### 前端

- 已确认前端是否有改动
- 已执行 `npm run build`
- 已覆盖 `/var/www/pymaster/frontend`
- 已重启 `nginx`

### 验证

- 课程中心能打开
- 目标课程能打开
- 新章节可见
- 练习区功能正常
- 后台管理中课程记录正确

---

## 6. 推荐的一键习惯

### 后端种子更新

```bash
cd /root/Python_Course/backend
source venv/bin/activate
set -a
source /root/Python_Course/backend/.env.prod
set +a
python seed_gesp_courses.py
sudo systemctl restart pymaster
```

### 前端发布

```bash
cd /root/Python_Course/frontend
npm install
npm run build
rm -rf /var/www/pymaster/frontend
cp -r dist /var/www/pymaster/frontend
chown -R www-data:www-data /var/www/pymaster/frontend
sudo systemctl restart nginx
```
