import os
import sys
import shutil
import urllib.request
import subprocess
from PIL import Image

# Setup directories
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
logo_dir = os.path.join(base_dir, "public", "app-logos")
backup_dir = os.path.join(base_dir, "public", "app-logos-backup")
temp_dir = os.path.join(base_dir, "public", "temp-dl")

print(f"Base dir: {base_dir}")

# Source mappings
source_mappings = {
    # 1. 电子邮箱
    "qq_mail": "public/新增图片/QQ邮箱.png",
    "wyyoux": "public/新增图片/wyyoux.webp",
    "outlook": "public/app-logos/outlook.jpg",
    "gmail": "public/app-logos/gmail.jpg",
    "mailbox": "public/app-logos/mailbox.jpg",
    "proton_mail": "public/app-logos/proton_mail.jpg",
    "tuta_mail": "public/app-logos/tuta_mail.jpg",

    # 2. 相册
    "vendor_gallery": "public/新增图片/厂商相册.jpg",
    "google_photos": "public/app-logos/google_photos.jpg",
    "apple_photos": "public/app-logos/apple_photos.jpg",
    "ente_photos": "public/app-logos/ente_photos.jpg",
    "photoprism": "public/app-logos/photoprism.jpg",
    "fossify_gallery": "public/app-logos/fossify_gallery.jpg",

    # 3. 搜索引擎
    "baidu": "public/新增图片/百度搜索.png",
    "sogou": "public/新增图片/搜狗（搜索和输入法）.png",
    "bing": "public/app-logos/bing.jpg",
    "360": "public/新增图片/360.png",
    "google_search": "public/app-logos/google_search.jpg",
    "duckduckgo": "public/app-logos/duckduckgo.jpg",
    "brave_search": "public/app-logos/brave_search.jpg",
    "startpage": "public/app-logos/startpage.jpg",
    "searxng": "public/app-logos/searxng.jpg",

    # 4. 浏览器
    "vendor_browser": "public/新增图片/厂商浏览器.jpg",
    "qq_browser": "public/新增图片/qq浏览器.jpg",
    "quark": "public/新增图片/夸克.webp",
    "edge": "public/app-logos/edge.jpg",
    "chrom": "public/app-logos/chrom.jpg",
    "firefox": "public/app-logos/firefox.jpg",
    "brave": "public/app-logos/brave.jpg",
    "waterfox": "public/app-logos/waterfox.jpg",
    "ironfox": "public/app-logos/ironfox.jpg",
    "vivaldi": "public/app-logos/vivaldi.jpg",
    "tor": "public/app-logos/tor.jpg",

    # 5. 通信软件
    "qq": "public/新增图片/qq(群聊和通信都用这个).png",
    "wechat": "public/新增图片/微信（支付复用）.png",
    "telegram": "public/app-logos/telegram.jpg",
    "Discord": "public/app-logos/discord.jpg",
    "simplex": "public/app-logos/simplex.jpg",
    "signal": "public/app-logos/signal.jpg",
    "Matrix": "public/app-logos/matrix.jpg",

    # 6. 笔记
    "vendor_notes": "public/新增图片/厂商便签.jpg",
    "google_keep": "public/app-logos/google_keep.jpg",
    "apple_notes": "public/app-logos/apple_notes.jpg",
    "notion": "public/app-logos/notion.jpg",
    "handwritten": "public/新增图片/所有手写用这个.jpg",
    "obsidian": "public/app-logos/obsidian.jpg",
    "logseq": "public/app-logos/logseq.jpg",
    "joplin": "public/app-logos/joplin.jpg",
    "ddocs_new": "public/app-logos/fileverse.jpg",
    "fossify_notes": "public/app-logos/fossify_notes.jpg",

    # 7. 云盘
    "baidu_wangpan": "public/新增图片/百度搜索.png",
    "quark_wangpan": "public/新增图片/夸克.webp",
    "xunlei": "public/新增图片/迅雷.png",
    "123pan": "public/新增图片/123云盘.webp",
    "icloud_guizhou": "public/新增图片/云上贵州.jpg",
    "onedrive": "public/app-logos/onedrive.jpg",
    "google_drive": "public/app-logos/google_drive.jpg",
    "icloud": "public/app-logos/icloud.jpg",
    "proton_drive": "public/app-logos/proton_drive.jpg",
    "filen": "public/app-logos/filen.jpg",
    "nextcloud": "public/app-logos/nextcloud.jpg",

    # 8. 密码管理
    "vendor_password_manager": "public/新增图片/厂商密码管理器.jpg",
    "google_passwords": "public/app-logos/google_passwords.jpg",
    "apple_passwords": "public/app-logos/apple_passwords.jpg",
    "bitwarden": "public/app-logos/bitwarden.jpg",
    "proton_pass": "public/app-logos/proton_pass.jpg",
    "keepass": "public/app-logos/keepass.jpg",
    "1password": "public/app-logos/1password.jpg",

    # 9. 两步验证器
    "google_auth": "public/app-logos/google_auth.jpg",
    "microsoft_auth": "public/app-logos/microsoft_auth.jpg",
    "authy": "public/app-logos/authy.jpg",
    "ente_auth": "public/app-logos/ente_auth.jpg",
    "aegis_auth": "public/app-logos/aegis_auth.jpg",
    "freeotp": "public/app-logos/freeotp.jpg",
    "proton_auth": "public/app-logos/proton_auth.jpg",
    "bitwarden_auth": "public/app-logos/bitwarden_auth.jpg",
    "yubico_auth": "public/app-logos/yubico_auth.jpg",
    "vaultwarden": "public/app-logos/vaultwarden.jpg",
    "stratum": "public/app-logos/stratum.jpg",
    "2fas_auth": "public/app-logos/2fas_auth.jpg",

    # 10. 日程
    "vendor_calendar": "public/新增图片/厂商日历.jpg",
    "google_calendar": "public/app-logos/google_calendar.jpg",
    "outlook_calendar": "public/app-logos/outlook_calendar.jpg",
    "proton_calendar": "public/app-logos/proton_calendar.jpg",
    "fossify_calendar": "public/app-logos/fossify_calendar.jpg",
    "nextcloud_calendar": "public/app-logos/nextcloud_calendar.jpg",

    # 11. 电话簿
    "vendor_contacts": "public/新增图片/厂商自带电话本.jpg",
    "google_contacts": "public/app-logos/google_contacts.jpg",
    "fossify_contacts": "public/app-logos/fossify_contacts.jpg",

    # 12. 应用商店
    "vendor_app_store": "public/新增图片/厂商自带商店.png",
    "yingyongbao": "public/新增图片/应用宝.webp",
    "coolapk": "public/新增图片/酷安.png",
    "play_store": "public/app-logos/play_store.jpg",
    "accrescent": "public/app-logos/accrescent.jpg",
    "f_droid": "public/app-logos/f_droid.jpg",
    "aurora_store": "public/app-logos/aurora_store.jpg",

    # 13. 科学上网
    "dont_know": "public/新增图片/我不会.png",
    "laowang_vpn": "public/新增图片/老王VPN.png",
    "kuailian_vpn": "public/新增图片/快连.jpg",
    "airport_subscription": "public/新增图片/机场.jpg",
    "self_hosted_vpn": "public/新增图片/自建vpn.png",
    "clash": "public/新增图片/clash-300x300.png",
    "v2rayng": "public/新增图片/V2RAYNG.png",
    "singbox": "public/新增图片/SINGBOX.png",
    "hiddify": "public/新增图片/Hiddify.png",

    # 14. AI
    "deepseek": "public/新增图片/deepseek.jpg",
    "doubao": "public/新增图片/豆包.jpg",
    "qianwen": "public/新增图片/千问.png",
    "yuanbao": "public/新增图片/元宝.png",
    "Kimi": "public/新增图片/Kimi.png",
    "microsoft_copilot": "public/app-logos/microsoft_copilot.jpg",
    "vendor_system": "public/新增图片/厂商系统.png",
    "chatgpt": "public/app-logos/chatgpt.jpg",
    "gemini": "public/app-logos/gemini.jpg",
    "claude": "public/app-logos/claude.jpg",
    "grok": "public/app-logos/grok.jpg",
    "mistralai": "public/app-logos/mistralai.jpg",
    "ollama": "public/app-logos/ollama.jpg",
    "duckai": "public/app-logos/duckai.jpg",
    "lumo": "public/app-logos/lumo.jpg",

    # 15. 全屋智能
    "buyongle": "public/新增图片/不用了.png",
    "apple_homekit": "public/app-logos/apple_homekit.jpg",
    "google_home": "public/app-logos/google_home.jpg",

    # 16. 地图
    "gaode": "public/新增图片/高德.jpg",
    "baidu_maps": "public/新增图片/百度地图.png",
    "tencent_maps": "public/新增图片/腾讯地图.png",
    "no_good_alternative": "public/新增图片/找不到.jpg",

    # 17. 翻译
    "baidu_translate": "public/新增图片/百度翻译.webp",
    "sogou_translate": "public/新增图片/搜狗翻译.png",
    "deepl": "public/app-logos/deepl.jpg",
    "google_translate": "public/app-logos/google_translate.jpg",
    "apple_translate": "public/app-logos/apple_translate.jpg",
    "libretranslate": "public/app-logos/libretranslate.jpg",
    "mozilla_translate": "public/app-logos/mozilla_translate.jpg",

    # 18. 群聊
    "discord": "public/app-logos/discord.jpg",
    "matrix": "public/app-logos/matrix.jpg",
    "fluxer": "public/app-logos/fluxer.jpg",

    # 19. 社交媒体
    "douyin": "public/新增图片/抖音.jpg",
    "kuaishou": "public/新增图片/快手.webp",
    "xiaohongshu": "public/新增图片/小红书.png",
    "weibo": "public/新增图片/微博.png",
    "zhihu": "public/新增图片/知乎.jpg",
    "baidu_tieba": "public/新增图片/百度贴吧.png",
    "NGA": "public/新增图片/nga.jpg",
    "facebook": "public/app-logos/facebook.jpg",
    "instagram": "public/app-logos/instagram.jpg",
    "threads": "public/app-logos/threads.jpg",
    "Twitter": "public/app-logos/Twitter.jpg",
    "reddit": "public/app-logos/reddit.jpg",
    "minds": "public/app-logos/minds.jpg",
    "pixelfed": "public/app-logos/pixelfed.jpg",

    # 20. 视频通话
    "tencent_meeting": "public/新增图片/腾讯会议.jpg",
    "dingtalk": "public/新增图片/钉钉.jpg",
    "microsoft_teams": "public/app-logos/microsoft_teams.jpg",
    "zoom": "public/app-logos/zoom.jpg",
    "google_meet": "public/app-logos/google_meet.jpg",
    "brave_talk": "public/app-logos/brave_talk.jpg",
    "jitsi": "public/app-logos/jitsi.jpg",
    "nextcloud_talk": "public/app-logos/nextcloud_talk.jpg",

    # 21. 支付方式
    "alipay": "public/新增图片/支付宝.jpg",
    "ecny": "public/新增图片/数字人民币.png",
    "cash_and_cards": "public/新增图片/现金&实体卡优先.png",
    "paypal": "public/app-logos/paypal.jpg",
    "google_pay": "public/app-logos/google_pay.jpg",
    "apple_pay": "public/app-logos/apple_pay.jpg",

    # 22. 加密钱包
    "coinbase_wallet": "public/app-logos/coinbase_wallet.jpg",
    "metamask": "public/app-logos/metamask.jpg",
    "phantom": "public/app-logos/phantom.jpg",
    "trust_wallet": "public/app-logos/trust_wallet.jpg",
    "brave_wallet": "public/app-logos/brave_wallet.jpg",
    "cake_wallet": "public/app-logos/cake_wallet.jpg",
    "proton_wallet": "public/app-logos/proton_wallet.jpg",
    "zodl": "public/app-logos/zodl.jpg",

    # 23. DNS
    "ISPDNS": "public/app-logos/ISPDNS.jpg",
    "cloudflare": "public/app-logos/cloudflare.jpg",
    "controld": "public/app-logos/controld.jpg",
    "nextdns": "public/app-logos/nextdns.jpg",
    "adguard": "public/app-logos/adguard.jpg",
    "quad9": "public/app-logos/quad9.jpg",
    "mullvad_dns": "public/app-logos/mullvad_dns.jpg",
    "opennic": "public/app-logos/opennic.jpg",

    # 24. 电脑操作系统
    "windows": "public/app-logos/windows.jpg",
    "macos": "public/app-logos/macos.jpg",
    "arch_linux": "public/app-logos/arch_linux.jpg",
    "linux_mint": "public/app-logos/linux_mint.jpg",
    "qubes_os": "public/app-logos/qubes_os.jpg",
    "fedora": "public/app-logos/fedora.jpg",
    "ubuntu": "public/app-logos/ubuntu.jpg",
    "debian": "public/app-logos/debian.jpg",
    "nixos": "public/app-logos/nixos.jpg",
    "opensuse": "public/app-logos/opensuse.jpg",
    "Artix": "DOWNLOAD_URL:https://cdn.jsdelivr.net/npm/simple-icons@v11/icons/artixlinux.svg",
    "Devuan": "DOWNLOAD_URL:https://devuan.org/ui/img/devuan-emblem.svg",
    "Gentoo": "DOWNLOAD_URL:https://cdn.jsdelivr.net/npm/simple-icons@v11/icons/gentoo.svg",
    "FreeBSD": "DOWNLOAD_URL:https://cdn.jsdelivr.net/npm/simple-icons@v11/icons/freebsd.svg",
    "OpenBSD": "DOWNLOAD_URL:https://cdn.jsdelivr.net/npm/simple-icons@v11/icons/openbsd.svg",
    "NetBSD": "DOWNLOAD_URL:https://cdn.jsdelivr.net/npm/simple-icons@v11/icons/netbsd.svg",

    # 25. 手机操作系统
    "vendor_android": "public/新增图片/厂商系统.png",
    "ios": "public/app-logos/ios.jpg",
    "graphene_os": "public/app-logos/graphene_os.jpg",
    "lineage_os": "public/app-logos/lineage_os.jpg",
    "e_os": "public/app-logos/e_os.jpg",
    "Evolution_X": "public/新增图片/Evolution X.png",
    "crDroid": "public/新增图片/crDroid.jpg",
    "calyx_os": "public/app-logos/calyx_os.jpg",
    "Project_Infinity_X": "public/新增图片/Project Infinity X.jpg",

    # 26. 影音娱乐
    "iqiyi": "public/新增图片/爱奇艺.jpg",
    "tencent_video": "public/新增图片/腾讯视频.png",
    "youku": "public/新增图片/优酷.jpg",
    "bilbil": "public/新增图片/bilibili.jpg",
    "netflix": "public/app-logos/netflix.jpg",
    "disney_plus": "public/app-logos/disney_plus.jpg",
    "self_hosted_service": "public/新增图片/自建服务.png",
    "Bangumi": "public/新增图片/Bangumi.png",
    "Animeko": "public/新增图片/Animeko.webp",
    "Kazumi": "public/新增图片/Kazumi.png",

    # 27. 办公套件
    "Microsoft_365": "public/app-logos/Microsoft_365.jpg",
    "WPS": "public/app-logos/WPS.jpg",
    "kingsoft_docs": "public/新增图片/金山文档.jpg",
    "Google_Workspace": "public/app-logos/Google_Workspace.jpg",
    "Apple_iWork": "public/app-logos/Apple_iWork.jpg",
    "LibreOffice": "public/app-logos/LibreOffice.jpg",
    "Collabora": "public/app-logos/Collabora.jpg",
    "OnlyOffice": "public/app-logos/OnlyOffice.jpg",
    "OpenOffice": "public/app-logos/OpenOffice.jpg",
    "CryptPad": "public/app-logos/CryptPad.jpg",
    "proton_docs": "public/app-logos/proton_docs.jpg",
    "fileverse": "public/app-logos/fileverse.jpg",

    # 28. 域名托管
    "tencent_cloud": "public/新增图片/腾讯云.png",
    "aliyun_cloud": "public/新增图片/阿里云.png",
    "godaddy": "public/app-logos/godaddy.jpg",
    "njalla": "public/app-logos/njalla.jpg",
    "1984_hosting": "public/app-logos/1984_hosting.jpg",
    "orangewebsite": "public/app-logos/orangewebsite.jpg",

    # 29. UGC 影音
    "piliplus": "public/新增图片/piliplus.png",
    "youtube": "public/新增图片/youtube.svg",

    # 30. 输入法
    "baidu_input": "public/新增图片/百度输入法.png",
    "sogou_input": "public/新增图片/搜狗（搜索和输入法）.png",
    "xunfei_input": "public/新增图片/迅飞.webp",
    "wechat_input": "public/新增图片/微信输入法.jpg",
    "Gboard": "public/新增图片/Gboard.png",
    "Fcitx5": "public/新增图片/Fcitx5.png",
    "rime": "public/新增图片/中州韵.png",
    "yuyan_input": "public/新增图片/语燕输入法.png"
}

