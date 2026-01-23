# 📚 COMPLETE DEPLOYMENT GUIDE

## Overview
Your Uber price predictor is now ready to deploy! This guide walks you through deploying to GitHub and Render.

---

## Part 1: Create GitHub Repository

### Step 1: Create a New Repo on GitHub
1. Go to https://github.com/new
2. Name it: `uber_price_predict` (or your preferred name)
3. **Description**: "Machine learning web app that predicts rideshare prices"
4. Choose **Public** or **Private** (your preference)
5. **DO NOT** initialize with README (we already have one)
6. Click "Create repository"

### Step 2: Add Remote and Push

Copy the repository URL from GitHub, then run:

```bash
cd /Users/rishabhkimothi/Desktop/projects/uber_price_predict

# Add the remote (replace YOUR_USERNAME)
git remote add origin https://github.com/YOUR_USERNAME/uber_price_predict.git

# Rename branch to main (if needed)
git branch -M main

# Push to GitHub
git push -u origin main
```

**What to replace:**
- `YOUR_USERNAME` → Your GitHub username

### Step 3: Verify on GitHub
- Visit `https://github.com/YOUR_USERNAME/uber_price_predict`
- You should see all your files uploaded

---

## Part 2: Deploy on Render

### Step 1: Create Render Account
1. Go to https://render.com
2. Sign up with GitHub (easier!)
3. Authorize Render to access your GitHub account

### Step 2: Create New Web Service
1. Click **"New +"** → **"Web Service"**
2. Select **"Connect a repository"**
3. Find and select `uber_price_predict`
4. Click **"Connect"**

### Step 3: Configure Deployment Settings

Fill in these settings:

| Field | Value |
|-------|-------|
| **Name** | `uber-price-predict` (no spaces, use hyphens) |
| **Region** | `Oregon` (US East, or your closest region) |
| **Branch** | `main` |
| **Runtime** | `Python 3` |
| **Build Command** | `pip install -r requirements.txt && python model.py` |
| **Start Command** | `gunicorn app:app` |

### Step 4: Environment Variables (Optional)
You can skip this for now, but here's how if needed:
- Click **"Advanced"** → **"Add Environment Variable"**
- Leave as default (Flask handles it automatically)

### Step 5: Deploy
1. Scroll down and click **"Create Web Service"**
2. Render will automatically:
   - Build your app
   - Install dependencies
   - Train your model
   - Start the server
3. Wait for the deploy (takes 2-5 minutes)

### Step 6: Get Your Live URL
Once deployed successfully, you'll see a URL like:
```
https://uber-price-predict.onrender.com
```

🎉 **That's your live app!** Share this link anywhere!

---

## Part 3: Monitor & Manage

### View Logs
1. In Render dashboard, click your service
2. Click **"Logs"** tab to see deployment details

### Redeploy After Changes
1. Make changes locally
2. Commit: `git add . && git commit -m "Your message"`
3. Push: `git push origin main`
4. Render automatically redeploys! (watch logs)

### Troubleshooting

**App says "Internal Server Error"**
- Check the Logs tab in Render
- Common issues:
  - Missing `rideshare_kaggle.csv` file
  - Wrong Python version
  - Missing dependencies in `requirements.txt`

**Model takes too long to train**
- First deployment trains the model (takes ~30-60 seconds)
- After that, it uses the cached `model.pkl`
- Normal!

---

## Part 4: Testing Your Live App

### Manual Testing
1. Open your Render URL
2. Enter test values:
   - Distance: `2.5`
   - Surge: `1.0`
   - Service: `Uber`
   - Ride: `UberX`
3. Click "Predict Price"
4. Should show an estimated price!

### API Testing (Advanced)
```bash
curl -X POST https://uber-price-predict.onrender.com/api/predict \
  -H "Content-Type: application/json" \
  -d '{
    "distance": 5.0,
    "surge_multiplier": 1.5,
    "cab_type": "Uber",
    "ride_name": "UberXL"
  }'
```

Expected response:
```json
{
  "success": true,
  "predicted_price": 18.75,
  "distance": 5.0,
  "surge_multiplier": 1.5,
  "cab_type": "Uber",
  "ride_name": "UberXL"
}
```

---

## Part 5: Continuous Deployment Workflow

### For Future Updates:

1. **Make changes locally**
   ```bash
   # Edit files in VS Code
   ```

2. **Test locally** (optional)
   ```bash
   python app.py
   # Visit http://localhost:5000
   ```

3. **Commit and push**
   ```bash
   git add .
   git commit -m "Feature: Added new ride type"
   git push origin main
   ```

4. **Render auto-deploys**
   - Check Render logs to confirm
   - Live updates in 1-3 minutes!

---

## Part 6: Sharing Your App

### Share the Link
- Send the Render URL to anyone: `https://uber-price-predict.onrender.com`
- No installation needed!
- Works on any device with a browser

### Add to Portfolio
- Add link to your GitHub README (already done!)
- Add link to your portfolio/resume
- Share on LinkedIn, Twitter, etc.

---

## File Structure Summary

```
uber_price_predict/
├── app.py                  ← Flask web server
├── model.py               ← ML model training
├── model.pkl              ← Trained model (auto-generated)
├── requirements.txt       ← Python dependencies
├── Procfile               ← Deployment config
├── runtime.txt            ← Python version
├── render.yaml            ← Render-specific config
├── README.md              ← Project documentation
├── .gitignore             ← Files to ignore in Git
├── rideshare_kaggle.csv   ← Training data
└── templates/
    └── index.html         ← Web interface
```

---

## Quick Command Reference

```bash
# Local development
cd /Users/rishabhkimothi/Desktop/projects/uber_price_predict
python app.py                    # Run locally
python model.py                  # Train model

# Git workflow
git status                       # Check changes
git add .                        # Stage all changes
git commit -m "message"          # Create commit
git push origin main             # Push to GitHub

# Common issues
rm -rf venv/                     # Remove virtual env if issues
pip install -r requirements.txt  # Reinstall dependencies
```

---

## Important Notes

⚠️ **Before First Deployment:**
- ✅ All files are created
- ✅ Git repo initialized
- ✅ Ready to push to GitHub

📌 **For Render:**
- Free tier includes 750 hours/month (plenty for a single app)
- App may sleep after 15 minutes of inactivity (wakes on request)
- No credit card required for free tier

🚀 **Next Steps:**
1. Create GitHub repository (if not done)
2. Push code: `git push -u origin main`
3. Connect to Render and deploy
4. Share your live link!

---

## Getting Help

- **Render Docs**: https://render.com/docs
- **Flask Docs**: https://flask.palletsprojects.com
- **GitHub Docs**: https://docs.github.com

Good luck! 🎉
