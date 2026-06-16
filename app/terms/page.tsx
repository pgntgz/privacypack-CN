import Link from "next/link";
 
const Terms = () => {
    return (
        <div className="flex min-h-screen w-full flex-col items-center">
            <div className="flex w-full flex-col gap-5 p-8 text-gray-400 lg:w-[56rem] lg:p-16">
                <h1 className="mb-8 text-3xl text-white uppercase">
                    服务条款
                </h1>
                <p>最后更新时间：2026年4月25日</p>
                <p>
                    本服务条款（以下简称“本协议”或“条款”）是由 pgntgz（以下简称“我们”）与任何访问或使用我们的网站 <strong>https://yinsi.pgntgz.top/</strong>（以下简称“本网站”）的个人（以下简称“用户”或“您”）之间达成的具有法律约束力的协议。本协议，连同我们的{" "}
                    <Link
                        href="/privacy"
                        className="underline underline-offset-2"
                    >
                        隐私政策
                    </Link>{" "}
                    及引用的任何其他政策，共同规范您对我们服务的使用。
                </p>
                <p>
                    访问或使用本网站即表示您同意受这些条款的约束。如果您不同意本协议的任何部分，请不要使用本网站。
                </p>
 
                <h2 className="text-xl text-white">
                    1. 服务描述
                </h2>
                <p>
                    <strong>https://yinsi.pgntgz.top/</strong> 允许用户创建并分享一张卡片，展示他们以前使用的主流应用程序以及他们已经切换到的保护隐私的替代方案。卡片是在用户的浏览器中生成的，可以由用户下载或分享。本网站仅用于信息和教育目的。
                </p>
 
                <h2 className="text-xl text-white">
                    2. Logo与知识产权的使用
                </h2>
                <p>
                    所有的应用 Logo 和商标均属于其各自所有者的财产。我们不对这些 Logo 主张任何所有权。Logo 的使用仅用于进行对比和评测，属于合理使用我们尊重所有第三方的知识产权。
                </p>
 
                <h2 className="text-xl text-white">3. 隐私政策</h2>
                <p>
                    我们的{" "}
                    <Link
                        href="/privacy"
                        className="underline underline-offset-2"
                    >
                        隐私政策
                    </Link>{" "}
                    解释了我们如何处理您的信息。使用本网站即表示您同意其中所述的规范。
                </p>
 
                <h2 className="text-xl text-white">4. 适用资格</h2>
                <p>使用本网站的用户必须满足以下条件：</p>
                <ul className="list-disc pl-8">
                    <li>年满 13 周岁。</li>
                    <li>
                        根据适用法律，未被禁止使用本网站。
                    </li>
                    <li>
                        不得将本网站用于非法、恶意竞争或恶意破坏的目的。
                    </li>
                </ul>
 
                <h2 className="text-xl text-white">5. 用户责任</h2>
                <p>
                    <strong>(a) 禁止恶意使用：</strong> 您同意不使用本网站分发恶意软件、垃圾邮件，或以其他方式干扰本网站或其服务的正常运行。
                </p>
                <p>
                    <strong>(b) 您的分享副本：</strong> 如果您在本网站之外下载或分享了生成的卡片，您应对该副本的分享地点和分享方式承担全部责任。
                </p>
 
                <h2 className="text-xl text-white">
                    6. 责任限制
                </h2>
                <p>
                    在法律允许的最大范围内，我们不对因您使用本网站、使用 Logo 或应用对比而产生的任何损害、损失或索赔承担任何责任。
                </p>
 
                <h2 className="text-xl text-white">7. 赔偿保证</h2>
                <p>
                    您同意，如果因您使用本网站、生成的卡片、分享的卡片副本或违反本条款而导致任何索赔、损害或法律费用，您将为我们进行辩护并免除我们的责任。
                </p>
 
                <h2 className="text-xl text-white">
                    8. 条款的修改
                </h2>
                <p>
                    我们可能随时更新这些条款。修改自发布时起生效。在更新发布后继续使用本网站即表示您接受修改后的条款。
                </p>
 
                <h2 className="text-xl text-white">9. 管辖法律</h2>
                <p>
                    本网站是一个独立的开源地缘隐私项目。我们不属于任何主权国家的法律实体，亦不接受任何威权体制或特定审查区域的法律管辖。
                </p>
 
                <h2 className="text-xl text-white">10. 其他条款</h2>
                <p>
                    这些条款连同隐私政策，构成了您与我们就本网站达成的完整协议。未执行任何条款不构成对我们在本条款项下权利的放弃。
                </p>
 
                <h2 className="text-xl text-white">11. 联系我们</h2>
                <p>
                    您可以通过电子邮件与我们取得联系：{" "}
                    <a
                        href="mailto:653j5usyg@mozmail.com"
                        className="underline underline-offset-2"
                    >
                        653j5usyg@mozmail.com
                    </a>
                </p>
                <p>
                    邮寄地址：nothing
                </p>
 
                <Link href="/" className="mt-8 underline underline-offset-2">
                    返回主页
                </Link>
            </div>
        </div>
    );
};
 
export default Terms;
