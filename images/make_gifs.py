"""
Run this once after saving the screenshots:

  qa_tools_1.png, qa_tools_2.png, qa_tools_3.png
  ridebaazi_1.png, ridebaazi_2.png, ridebaazi_3.png

into this folder (images/).

Usage:
  python3 images/make_gifs.py
"""

from PIL import Image
import os

HERE = os.path.dirname(os.path.abspath(__file__))


def make_gif(frames_paths, output_path, duration=1800):
    frames = []
    for p in frames_paths:
        img = Image.open(p).convert("RGBA")
        frames.append(img)

    if not frames:
        print(f"No frames found for {output_path}")
        return

    frames[0].save(
        output_path,
        save_all=True,
        append_images=frames[1:],
        loop=0,
        duration=duration,
        disposal=2,
    )
    print(f"Created {output_path}")


qa_frames = [os.path.join(HERE, f"qa_tools_{i}.png") for i in range(1, 4)]
rb_frames = [os.path.join(HERE, f"ridebaazi_{i}.png") for i in range(1, 4)]

missing = [f for f in qa_frames + rb_frames if not os.path.exists(f)]
if missing:
    print("Missing screenshots — save these files first:")
    for f in missing:
        print(f"  {f}")
else:
    make_gif(qa_frames, os.path.join(HERE, "project_qa_tools.gif"))
    make_gif(rb_frames, os.path.join(HERE, "project_ridebaazi.gif"))
    print("Done. Both GIFs are ready.")
