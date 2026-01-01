#!/bin/bash
cd ~/Desktop/aford

# Create proper requirements.txt
cat > requirements.txt << 'EOF'
streamlit==1.28.1
pandas==2.0.3
numpy==1.24.3
EOF

# Create runtime.txt
echo "python-3.9" > runtime.txt

# Push to GitHub
git add .
git commit -m "Fix deployment requirements"
git push origin main

echo "✅ Updated requirements pushed to GitHub"
echo "Streamlit will auto-redeploy in 1-2 minutes"