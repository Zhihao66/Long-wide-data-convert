# 🌐 GitHub Pages 部署指南 / Web Deployment Guide

## 快速部署 - 仅需 3 步

### 第 1 步：修改配置

编辑 `web/index.html`，找到 footer 部分，替换为你的信息：

```html
<a href="https://github.com/你的用户名/data-transformer" target="_blank">GitHub</a>
```

### 第 2 步：推送到 GitHub

```powershell
# 进入项目根目录
cd e:\数据转换

# 初始化 Git（如果尚未）
git init
git add .
git commit -m "feat: add web version with GitHub Pages support"

# 添加远程仓库
git remote add origin https://github.com/你的用户名/data-transformer.git
git branch -M main
git push -u origin main
```

### 第 3 步：启用 GitHub Pages

1. 打开你的 GitHub 仓库
2. 进入 **Settings** → **Pages**
3. 在 "Source" 下选择：
   - Branch: `main`
   - Folder: `/` (根目录) 或 `/web`（根据实际结构）
4. 点击 "Save"
5. 等待几分钟，GitHub 会显示你的网站 URL

## 📍 网站访问地址

部署完成后，你可以访问：

```
https://你的用户名.github.io/data-transformer/
```

或

```
https://你的用户名.github.io/data-transformer/web/
```

（具体取决于你的配置）

## 🔧 配置选项

### 选项 1：根目录部署

如果想在根目录部署（推荐）：

1. 将 `web/index.html` 移到项目根目录
2. 将 `web/app.js` 移到项目根目录
3. GitHub Pages 选择 `/` 文件夹

### 选项 2：子文件夹部署

保持当前结构：

1. GitHub Pages 选择 `/web` 文件夹
2. 或者选择 `/` 文件夹，URL 会自动包含 `/web`

### 选项 3：自定义域名

如果你有自己的域名：

1. 在 GitHub Settings → Pages 中设置自定义域名
2. 在你的域名提供商处添加 DNS 记录
3. 等待 DNS 生效（通常 24 小时）

## 📁 项目结构

```
data-transformer/
├── web/                          # 网页版（GitHub Pages）
│   ├── index.html               # 主页面
│   ├── app.js                   # 核心逻辑
│   ├── package.json             # 项目信息
│   └── README.md                # 网页版说明
├── data_transformer/            # Python 版（可选）
├── tests/                       # 测试（可选）
├── pyproject.toml              # Python 配置（可选）
└── README.md                   # 主说明

# 或简化为只有网页版：
data-transformer/
├── index.html
├── app.js
├── package.json
├── README.md
└── .gitignore
```

## ✅ 验证部署

### 检查清单

- [ ] GitHub 仓库已创建
- [ ] 代码已推送到 main 分支
- [ ] GitHub Pages 已启用
- [ ] 构建完成（Settings → Pages 显示绿色对勾）
- [ ] 可以访问网站

### 调试步骤

1. **检查推送**
   ```powershell
   git log --oneline -5
   ```

2. **检查分支**
   ```powershell
   git branch
   ```

3. **查看 GitHub Actions**
   - 进入仓库 → Actions 标签
   - 查看部署日志

4. **清除浏览器缓存**
   - Ctrl + Shift + Delete
   - 清除缓存并重新加载

## 🎨 自定义

### 修改样式

编辑 `web/index.html` 中的 `<style>` 部分：

```css
/* 修改主色调 */
background: linear-gradient(135deg, 你的颜色1 0%, 你的颜色2 100%);

/* 修改字体 */
font-family: 'Your Font Name', sans-serif;
```

### 修改文本

编辑 `web/index.html` 中的内容：

```html
<h1>你的标题</h1>
<p>你的描述</p>
```

### 添加功能

编辑 `web/app.js` 添加新功能：

```javascript
function yourNewFunction() {
    // 你的代码
}
```

## 🚀 高级部署

### 使用 GitHub Actions 自动部署

创建 `.github/workflows/deploy.yml`：

```yaml
name: Deploy to GitHub Pages

on:
  push:
    branches: [ main ]

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v3
    - name: Deploy
      run: |
        echo "Deploying to GitHub Pages..."
```

### 自定义域名

1. 在项目根目录创建 `CNAME` 文件
2. 添加你的域名：
   ```
   yourdomain.com
   ```
3. 在域名 DNS 设置中添加记录

### CDN 加速

可以配置 Cloudflare 加速：

1. 注册 Cloudflare 账户
2. 添加你的域名
3. 更新 DNS 记录指向 GitHub Pages

## 📊 分析和监控

### 查看访问统计

GitHub Pages 本身不提供分析，可以添加：

1. **Google Analytics**
   - 添加脚本到 HTML
   
2. **Vercel Analytics**
   - 部署到 Vercel 代替

3. **自定义追踪**
   - 添加到 app.js

### 性能优化

- 压缩 HTML/CSS/JS
- 优化图片大小
- 使用 CDN

## 🔐 安全性

### HTTPS

GitHub Pages 默认支持 HTTPS，无需配置。

### 隐私

- 不在代码中存储敏感信息
- 避免在 HTML 中嵌入密钥
- 使用环境变量（如果使用 CI/CD）

## 📱 移动适配

网页版已经响应式设计，支持：
- 桌面
- 平板
- 手机

使用 `@media` 查询自定义移动端样式。

## 🔄 更新部署

每次修改后：

```powershell
git add .
git commit -m "Update description"
git push
```

GitHub Pages 会自动重新部署（通常在 1-2 分钟内）。

## ❌ 常见问题

### Q: 网站显示 404

A: 检查以下几点
- GitHub Pages 是否已启用
- 分支和文件夹选择是否正确
- DNS 是否已生效（自定义域名情况下）

### Q: 样式加载失败

A: 可能的原因
- 路径错误
- 浏览器缓存
- 权限问题

**解决**: 
```powershell
git add web/*
git commit -m "Fix styles"
git push
```

### Q: 脚本不工作

A: 检查
- 是否有 JavaScript 错误（F12 → Console）
- 文件是否正确上传
- 浏览器是否支持该功能

### Q: 无法上传大文件

A: GitHub 单个文件限制 100MB
- 拆分文件
- 使用 Git LFS
- 或部署到其他平台

## 🆘 需要帮助？

- 📖 [GitHub Pages 官方文档](https://pages.github.com/)
- 🐛 [报告问题](https://github.com/yourusername/data-transformer/issues)
- 💬 [讨论](https://github.com/yourusername/data-transformer/discussions)

## 📝 部署检查清单

```
部署前：
☐ 测试所有功能
☐ 检查移动端显示
☐ 更新作者信息
☐ 检查链接有效性

推送代码：
☐ git add .
☐ git commit -m "message"
☐ git push origin main

GitHub 配置：
☐ 进入 Settings → Pages
☐ 选择 main 分支
☐ 选择文件夹 (/ 或 /web)
☐ 保存并等待部署

验证：
☐ 检查网站可访问
☐ 测试所有功能
☐ 检查控制台是否有错误
☐ 测试响应式设计
```

---

**恭喜！你的网页版应用已部署到 GitHub Pages！** 🎉

立即访问：https://你的用户名.github.io/data-transformer/