# Create backup directory
if os.path.exists(logo_dir):
    if os.path.exists(backup_dir):
        shutil.rmtree(backup_dir)
    shutil.copytree(logo_dir, backup_dir)
    print("Backed up existing app logos.")

# Recreate logo directory empty
if os.path.exists(logo_dir):
    shutil.rmtree(logo_dir)
os.makedirs(logo_dir, exist_ok=True)
os.makedirs(temp_dir, exist_ok=True)

def process_image(src_path, dst_path):
    """Resizes and crops/pads image to 200x200 JPEG under 50KB"""
    try:
        # If it is an SVG file, ImageMagick convert is needed
        if src_path.lower().endswith('.svg'):
            cmd = [
                "convert",
                "-background", "white",
                src_path,
                "-flatten",
                "-resize", "200x200",
                "-gravity", "center",
                "-extent", "200x200",
                "-quality", "92",
                dst_path
            ]
            subprocess.run(cmd, check=True)
            return True

        img = Image.open(src_path)
        
        # Handle transparency or different modes
        if img.mode in ('RGBA', 'LA') or (img.mode == 'P' and 'transparency' in img.info):
            bg = Image.new('RGB', img.size, (255, 255, 255))
            # Get transparency mask
            mask = img.convert('RGBA').split()[3]
            bg.paste(img.convert('RGB'), mask=mask)
            img = bg
        elif img.mode != 'RGB':
            img = img.convert('RGB')

        w, h = img.size
        # Crop to square
        if w != h:
            min_side = min(w, h)
            left = (w - min_side) // 2
            top = (h - min_side) // 2
            right = left + min_side
            bottom = top + min_side
            img = img.crop((left, top, right, bottom))
        
        # Resize
        img = img.resize((200, 200), Image.Resampling.LANCZOS)
        
        # Save as JPEG
        img.save(dst_path, 'JPEG', quality=90)
        return True
    except Exception as e:
        print(f"Error processing image {src_path}: {e}")
        return False

