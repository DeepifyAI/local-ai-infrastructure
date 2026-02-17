#!/usr/bin/env python3
"""Capture script output as asciinema .cast file (v2 format), then convert to MP4."""
import subprocess
import sys
import os
import time
import json

def capture_to_cast(cmd, cast_path, title=""):
    """Run a command and create an asciinema v2 cast file from its output."""
    start = time.time()
    
    result = subprocess.run(
        cmd, shell=True,
        capture_output=True, text=True, timeout=30,
        env={**os.environ, "PYTHONUNBUFFERED": "1"}
    )
    
    output = result.stdout + (result.stderr if result.returncode != 0 else "")
    elapsed = time.time() - start
    
    # Build cast v2 (header + events)
    header = {
        "version": 2,
        "width": 100,
        "height": 30,
        "timestamp": int(start),
        "title": title,
        "env": {"TERM": "xterm-256color", "SHELL": "/bin/bash"}
    }
    
    lines = output.split("\n")
    events = []
    # Simulate typing output line by line with realistic delays
    t = 0.1
    for line in lines:
        events.append([round(t, 3), "o", line + "\r\n"])
        t += max(0.05, min(0.3, len(line) * 0.005))  # proportional to line length
    
    with open(cast_path, "w") as f:
        f.write(json.dumps(header) + "\n")
        for event in events:
            f.write(json.dumps(event) + "\n")
    
    return True

def cast_to_mp4(cast_path, mp4_path):
    """Convert .cast to .mp4 via agg (gif) then ffmpeg."""
    gif_path = cast_path.replace(".cast", ".gif")
    
    r = subprocess.run(
        ["agg", "--font-size", "16", "--cols", "100", "--rows", "30", cast_path, gif_path],
        capture_output=True, timeout=30
    )
    if r.returncode != 0 or not os.path.exists(gif_path):
        print(f"  agg failed: {r.stderr.decode()[:100]}")
        return False
    
    r = subprocess.run([
        "ffmpeg", "-y", "-i", gif_path,
        "-movflags", "faststart",
        "-pix_fmt", "yuv420p",
        "-vf", "scale=trunc(iw/2)*2:trunc(ih/2)*2",
        mp4_path
    ], capture_output=True, timeout=30)
    
    # Cleanup
    os.remove(cast_path)
    if os.path.exists(gif_path):
        os.remove(gif_path)
    
    return os.path.exists(mp4_path)

def main():
    demos_dir = os.path.dirname(os.path.abspath(__file__))
    scripts_dir = os.path.join(demos_dir, "scripts")
    mp4_dir = os.path.join(demos_dir, "mp4")
    os.makedirs(mp4_dir, exist_ok=True)
    
    scripts = sorted([f for f in os.listdir(scripts_dir) if f.endswith((".py", ".sh"))])
    
    recorded = []
    failed = []
    
    print(f"=== Recording {len(scripts)} demos ===\n")
    
    for script in scripts:
        path = os.path.join(scripts_dir, script)
        name = script.rsplit(".", 1)[0]
        cast_path = f"/tmp/demo-{name}.cast"
        mp4_path = os.path.join(mp4_dir, f"{name}.mp4")
        
        ext = script.rsplit(".", 1)[1]
        cmd = f"python3 {path}" if ext == "py" else f"bash {path}"
        
        print(f"  {script}...", end=" ", flush=True)
        
        try:
            if capture_to_cast(cmd, cast_path, title=name):
                if cast_to_mp4(cast_path, mp4_path):
                    size_kb = os.path.getsize(mp4_path) // 1024
                    print(f"OK ({size_kb}KB)")
                    recorded.append(name)
                else:
                    print("FAIL (convert)")
                    failed.append(name)
            else:
                print("FAIL (capture)")
                failed.append(name)
        except subprocess.TimeoutExpired:
            print("TIMEOUT")
            failed.append(name)
        except Exception as e:
            print(f"ERROR: {e}")
            failed.append(name)
    
    print(f"\n=== Done: {len(recorded)} recorded, {len(failed)} failed ===")
    
    # Write manifest
    manifest = {
        "recorded": recorded,
        "failed": failed,
        "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ")
    }
    with open(os.path.join(mp4_dir, "manifest.json"), "w") as f:
        json.dump(manifest, f, indent=2)

if __name__ == "__main__":
    main()
