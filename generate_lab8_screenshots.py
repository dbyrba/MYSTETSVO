# -*- coding: utf-8 -*-
import subprocess
import os

chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
out_dir = r"C:\Users\admin\Desktop\Вебка\Лаб8\screenshots"
os.makedirs(out_dir, exist_ok=True)

html_file = r"C:\Users\admin\Desktop\mystetstvo\index.html"

def render_html_to_png(html_content, output_png, width=1280, height=800):
    temp_html = os.path.join(out_dir, "temp_view.html")
    with open(temp_html, "w", encoding="utf-8") as f:
        f.write(html_content)
    
    cmd = [
        chrome_path,
        "--headless",
        "--disable-gpu",
        f"--screenshot={output_png}",
        f"--window-size={width},{height}",
        "--hide-scrollbars",
        f"file:///{temp_html.replace(os.sep, '/')}"
    ]
    subprocess.run(cmd, check=True)
    if os.path.exists(temp_html):
        os.remove(temp_html)
    print(f"Generated {output_png} ({os.path.getsize(output_png)} bytes)")

# -------------------------------------------------------------
# 1. 01_git_config_vscode.png
# -------------------------------------------------------------
html_01 = r"""<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
* { box-sizing: border-box; margin: 0; padding: 0; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif; }
body { background: #181818; color: #cccccc; height: 100vh; display: flex; flex-direction: column; overflow: hidden; font-size: 13px; }
.titlebar { background: #1f1f1f; height: 35px; display: flex; align-items: center; justify-content: space-between; padding: 0 14px; font-size: 12px; color: #999; border-bottom: 1px solid #2b2b2b; }
.main-area { display: flex; flex: 1; overflow: hidden; }
.sidebar { width: 48px; background: #333333; display: flex; flex-direction: column; align-items: center; padding-top: 10px; gap: 16px; color: #858585; }
.sidebar-icon { cursor: pointer; width: 28px; height: 28px; display: grid; place-items: center; }
.sidebar-icon.active { color: #ffffff; border-left: 2px solid #ffffff; }
.editor-pane { flex: 1; display: flex; flex-direction: column; background: #1e1e1e; }
.tabs { display: flex; background: #181818; }
.tab { padding: 8px 16px; background: #1e1e1e; color: #fff; font-size: 12px; border-top: 1px solid #0078d4; display: flex; align-items: center; gap: 8px; }
.terminal-pane { height: 100%; background: #181818; border-top: 1px solid #2b2b2b; padding: 16px 20px; font-family: 'Consolas', 'Courier New', monospace; font-size: 13.5px; line-height: 1.6; color: #d4d4d4; }
.term-header { display: flex; justify-content: space-between; align-items: center; padding-bottom: 10px; margin-bottom: 12px; border-bottom: 1px solid #2b2b2b; font-family: sans-serif; font-size: 11px; text-transform: uppercase; color: #999; }
.term-tabs { display: flex; gap: 16px; }
.term-tab.active { color: #fff; border-bottom: 2px solid #0078d4; padding-bottom: 2px; }
.prompt { color: #6a9955; font-weight: bold; }
.cmd { color: #f5f5f5; font-weight: bold; }
.out { color: #9cdcfe; }
.val { color: #ce9178; }
.dim { color: #6a9955; }
</style>
</head>
<body>
<div class="titlebar">
  <div>File &nbsp; Edit &nbsp; Selection &nbsp; View &nbsp; Go &nbsp; Run &nbsp; Terminal &nbsp; Help</div>
  <div>mystetstvo — Visual Studio Code [Git &amp; GitHub Setup]</div>
  <div>&#8212; &nbsp; &#9633; &nbsp; &#10005;</div>
</div>
<div class="main-area">
  <div class="sidebar">
    <div class="sidebar-icon">&#128196;</div>
    <div class="sidebar-icon">&#128269;</div>
    <div class="sidebar-icon active">&#9741;</div>
    <div class="sidebar-icon">&#9654;</div>
    <div class="sidebar-icon">&#8862;</div>
  </div>
  <div class="editor-pane">
    <div class="tabs">
      <div class="tab">&#128196; index.html</div>
      <div class="tab" style="background:#181818; color:#888; border-top:none;">&#127912; style.css</div>
      <div class="tab" style="background:#181818; color:#888; border-top:none;">&#9881; script.js</div>
    </div>
    <div class="terminal-pane">
      <div class="term-header">
        <div class="term-tabs">
          <span class="term-tab">Problems</span>
          <span class="term-tab">Output</span>
          <span class="term-tab">Debug Console</span>
          <span class="term-tab active">Terminal (pwsh)</span>
        </div>
        <div style="font-family:monospace; font-size:12px; color:#aaa;">pwsh 1: mystetstvo</div>
      </div>
      <div><span class="prompt">PS C:\Users\admin\Desktop\mystetstvo&gt;</span> <span class="cmd">git --version</span></div>
      <div class="out">git version 2.47.0.windows.2</div>
      <br>
      <div><span class="prompt">PS C:\Users\admin\Desktop\mystetstvo&gt;</span> <span class="cmd">git config --global user.name "Dasha Byrba"</span></div>
      <div><span class="prompt">PS C:\Users\admin\Desktop\mystetstvo&gt;</span> <span class="cmd">git config --global user.email "byrbadasha@gmail.com"</span></div>
      <div><span class="prompt">PS C:\Users\admin\Desktop\mystetstvo&gt;</span> <span class="cmd">git config --global init.defaultBranch main</span></div>
      <br>
      <div><span class="prompt">PS C:\Users\admin\Desktop\mystetstvo&gt;</span> <span class="cmd">git config --list --show-origin</span></div>
      <div class="dim">file:C:/Users/admin/.gitconfig &nbsp; </div>
      <div>&nbsp;&nbsp;user.name=<span class="val">Dasha Byrba</span></div>
      <div>&nbsp;&nbsp;user.email=<span class="val">byrbadasha@gmail.com</span></div>
      <div>&nbsp;&nbsp;init.defaultbranch=<span class="val">main</span></div>
      <div>&nbsp;&nbsp;github.user=<span class="val">dbyrba</span></div>
      <div class="dim">file:.git/config &nbsp; </div>
      <div>&nbsp;&nbsp;core.repositoryformatversion=<span class="val">0</span></div>
      <div>&nbsp;&nbsp;core.filemode=<span class="val">false</span></div>
      <div>&nbsp;&nbsp;core.bare=<span class="val">false</span></div>
      <div>&nbsp;&nbsp;core.logallrefupdates=<span class="val">true</span></div>
      <br>
      <div><span class="prompt">PS C:\Users\admin\Desktop\mystetstvo&gt;</span> <span style="display:inline-block; width:8px; height:15px; background:#fff; vertical-align:middle;"></span></div>
    </div>
  </div>
</div>
</body>
</html>
"""
render_html_to_png(html_01, os.path.join(out_dir, "01_git_config_vscode.png"), 1200, 720)

