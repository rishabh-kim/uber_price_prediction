# 🚀 QUICK START GUIDE

## For You: Deploying to GitHub & Render

### Step 1: Push to GitHub (5 minutes)

1. **Create a GitHub repo** at https://github.com/new
   - Name: `uber_price_predict`
   - Choose public or private
   - DON'T initialize with files

2. **In your terminal, run:**
   ```bash
   cd /Users/rishabhkimothi/Desktop/projects/uber_price_predict
   git remote add origin https://github.com/YOUR_USERNAME/uber_price_predict.git
   git branch -M main
   git push -u origin main
   ```
   Replace `YOUR_USERNAME` with your GitHub username

3. **Verify:** Visit https://github.com/YOUR_USERNAME/uber_price_predict
   - You should see all your files

---

### Step 2: Deploy to Render (10 minutes)

1. **Go to** https://render.com and sign up with GitHub

2. **Click:** "New +" → "Web Service"

3. **Select:** Your `uber_price_predict` repository

4. **Configure:**
   - Name: `uber-price-predict`
   - Build Command: `pip install -r requirements.txt && python model.py`
   - Start Command: `gunicorn app:app`
   - Runtime: Python 3

5. **Click:** "Create Web Service"

6. **Wait:** 2-5 minutes for deployment

7. **Get URL:** Something like `https://uber-price-predict.onrender.com`

---

### Step 3: Done! 🎉

Your app is now **LIVE** and accessible 24/7!

**Share your link:**
```
https://uber-price-predict.onrender.com
```

---

## For Users: Using Your App

1. Open the link
2. Enter ride details:
   - Distance (miles)
   - Surge multiplier (1.0 = normal price)
   - Service (Uber/Lyft)
   - Ride type (UberX, UberXL, etc.)
3. Click "Predict Price"
4. See estimated price! 💰

---

## What You Built ✨

- **Backend**: Python Flask API with ML model
- **Frontend**: Beautiful responsive HTML/CSS/JS
- **Model**: Multivariate linear regression trained on rideshare data
- **Deployment**: Fully automated on Render

---

## Update Your App Anytime

```bash
# 1. Make changes locally
# 2. Commit
git add .
git commit -m "Your changes"
# 3. Push
git push origin main
# 4. Render auto-deploys! (watch in dashboard)
```

---

## Need Help?

See `DEPLOYMENT_GUIDE.md` for detailed instructions and troubleshooting.

**You're all set! 🚀**
