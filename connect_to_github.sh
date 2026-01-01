#!/bin/bash
echo "🔗 Connecting hgpro101's aford folder to GitHub..."

# Go to folder
cd ~/Desktop/aford

# Clean any existing git
rm -rf .git

# Initialize
git init
echo "✅ Git initialized"

# Add files
git add .
echo "✅ Added all files"

# Commit
git commit -m "Aford.ai: Financial planning assistant"
echo "✅ Committed changes"

# Connect to GitHub
git remote add origin https://github.com/hgpro101/afordai.git
echo "✅ Connected to GitHub repository"

# Set branch
git branch -M main

# Push
echo "🚀 Pushing to GitHub..."
echo "📝 When asked:"
echo "   Username: hgpro101"
echo "   Password: GitHub Personal Access Token"
git push -u origin main

echo ""
echo "✅ Check your repository:"
echo "   https://github.com/hgpro101/afordai"