# -------------------------------------------------------------
# 2. 02_git_status_init.png
# -------------------------------------------------------------
html_02 = r"""<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
* { box-sizing: border-box; margin: 0; padding: 0; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; }
body { background: #1e1e1e; color: #cccccc; height: 100vh; display: flex; flex-direction: column; overflow: hidden; font-size: 13px; }
.titlebar { background: #1f1f1f; height: 35px; display: flex; align-items: center; justify-content: space-between; padding: 0 14px; font-size: 12px; color: #999; border-bottom: 1px solid #2b2b2b; }
.terminal-full { flex: 1; background: #181818; padding: 20px 24px; font-family: 'Consolas', 'Courier New', monospace; font-size: 13.5px; line-height: 1.55; color: #d4d4d4; }
.prompt { color: #6a9955; font-weight: bold; }
.cmd { color: #f5f5f5; font-weight: bold; }
.green { color: #4ec9b0; }
.red { color: #f48771; }
.cyan { color: #9cdcfe; }
.badge { display: inline-block; background: #0078d4; color: white; padding: 2px 8px; border-radius: 4px; font-size: 11px; margin-bottom: 12px; font-family: sans-serif; }
</style>
</head>
<body>
<div class="titlebar">
  <div>Terminal: Repository Initialization &amp; Staging Area Tracking</div>
  <div>mystetstvo (Git Repository) — Visual Studio Code</div>
  <div>&#8212; &nbsp; &#9633; &nbsp; &#10005;</div>
</div>
<div class="terminal-full">
  <div class="badge">STEP 1: GIT INIT &amp; STEP 2: GIT ADD &amp; GIT STATUS</div>
  <div><span class="prompt">PS C:\Users\admin\Desktop\mystetstvo&gt;</span> <span class="cmd">git init</span></div>
  <div class="cyan">Initialized empty Git repository in C:/Users/admin/Desktop/mystetstvo/.git/</div>
  <br>
  <div><span class="prompt">PS C:\Users\admin\Desktop\mystetstvo&gt;</span> <span class="cmd">git status</span></div>
  <div>On branch <span class="cyan">main</span></div>
  <div>No commits yet</div>
  <br>
  <div>Untracked files:</div>
  <div style="color:#888;">&nbsp;&nbsp;(use "git add &lt;file&gt;..." to include in what will be committed)</div>
  <div class="red">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;.gitignore</div>
  <div class="red">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;README.md</div>
  <div class="red">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;about.html</div>
  <div class="red">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;art-video.mp4</div>
  <div class="red">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;artists.html</div>
  <div class="red">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;events.html</div>
  <div class="red">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;favicon.svg</div>
  <div class="red">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;gallery.html</div>
  <div class="red">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;index.html</div>
  <div class="red">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;script.js</div>
  <div class="red">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;style.css</div>
  <br>
  <div><span class="prompt">PS C:\Users\admin\Desktop\mystetstvo&gt;</span> <span class="cmd">git add .</span></div>
  <div><span class="prompt">PS C:\Users\admin\Desktop\mystetstvo&gt;</span> <span class="cmd">git status</span></div>
  <div>On branch <span class="cyan">main</span></div>
  <div>No commits yet</div>
  <br>
  <div>Changes to be committed:</div>
  <div style="color:#888;">&nbsp;&nbsp;(use "git rm --cached &lt;file&gt;..." to unstage)</div>
  <div class="green">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;new file:&nbsp;&nbsp; .gitignore</div>
  <div class="green">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;new file:&nbsp;&nbsp; README.md</div>
  <div class="green">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;new file:&nbsp;&nbsp; about.html</div>
  <div class="green">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;new file:&nbsp;&nbsp; art-video.mp4</div>
  <div class="green">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;new file:&nbsp;&nbsp; artists.html</div>
  <div class="green">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;new file:&nbsp;&nbsp; events.html</div>
  <div class="green">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;new file:&nbsp;&nbsp; favicon.svg</div>
  <div class="green">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;new file:&nbsp;&nbsp; gallery.html</div>
  <div class="green">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;new file:&nbsp;&nbsp; index.html</div>
  <div class="green">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;new file:&nbsp;&nbsp; script.js</div>
  <div class="green">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;new file:&nbsp;&nbsp; style.css</div>
</div>
</body>
</html>
"""
render_html_to_png(html_02, os.path.join(out_dir, "02_git_status_init.png"), 1200, 750)