# 1. Process all logos in source_mappings
for app_id, source in source_mappings.items():
    dst_path = os.path.join(logo_dir, f"{app_id}.jpg")
    
    if source.startswith("DOWNLOAD_URL:"):
        url = source.split(":", 1)[1]
        temp_svg = os.path.join(temp_dir, f"{app_id}.svg")
        print(f"Downloading SVG for {app_id} from {url}...")
        try:
            # Download with custom user agent to avoid Wikipedia blocking
            req = urllib.request.Request(
                url,
                headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
            )
            with urllib.request.urlopen(req) as response:
                with open(temp_svg, 'wb') as out_file:
                    out_file.write(response.read())
            
            # Convert downloaded SVG to JPEG
            success = process_image(temp_svg, dst_path)
            if success:
                print(f"Successfully processed downloaded logo for {app_id}")
            else:
                print(f"Failed to process downloaded SVG for {app_id}")
        except Exception as e:
            print(f"Error downloading {app_id}: {e}")
            # Fallback: Draw placeholder text logo using Pillow
            try:
                img = Image.new('RGB', (200, 200), color=(34, 197, 94))
                img.save(dst_path, 'JPEG')
                print(f"Created fallback placeholder logo for {app_id}")
            except Exception as ex:
                print(f"Fallback creation failed: {ex}")
    else:
        # Local file source
        # If the path points to existing app logos, retrieve from backup directory
        resolved_src = source
        if source.startswith("public/app-logos/"):
            rel_name = os.path.basename(source)
            resolved_src = os.path.join(backup_dir, rel_name)
        else:
            resolved_src = os.path.join(base_dir, source)

        if os.path.exists(resolved_src):
            success = process_image(resolved_src, dst_path)
            if success:
                print(f"Processed local logo for {app_id}")
            else:
                print(f"Failed to process local logo for {app_id}")
        else:
            print(f"Local source not found: {resolved_src}")

