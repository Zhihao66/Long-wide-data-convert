#!/bin/bash
# 初始化 Git 仓库并推送到 GitHub 的脚本
# Script to initialize Git repository and push to GitHub

echo ""
echo "========================================"
echo "数据转换工具 - GitHub 初始化脚本"
echo "Data Transformer - GitHub Init Script"
echo "========================================"
echo ""

# 检查 git 是否安装
if ! command -v git &> /dev/null; then
    echo "❌ 错误: Git 未安装"
    echo "Error: Git not installed"
    exit 1
fi

# 初始化本地仓库
echo "✓ 初始化 Git 仓库..."
echo "✓ Initializing Git repository..."
git init || exit 1

# 配置用户（可选）
echo ""
read -p "请输入你的 GitHub 用户名 [skip]: " username
if [ ! -z "$username" ]; then
    git config user.name "$username"
fi

read -p "请输入你的 GitHub 邮箱 [skip]: " email
if [ ! -z "$email" ]; then
    git config user.email "$email"
fi

# 添加所有文件
echo ""
echo "✓ 添加所有文件..."
echo "✓ Adding all files..."
git add . || exit 1

# 首次提交
echo ""
echo "✓ 创建初始提交..."
echo "✓ Creating initial commit..."
git commit -m "feat: initial project setup with wide-long format converter" || exit 1

# 重命名主分支
echo ""
echo "✓ 重命名主分支为 main..."
echo "✓ Renaming main branch to main..."
git branch -M main

# 提示添加远程仓库
echo ""
echo "========================================"
echo "后续步骤 (Next Steps):"
echo "========================================"
echo ""
echo "1. 在 GitHub 上创建新仓库:"
echo "   Go to: https://github.com/new"
echo "   Repository name: data-transformer"
echo "   选择 \"Public\" (Choose \"Public\")"
echo "   不要初始化任何文件 (Don't initialize any files)"
echo ""
echo "2. 添加远程仓库并推送:"
echo "   (Add remote repository and push:)"
echo ""
echo "   git remote add origin https://github.com/你的用户名/data-transformer.git"
echo "   (Replace 你的用户名 with your username)"
echo ""
echo "   git push -u origin main"
echo ""
echo "3. 验证推送成功:"
echo "   (Verify push successful:)"
echo "   - 访问 https://github.com/你的用户名/data-transformer"
echo "   - Visit your GitHub repository page"
echo ""
echo "========================================"
echo ""

exit 0