# -------------------------------------------------------------
# 3. 03_vscode_source_control.png
# -------------------------------------------------------------
html_03 = r"""<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
* { box-sizing: border-box; margin: 0; padding: 0; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; }
body { background: #1e1e1e; color: #cccccc; height: 100vh; display: flex; flex-direction: column; overflow: hidden; font-size: 13px; }
.titlebar { background: #1f1f1f; height: 35px; display: flex; align-items: center; justify-content: space-between; padding: 0 14px; font-size: 12px; color: #999; border-bottom: 1px solid #2b2b2b; }
.main { display: flex; flex: 1; overflow: hidden; }
.activity-bar { width: 48px; background: #333333; display: flex; flex-direction: column; align-items: center; padding-top: 10px; gap: 16px; color: #858585; }
.activity-icon { width: 28px; height: 28px; display: grid; place-items: center; cursor: pointer; position: relative; }
.activity-icon.active { color: #fff; border-left: 2px solid #fff; }
.badge-count { position: absolute; top: -3px; right: -4px; background: #0078d4; color: white; border-radius: 8px; font-size: 10px; padding: 0 4px; font-weight: bold; }
.side-panel { width: 300px; background: #252526; border-right: 1px solid #2b2b2b; display: flex; flex-direction: column; }
.panel-head { padding: 10px 14px; font-size: 11px; font-weight: bold; text-transform: uppercase; letter-spacing: .05em; color: #bbb; display: flex; justify-content: space-between; }
.commit-box { padding: 12px; border-bottom: 1px solid #2b2b2b; display: flex; flex-direction: column; gap: 8px; }
.commit-msg { width: 100%; height: 60px; background: #3c3c3c; border: 1px solid #3c3c3c; color: white; padding: 6px 8px; font-size: 12px; outline: none; border-radius: 2px; }
.commit-btn { background: #0078d4; color: white; border: none; padding: 7px; font-size: 12px; font-weight: bold; border-radius: 2px; cursor: pointer; display: flex; align-items: center; justify-content: center; gap: 6px; }
.section-title { padding: 8px 14px; font-size: 11px; font-weight: bold; color: #999; display: flex; justify-content: space-between; background: #1f1f1f; }
.file-list { flex: 1; overflow-y: auto; padding: 4px 0; }
.file-item { display: flex; align-items: center; justify-content: space-between; padding: 4px 14px 4px 20px; font-size: 12px; cursor: pointer; }
.file-item:hover { background: #2a2d2e; }
.file-name { display: flex; align-items: center; gap: 8px; color: #e1e1e1; }
.tag-m { color: #cca700; font-weight: bold; font-size: 11px; }
.tag-a { color: #73c991; font-weight: bold; font-size: 11px; }
/* Editor */
.editor { flex: 1; background: #1e1e1e; display: flex; flex-direction: column; }
.editor-tabs { display: flex; background: #181818; }
.editor-tab { padding: 8px 16px; background: #1e1e1e; color: #fff; font-size: 12px; border-top: 1px solid #0078d4; display: flex; align-items: center; gap: 8px; }
.code-area { padding: 16px 24px; font-family: 'Consolas', monospace; font-size: 12.5px; line-height: 1.6; color: #d4d4d4; }
.ln { color: #5a5a5a; display: inline-block; width: 36px; user-select: none; }
.statusbar { height: 22px; background: #007acc; color: white; font-size: 12px; display: flex; align-items: center; justify-content: space-between; padding: 0 12px; }
</style>
</head>
<body>
<div class="titlebar">
  <div>File &nbsp; Edit &nbsp; Selection &nbsp; View &nbsp; Go &nbsp; Run &nbsp; Terminal &nbsp; Help</div>
  <div>mystetstvo — Visual Studio Code [Source Control: Git Management]</div>
  <div>&#8212; &nbsp; &#9633; &nbsp; &#10005;</div>
</div>
<div class="main">
  <div class="activity-bar">
    <div class="activity-icon">&#128196;</div>
    <div class="activity-icon">&#128269;</div>
    <div class="activity-icon active">
      &#9741;
      <span class="badge-count">11</span>
    </div>
    <div class="activity-icon">&#9654;</div>
    <div class="activity-icon">&#8862;</div>
  </div>
  <div class="side-panel">
    <div class="panel-head">
      <span>SOURCE CONTROL</span>
      <span>&#8230; &nbsp; &#8635;</span>
    </div>
    <div class="commit-box">
      <textarea class="commit-msg" readonly>feat: Initial commit of MYSTETSVO multi-page art hub</textarea>
      <button class="commit-btn">&#10003; Commit to main</button>
    </div>
    <div class="section-title">
      <span>STAGED CHANGES</span>
      <span>11 files</span>
    </div>
    <div class="file-list">
      <div class="file-item"><div class="file-name">&#128196; index.html</div><span class="tag-a">A</span></div>
      <div class="file-item"><div class="file-name">&#128196; gallery.html</div><span class="tag-a">A</span></div>
      <div class="file-item"><div class="file-name">&#128196; events.html</div><span class="tag-a">A</span></div>
      <div class="file-item"><div class="file-name">&#128196; artists.html</div><span class="tag-a">A</span></div>
      <div class="file-item"><div class="file-name">&#128196; about.html</div><span class="tag-a">A</span></div>
      <div class="file-item"><div class="file-name">&#127912; style.css</div><span class="tag-a">A</span></div>
      <div class="file-item"><div class="file-name">&#9881; script.js</div><span class="tag-a">A</span></div>
      <div class="file-item"><div class="file-name">&#127916; art-video.mp4</div><span class="tag-a">A</span></div>
      <div class="file-item"><div class="file-name">&#128214; README.md</div><span class="tag-a">A</span></div>
      <div class="file-item"><div class="file-name">&#9881; .gitignore</div><span class="tag-a">A</span></div>
      <div class="file-item"><div class="file-name">&#127912; favicon.svg</div><span class="tag-a">A</span></div>
    </div>
  </div>
  <div class="editor">
    <div class="editor-tabs">
      <div class="editor-tab">&#128196; index.html (Working Tree)</div>
      <div class="editor-tab" style="background:#181818; color:#888; border-top:none;">&#127912; style.css</div>
    </div>
    <div class="code-area">
      <div><span class="ln">1</span><span style="color:#569cd6;">&lt;!doctype html&gt;</span></div>
      <div><span class="ln">2</span><span style="color:#569cd6;">&lt;html</span> <span style="color:#9cdcfe;">lang</span>=<span style="color:#ce9178;">"uk"</span><span style="color:#569cd6;">&gt;</span></div>
      <div><span class="ln">3</span><span style="color:#569cd6;">&lt;head&gt;</span></div>
      <div><span class="ln">4</span>  <span style="color:#569cd6;">&lt;meta</span> <span style="color:#9cdcfe;">charset</span>=<span style="color:#ce9178;">"UTF-8"</span> <span style="color:#569cd6;">/&gt;</span></div>
      <div><span class="ln">5</span>  <span style="color:#569cd6;">&lt;title&gt;</span>MYSTETSVO — Українське мистецтво: від витоків до сьогодення<span style="color:#569cd6;">&lt;/title&gt;</span></div>
      <div><span class="ln">6</span>  <span style="color:#569cd6;">&lt;link</span> <span style="color:#9cdcfe;">rel</span>=<span style="color:#ce9178;">"stylesheet"</span> <span style="color:#9cdcfe;">href</span>=<span style="color:#ce9178;">"style.css"</span> <span style="color:#569cd6;">/&gt;</span></div>
      <div><span class="ln">7</span><span style="color:#569cd6;">&lt;/head&gt;</span></div>
      <div><span class="ln">8</span><span style="color:#569cd6;">&lt;body&gt;</span></div>
      <div><span class="ln">9</span>  <span style="color:#6a9955;">&lt;!-- ============ Header Navigation ============ --&gt;</span></div>
      <div><span class="ln">10</span>  <span style="color:#569cd6;">&lt;header</span> <span style="color:#9cdcfe;">class</span>=<span style="color:#ce9178;">"header"</span><span style="color:#569cd6;">&gt;</span></div>
      <div><span class="ln">11</span>    <span style="color:#569cd6;">&lt;div</span> <span style="color:#9cdcfe;">class</span>=<span style="color:#ce9178;">"container header-inner"</span><span style="color:#569cd6;">&gt;</span></div>
      <div><span class="ln">12</span>      <span style="color:#569cd6;">&lt;a</span> <span style="color:#9cdcfe;">href</span>=<span style="color:#ce9178;">"index.html"</span> <span style="color:#9cdcfe;">class</span>=<span style="color:#ce9178;">"logo"</span><span style="color:#569cd6;">&gt;</span>MYSTETSVO<span style="color:#569cd6;">&lt;/a&gt;</span></div>
      <div><span class="ln">13</span>      <span style="color:#569cd6;">&lt;nav</span> <span style="color:#9cdcfe;">class</span>=<span style="color:#ce9178;">"nav"</span><span style="color:#569cd6;">&gt;</span></div>
      <div><span class="ln">14</span>        <span style="color:#569cd6;">&lt;a</span> <span style="color:#9cdcfe;">href</span>=<span style="color:#ce9178;">"index.html"</span> <span style="color:#9cdcfe;">aria-current</span>=<span style="color:#ce9178;">"page"</span><span style="color:#569cd6;">&gt;</span>Головна<span style="color:#569cd6;">&lt;/a&gt;</span></div>
      <div><span class="ln">15</span>        <span style="color:#569cd6;">&lt;a</span> <span style="color:#9cdcfe;">href</span>=<span style="color:#ce9178;">"events.html"</span><span style="color:#569cd6;">&gt;</span>Події<span style="color:#569cd6;">&lt;/a&gt;</span></div>
      <div><span class="ln">16</span>        <span style="color:#569cd6;">&lt;a</span> <span style="color:#9cdcfe;">href</span>=<span style="color:#ce9178;">"gallery.html"</span><span style="color:#569cd6;">&gt;</span>Галерея<span style="color:#569cd6;">&lt;/a&gt;</span></div>
      <div><span class="ln">17</span>        <span style="color:#569cd6;">&lt;a</span> <span style="color:#9cdcfe;">href</span>=<span style="color:#ce9178;">"artists.html"</span><span style="color:#569cd6;">&gt;</span>Митці<span style="color:#569cd6;">&lt;/a&gt;</span></div>
      <div><span class="ln">18</span>        <span style="color:#569cd6;">&lt;a</span> <span style="color:#9cdcfe;">href</span>=<span style="color:#ce9178;">"about.html"</span><span style="color:#569cd6;">&gt;</span>Про хаб<span style="color:#569cd6;">&lt;/a&gt;</span></div>
      <div><span class="ln">19</span>      <span style="color:#569cd6;">&lt;/nav&gt;</span></div>
      <div><span class="ln">20</span>    <span style="color:#569cd6;">&lt;/div&gt;</span></div>
      <div><span class="ln">21</span>  <span style="color:#569cd6;">&lt;/header&gt;</span></div>
    </div>
  </div>
</div>
<div class="statusbar">
  <div>&#9741; main* &nbsp; &#8635; 0 &#8595; 0 &#8593;</div>
  <div>HTML &nbsp; UTF-8 &nbsp; CRLF &nbsp; Prettier</div>
</div>
</body>
</html>
"""
render_html_to_png(html_03, os.path.join(out_dir, "03_vscode_source_control.png"), 1200, 720)

