#!/usr/bin/env python3
"""
Obsidian 파일명을 Front Matter의 title 기반으로 일괄 변경하는 스크립트

Usage:
    python3 rename-by-title.py <directory> [lang]
    
Example:
    python3 rename-by-title.py ./초안 ko
    python3 rename-by-title.py ./draft en
"""

import os
import re
import sys
from pathlib import Path

def slugify(text, lang='ko'):
    """
    텍스트를 URL 친화적인 slug으로 변환
    
    Args:
        text: 변환할 텍스트
        lang: 언어 (ko 또는 en)
    
    Returns:
        변환된 slug
    """
    text = text.lower()
    
    if lang == 'ko':
        # 한글, 영문, 숫자만 허용
        text = re.sub(r'[^\w\s가-힣ㄱ-ㅎㅏ-ㅣ0-9-]', '', text)
    else:
        # 영문, 숫자만 허용
        text = re.sub(r'[^\w\s0-9-]', '', text)
    
    # 공백을 하이픈으로
    text = re.sub(r'\s+', '-', text)
    # 연속된 하이픈 제거
    text = re.sub(r'-+', '-', text)
    # 앞뒤 하이픈 제거
    text = text.strip('-')
    
    return text

def get_title_from_file(filepath):
    """
    마크다운 파일의 Front Matter에서 title 추출
    
    Args:
        filepath: 파일 경로
    
    Returns:
        title 문자열 또는 None
    """
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Front Matter 추출
        match = re.match(r'^---\n(.*?)\n---', content, re.DOTALL)
        if not match:
            return None
        
        front_matter = match.group(1)
        
        # title 필드 찾기
        title_match = re.search(r'^title:\s*["\']?([^"\'\n]+)["\']?', front_matter, re.MULTILINE)
        if title_match:
            return title_match.group(1).strip()
        
        return None
    except Exception as e:
        print(f"❌ Error reading {filepath.name}: {e}")
        return None

def rename_files(directory, lang='ko', dry_run=False):
    """
    디렉토리의 모든 마크다운 파일을 title 기반으로 일괄 변경
    
    Args:
        directory: 대상 디렉토리
        lang: 언어 접미사 (ko 또는 en)
        dry_run: True면 실제 변경 없이 미리보기만
    """
    directory = Path(directory)
    
    if not directory.exists():
        print(f"❌ Directory not found: {directory}")
        return
    
    files = list(directory.glob('*.md'))
    
    if not files:
        print(f"⚠️  No markdown files found in {directory}")
        return
    
    print(f"\n{'[DRY RUN] ' if dry_run else ''}Processing {len(files)} files in: {directory}")
    print(f"Language suffix: .{lang}.md")
    print("-" * 70)
    
    renamed_count = 0
    skipped_count = 0
    error_count = 0
    
    for filepath in files:
        # 이미 언어 접미사가 있는지 확인
        if filepath.stem.endswith(f'.{lang}'):
            basename = filepath.stem[:-len(f'.{lang}')]
        else:
            basename = filepath.stem
        
        title = get_title_from_file(filepath)
        
        if not title:
            print(f"⚠️  No title: {filepath.name}")
            skipped_count += 1
            continue
        
        slug = slugify(title, lang)
        
        if not slug:
            print(f"⚠️  Empty slug: {filepath.name} (title: {title})")
            skipped_count += 1
            continue
        
        new_filename = f"{slug}.{lang}.md"
        new_filepath = directory / new_filename
        
        # 이미 올바른 파일명
        if filepath.name == new_filename:
            print(f"✓ Already correct: {filepath.name}")
            skipped_count += 1
            continue
        
        # 파일 중복 체크
        if new_filepath.exists() and new_filepath != filepath:
            print(f"❌ Target exists: {filepath.name} → {new_filename}")
            error_count += 1
            continue
        
        # 파일명 변경
        if dry_run:
            print(f"🔄 Would rename: {filepath.name} → {new_filename}")
        else:
            try:
                filepath.rename(new_filepath)
                print(f"✅ Renamed: {filepath.name} → {new_filename}")
                renamed_count += 1
            except Exception as e:
                print(f"❌ Error: {filepath.name} - {e}")
                error_count += 1
    
    print("-" * 70)
    print(f"Summary:")
    print(f"  ✅ Renamed: {renamed_count}")
    print(f"  ⚠️  Skipped: {skipped_count}")
    print(f"  ❌ Errors: {error_count}")
    print()

def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)
    
    directory = sys.argv[1]
    lang = sys.argv[2] if len(sys.argv) > 2 else 'ko'
    dry_run = '--dry-run' in sys.argv or '-n' in sys.argv
    
    if lang not in ['ko', 'en']:
        print(f"❌ Invalid language: {lang} (must be 'ko' or 'en')")
        sys.exit(1)
    
    rename_files(directory, lang, dry_run)

if __name__ == '__main__':
    main()

