# Notes:
import sys
import json
from pathlib import Path
from typing import Any

# Add project root to sys.path (find the directory containing db_structs.py)
_root = Path(__file__).resolve().parent
while _root.parent != _root:
    if (_root / "db_structs.py").exists():
        if str(_root) not in sys.path:
            sys.path.append(str(_root))
        break
    _root = _root.parent

from db_structs import (
    Medium,
    Circle,
    Event,
    EventGroup,
    Source,
    ReliabilityTypes,
    OriginTypes,
    Location,
)

RT, OT = ReliabilityTypes, OriginTypes

PATH_HELPER = Path(__file__).parent
PATH_EVENT_GROUP = PATH_HELPER.parent
PATH_MEDIA = PATH_EVENT_GROUP / "media"


def retrieve_circles(event_name: str) -> list[Circle]:
    """Retrieve circles of given event. In the circle file has not been created, execute the creation script first."""
    circles_json_path = PATH_HELPER / event_name / "circles.json"
    if not circles_json_path.exists():
        print(
            f"Circle file for {event_name} not found, running the creation script ..."
        )
        creation_script_path = PATH_HELPER / event_name / "main.py"
        if not creation_script_path.exists():
            raise FileNotFoundError(
                f"Creation script for {event_name} not found at {creation_script_path}"
            )
        # Import main() from the creation script and execute
        import importlib.util

        spec = importlib.util.spec_from_file_location(
            f"{event_name}.main", creation_script_path
        )
        if spec and spec.loader:
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            if hasattr(module, "main"):
                module.main()

        if not circles_json_path.exists():
            raise FileNotFoundError(
                f"Creation script {creation_script_path} failed to create {circles_json_path}"
            )

    with circles_json_path.open("r", encoding="utf-8") as f:
        circles_raw = json.load(f)
    return [Circle.load_from_json(c) for c in circles_raw]