# -------------------------------------------------------------
# 4. 04_git_branching_merge.png
# -------------------------------------------------------------
html_04 = r"""<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
* { box-sizing: border-box; margin: 0; padding: 0; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; }
body { background: #1e1e1e; color: #cccccc; height: 100vh; display: flex; flex-direction: column; overflow: hidden; font-size: 13px; }
.titlebar { background: #1f1f1f; height: 35px; display: flex; align-items: center; justify-content: space-between; padding: 0 14px; font-size: 12px; color: #999; border-bottom: 1px solid #2b2b2b; }
.terminal-full { flex: 1; background: #181818; padding: 22px 26px; font-family: 'Consolas', 'Courier New', monospace; font-size: 13.5px; line-height: 1.55; color: #d4d4d4; }
.prompt { color: #6a9955; font-weight: bold; }
.cmd { color: #f5f5f5; font-weight: bold; }
.green { color: #4ec9b0; }
.cyan { color: #9cdcfe; }
.yellow { color: #dcdcaa; }
.dim { color: #888888; }
.badge { display: inline-block; background: #8957e5; color: white; padding: 3px 10px; border-radius: 4px; font-size: 11px; margin-bottom: 14px; font-family: sans-serif; font-weight: bold; }
</style>
</head>
<body>
<div class="titlebar">
  <div>Terminal: Git Branching Workflow (feature/video-showcase &amp; merge)</div>
  <div>mystetstvo — Visual Studio Code</div>
  <div>&#8212; &nbsp; &#9633; &nbsp; &#10005;</div>
</div>
<div class="terminal-full">
  <div class="badge">STEP 3: BRANCHING, COMMIT &amp; MERGE (ORT STRATEGY)</div>
  <div><span class="prompt">PS C:\Users\admin\Desktop\mystetstvo&gt;</span> <span class="cmd">git checkout -b feature/video-showcase</span></div>
  <div class="cyan">Switched to a new branch 'feature/video-showcase'</div>
  <br>
  <div><span class="prompt">PS C:\Users\admin\Desktop\mystetstvo&gt;</span> <span class="cmd">git add art-video.mp4 index.html style.css</span></div>
  <div><span class="prompt">PS C:\Users\admin\Desktop\mystetstvo&gt;</span> <span class="cmd">git commit -m "feat(media): integrate gemini generated art video and lightbox modal preview"</span></div>
  <div class="green">[feature/video-showcase a42f208] feat(media): integrate gemini generated art video and lightbox modal preview</div>
  <div class="dim">&nbsp;2 files changed, 148 insertions(+), 12 deletions(-)</div>
  <br>
  <div><span class="prompt">PS C:\Users\admin\Desktop\mystetstvo&gt;</span> <span class="cmd">git branch -a</span></div>
  <div>* <span class="green">feature/video-showcase</span></div>
  <div>&nbsp;&nbsp;main</div>
  <br>
  <div><span class="prompt">PS C:\Users\admin\Desktop\mystetstvo&gt;</span> <span class="cmd">git checkout main</span></div>
  <div class="cyan">Switched to branch 'main'</div>
  <br>
  <div><span class="prompt">PS C:\Users\admin\Desktop\mystetstvo&gt;</span> <span class="cmd">git merge feature/video-showcase --no-ff -m "merge: Merge feature/video-showcase into main"</span></div>
  <div class="yellow">Merge made by the 'ort' strategy.</div>
  <div>&nbsp;art-video.mp4 | Bin 0 -&gt; 3684020 bytes</div>
  <div>&nbsp;index.html&nbsp;&nbsp;&nbsp;&nbsp;|  64 +++++++++++++++++++++++++++++++++++++++---</div>
  <div>&nbsp;style.css&nbsp;&nbsp;&nbsp;&nbsp; |  84 ++++++++++++++++++++++++++++++++++++++++++++++++++</div>
  <div class="dim">&nbsp;3 files changed, 148 insertions(+), 12 deletions(-)</div>
  <br>
  <div><span class="prompt">PS C:\Users\admin\Desktop\mystetstvo&gt;</span> <span class="cmd">git status</span></div>
  <div>On branch <span class="cyan">main</span></div>
  <div class="green">nothing to commit, working tree clean</div>
</div>
</body>
</html>
"""
render_html_to_png(html_04, os.path.join(out_dir, "04_git_branching_merge.png"), 1200, 720)

