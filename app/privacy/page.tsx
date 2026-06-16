import Link from "next/link";
 
const Privacy = () => {
    return (
        <div className="flex min-h-screen w-full flex-col items-center">
            <div className="flex w-full flex-col gap-5 p-8 text-gray-400 lg:w-[56rem] lg:p-16">
                <h1 className="mb-8 text-3xl text-white uppercase">
                    隐私政策
                </h1>
                <p>最后更新时间：2026年4月25日</p>
                <p>
                    我们非常尊重用户（以下简称“用户”或“您”）的隐私。本隐私政策（以下简称“本政策”）阐述了您在访问和使用我们的网站 <strong>https://yinsi.pgntgz.top/</strong>（以下简称“本网站”）时，我们如何处理相关信息。
                </p>
                <p>
                    访问或使用本网站即表示您同意本政策的条款。如果您不同意本政策的条款，请不要访问或使用本网站。
                </p>
 
                <h2 className="text-xl text-white">1. 服务简介</h2>
                <p>
                    <strong>https://yinsi.pgntgz.top/</strong> 允许用户创建并分享一张卡片，展示他们以前使用的主流应用程序以及他们已经切换到的保护隐私的替代方案。该卡片完全在您的浏览器中生成。
                </p>
 
                <h2 className="text-xl text-white">
                    2. 数据收集与使用
                </h2>
                <p>
                    本网站不需要注册账户，不要求您输入个人信息，也不会上传或存储您在制作卡片时选择的应用程序数据。
                </p>
                <p>
                    与大多数网站一样，本网站的托管服务商可能会处理提供网页服务所需的基本请求信息，例如 IP 地址、浏览器信息和请求时间戳。
                </p>
 
                <h2 className="text-xl text-white">3. 数据共享</h2>
                <p>
                    我们不会发布、托管或索引您的卡片。如果您下载或分享卡片，该过程完全是通过您的浏览器、设备或您选择的第三方应用程序或服务在本地完成的。
                </p>
 
                <h2 className="text-xl text-white">4. 用户权利</h2>
                <p>
                    用户有权随时停止使用本网站。如果您下载或在其他地方分享了卡片，您可以通过保存或分享卡片的地方自行控制该副本。
                </p>
 
                <h2 className="text-xl text-white">5. 数据保留</h2>
                <p>
                    本网站不会保留您生成的卡片或您选择的任何应用选项。
                </p>
 
                <h2 className="text-xl text-white">
                    6. 未成年人隐私 Protection
                </h2>
                <p>
                    本网站不面向 13 岁以下的儿童，我们不会有意收集 13 岁以下儿童的个人数据。如果您未满 13 岁，请不要使用本网站。
                </p>
 
                <h2 className="text-xl text-white">7. Cookie 使用</h2>
                <p>
                    我们不会出于追踪目的在您的设备上放置 Cookie。
                </p>
 
                <h2 className="text-xl text-white">
                    8. 隐私政策的变更
                </h2>
                <p>
                    我们可能会更新本隐私政策，以反映我们实践的变化或其他运营、法律或监管原因。更新将在此页面上公布。
                </p>
 
                <h2 className="text-xl text-white">9. 联系我们</h2>
                <p>
                    您可以通过电子邮件与我们取得联系：{" "}
                    <a
                        href="mailto:privacy@ente.io"
                        className="underline underline-offset-2"
                    >
                        privacy@ente.io
                    </a>
                </p>
                <p>
                    邮寄地址：EnteIO Technologies Private Limited, 72/12, Whitefield, Bengaluru, India.
                </p>
 
                <Link href="/" className="mt-8 underline underline-offset-2">
                    返回主页
                </Link>
            </div>
        </div>
    );
};
 
export default Privacy;
