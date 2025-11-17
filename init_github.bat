@echo off
REM 初始化 Git 仓库并推送到 GitHub 的脚本
REM Script to initialize Git repository and push to GitHub

setlocal enabledelayedexpansion

echo.
echo ========================================
echo 数据转换工具 - GitHub 初始化脚本
echo Data Transformer - GitHub Init Script
echo ========================================
echo.

REM 检查 git 是否安装
git --version >nul 2>&1
if errorlevel 1 (
    echo ❌ 错误: Git 未安装或不在 PATH 中
    echo Error: Git not installed or not in PATH
    pause
    exit /b 1
)

REM 初始化本地仓库
echo ✓ 初始化 Git 仓库...
echo ✓ Initializing Git repository...
git init
if errorlevel 1 goto error

REM 配置用户（可选）
echo.
set /p username="请输入你的 GitHub 用户名 (Enter your GitHub username) [skip]: "
if not "!username!"=="" (
    git config user.name "!username!"
)

set /p email="请输入你的 GitHub 邮箱 (Enter your GitHub email) [skip]: "
if not "!email!"=="" (
    git config user.email "!email!"
)

REM 添加所有文件
echo.
echo ✓ 添加所有文件...
echo ✓ Adding all files...
git add .
if errorlevel 1 goto error

REM 首次提交
echo.
echo ✓ 创建初始提交...
echo ✓ Creating initial commit...
git commit -m "feat: initial project setup with wide-long format converter"
if errorlevel 1 goto error

REM 重命名主分支
echo.
echo ✓ 重命名主分支为 main...
echo ✓ Renaming main branch to main...
git branch -M main

REM 提示添加远程仓库
echo.
echo ========================================
echo 后续步骤 (Next Steps):
echo ========================================
echo.
echo 1. 在 GitHub 上创建新仓库:
echo    Go to: https://github.com/new
echo    Repository name: data-transformer
echo    选择 "Public" (Choose "Public")
echo    不要初始化任何文件 (Don't initialize any files)
echo.
echo 2. 添加远程仓库并推送:
echo    (Add remote repository and push:)
echo.
echo    git remote add origin https://github.com/你的用户名/data-transformer.git
echo    (Replace 你的用户名 with your username)
echo.
echo    git push -u origin main
echo.
echo 3. 验证推送成功:
echo    (Verify push successful:)
echo    - 访问 https://github.com/你的用户名/data-transformer
echo    - Visit your GitHub repository page
echo.
echo ========================================
echo.

pause
exit /b 0

:error
echo.
echo ❌ 发生错误! (An error occurred!)
pause
exit /b 1