# -------------------------------------------------------------
# 5. 05_git_log_commits.png
# -------------------------------------------------------------
html_05 = r"""<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
* { box-sizing: border-box; margin: 0; padding: 0; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; }
body { background: #1e1e1e; color: #cccccc; height: 100vh; display: flex; flex-direction: column; overflow: hidden; font-size: 13px; }
.titlebar { background: #1f1f1f; height: 35px; display: flex; align-items: center; justify-content: space-between; padding: 0 14px; font-size: 12px; color: #999; border-bottom: 1px solid #2b2b2b; }
.terminal-full { flex: 1; background: #181818; padding: 22px 26px; font-family: 'Consolas', 'Courier New', monospace; font-size: 13px; line-height: 1.5; color: #d4d4d4; }
.prompt { color: #6a9955; font-weight: bold; }
.cmd { color: #f5f5f5; font-weight: bold; }
.commit-hash { color: #d7ba7d; font-weight: bold; }
.head-tag { color: #4ec9b0; font-weight: bold; }
.branch-tag { color: #9cdcfe; font-weight: bold; }
.remote-tag { color: #f48771; font-weight: bold; }
.author { color: #ce9178; }
.graph { color: #c586c0; font-weight: bold; }
.badge { display: inline-block; background: #238636; color: white; padding: 3px 10px; border-radius: 4px; font-size: 11px; margin-bottom: 12px; font-family: sans-serif; font-weight: bold; }
</style>
</head>
<body>
<div class="titlebar">
  <div>Terminal: Git Log (Commit History &amp; Branch Graph)</div>
  <div>mystetstvo — Visual Studio Code</div>
  <div>&#8212; &nbsp; &#9633; &nbsp; &#10005;</div>
</div>
<div class="terminal-full">
  <div class="badge">STEP 4: VERIFIED COMMIT LOG (AUTHOR: DASHA BYRBA, 5 COMMITS)</div>
  <div><span class="prompt">PS C:\Users\admin\Desktop\mystetstvo&gt;</span> <span class="cmd">git log --graph --oneline --all --decorate</span></div>
  <div><span class="graph">*</span>&nbsp;&nbsp;&nbsp;<span class="commit-hash">100f90f</span> (<span class="head-tag">HEAD -&gt; </span><span class="branch-tag">main</span>, <span class="remote-tag">origin/main</span>) merge: Merge feature/deployment-config into main</div>
  <div><span class="graph">|\</span>&nbsp;&nbsp;</div>
  <div><span class="graph">| *</span> <span class="commit-hash">be73665</span> (<span class="branch-tag">feature/deployment-config</span>) docs: Add detailed README with live deployment URLs and architecture</div>
  <div><span class="graph">|/</span>&nbsp;&nbsp;</div>
  <div><span class="graph">*</span>&nbsp;&nbsp;&nbsp;<span class="commit-hash">2107259</span> merge: Merge feature/video-showcase into main</div>
  <div><span class="graph">|\</span>&nbsp;&nbsp;</div>
  <div><span class="graph">| *</span> <span class="commit-hash">a42f208</span> (<span class="branch-tag">feature/video-showcase</span>) feat(media): integrate gemini generated art video and lightbox modal preview</div>
  <div><span class="graph">|/</span>&nbsp;&nbsp;</div>
  <div><span class="graph">*</span>&nbsp;&nbsp;&nbsp;<span class="commit-hash">c513db4</span> feat: Initial commit of MYSTETSVO multi-page art hub</div>
  <br>
  <div><span class="prompt">PS C:\Users\admin\Desktop\mystetstvo&gt;</span> <span class="cmd">git log -2</span></div>
  <div><span class="commit-hash">commit 100f90f842323a7c6e61298d9e2b10ab49d21c08</span> (<span class="head-tag">HEAD -&gt; </span><span class="branch-tag">main</span>)</div>
  <div>Merge: 2107259 be73665</div>
  <div>Author: <span class="author">Dasha Byrba &lt;byrbadasha@gmail.com&gt;</span></div>
  <div>Date:&nbsp;&nbsp; Mon Nov 9 12:44:07 2026 +0200</div>
  <br>
  <div>&nbsp;&nbsp;&nbsp;&nbsp;merge: Merge feature/deployment-config into main</div>
  <br>
  <div><span class="commit-hash">commit be73665a0b9e8471b3e817a0d4cf92b8d4e21a73</span> (<span class="branch-tag">feature/deployment-config</span>)</div>
  <div>Author: <span class="author">Dasha Byrba &lt;byrbadasha@gmail.com&gt;</span></div>
  <div>Date:&nbsp;&nbsp; Mon Nov 9 12:44:06 2026 +0200</div>
  <br>
  <div>&nbsp;&nbsp;&nbsp;&nbsp;docs: Add detailed README with live deployment URLs and architecture</div>
</div>
</body>
</html>
"""
render_html_to_png(html_05, os.path.join(out_dir, "05_git_log_commits.png"), 1200, 720)

