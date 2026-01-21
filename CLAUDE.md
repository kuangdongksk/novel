# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Chinese web novel writing and management project with multiple components:
1. **天玄大陆 (Tianxuan Continent)** - Original fantasy novel with detailed world-building
2. **小说分割工具** - Python script for splitting novel chapters (deleted but recoverable from git)
3. **其他小说项目** - Additional novel projects: 别墅谜案, 长安谜案, 龙旗纪元, 股神的陨落新编
4. **Demo 内容** - Sample novels and split tool output examples

## Key Tools & Commands

### Novel Chapter Splitting Tool
The `split_novel.py` script (deleted but available in git history) processes large novel files:
```bash
# Restore from git history if needed
git show HEAD:split_novel.py > split_novel.py

# Run the script
python split_novel.py
```
- Processes "万相之王" novel files in `demo/万相之王/` (4 large files: 1-500, 501-1000, 1001-1500, 1501-1767 chapters)
- Splits into 10-chapter segments stored in `demo/万相之王_分割版/`
- Uses regex to identify chapter boundaries: `第[一二三四五六七八九十百千万\d]+章`
- Output format: `万相之王_001-010章.txt`, `万相之王_011-020章.txt`, etc.

### Claude Permissions Configuration
- `.claude/settings.local.json`: Allows python, mkdir, find, rm, mv, dir, ls, cp commands
- `.claude/settings.json`: Allows git log commands

## Project Architecture

### Main Novel Projects Structure

#### 天玄大陆 (Tianxuan Continent) - Primary Fantasy Novel
```
Tianxuan Continent/
├── 天玄大陆.md              # Main index with hyperlinks to all content
├── 天玄大陆/
│   ├── AI提示/              # AI writing prompts and instructions
│   ├── 世界观/              # World-building documents (整体架构.md)
│   ├── 人物/                # Character profiles (丹无极.md, 剑无尘.md, etc.)
│   ├── 地点/                # Location descriptions (丹王谷.md, 林家禁地.md, etc.)
│   ├── 地点和人物/          # Combined location-character hierarchy
│   │   └── 北域/云国/洛峰郡/ # Nested structure: 寒天.md, 寒雪儿.md, 云无尘.md
│   ├── 情节/                # Plot outlines and story arcs
│   │   ├── 总览.md          # Overall plot summary
│   │   ├── 基础/等级/       # Power system: 灵圣.md, 灵帝.md, 灵皇.md, etc.
│   │   └── 北海大战.md      # Major story arcs
│   ├── 正文/                # Main story chapters
│   │   ├── 第一卷 求索/     # Volume 1 chapters
│   │   ├── 第二卷 北海大战/  # Volume 2 chapters
│   │   └── 第二卷 血脉觉醒/  # Volume 2 continuation
│   ├── 物品/                # Artifact/item descriptions
│   └── 章节大纲/            # Chapter-by-chapter outlines
```

#### Other Novel Projects
- **别墅谜案/** - "Villa Mystery" (6 chapters + outline)
- **长安谜案/** - "Chang'an Mystery" (4 chapters + outline)
- **龙旗纪元/** - "Dragon Flag Era" (similar structure to 天玄大陆)
- **股神的陨落新编/** - "God of Stocks' Fall" (two versions)

#### Demo Content
- `demo/万相之王/` - Original large novel files for splitting
- `demo/万相之王_分割版/` - Split versions (10 chapters per file)
- Other demo novels: 《万剑朝宗》, 《万蛊之王》, 《逆骨》, 《代码修真者》, 《九天剑域》

## Writing Workflow & Guidelines

### Core Writing Process
1. **Character Creation**: Add characters to `天玄大陆/人物/` or `天玄大陆/地点和人物/` hierarchy
2. **Location Building**: Document locations with nested folder structure (e.g., `北域/云国/洛峰郡/`)
3. **Plot Development**: Update `天玄大陆/情节/` with new story arcs and power system details
4. **Chapter Writing**: Add ~2000-character chapters to appropriate volume folders in `天玄大陆/正文/`
5. **Cross-linking**: Update `天玄大陆.md` index with `[显示文本](相对路径.md)` hyperlinks
6. **File Organization**: Each character, location, item gets dedicated .md file

### AI-Assisted Writing
- Use prompts from `AI提示.md` and `天玄大陆/AI提示/`
- **Style extraction**: "阅读前十章，提炼风格特征"
- **Content generation**: "使用中文续写，一章两千字，续写一百章"
- **Workflow**: Extract style → Generate content → Create individual files → Add hyperlinks
- Always maintain: Character consistency, plot coherence, proper hierarchy

### Content Standards
- **Language**: All content in Chinese (Simplified)
- **Chapter Length**: ~2000 characters per chapter
- **File Naming**: Use descriptive Chinese names with .md extension
- **Hyperlinks**: `[显示文本](相对路径.md)` for internal navigation
- **Hierarchy**: Reflect geographical/political relationships in folder structure

## Git Management
- Current branch: master
- Recent commits focus on rewriting mystery novels
- `split_novel.py` is deleted (D status) but recoverable from git history
- Commit messages typically describe novel content updates

## Development Notes
- No build/test/lint processes - this is a content creation project
- Primary tools: Python for file processing, Git for version control
- All novel content is in markdown/text format for easy editing
- Project demonstrates systematic approach to Chinese web novel development with AI assistance