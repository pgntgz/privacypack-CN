# PrivacyPack 隐私卡牌 (中文分支)

选择以前使用过的主流应用程序，展示切换到的更尊重隐私的替代方案，并分享您的隐私化成果！

您可以在本地或部署的服务器上创建卡片。本分支由[pgntgz](https://pgntgz.top/) 维护。

感谢项目的[PrivacyPack](https://github.com/ente-io/privacypack)贡献者
ente你们的相册真的很棒！

本项目对应的 GitHub 仓库地址为：[https://github.com/pgntgz/privacypack-CN](https://github.com/pgntgz/privacypack-CN)
我维护的网站链接是[PrivacyPack-CN](https://yinsi.pgntgz.top/)

![PrivacyPack Banner](public/og-image.png)

## 开发配置

### 依赖条件

- Node.js (v18 或更高版本)
- npm

### 本地运行

1. 克隆仓库

```bash
git clone https://github.com/pgntgz/privacypack-CN.git
cd privacypack-CN
```

2. 安装依赖

```bash
npm install
```[PrivacyPack](https://github.com/ente-io/privacypack)

3. 启动开发服务器

```bash
npm run dev
```

启动后，访问 `http://localhost:3000`或相应端口，即可查看项目页面。

## 我有不错的替代应用

您可以通过修改 `/data/apps.json` 来向目录中添加新应用。每个应用都属于一个特定的类别，并且可以是主流应用，也可以是隐私保护的替代方案。

如果您需要批量处理或转换图片，请在本地运行：
```bash
python3 scripts/convert_images.py
```

### 新增 Logo 要求

在添加新应用时，确保 Logo 满足以下规范防止bug：

- 格式：JPG
- 尺寸：200x200 像素，无圆角，无透明背景，Logo 周围有足够的边距
- 文件大小：不超过 50KB
- 位置：将 Logo 文件放在 `/public/app-logos/{app_id}.jpg` 中

## 关于本项目

本中文分支基于 [Ente](https://ente.io) 团队制作的 PrivacyPack ，我对其进行了汉化、增减选项让他适合中国的软件市场
再次感谢[PrivacyPack](https://github.com/ente-io/privacypack)贡献者们
## 许可证

本项目沿用[PrivacyPack](https://github.com/ente-io/privacypack)的 [MIT 许可证](/LICENSE) 进行分发。