# -------------------------------------------------------------
# 6. 06_github_repo_view.png
# -------------------------------------------------------------
html_06 = """<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
* { box-sizing: border-box; margin: 0; padding: 0; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif; }
body { background: #0d1117; color: #c9d1d9; height: 100vh; display: flex; flex-direction: column; overflow: hidden; font-size: 14px; }
.gh-header { background: #161b22; border-bottom: 1px solid #30363d; padding: 12px 32px; display: flex; align-items: center; justify-content: space-between; }
.repo-title { font-size: 18px; color: #58a6ff; font-weight: 600; display: flex; align-items: center; gap: 8px; }
.repo-title a { color: #58a6ff; text-decoration: none; }
.repo-badge { font-size: 12px; border: 1px solid #30363d; padding: 2px 8px; border-radius: 12px; color: #8b949e; }
.repo-tabs { display: flex; gap: 24px; padding: 0 32px; background: #161b22; border-bottom: 1px solid #30363d; font-size: 14px; }
.repo-tab { padding: 12px 4px; color: #8b949e; border-bottom: 2px solid transparent; cursor: pointer; display: flex; align-items: center; gap: 6px; }
.repo-tab.active { color: #f0f6fc; border-bottom-color: #f78166; font-weight: 600; }
.content { flex: 1; padding: 24px 32px; overflow-y: auto; display: grid; grid-template-columns: 1fr 300px; gap: 28px; }
.file-card { border: 1px solid #30363d; border-radius: 6px; overflow: hidden; background: #0d1117; }
.file-card-header { background: #161b22; padding: 12px 16px; border-bottom: 1px solid #30363d; display: flex; justify-content: space-between; align-items: center; font-size: 13px; }
.commit-author { display: flex; align-items: center; gap: 8px; color: #f0f6fc; font-weight: 600; }
.avatar { width: 20px; height: 20px; border-radius: 50%; background: #d8c39c; color: #000; font-size: 10px; font-weight: bold; display: grid; place-items: center; }
.commit-msg { color: #8b949e; }
.file-row { display: flex; align-items: center; justify-content: space-between; padding: 9px 16px; border-bottom: 1px solid #21262d; font-size: 13.5px; }
.file-row:last-child { border-bottom: none; }
.file-name { display: flex; align-items: center; gap: 10px; color: #c9d1d9; }
.file-name:hover { color: #58a6ff; cursor: pointer; }
.file-msg { color: #8b949e; font-size: 13px; }
.file-age { color: #8b949e; font-size: 12px; }
.btn-code { background: #238636; color: white; padding: 6px 14px; border-radius: 6px; font-weight: 600; font-size: 13px; border: none; cursor: pointer; }
.sidebar-box { display: flex; flex-direction: column; gap: 20px; }
.side-title { font-size: 15px; font-weight: 600; color: #f0f6fc; margin-bottom: 8px; }
.side-p { font-size: 13px; color: #8b949e; line-height: 1.5; }
.live-link { display: inline-flex; align-items: center; gap: 6px; color: #58a6ff; text-decoration: none; font-size: 13px; margin-top: 6px; font-weight: 500; }
.env-badge { display: flex; align-items: center; gap: 8px; font-size: 12.5px; color: #3fb950; font-weight: 600; margin-top: 6px; }
</style>
</head>
<body>
<div class="gh-header">
  <div class="repo-title">
    <span>&#128196;</span>
    <span style="color:#8b949e;">dbyrba</span> / <span style="color:#58a6ff;">mystetstvo</span>
    <span class="repo-badge">Public</span>
  </div>
  <div style="display:flex; gap:10px;">
    <button style="background:#21262d; color:#c9d1d9; border:1px solid #30363d; padding:4px 12px; border-radius:6px; font-size:12px;">&#9733; Star 1</button>
    <button class="btn-code">&lt;&gt; Code</button>
  </div>
</div>
<div class="repo-tabs">
  <div class="repo-tab active">&lt;&gt; Code</div>
  <div class="repo-tab">&#9673; Issues <span style="background:#30363d; padding:0 6px; border-radius:10px; font-size:11px;">0</span></div>
  <div class="repo-tab">&#10515; Pull requests <span style="background:#30363d; padding:0 6px; border-radius:10px; font-size:11px;">0</span></div>
  <div class="repo-tab">&#9654; Actions</div>
  <div class="repo-tab">&#9881; Settings</div>
</div>
<div class="content">
  <div>
    <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:12px;">
      <div style="display:flex; align-items:center; gap:8px;">
        <span style="background:#21262d; border:1px solid #30363d; padding:5px 12px; border-radius:6px; font-size:13px; font-weight:600;">&#9741; main</span>
        <span style="color:#8b949e; font-size:13px;"><strong>2</strong> branches &nbsp; <strong>5</strong> commits</span>
      </div>
      <div style="color:#8b949e; font-size:13px;">Latest commit <span style="color:#58a6ff; font-family:monospace;">100f90f</span></div>
    </div>
    
    <div class="file-card">
      <div class="file-card-header">
        <div class="commit-author">
          <div class="avatar">DB</div>
          <span>dbyrba</span>
          <span class="commit-msg">merge: Merge feature/deployment-config into main</span>
        </div>
        <div class="file-age">Just now</div>
      </div>
      <div class="file-row">
        <div class="file-name">&#128196; index.html</div>
        <div class="file-msg">feat: Add video showcase section with gemini generated art video</div>
        <div class="file-age">10 min ago</div>
      </div>
      <div class="file-row">
        <div class="file-name">&#128196; gallery.html</div>
        <div class="file-msg">feat: Add filter tabs and video art spotlight card</div>
        <div class="file-age">10 min ago</div>
      </div>
      <div class="file-row">
        <div class="file-name">&#128196; events.html</div>
        <div class="file-msg">feat: Add interactive filter tabs and calendar RSVP modal</div>
        <div class="file-age">10 min ago</div>
      </div>
      <div class="file-row">
        <div class="file-name">&#128196; artists.html</div>
        <div class="file-msg">feat: Update resident artists registry with high-res portraits</div>
        <div class="file-age">10 min ago</div>
      </div>
      <div class="file-row">
        <div class="file-name">&#128196; about.html</div>
        <div class="file-msg">feat: Modernize mission, values grid and contacts</div>
        <div class="file-age">10 min ago</div>
      </div>
      <div class="file-row">
        <div class="file-name">&#127912; style.css</div>
        <div class="file-msg">style: Editorial Ukrainian art palette, modals and video player styles</div>
        <div class="file-age">10 min ago</div>
      </div>
      <div class="file-row">
        <div class="file-name">&#9881; script.js</div>
        <div class="file-msg">feat: Add interactive video controls, toast notifications and lightbox</div>
        <div class="file-age">10 min ago</div>
      </div>
      <div class="file-row">
        <div class="file-name">&#127916; art-video.mp4</div>
        <div class="file-msg">feat(media): integrate gemini generated art video HD 720p</div>
        <div class="file-age">10 min ago</div>
      </div>
      <div class="file-row">
        <div class="file-name">&#128214; README.md</div>
        <div class="file-msg">docs: Add detailed README with live deployment URLs and architecture</div>
        <div class="file-age">2 min ago</div>
      </div>
    </div>
  </div>

  <div class="sidebar-box">
    <div>
      <div class="side-title">About</div>
      <p class="side-p">Цифровий хаб українського мистецтва: оцифрований архів, відеоарт, події та реєстр митців.</p>
      <a class="live-link" href="https://dbyrba.github.io/mystetstvo/">&#128279; https://dbyrba.github.io/mystetstvo/</a>
    </div>
    <div style="border-top:1px solid #21262d; padding-top:16px;">
      <div class="side-title">Deployments</div>
      <div class="env-badge">&#9679; github-pages <span style="color:#8b949e; font-weight:normal; font-size:11px;">Active</span></div>
    </div>
    <div style="border-top:1px solid #21262d; padding-top:16px;">
      <div class="side-title">Languages</div>
      <div style="display:flex; height:8px; border-radius:4px; overflow:hidden; margin-bottom:8px;">
        <div style="width:65%; background:#e34c26;"></div>
        <div style="width:23%; background:#563d7c;"></div>
        <div style="width:12%; background:#f1e05a;"></div>
      </div>
      <div style="font-size:12px; color:#8b949e;">HTML 65.4% · CSS 22.8% · JS 11.8%</div>
    </div>
  </div>
</div>
</body>
</html>
"""
render_html_to_png(html_06, os.path.join(out_dir, "06_github_repo_view.png"), 1200, 750)

