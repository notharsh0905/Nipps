#Simulate a simple JSON API response for a blog post.
#Return title, author, and content fields with default values.

import json

post = {
    "title": input("Enter post title (default: 'Hello'): ") or "Hello",
    "author": input("Enter author (default: 'Anonymous'): ") or "Anonymous",
    "content": input("Enter content (default: 'Welcome!'): ") or "Welcome!"
}
print(json.dumps(post, indent=2))