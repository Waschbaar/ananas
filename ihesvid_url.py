# Usage: ihesvid_url video_number time
#   video_number: integer 1-24
#   time: string [hh:]mm:ss
# Output: the URL pointing to the time in the video playlist

import argparse

video_urls = [
    "https://www.youtube.com/watch?v=YxSZ1mTIpaA&list=PLx5f8IelFRgGmu6gmL-Kf_Rl_6Mm7juZO",
    "https://www.youtube.com/watch?v=_4G582SIo28&list=PLx5f8IelFRgGmu6gmL-Kf_Rl_6Mm7juZO&index=2",
    "https://www.youtube.com/watch?v=me1KNo3WJHE&list=PLx5f8IelFRgGmu6gmL-Kf_Rl_6Mm7juZO&index=3",
    "https://www.youtube.com/watch?v=EW39K0J7Hqo&list=PLx5f8IelFRgGmu6gmL-Kf_Rl_6Mm7juZO&index=4",
    "https://www.youtube.com/watch?v=bdQ-_CZ5tl8&list=PLx5f8IelFRgGmu6gmL-Kf_Rl_6Mm7juZO&index=5",
    "https://www.youtube.com/watch?v=KKzt6C9ggWA&list=PLx5f8IelFRgGmu6gmL-Kf_Rl_6Mm7juZO&index=6",
    "https://www.youtube.com/watch?v=fUjn2rGw9SA&list=PLx5f8IelFRgGmu6gmL-Kf_Rl_6Mm7juZO&index=7",
    "https://www.youtube.com/watch?v=dIwBTJNN7a0&list=PLx5f8IelFRgGmu6gmL-Kf_Rl_6Mm7juZO&index=8",
    "https://www.youtube.com/watch?v=lJTLj8gYAtg&list=PLx5f8IelFRgGmu6gmL-Kf_Rl_6Mm7juZO&index=9",
    "https://www.youtube.com/watch?v=YLQt_tV4tHo&list=PLx5f8IelFRgGmu6gmL-Kf_Rl_6Mm7juZO&index=10",
    "https://www.youtube.com/watch?v=87-wuqGA8GE&list=PLx5f8IelFRgGmu6gmL-Kf_Rl_6Mm7juZO&index=11",
    "https://www.youtube.com/watch?v=VMgZSP9sRdo&list=PLx5f8IelFRgGmu6gmL-Kf_Rl_6Mm7juZO&index=12",
    "https://www.youtube.com/watch?v=38PzTzCiMow&list=PLx5f8IelFRgGmu6gmL-Kf_Rl_6Mm7juZO&index=13",
    "https://www.youtube.com/watch?v=krq6jCy-dhE&list=PLx5f8IelFRgGmu6gmL-Kf_Rl_6Mm7juZO&index=14",
    "https://www.youtube.com/watch?v=EEH_0QhrgEg&list=PLx5f8IelFRgGmu6gmL-Kf_Rl_6Mm7juZO&index=15",
    "https://www.youtube.com/watch?v=BV0-dlAuS3U&list=PLx5f8IelFRgGmu6gmL-Kf_Rl_6Mm7juZO&index=16",
    "https://www.youtube.com/watch?v=rN_iM7Z8vdE&list=PLx5f8IelFRgGmu6gmL-Kf_Rl_6Mm7juZO&index=17",
    "https://www.youtube.com/watch?v=vRUmXU8ijIk&list=PLx5f8IelFRgGmu6gmL-Kf_Rl_6Mm7juZO&index=18",
    "https://www.youtube.com/watch?v=T9XhPCI8828&list=PLx5f8IelFRgGmu6gmL-Kf_Rl_6Mm7juZO&index=19",
    "https://www.youtube.com/watch?v=wk_wInYTasQ&list=PLx5f8IelFRgGmu6gmL-Kf_Rl_6Mm7juZO&index=20",
    "https://www.youtube.com/watch?v=R5JNomeHjtI&list=PLx5f8IelFRgGmu6gmL-Kf_Rl_6Mm7juZO&index=21",
    "https://www.youtube.com/watch?v=fnEPiDIF9_k&list=PLx5f8IelFRgGmu6gmL-Kf_Rl_6Mm7juZO&index=22",
    "https://www.youtube.com/watch?v=vXZC3WzKZgo&list=PLx5f8IelFRgGmu6gmL-Kf_Rl_6Mm7juZO&index=23",
    "https://www.youtube.com/watch?v=YKw1XaueLJY&list=PLx5f8IelFRgGmu6gmL-Kf_Rl_6Mm7juZO&index=24"
]

parser = argparse.ArgumentParser("ihesvid_url")
parser.add_argument("video_number", help = "The index of the video", type=int)
parser.add_argument("time", help = "Time in the video in format [hh:]mm:ss", type=str)
args = parser.parse_args()

def convert_time(t):
    parts = t.split(":")
    if len(parts) == 2:
        m = int(parts[0])
        s = int(parts[1])
        return m * 60 + s
    elif len(parts) == 3:
        h = int(parts[0])
        m = int(parts[1])
        s = int(parts[2])
        return h * 3600 + m * 60 + s
    else:
        raise ValueError("Time should be in the format [hh:]mm:ss")

# escaping the characters: & % $ # _ { } ~ ^ \ 
def latex_escapes(s):
    latex_special = {
        r"&": r"\&",
        r"%": r"\%",
        r"$": r"\$",
        r"#": r"\#",
        r"_": r"\_",
        r"{": r"\{",
        r"}": r"\}",
        r"~": r"{\textasciitilde}",
        r"^": r"{\textasciicircum}",
    }
    x = s.replace("\\", r"{\textbackslash}")
    for k, v in latex_special.items():
        x = x.replace(k, v)
    return x

if args.video_number > 24 or args.video_number < 1:
    raise ValueError("Video index should be between 1 and 24")

seconds = convert_time(args.time)
url_suffix = f"&t={seconds}s"
url = video_urls[args.video_number - 1] + url_suffix
escaped = latex_escapes(url)
caption = f"Video {args.video_number}, {args.time}"
cite_string = "\\cite[\\href{" + escaped + "}{" + caption + "}]{ihesvid}" 

print(cite_string)