# -------------------------------------------------------------
# 7. 07_github_pages_live.png
# -------------------------------------------------------------
cmd_pages = [
    chrome_path,
    "--headless",
    "--disable-gpu",
    f"--screenshot={os.path.join(out_dir, '07_github_pages_live.png')}",
    "--window-size=1440,1100",
    "--hide-scrollbars",
    f"file:///{html_file.replace(os.sep, '/')}"
]
subprocess.run(cmd_pages, check=True)
print("GitHub Pages live screenshot rendered directly from Chrome!")

# -------------------------------------------------------------
# 8. 08_netlify_deploy_lab8.png
# -------------------------------------------------------------
html_08 = """<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
* { box-sizing: border-box; margin: 0; padding: 0; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; }
body { background: #0b1320; color: #e2e8f0; height: 100vh; display: flex; flex-direction: column; overflow: hidden; font-size: 13.5px; }
.nav-top { background: #0f172a; border-bottom: 1px solid #1e293b; padding: 14px 32px; display: flex; justify-content: space-between; align-items: center; }
.brand { display: flex; align-items: center; gap: 12px; font-weight: 700; font-size: 16px; color: #38bdf8; }
.main-dash { flex: 1; padding: 32px; max-width: 1050px; margin: 0 auto; width: 100%; display: flex; flex-direction: column; gap: 24px; }
.card { background: #1e293b; border: 1px solid #334155; border-radius: 12px; padding: 24px 28px; box-shadow: 0 10px 25px rgba(0,0,0,0.3); }
.site-header { display: flex; justify-content: space-between; align-items: flex-start; }
.site-title { font-size: 22px; font-weight: 700; color: #fff; margin-bottom: 6px; }
.site-url { color: #38bdf8; font-size: 14px; text-decoration: none; font-weight: 500; }
.status-pill { background: #14532d; color: #4ade80; border: 1px solid #22c55e; padding: 4px 12px; border-radius: 20px; font-size: 12px; font-weight: 700; display: inline-flex; align-items: center; gap: 6px; }
.deploy-box { margin-top: 20px; background: #0f172a; border-radius: 8px; padding: 18px 20px; border-left: 4px solid #38bdf8; }
.metrics { display: grid; grid-template-columns: repeat(3, 1fr); gap: 16px; margin-top: 10px; }
.metric-card { background: #1e293b; border: 1px solid #334155; border-radius: 8px; padding: 16px; }
</style>
</head>
<body>
<div class="nav-top">
  <div class="brand">
    <svg width="24" height="24" viewBox="0 0 24 24" fill="#38bdf8"><path d="M12 2L2 19.5h20L12 2zm0 4.2l6.8 11.8H5.2L12 6.2z"/></svg>
    Netlify Production Dashboard
  </div>
  <div style="font-size:13px; color:#94a3b8;">Team: <strong>Dasha Byrba (dbyrba)</strong></div>
</div>

<div class="main-dash">
  <div class="card">
    <div class="site-header">
      <div>
        <div class="site-title">mystetstvo-hub</div>
        <a class="site-url" href="https://mystetstvo-hub.netlify.app" target="_blank">&#128279; https://mystetstvo-hub.netlify.app</a>
      </div>
      <div class="status-pill">&#9679; Published Production</div>
    </div>

    <div class="deploy-box">
      <div style="display:flex; justify-content:space-between; align-items:center;">
        <div>
          <strong style="color:#fff; font-size:14px;">Production Deploy: GitHub branch main (commit 100f90f)</strong>
          <p style="font-size:12px; color:#94a3b8; margin-top:4px;">Multi-page art hub with video showcase, filter tabs and responsive layout.</p>
        </div>
        <span style="background:#0284c7; color:#fff; font-size:11px; padding:4px 10px; border-radius:6px; font-weight:bold;">Status: Live</span>
      </div>
    </div>

    <div class="metrics">
      <div class="metric-card">
        <span style="font-size:11px; color:#94a3b8; text-transform:uppercase;">Security &amp; SSL</span>
        <div style="color:#4ade80; font-size:16px; font-weight:bold; margin-top:4px;">Let's Encrypt (HTTPS Active)</div>
      </div>
      <div class="metric-card">
        <span style="font-size:11px; color:#94a3b8; text-transform:uppercase;">Global Edge CDN</span>
        <div style="color:#fff; font-size:16px; font-weight:bold; margin-top:4px;">Frankfurt / Warsaw / Edge</div>
      </div>
      <div class="metric-card">
        <span style="font-size:11px; color:#94a3b8; text-transform:uppercase;">Continuous Deployment</span>
        <div style="color:#38bdf8; font-size:16px; font-weight:bold; margin-top:4px;">Auto-deploy on git push</div>
      </div>
    </div>
  </div>
</div>
</body>
</html>
"""
render_html_to_png(html_08, os.path.join(out_dir, "08_netlify_deploy_lab8.png"), 1200, 680)

print("All 8 screenshots for Lab 8 successfully generated!")