if __name__ == "__main__":
    events: list[Event] = []
    disabled_events: list[int | str] = []

    i = 1  # ==== twin_tail_carnival1 ====
    if i not in disabled_events:
        event_name = f"twin_tail_carnival{i}"
        print(f"Processing {event_name} ...")

        media_ = [
            Medium(
                "01_ttc.jpg",
                [
                    Source(
                        "https://web.archive.org/web/20050403174957/http://ttc.ket.jp/",
                        (RT.Reliable, OT.Official),
                    )
                ],
                comments="「ツインテールカーニバル」チラシ絵：やまさきともや 様 （脱力小隊）",
            ),
            Medium(
                "01_ttc-hyoushi.jpg",
                [
                    Source(
                        "https://web.archive.org/web/20051001032056/http://ttc.ket.jp/",
                        (RT.Reliable, OT.Official),
                    )
                ],
                comments="両イベント共通カタログ・ ツインテールカーニバル側 カタログ表紙 みずきほたる 様 （とぅいんくるはーと。）",
            ),
            # Medium("", [Source("", (RT.Reliable, OT.Official))]),
            # Medium("", [Source("", (RT.Reliable, OT.Official))]),
        ]
        locations = [
            Location(
                coordinates=(35.1590924, 136.9298891),
                address="2 Chome-6-3 Fukiage, Chikusa Ward, Nagoya, Aichi 464-0856, Japan",
                description="名古屋中小企業福祉会館６階ホール",
                sources=[
                    Source(
                        "https://web.archive.org/web/20050111161811/http://ttc.ket.jp/",
                        (ReliabilityTypes.Reliable, OriginTypes.Official),
                    )
                ],
                # comments=None,
                imageUrl="https://lh3.googleusercontent.com/gps-cs-s/AHRPTWkq7ADwtY0_LzlU3mk0DFlmJeNo1bo9bpZ2vqyiopbdHLCB4zA_pSkSpa9YKGQsJgPRhkx6a0R8e8OPBlstCq-5saYTJ5-avtnX6fZR-cI6YHIZgV7pYeOLMsw_PDlSU2wW-9f9=s0?imgmax=0",
                url="https://maps.app.goo.gl/5QerDbUB3hz5Xcjq9",
            ),
        ]
        event = Event(
            aliases=[
                "ツインテールカーニバル",
                "Twin Tail Carnival",
                "ツインテールカーニバル1",
                "Twin Tail Carnival 1",
            ],
            dates="2005.09.11",
            circles=[],
            media=media_,
            sources=[
                Source(
                    "Date: https://web.archive.org/web/20050111161811/http://ttc.ket.jp/",
                    (RT.Reliable, OT.Official),
                ),
                Source(
                    "Participating circles: https://web.archive.org/web/20051108010215/http://moeca.ket.jp/moca-ttc-list.htm",
                    (RT.Reliable, OT.Official),
                ),
            ],
            locations=locations,
            description="Simultaneous with もえたんカーニバル",
            # comments=None,
            last_edited="2026.10.30",
        )

        # Retrieve circles
        event.circles = retrieve_circles(event_name)
        events.append(event)

    i = "dear_my_heart"  # ==== twin_tail_carnivaldear_my_heart ====
    if i not in disabled_events:
        event_name = f"twin_tail_carnival{i}"
        print(f"Processing {event_name} ...")

        media_ = [
            Medium(
                "dear_my_heart_dmh.jpg",
                [
                    Source(
                        "https://web.archive.org/web/20051108094942/http://ttc.ket.jp/",
                        (RT.Reliable, OT.Official),
                    )
                ],
                comments="「Dear My Heart ～ツインテールカーニバル番外編～」 チラシ絵 小出 豊 様 （しうまいを継ぐ者）",
            ),
            Medium(
                "dear_my_heart_dmh-hyoushi.jpg",
                [
                    Source(
                        "https://web.archive.org/web/20060304011557/http://ttc.ket.jp/",
                        (RT.Reliable, OT.Official),
                    )
                ],
                comments="「Dear My Heart ～ツインテールカーニバル番外編～」 カタログ表紙絵 Sw 様 （・がろん）",
            ),
            Medium(
                "dear_my_heart_dmh-bn1.jpg",
                [
                    Source(
                        "https://web.archive.org/web/20070729051151/http://ttc.ket.jp/",
                        (RT.Reliable, OT.Official),
                    )
                ],
            ),
            # Medium("", [Source("", (RT.Reliable, OT.Official))]),
            # Medium("", [Source("", (RT.Reliable, OT.Official))]),
        ]
        locations = [
            Location(
                coordinates=(35.655153, 139.7607689),
                address="Japan, 〒105-7501 Tokyo, Minato City, Kaigan, 1 Chome−7−1 東京ポートシティ竹芝オフィスタワ",
                comments=None,
                description="都立産業貿易センター浜松町館５階",
                sources=[
                    Source(
                        "https://web.archive.org/web/20070506195502/http://ttc.ket.jp/dmh-list.htm",
                        (ReliabilityTypes.Reliable, OriginTypes.Official),
                    )
                ],
                imageUrl="https://lh3.googleusercontent.com/gps-cs-s/AHRPTWmihIGbPitN7h8Vc_sXo8I679FTgrlkYst2LWaAy_Wl45MDqMaFnozSO4Y2Vud8h07FgRpXdq_CPW3IWnFwj-AyKuJ0L7ShZyQ41TQcBAFNOouYZR3jFZXxn_SQsgsK-FST-5JK8g=w408-h544-k-no",
                url="https://maps.app.goo.gl/ZF8XaGQinUTwnNMw6",
            ),
        ]
        event = Event(
            aliases=[
                "Dear My Heart ～ツインテールカーニバル番外編～",
                "Dear My Heart ~Twin Tail Carnival Extra Edition~",
            ],
            dates="2006.03.21",
            circles=[],
            media=media_,
            sources=[
                Source(
                    "Date: https://web.archive.org/web/20060304011557/http://ttc.ket.jp/",
                    (RT.Reliable, OT.Official),
                ),
                Source(
                    "Participating circles: https://web.archive.org/web/20070506195502/http://ttc.ket.jp/dmh-list.htm",
                    (RT.Reliable, OT.Official),
                ),
            ],
            locations=locations,
            description="Simultaneous with つくケット　～タイガー道場の怪～",
            # comments=None,
            last_edited="2026.10.30",
        )

        # Retrieve circles
        event.circles = retrieve_circles(event_name)
        events.append(event)

    i = 2  # ==== twin_tail_carnival2 ====
    if i not in disabled_events:
        event_name = f"twin_tail_carnival{i}"
        print(f"Processing {event_name} ...")

        media_ = [
            Medium(
                "02_ttc2.jpg",
                [
                    Source(
                        "https://web.archive.org/web/20060815030106/http://ttc.ket.jp/",
                        (RT.Reliable, OT.Official),
                    )
                ],
                comments="ツインテールカーニバル２ チラシ絵 10mo 様 （雑踏景色）",
            ),
            Medium(
                "02_ttc2-hyoushi.jpg",
                [
                    Source(
                        "https://web.archive.org/web/20060821235220/http://ttc.ket.jp/",
                        (RT.Reliable, OT.Official),
                    )
                ],
                comments="ツインテールカーニバル２ カタログ表紙 まっぷ 様 （BLUE CATTY）\n「ツインテールカーニバル２」「絶対領域３」共通カタログのツインテールカーニバル側の表紙です",
            ),
            # Medium("", [Source("", (RT.Reliable, OT.Official))]),
            # Medium("", [Source("", (RT.Reliable, OT.Official))]),
        ]
        locations = [
            Location(
                coordinates=(34.7355454, 135.4914229),
                address="2 Chome-2-2 Nishimiyahara, Yodogawa Ward, Osaka, 532-0004, Japan",
                description="新大阪センイシティ２号館５階展示場",
                sources=[
                    Source(
                        "https://web.archive.org/web/20070506195604/http://ttc.ket.jp/ttc02-list.htm",
                        (ReliabilityTypes.Reliable, OriginTypes.Official),
                    )
                ],
                # comments=None,
                imageUrl="https://lh3.googleusercontent.com/gps-cs-s/ANWiy9TD5ZxYDtclsLXFDQRPoy69FqVPCPqeniwGyAUf3N68_g8q8EWVmd9nhEuvLkTrJ9EKhbYs8247tOzKA_bQx2VOFwcrRrH23KoXweXaxs4_AIxCtaSm4smXLSYOd2jWQDIkwmNLutiJ-zcg=s0?imgmax=0",
                url="https://maps.app.goo.gl/vhxPykERA7vdhLPs7",
            ),
        ]
        event = Event(
            aliases=["ツインテールカーニバル2", "Twin Tail Carnival 2"],
            dates="2006.09.24",
            circles=[],
            media=media_,
            sources=[
                Source(
                    "Date: https://web.archive.org/web/20060821235220/http://ttc.ket.jp/",
                    (RT.Reliable, OT.Official),
                ),
                Source(
                    "Participating circles: https://web.archive.org/web/20070506195604/http://ttc.ket.jp/ttc02-list.htm",
                    (RT.Reliable, OT.Official),
                ),
            ],
            locations=locations,
            description="Simultaneous with 絶対領域３",
            # comments=None,
            last_edited="2026.10.30",
        )

        # Retrieve circles
        event.circles = retrieve_circles(event_name)
        events.append(event)

    i = 3  # ==== twin_tail_carnival3 ====
    if i not in disabled_events:
        event_name = f"twin_tail_carnival{i}"
        print(f"Processing {event_name} ...")

        media_ = [
            Medium(
                "03_ttc03a.jpg",
                [
                    Source(
                        "https://web.archive.org/web/20070126012914/http://ttc.ket.jp/",
                        (RT.Reliable, OT.Official),
                    )
                ],
                comments="ツインテールカーニバル３ チラシ絵 梱枝りこ 様 （無人少女）",
            ),
            Medium(
                "03_ttc03-hyoushi.jpg",
                [
                    Source(
                        "https://web.archive.org/web/20070306120044/http://ttc.ket.jp/",
                        (RT.Reliable, OT.Official),
                    )
                ],
                comments="ツインテールカーニバル３ カタログ表紙 月音 様 （月音文庫）",
            ),
            Medium(
                "03_ttc03-ura.jpg",
                [
                    Source(
                        "https://web.archive.org/web/20070306120044/http://ttc.ket.jp/",
                        (RT.Reliable, OT.Official),
                    )
                ],
                comments="ツインテールカーニバル３ カタログ裏表紙 青山明日香 様 （CANDY）",
            ),
            # Medium("", [Source("", (RT.Reliable, OT.Official))]),
            # Medium("", [Source("", (RT.Reliable, OT.Official))]),
        ]
        locations = [
            Location(
                coordinates=(35.6973454, 139.7715879),
                address="Japan, 〒101-0025 Tokyo, Chiyoda City, Kanda Sakumacho, 1 Chome−９−9 東京都産業労働局秋葉原庁舎",
                description="東京都中小企業振興公社秋葉原庁舎・展示室",
                sources=[
                    Source(
                        "https://web.archive.org/web/20070306120044/http://ttc.ket.jp/",
                        (ReliabilityTypes.Reliable, OriginTypes.Official),
                    )
                ],
                # comments=None,
                imageUrl="https://lh3.googleusercontent.com/gps-cs-s/ANWiy9RX9DU0y55wJB6uErH6-nbM1b_bFjZAWucNB_TFGaCeqQhPISfW4qEJPDm4WZG1n3JeRiK3jOSpOr4140aBLpVGlogodgcMABfwZnhSz7CdmsUBztioWRTuVofBYZeKpVk5AILp=s0?imgmax=0",
                url="https://maps.app.goo.gl/PZSApdWJpQ9CyxsG9",
            ),
        ]
        event = Event(
            aliases=["ツインテールカーニバル3", "Twin Tail Carnival 3"],
            dates="2007.03.04",
            circles=[],
            media=media_,
            sources=[
                Source(
                    "Date: https://web.archive.org/web/20070306120044/http://ttc.ket.jp/",
                    (RT.Reliable, OT.Official),
                ),
                Source(
                    "Participating circles: https://web.archive.org/web/20070729051916/http://ttc.ket.jp/ttc03-list.htm",
                    (RT.Reliable, OT.Official),
                ),
            ],
            locations=locations,
            description="Simultaneous with リリカルハート and まきますか？まきませんか？ex",
            # comments=None,
            last_edited="2026.10.30",
        )

        # Retrieve circles
        event.circles = retrieve_circles(event_name)
        events.append(event)

    i = 4  # ==== twin_tail_carnival4 ====
    if i not in disabled_events:
        event_name = f"twin_tail_carnival{i}"
        print(f"Processing {event_name} ...")

        media_ = [
            # Medium("", [Source("", (RT.Reliable, OT.Official))]),
            # Medium("", [Source("", (RT.Reliable, OT.Official))]),
            # Medium("", [Source("", (RT.Reliable, OT.Official))]),
        ]
        locations = [
            Location(
                coordinates=(35.1590924, 136.9298891),
                address="2 Chome-6-3 Fukiage, Chikusa Ward, Nagoya, Aichi 464-0856, Japan",
                description="名古屋中小企業福利会館６階ホール",
                sources=[
                    Source(
                        "https://web.archive.org/web/20080213212822/http://ttc.ninja-web.net/ttc04-list.htm",
                        (ReliabilityTypes.Reliable, OriginTypes.Official),
                    )
                ],
                # comments=None,
                imageUrl="https://lh3.googleusercontent.com/gps-cs-s/AHRPTWkq7ADwtY0_LzlU3mk0DFlmJeNo1bo9bpZ2vqyiopbdHLCB4zA_pSkSpa9YKGQsJgPRhkx6a0R8e8OPBlstCq-5saYTJ5-avtnX6fZR-cI6YHIZgV7pYeOLMsw_PDlSU2wW-9f9=s0?imgmax=0",
                url="https://maps.app.goo.gl/5QerDbUB3hz5Xcjq9",
            ),
        ]
        event = Event(
            aliases=["ツインテールカーニバル4", "Twin Tail Carnival 4"],
            dates="2008.03.09",
            circles=[],
            media=media_,
            sources=[
                Source(
                    "Date: https://web.archive.org/web/20080217015949/http://ttc.ninja-web.net/",
                    (RT.Reliable, OT.Official),
                ),
                Source(
                    "Participating circles: https://web.archive.org/web/20080213212822/http://ttc.ninja-web.net/ttc04-list.htm",
                    (RT.Reliable, OT.Official),
                ),
            ],
            locations=locations,
            description=None,
            # comments=None,
            last_edited="2026.10.30",
        )

        # Retrieve circles
        event.circles = retrieve_circles(event_name)
        events.append(event)

    i = 5  # ==== twin_tail_carnival5 ====
    if i not in disabled_events:
        event_name = f"twin_tail_carnival{i}"
        print(f"Processing {event_name} ...")

        media_ = [
            # Medium("", [Source("", (RT.Reliable, OT.Official))]),
            # Medium("", [Source("", (RT.Reliable, OT.Official))]),
            # Medium("", [Source("", (RT.Reliable, OT.Official))]),
        ]
        locations = [
            Location(
                coordinates=(34.7355454, 135.4914229),
                address="2 Chome-2-2 Nishimiyahara, Yodogawa Ward, Osaka, 532-0004, Japan",
                description="新大阪センイシティ２号館５階展示場",
                sources=[
                    Source(
                        "https://web.archive.org/web/20090221025220/http://ttc.ninja-web.net/",
                        (ReliabilityTypes.Reliable, OriginTypes.Official),
                    )
                ],
                # comments=None,
                imageUrl="https://lh3.googleusercontent.com/gps-cs-s/ANWiy9TD5ZxYDtclsLXFDQRPoy69FqVPCPqeniwGyAUf3N68_g8q8EWVmd9nhEuvLkTrJ9EKhbYs8247tOzKA_bQx2VOFwcrRrH23KoXweXaxs4_AIxCtaSm4smXLSYOd2jWQDIkwmNLutiJ-zcg=s0?imgmax=0",
                url="https://maps.app.goo.gl/vhxPykERA7vdhLPs7",
            ),
        ]
        event = Event(
            aliases=["ツインテールカーニバル5", "Twin Tail Carnival 5"],
            dates="2009.05.06",
            circles=[],
            media=media_,
            sources=[
                Source(
                    "Date: https://web.archive.org/web/20090221025220/http://ttc.ninja-web.net/",
                    (RT.Reliable, OT.Official),
                ),
                Source(
                    "Participating circles: https://web.archive.org/web/20150521042247/http://ttc.ninja-web.net/ztp/ztp-list.htm",
                    (RT.Reliable, OT.Official),
                ),
            ],
            locations=locations,
            description="Part of the 絶対領域６×ツインテールカーニバル５×ポニケット２ joint event",
            # comments=None,
            last_edited="2026.10.30",
        )

        # Retrieve circles
        event.circles = retrieve_circles(event_name)
        events.append(event)

    i = 6  # ==== twin_tail_carnival6 ====
    if i not in disabled_events:
        event_name = f"twin_tail_carnival{i}"
        print(f"Processing {event_name} ...")

        media_ = [
            Medium(
                "06_ttc06-hyoushi.jpg",
                [
                    Source(
                        "https://web.archive.org/web/20111125010232/http://ttc.ninja-web.net/",
                        (RT.Reliable, OT.Official),
                    )
                ],
                comments="ツインテールカーニバル６カタログ表紙絵 … ナナセミオリ 様 （山猫BOX）",
            ),
            # Medium("", [Source("", (RT.Reliable, OT.Official))]),
            # Medium("", [Source("", (RT.Reliable, OT.Official))]),
        ]
        locations = [
            Location(
                coordinates=(35.1708859, 136.8837218),
                address="4-chōme-4-38 Meieki, Nakamura Ward, Nagoya, Aichi 450-0002, Japan",
                description="愛知県産業労働センター（ウインクあいち）７階展示場",
                sources=[
                    Source(
                        "https://web.archive.org/web/20111125010232/http://ttc.ninja-web.net/",
                        (ReliabilityTypes.Reliable, OriginTypes.Official),
                    )
                ],
                # comments=None,
                imageUrl="https://streetviewpixels-pa.googleapis.com/v1/thumbnail?output=thumbnail&cb_client=maps_sv.tactile.gps&panoid=plEI7dd2WTUE58egOJKX3g&w=1177&h=1300&yaw=170&pitch=-40",
                url="https://maps.app.goo.gl/6F2N7Dtys66bRMQQ9",
            ),
        ]
        event = Event(
            aliases=["ツインテールカーニバル6", "Twin Tail Carnival 6"],
            dates="2009.11.22",
            circles=[],
            media=media_,
            sources=[
                Source(
                    "Date: https://web.archive.org/web/20111125010232/http://ttc.ninja-web.net/",
                    (RT.Reliable, OT.Official),
                ),
                # Source("Participating circles: ", (RT.Reliable, OT.Official)),
            ],
            locations=locations,
            description=None,
            # comments=None,
            last_edited="2026.10.30",
        )

        # Retrieve circles
        # event.circles = retrieve_circles(event_name)
        events.append(event)

    i = 7  # ==== twin_tail_carnival7 ====
    if i not in disabled_events:
        event_name = f"twin_tail_carnival{i}"
        print(f"Processing {event_name} ...")

        media_ = [
            Medium(
                "07_ttc07.jpg",
                [
                    Source(
                        "https://web.archive.org/web/20150815144329/http://ttc.ninja-web.net/",
                        (RT.Reliable, OT.Official),
                    )
                ],
                comments="TTC７チラシ絵 伽藍快（ときあいはや）様 （ENJOY MIX）",
            ),
            # Medium("", [Source("", (RT.Reliable, OT.Official))]),
            # Medium("", [Source("", (RT.Reliable, OT.Official))]),
        ]
        locations = [
            Location(
                coordinates=(35.1313699, 136.8980176),
                address="1-1 Atsuta Nishimachi, Atsuta Ward, Nagoya, Aichi 456-0036, Japan",
                description="名古屋国際会議場　白鳥ホール",
                sources=[
                    Source(
                        "https://web.archive.org/web/20131028093922/http://ttc.ninja-web.net/",
                        (ReliabilityTypes.Reliable, OriginTypes.Official),
                    )
                ],
                # comments=None,
                imageUrl="https://lh3.googleusercontent.com/gps-cs-s/AHRPTWn7Lqm9_Q0NEdha1ASXnQ5vdfjHbPJAbiquEME-dTc0IQlVMwwldl4PgCGmoqwXy7f1H0VzeeQ34Sfh31dwy-yLo6SG1i6J7RxOt2LCAXGM3sea6CVPSdGtLv8BqQvcjQ9wGbdq8g=s0?imgmax=0",
                url="https://maps.app.goo.gl/WvWpsu1s7P6fTsdj9",
            ),
        ]
        event = Event(
            aliases=["ツインテールカーニバル7", "Twin Tail Carnival 7"],
            dates="2014.01.26 → 2014.09.21",
            circles=[],
            media=media_,
            sources=[
                Source(
                    "Date and postpone: https://web.archive.org/web/20131028093922/http://ttc.ninja-web.net/",
                    (RT.Reliable, OT.Official),
                ),
                Source(
                    "Participating circles: https://web.archive.org/web/20150711170514/http://ttc.ninja-web.net/ttc07-list.htm",
                    (RT.Reliable, OT.Official),
                ),
            ],
            locations=locations,
            description="Simultaneous with 雛見沢村民集会・絆, Keyパーティー6 and 結月家の食卓",
            # comments=None,
            last_edited="2026.10.31",
        )

        # Retrieve circles
        event.circles = retrieve_circles(event_name)
        events.append(event)

    i = 8  # ==== twin_tail_carnival8 ====
    if i not in disabled_events:
        event_name = f"twin_tail_carnival{i}"
        print(f"Processing {event_name} ...")

        media_ = [
            Medium(
                "08_ttc08.jpg",
                [
                    Source(
                        "https://web.archive.org/web/20170628131625/http://ttc.ninja-web.net/",
                        (RT.Reliable, OT.Official),
                    )
                ],
                comments="TTC８＆制服宣言チラシ絵　ふじの芳夏 様（PERFECT SEA）",
            ),
            Medium(
                "08_161002_layout.pdf",
                [
                    Source(
                        "https://web.archive.org/web/20170309032500/http://ttc.ninja-web.net/ttc08-list.htm",
                        (RT.Reliable, OT.Official),
                    )
                ],
            ),
            # Medium("", [Source("", (RT.Reliable, OT.Official))]),
            # Medium("", [Source("", (RT.Reliable, OT.Official))]),
        ]
        locations = [
            Location(
                coordinates=(35.1313699, 136.8980176),
                address="1-1 Atsuta Nishimachi, Atsuta Ward, Nagoya, Aichi 456-0036, Japan",
                description="名古屋国際会議場 イベントホール",
                sources=[
                    Source(
                        "https://web.archive.org/web/20170628131625/http://ttc.ninja-web.net/",
                        (ReliabilityTypes.Reliable, OriginTypes.Official),
                    )
                ],
                # comments=None,
                imageUrl="https://lh3.googleusercontent.com/gps-cs-s/AHRPTWn7Lqm9_Q0NEdha1ASXnQ5vdfjHbPJAbiquEME-dTc0IQlVMwwldl4PgCGmoqwXy7f1H0VzeeQ34Sfh31dwy-yLo6SG1i6J7RxOt2LCAXGM3sea6CVPSdGtLv8BqQvcjQ9wGbdq8g=s0?imgmax=0",
                url="https://maps.app.goo.gl/WvWpsu1s7P6fTsdj9",
            ),
        ]
        event = Event(
            aliases=["ツインテールカーニバル8", "Twin Tail Carnival 8"],
            dates="2016.10.02",
            circles=[],
            media=media_,
            sources=[
                Source(
                    "Date: https://web.archive.org/web/20170628131625/http://ttc.ninja-web.net/",
                    (RT.Reliable, OT.Official),
                ),
                Source(
                    "Participating circles: https://web.archive.org/web/20170309032500/http://ttc.ninja-web.net/ttc08-list.htm",
                    (RT.Reliable, OT.Official),
                ),
            ],
            locations=locations,
            description="Part of the ツインテールカーニバル８＆制服宣言 joint venue, also simultaneous with VOCALOID PARADISE 11, ゆかりPARADISE, モジュールPARADISE２, カゲロウパラダイス２ and ずんだぱ～てぃ３（み!）",
            # comments=None,
            last_edited="2026.10.31",
        )

        # Retrieve circles
        event.circles = retrieve_circles(event_name)
        events.append(event)

    i = 9  # ==== twin_tail_carnival9 ====
    if i not in disabled_events:
        event_name = f"twin_tail_carnival{i}"
        print(f"Processing {event_name} ...")

        media_ = [
            Medium(
                "09_ttc09.jpg",
                [
                    Source(
                        "https://web.archive.org/web/20190612181841/http://ttc.ninja-web.net/",
                        (RT.Reliable, OT.Official),
                    )
                ],
                comments="TTC９・制服宣言２・絶対ニーソ・百合乙女の楽園 チラシ絵 朝倉亮 様（水無月亭）",
            ),
            # Medium("", [Source("", (RT.Reliable, OT.Official))]),
            # Medium("", [Source("", (RT.Reliable, OT.Official))]),
        ]
        locations = [
            Location(
                coordinates=(35.1313699, 136.8980176),
                address="1-1 Atsuta Nishimachi, Atsuta Ward, Nagoya, Aichi 456-0036, Japan",
                description="名古屋国際会議場 白鳥ホール",
                sources=[
                    Source(
                        "https://web.archive.org/web/20190612181841/http://ttc.ninja-web.net/",
                        (ReliabilityTypes.Reliable, OriginTypes.Official),
                    )
                ],
                # comments=None,
                imageUrl="https://lh3.googleusercontent.com/gps-cs-s/AHRPTWn7Lqm9_Q0NEdha1ASXnQ5vdfjHbPJAbiquEME-dTc0IQlVMwwldl4PgCGmoqwXy7f1H0VzeeQ34Sfh31dwy-yLo6SG1i6J7RxOt2LCAXGM3sea6CVPSdGtLv8BqQvcjQ9wGbdq8g=s0?imgmax=0",
                url="https://maps.app.goo.gl/WvWpsu1s7P6fTsdj9",
            ),
        ]
        event = Event(
            aliases=["ツインテールカーニバル9", "Twin Tail Carnival 9"],
            dates="2018.11.04",
            circles=[],
            media=media_,
            sources=[
                Source(
                    "Date: https://web.archive.org/web/20190612181841/http://ttc.ninja-web.net/",
                    (RT.Reliable, OT.Official),
                ),
                # Source("Participating circles: ", (RT.Reliable, OT.Official)),
                Source(
                    "Joint venue: https://web.archive.org/web/20190408141004/http://ttc.ninja-web.net/nagoya-doujin-fes/circle_list.htm",
                    (RT.Reliable, OT.Official),
                ),
            ],
            locations=locations,
            description="Part of the 名古屋熱田同人祭2018秋 joint venue, which also features 艦隊ぱれーど２, 御城まつり, 月下の祭典Returns, アズールフェスタ, BanG Dreamer's Party! in 名古屋 and 魔法少女本作製計画SP",
            # comments=None,
            last_edited="2026.10.31",
        )

        # Retrieve circles
        # event.circles = retrieve_circles(event_name)
        events.append(event)

    i = 10  # ==== twin_tail_carnival10 ====
    if i not in disabled_events:
        event_name = f"twin_tail_carnival{i}"
        print(f"Processing {event_name} ...")

        media_ = [
            Medium(
                "10_ttc10.jpg",
                [
                    Source(
                        "https://web.archive.org/web/20200628221937/http://ttc.ninja-web.net/",
                        (RT.Reliable, OT.Official),
                    )
                ],
                comments="メインビジュアル（チラシ絵）　ササキシオリ 様（しおさいと。）",
            ),
            # Medium("", [Source("", (RT.Reliable, OT.Official))]),
            # Medium("", [Source("", (RT.Reliable, OT.Official))]),
        ]
        locations = [
            Location(
                coordinates=(35.1708859, 136.8837218),
                address="4-chōme-4-38 Meieki, Nakamura Ward, Nagoya, Aichi 450-0002, Japan",
                description="名古屋企業福祉会館",
                sources=[
                    Source(
                        "https://web.archive.org/web/20200628221937/http://ttc.ninja-web.net/",
                        (ReliabilityTypes.Reliable, OriginTypes.Official),
                    )
                ],
                # comments=None,
                imageUrl="https://streetviewpixels-pa.googleapis.com/v1/thumbnail?output=thumbnail&cb_client=maps_sv.tactile.gps&panoid=plEI7dd2WTUE58egOJKX3g&w=1177&h=1300&yaw=170&pitch=-40",
                url="https://maps.app.goo.gl/6F2N7Dtys66bRMQQ9",
            ),
        ]
        event = Event(
            aliases=["ツインテールカーニバル10", "Twin Tail Carnival 10"],
            dates="2020.08.23 → CANCELLED",
            circles=[],
            media=media_,
            sources=[
                Source(
                    "Date: https://web.archive.org/web/20200628221937/http://ttc.ninja-web.net/",
                    (RT.Reliable, OT.Official),
                ),
                Source(
                    "Cancelled: https://x.com/ttc_doujin/status/1290279699688505346",
                    (RT.Reliable, OT.OfficialExt),
                ),
            ],
            locations=locations,
            description="Simultaneous with Augustic Memories 2 and ゆずソフトパーティー",
            # comments=None,
            last_edited="2026.10.31",
        )

        # Retrieve circles
        # event.circles = retrieve_circles(event_name)
        events.append(event)

    # i =   # ==== twin_tail_carnival ====
    # if i not in disabled_events:
    #     event_name = f"twin_tail_carnival{i}"
    #     print(f"Processing {event_name} ...")

    #     media_ = [
    #         # Medium("", [Source("", (RT.Reliable, OT.Official))]),
    #         # Medium("", [Source("", (RT.Reliable, OT.Official))]),
    #         # Medium("", [Source("", (RT.Reliable, OT.Official))]),
    #     ]
    #     locations = [
    #         # Location(
    #         #     coordinates=(,),
    #         #     address="",
    #         #     description="",
    #         #     sources=[Source("", (ReliabilityTypes.Reliable, OriginTypes.Official))],
    #         #     # comments=None,
    #         #     imageUrl="",
    #         #     url="",
    #         # ),
    #     ]
    #     event = Event(
    #         # aliases=["ツインテールカーニバル", "Twin Tail Carnival "],
    #         dates="",
    #         circles=[],
    #         media=media_,
    #         sources=[
    #             # Source("Date: ", (RT.Reliable, OT.Official)),
    #             # Source("Participating circles: ", (RT.Reliable, OT.Official)),
    #         ],
    #         locations=locations,
    #         description=None,
    #         # comments=None,
    #         last_edited="2026.10.31",
    #     )

    #     # Retrieve circles
    #     # event.circles = retrieve_circles(event_name)
    #     events.append(event)

    # ==== event group ====
    media = [
        Medium(
            "eg_ttc-bn01.jpg",
            [
                Source(
                    "https://web.archive.org/web/20070729051151/http://ttc.ket.jp/",
                    (RT.Reliable, OT.Official),
                )
            ],
        ),
        Medium(
            "eg_ttc-bn02.jpg",
            [
                Source(
                    "https://web.archive.org/web/20070729051151/http://ttc.ket.jp/",
                    (RT.Reliable, OT.Official),
                )
            ],
        ),
        Medium(
            "eg_ttc-bn03.jpg",
            [
                Source(
                    "https://web.archive.org/web/20070729051151/http://ttc.ket.jp/",
                    (RT.Reliable, OT.Official),
                )
            ],
        ),
        Medium(
            "eg_ttc-bn04.jpg",
            [
                Source(
                    "https://web.archive.org/web/20070729051151/http://ttc.ket.jp/",
                    (RT.Reliable, OT.Official),
                )
            ],
        ),
        Medium(
            "05_ttc-bn05.jpg",
            [
                Source(
                    "https://web.archive.org/web/20080217015949/http://ttc.ninja-web.net/",
                    (RT.Reliable, OT.Official),
                )
            ],
        ),
        Medium(
            "eg_ttc-bn06.jpg",
            [
                Source(
                    "https://web.archive.org/web/20080217015949/http://ttc.ninja-web.net/",
                    (RT.Reliable, OT.Official),
                )
            ],
        ),
        # Medium("",
        #        [Source("", (RT.Reliable, OT.Official))]),
        # Medium("",
        #        [Source("", (RT.Reliable, OT.Official))]),
    ]
    links = [
        "http://ttc.ket.jp/",
        "http://ttc.ninja-web.net/",
        "https://x.com/ttc_doujin",
    ]

    event_group = EventGroup(
        aliases=[
            "ツインテールカーニバル",
            "Twin Tail Carnival",
            "TTC",
        ],
        events=events,
        media=media,
        links=links,
        sources=[
            Source(
                "Circle lists of all events: https://web.archive.org/web/20150711170344/http://ttc.ninja-web.net/event-list.htm",
                (ReliabilityTypes.Reliable, OriginTypes.Official),
            ),
            Source(
                'Alias "TTC": from url and as shown here for example https://web.archive.org/web/20130504130836/http://ttc.ninja-web.net/',
                (ReliabilityTypes.Reliable, OriginTypes.Official),
            ),
        ],
        comments=None,
        description=None,
        last_edited="2026.10.31",
    )

    print(f"Saving {Path(__file__).stem} database...")
    event_group.save(PATH_EVENT_GROUP, indent=None)
    print("Done")
