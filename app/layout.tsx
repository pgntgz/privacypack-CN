import type { Metadata } from "next";
import localFont from "next/font/local";
import "./globals.css";

const jetBrainsMono = localFont({
    src: "/JetBrainsMono.ttf",
});

const SITE_URL = "https://yinsi.pgntgz.top";
const SITE_NAME = "隐私卡";
const SITE_TITLE = "隐私卡 — 展示你的隐私工具组合";
const SITE_DESCRIPTION =
    "选择你曾使用的主流应用，展示你已切换到的隐私友好替代工具，用一张卡片分享你的隐私实践成果！";

export const metadata: Metadata = {
    title: {
        default: SITE_TITLE,
        template: `%s | ${SITE_NAME}`,
    },
    description: SITE_DESCRIPTION,
    metadataBase: new URL(SITE_URL),
    alternates: {
        canonical: "/",
    },
    keywords: [
        "隐私",
        "隐私保护",
        "隐私工具",
        "开源替代",
        "隐私软件",
        "PrivacyPack",
        "隐私卡",
        "数字安全",
        "去谷歌化",
        "privacy tools",
        "open source",
    ],
    authors: [{ name: "pgntgz", url: "https://pgntgz.top" }],
    creator: "pgntgz",
    publisher: SITE_NAME,
    robots: {
        index: true,
        follow: true,
        googleBot: {
            index: true,
            follow: true,
            "max-video-preview": -1,
            "max-image-preview": "large",
            "max-snippet": -1,
        },
    },
    openGraph: {
        title: SITE_TITLE,
        description: SITE_DESCRIPTION,
        url: SITE_URL,
        siteName: SITE_NAME,
        images: [
            {
                url: `${SITE_URL}/og-image.png`,
                width: 1200,
                height: 630,
                alt: "隐私卡 — 展示你的隐私工具组合",
            },
        ],
        locale: "zh_CN",
        type: "website",
    },
    twitter: {
        card: "summary_large_image",
        title: SITE_TITLE,
        description: SITE_DESCRIPTION,
        images: [`${SITE_URL}/og-image.png`],
        creator: "@pgntgz",
    },
};

export default function RootLayout({
    children,
}: Readonly<{
    children: React.ReactNode;
}>) {
    return (
        <html lang="zh-CN">
            <head>
                <link rel="canonical" href={SITE_URL} />
                <meta name="theme-color" content="#121212" />
                <meta name="color-scheme" content="dark" />
            </head>
            <body className={`${jetBrainsMono.className} antialiased`}>
                {children}
            </body>
        </html>
    );
}
