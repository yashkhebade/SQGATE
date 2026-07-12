import os
import json
import urllib.request
import urllib.error
import math
import re
from datetime import datetime

# Configure Paths
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BLOG_DIR = os.path.join(ROOT_DIR, 'blog')
POSTS_DIR = os.path.join(BLOG_DIR, 'posts')
CONFIG_PATH = os.path.join(ROOT_DIR, 'scripts', 'blog-config.json')
TEMPLATE_PATH = os.path.join(BLOG_DIR, 'template.html')
ARCHIVE_PATH = os.path.join(BLOG_DIR, 'index.html')

def load_config():
    with open(CONFIG_PATH, 'r', encoding='utf-8') as f:
        return json.load(f)

def generate_content(prompt_text):
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        print("WARNING: GEMINI_API_KEY not found. Using placeholder content.")
        return "<h2>Introduction</h2><p>This is a placeholder article because no API key was provided.</p><h3>Detailed Section</h3><p>Configure the GEMINI_API_KEY environment variable to generate real content.</p>"

    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={api_key}"
    
    payload = {
        "contents": [{"parts": [{"text": prompt_text}]}],
        "generationConfig": {
            "temperature": 0.7,
        }
    }
    
    data = json.dumps(payload).encode('utf-8')
    req = urllib.request.Request(url, data=data, headers={'Content-Type': 'application/json'})
    
    try:
        with urllib.request.urlopen(req) as response:
            result = json.loads(response.read().decode('utf-8'))
            text = result['candidates'][0]['content']['parts'][0]['text']
            
            # Clean up markdown formatting if the model accidentally returns markdown code blocks
            text = re.sub(r'^```html\s*', '', text, flags=re.MULTILINE)
            text = re.sub(r'^```\s*$', '', text, flags=re.MULTILINE)
            return text.strip()
    except Exception as e:
        print(f"API Error: {e}")
        return "<p>Error generating content.</p>"

def estimate_read_time(html_content):
    # Strip HTML tags to get pure text length
    text = re.sub(r'<[^>]+>', ' ', html_content)
    words = len(text.split())
    minutes = math.ceil(words / 200) # 200 WPM
    if minutes == 0:
        minutes = 1
    return f"{minutes} min read"

def inject_post_into_archive(slug, title, author, date, excerpt):
    with open(ARCHIVE_PATH, 'r', encoding='utf-8') as f:
        archive_html = f.read()
        
    # Check if already injected
    if f'href="/blog/posts/{slug}.html"' in archive_html:
        return
        
    card_html = f"""
    <a href="/blog/posts/{slug}.html" class="card">
      <div class="card-img-container">
        <img src="/blog/posts/images/{slug}.png" alt="{title}" class="card-img" onerror="this.src='/og-image.png'">
      </div>
      <div class="card-content">
        <span class="card-tag">Latest Updates</span>
        <h2 class="card-title">{title}</h2>
        <p class="card-desc">{excerpt}</p>
        <div class="card-meta">
          <span>{date}</span>
          <span>By {author}</span>
        </div>
      </div>
    </a>
"""
    
    # Inject right after <!-- Posts will be injected here by the build script -->
    target = "<!-- Posts will be injected here by the build script -->"
    archive_html = archive_html.replace(target, target + "\n" + card_html)
    
    with open(ARCHIVE_PATH, 'w', encoding='utf-8') as f:
        f.write(archive_html)

def main():
    if not os.path.exists(POSTS_DIR):
        os.makedirs(POSTS_DIR)
        
    config = load_config()
    system_prompt = config['llm_prompt']['system_prompt']
    
    with open(TEMPLATE_PATH, 'r', encoding='utf-8') as f:
        template = f.read()
        
    for topic in config['topics']:
        slug = topic['slug']
        title = topic['title']
        keywords = topic['keywords']
        post_path = os.path.join(POSTS_DIR, f"{slug}.html")
        
        print(f"Processing: {title}")
        
        if os.path.exists(post_path):
            print(f"Skipping {slug} HTML generation (already exists)")
            
            # Still attempt to inject into archive if missing
            with open(post_path, 'r', encoding='utf-8') as f:
                content_html = f.read()
            import re
            excerpt_match = re.search(r'<p>(.*?)</p>', content_html)
            excerpt = excerpt_match.group(1)[:120] + "..." if excerpt_match else "A comprehensive guide on " + title
            excerpt = re.sub(r'<[^>]+>', '', excerpt)
            date_str = "Recently Published"
            print("Injecting into archive...")
            inject_post_into_archive(slug, title, config['author']['name'], date_str, excerpt)
            
            continue
            
        full_prompt = f"{system_prompt}\n\nWrite a comprehensive article about: '{title}'.\nTarget Keywords: {keywords}.\nMake sure it is pure HTML. No markdown."
        
        print("Generating content from LLM...")
        content = generate_content(full_prompt)
        
        # Try to extract a simple excerpt (first paragraph)
        excerpt_match = re.search(r'<p>(.*?)</p>', content)
        excerpt = excerpt_match.group(1)[:120] + "..." if excerpt_match else "A comprehensive guide on " + title
        excerpt = re.sub(r'<[^>]+>', '', excerpt) # strip tags
        
        read_time = estimate_read_time(content)
        date_str = datetime.now().strftime("%B %d, %Y")
        
        print("Building HTML...")
        html = template
        html = html.replace("{{META_TITLE}}", f"{title} | SQGATE Blog")
        html = html.replace("{{META_DESCRIPTION}}", excerpt)
        html = html.replace("{{META_KEYWORDS}}", keywords)
        html = html.replace("{{CANONICAL_URL}}", f"{config['site_url']}/blog/posts/{slug}.html")
        html = html.replace("{{TITLE}}", title)
        html = html.replace("{{AUTHOR}}", config['author']['name'])
        html = html.replace("{{DATE}}", date_str)
        html = html.replace("{{READ_TIME}}", read_time)
        html = html.replace("{{CONTENT}}", content)
        
        # Basic Schema JSON
        schema = {
            "@context": "https://schema.org",
            "@type": "Article",
            "headline": title,
            "author": {
                "@type": "Person",
                "name": config['author']['name'],
                "url": config['author']['url']
            },
            "datePublished": datetime.now().isoformat()
        }
        html = html.replace("{{SCHEMA_JSON}}", json.dumps(schema, indent=2))
        
        with open(post_path, 'w', encoding='utf-8') as f:
            f.write(html)
            
        print("Injecting into archive...")
        inject_post_into_archive(slug, title, config['author']['name'], date_str, excerpt)
        
        print(f"Successfully built {slug}.html\n")

if __name__ == "__main__":
    main()
