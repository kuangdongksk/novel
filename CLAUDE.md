# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Chinese web novel writing project with two main components:
1. **天玄大陆 (Tianxuan Continent)** - An original fantasy novel project
2. **小说分割工具** - A Python script for splitting novel chapters into manageable files

## Key Tools & Commands

### Novel Chapter Splitting
```bash
python split_novel.py
```
- Automatically processes "万相之王" novel files in `demo/万相之王/`
- Splits into 10-chapter segments stored in `demo/万相之王_分割版/`

### File Structure for Original Novel (天玄大陆)
```
Tianxuan Continent/
├── 天玄大陆.md              # Main index with hyperlinks
├── 天玄大陆/
│   ├── AI提示/              # AI writing prompts
│   ├── 世界观/              # World-building documents
│   ├── 人物/                # Character profiles
│   ├── 地点/                # Location descriptions
│   ├── 情节/                # Plot outlines
│   ├── 正文/                # Main story chapters
│   ├── 物品/                # Artifact/item descriptions
│   └── 章节大纲/            # Chapter-by-chapter outlines
```

### Writing Workflow
1. **Character Creation**: Add new characters to `天玄大陆/人物/` as individual .md files
2. **Location Building**: Document new locations in `天玄大陆/地点/`
3. **Plot Development**: Update `天玄大陆/情节/` with new story arcs
4. **Chapter Writing**: Add new chapters to appropriate volume folders in `天玄大陆/正文/`
5. **Cross-linking**: Update `天玄大陆.md` index to include new files

### Content Guidelines
- **Language**: All content in Chinese (Simplified)
- **Chapter Format**: Each chapter ~2000 characters
- **Hyperlink Convention**: Use `[显示文本](相对路径.md)` for internal links
- **Character Files**: Each character gets dedicated .md with detailed descriptions
- **Hierarchy**: Use nested folders for locations (e.g., `北域/云国/洛峰郡/`)

### AI Writing Integration
- Use prompts from `天玄大陆/AI提示/` for consistent style
- Extract style from existing chapters using: "阅读前十章，提炼风格特征"
- Generate new content with: "使用中文续写，一章两千字..."
- Always update corresponding index files after adding new content