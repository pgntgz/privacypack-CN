import { ArrowRight } from "lucide-react";
import Image from "next/image";
import React from "react";
import { PRIVACY_PACK_FONT_FAMILY } from "@/lib/utils";

interface PrivacyPackResultProps {
    pack: Array<{
        category: string;
        order: number;
        mainstream_app_name: string;
        mainstream_app_id: string;
        private_alternatives: Array<{
            id: string;
            name: string;
        }>;
    }>;
}

type AppLogo = {
    id: string;
    name: string;
};

const PrivacyPackResult: React.FC<PrivacyPackResultProps> = ({ pack }) => {
    const smallColumnCount = Math.max(1, Math.min(pack.length, 3));
    const layout =
        pack.length <= 12
            ? {
                  kind: "classic",
                  gridTop: "200px",
                  gridTemplateColumns: `repeat(${smallColumnCount}, 380px)`,
                  justifyContent: "center",
                  columnGap: "110px",
                  rowGap: "56px",
                  cardClass: "h-[270px] w-[380px] pt-6",
                  logoClass: "h-[150px] w-[150px]",
                  textClass: "max-w-[150px] text-[28px]",
                  multiTextClass: "max-w-[190px] text-[22px]",
                  arrowClass: "-mt-20",
                  arrowSize: 42,
              }
            : pack.length <= 20
              ? {
                    kind: "classic",
                    gridTop: "180px",
                    gridTemplateColumns: "repeat(4, 290px)",
                    justifyContent: "center",
                    columnGap: "72px",
                    rowGap: "52px",
                    cardClass: "h-[190px] w-[290px] pt-6",
                    logoClass: "h-[120px] w-[120px]",
                    textClass: "max-w-[120px] text-[25px]",
                    multiTextClass: "max-w-[150px] text-[18px]",
                    arrowClass: "-mt-12",
                    arrowSize: 32,
                }
              : {
                    kind: "dense",
                    gridTop: "142px",
                    gridTemplateColumns: "repeat(4, 1fr)",
                    justifyContent: "normal",
                    columnGap: "22px",
                    rowGap: "18px",
                    cardClass:
                        "h-[166px] w-full rounded-lg border border-white/8 bg-[#181818] px-3 py-2.5",
                    logoClass: "h-[66px] w-[66px]",
                    textClass: "max-w-[118px] text-[15px]",
                    multiTextClass: "max-w-[118px] text-[14px]",
                    arrowClass: "",
                    arrowSize: 22,
                };

    const getAlternativeLabel = (
        alternatives: Array<{ id: string; name: string }>,
        compact = false,
    ) => {
        if (compact && alternatives.length > 1) {
            return `${alternatives[0].name} +${alternatives.length - 1}`;
        }

        return alternatives.map((alternative) => alternative.name).join(" + ");
    };

    const renderLogo = (app: AppLogo, logoClass: string) => (
        <div className={logoClass}>
            <Image
                src={`/app-logos/${app.id}.jpg`}
                alt={app.name}
                width={0}
                height={0}
                sizes="100vw"
                className="h-full w-full rounded-2xl object-cover"
            />
        </div>
    );

    const renderDenseAlternativeLogo = (
        alternatives: Array<{ id: string; name: string }>,
    ) => {
        const [primary, secondary] = alternatives;

        if (!secondary) {
            return renderLogo(primary, layout.logoClass);
        }

        return (
            <div className={`${layout.logoClass} relative`}>
                <Image
                    src={`/app-logos/${primary.id}.jpg`}
                    alt={primary.name}
                    width={0}
                    height={0}
                    sizes="100vw"
                    className="h-full w-full rounded-2xl object-cover"
                />
                <div className="absolute -right-1 -bottom-1 h-[34px] w-[34px] overflow-hidden rounded-lg border-[3px] border-[#181818] bg-[#181818]">
                    <Image
                        src={`/app-logos/${secondary.id}.jpg`}
                        alt={secondary.name}
                        width={0}
                        height={0}
                        sizes="40px"
                        className="h-full w-full object-cover"
                    />
                </div>
                {alternatives.length > 2 ? (
                    <div className="absolute -top-1 -right-1 flex h-[25px] min-w-[25px] items-center justify-center rounded-full bg-[#00d51b] px-1 text-[12px] leading-none font-bold text-[#111111]">
                        +{alternatives.length - 1}
                    </div>
                ) : null}
            </div>
        );
    };

    const renderClassicAlternativeLogo = (
        alternatives: Array<{ id: string; name: string }>,
    ) => {
        const hasMultipleAlternatives = alternatives.length > 1;

        if (!hasMultipleAlternatives) {
            return renderLogo(alternatives[0], layout.logoClass);
        }

        return (
            <div className={layout.logoClass}>
                <div className="grid h-full w-full grid-cols-2 place-items-center gap-2">
                    {alternatives.map((alternative) => (
                        <div
                            key={alternative.id}
                            className="aspect-square w-full overflow-hidden rounded-xl bg-white/5"
                        >
                            <Image
                                src={`/app-logos/${alternative.id}.jpg`}
                                alt={alternative.name}
                                width={0}
                                height={0}
                                sizes="120px"
                                className="h-full w-full object-contain"
                            />
                        </div>
                    ))}
                </div>
            </div>
        );
    };

    return (
        <div
            style={{
                display: "none",
                width: "1500px",
                height: "1500px",
                backgroundColor: "#121212",
                position: "relative",
                boxSizing: "border-box",
                overflow: "hidden",
                fontFamily: PRIVACY_PACK_FONT_FAMILY,
            }}
            id="privacy-pack-result-to-capture"
        >
            <div
                style={{
                    position: "absolute",
                    top: "48px",
                    left: "48px",
                    right: "55px",
                    height: "72px",
                }}
            >
                <div
                    style={{
                        position: "absolute",
                        left: "0",
                        top: "0",
                    }}
                >
                    <Image
                        src="/url-logo.png"
                        alt="PrivacyPack Logo"
                        width={474}
                        height={72}
                    />
                </div>

                <div
                    style={{
                        position: "absolute",
                        right: "0",
                        top: "-16px",
                        width: "130px",
                        height: "92px",
                    }}
                >
                    <Image
                        src="/small-logo.png"
                        alt="Privacy Pack logo"
                        width={0}
                        height={0}
                        sizes="100vw"
                        className="h-auto w-full"
                    />
                </div>
            </div>

            <div
                style={{
                    position: "absolute",
                    top: layout.gridTop,
                    left: "48px",
                    right: "48px",
                    display: "grid",
                    gridTemplateColumns: layout.gridTemplateColumns,
                    justifyContent: layout.justifyContent,
                    columnGap: layout.columnGap,
                    rowGap: layout.rowGap,
                    justifyItems:
                        layout.kind === "dense" ? "stretch" : "center",
                }}
            >
                {pack.map((item) => {
                    const alternatives = item.private_alternatives;
                    const hasMultipleAlternatives = alternatives.length > 1;

                    if (layout.kind === "dense") {
                        return (
                            <div
                                key={item.category}
                                className={`${layout.cardClass} flex flex-col`}
                            >
                                <div className="mb-2 text-center text-[12px] leading-none font-semibold text-[#777777]">
                                    {item.category}
                                </div>
                                <div className="flex min-h-0 flex-1 items-start justify-between gap-2">
                                    <div className="flex h-full w-[118px] min-w-0 flex-col items-center">
                                        {renderLogo(
                                            {
                                                id: item.mainstream_app_id,
                                                name: item.mainstream_app_name,
                                            },
                                            layout.logoClass,
                                        )}
                                        <div
                                            className={`${layout.textClass} mt-2 text-center leading-[1.12] break-words text-[#b7b7b7]`}
                                        >
                                            {item.mainstream_app_name}
                                        </div>
                                    </div>
                                    <div className="flex h-[72px] shrink-0 items-center pt-3">
                                        <ArrowRight
                                            size={layout.arrowSize}
                                            className="text-[#d8d8d8]"
                                        />
                                    </div>
                                    <div className="flex h-full w-[118px] min-w-0 flex-col items-center">
                                        {renderDenseAlternativeLogo(
                                            alternatives,
                                        )}
                                        <div
                                            className={`${
                                                hasMultipleAlternatives
                                                    ? layout.multiTextClass
                                                    : layout.textClass
                                            } mt-2 text-center leading-[1.12] break-words text-[#b7b7b7]`}
                                        >
                                            {getAlternativeLabel(
                                                alternatives,
                                                true,
                                            )}
                                        </div>
                                    </div>
                                </div>
                            </div>
                        );
                    }

                    return (
                        <div
                            key={item.category}
                            className={`${layout.cardClass} group relative flex flex-row items-center justify-between rounded-md transition`}
                        >
                            <div className="flex h-full flex-col items-center transition outline-none">
                                {renderLogo(
                                    {
                                        id: item.mainstream_app_id,
                                        name: item.mainstream_app_name,
                                    },
                                    layout.logoClass,
                                )}
                                <div
                                    className={`${layout.textClass} mt-3 text-center leading-tight break-words text-[#aeaeae]`}
                                >
                                    {item.mainstream_app_name}
                                </div>
                            </div>
                            <div className={layout.arrowClass}>
                                <ArrowRight
                                    size={layout.arrowSize}
                                    className="text-[#e6e6e6]"
                                />
                            </div>
                            <div className="flex h-full flex-col items-center transition outline-none">
                                {renderClassicAlternativeLogo(alternatives)}
                                <div
                                    className={`${
                                        hasMultipleAlternatives
                                            ? layout.multiTextClass
                                            : layout.textClass
                                    } mt-3 text-center leading-tight break-words text-[#aeaeae]`}
                                >
                                    {getAlternativeLabel(alternatives)}
                                </div>
                            </div>
                        </div>
                    );
                })}
            </div>
        </div>
    );
};

export default PrivacyPackResult;