# Cleanup temp dir and backup dir
if os.path.exists(temp_dir):
    shutil.rmtree(temp_dir)
if os.path.exists(backup_dir):
    shutil.rmtree(backup_dir)

print("\nApp logos processed and cleaned up successfully.")

# 2. Process Home Page Assets
logo_src = os.path.join(base_dir, "public/新的资产/new-loga.jpg")
hero_src = os.path.join(base_dir, "public/新的资产/newhero.png")
author_src = os.path.join(base_dir, "public/新的资产/在ente的作者位边上放置.png")

logo_dst = os.path.join(base_dir, "public/logo.png")
hero_dst = os.path.join(base_dir, "public/hero.png")
author_dst = os.path.join(base_dir, "public/author.png")

if os.path.exists(logo_src):
    try:
        # Convert new logo to PNG (the codebase expects logo.png)
        img = Image.open(logo_src)
        img.save(logo_dst, "PNG")
        print("Replaced public/logo.png successfully.")
    except Exception as e:
        print(f"Failed to process logo image: {e}")

if os.path.exists(hero_src):
    try:
        # Resize hero image to 1000x1000 for faster loading and save as PNG
        img = Image.open(hero_src)
        img = img.resize((1000, 1000), Image.Resampling.LANCZOS)
        img.save(hero_dst, "PNG", optimize=True)
        print("Replaced public/hero.png successfully.")
    except Exception as e:
        print(f"Failed to process hero image: {e}")

if os.path.exists(author_src):
    try:
        # Resize author badge to 128x128 PNG to save space (from 8.4MB)
        img = Image.open(author_src)
        img = img.resize((128, 128), Image.Resampling.LANCZOS)
        img.save(author_dst, "PNG", optimize=True)
        print("Created public/author.png successfully.")
    except Exception as e:
        print(f"Failed to process author image: {e}")
