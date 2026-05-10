import urllib.request
import os

urls = [
    "https://lh5.googleusercontent.com/p/CIABIhBX9pH-Fz7z1GO94Y0FjPvQ=w1200-h800-k-no",
    "https://lh3.googleusercontent.com/p/AF1QipMEpc-svp5yrew5UiITV0OsHy1DMNg1VLPRE1z8=w1200-h800-k-no",
    "https://lh3.googleusercontent.com/p/AF1QipPKN2xdSa23tIIUOxC8oAmnEd8m-D92ohU3r_rh=w1200-h800-k-no",
    "https://lh3.googleusercontent.com/p/AF1QipMu1qKYyZSKjTNh3n_wjA7B6dMuuxXxDWEKRvWS=w1200-h800-k-no",
    "https://lh3.googleusercontent.com/p/AF1QipOtqxAXRgwGIqSLCYgsJI03VbYrgZlrWfFeAjPW=w1200-h800-k-no",
    "https://lh3.googleusercontent.com/p/AF1QipOlFLEoApOGgFlQRvMfoPhTiNeb4INjs2J2Ww6V=w1200-h800-k-no",
    "https://lh3.googleusercontent.com/p/AF1QipMZE99hYM9IFak0YIffcyecvinF5Xbd7dF2y85O=w1200-h800-k-no",
    "https://lh3.googleusercontent.com/p/AF1QipM3DDO9HWQZxzRXgj_1gzwQrZNUxPeWIwGqkyN_=w1200-h800-k-no",
    "https://lh3.googleusercontent.com/p/AF1QipOb1Gu97pIxz7ggm0yXrb1rGkn8P5Ik8ZH1eLEZ=w1200-h800-k-no",
    "https://lh3.googleusercontent.com/p/AF1QipMtwHTz96qXZOXpWf_UcBk8oeY5A1RF0Xvkk-D8=w1200-h800-k-no",
    "https://lh3.googleusercontent.com/p/AF1QipNYG-flIyVXmbaVvXoK8HswUmiYFkNAqpop1Q4u=w1200-h800-k-no",
    "https://lh3.googleusercontent.com/p/AF1QipP2v69zk4zXQsoggE5kTJ0Kuj5lqxH9PBQ9wppS=w1200-h800-k-no",
    "https://lh3.googleusercontent.com/p/AF1QipPZXmBkF5D-QFVDJ0yZuGdNUtFHp2aDNCxF3eHO=w1200-h800-k-no",
    "https://lh3.googleusercontent.com/p/AF1QipNWWWmbNf6oENAlWVJyc8zZSHUFABDYkms95dT3=w1200-h800-k-no",
    "https://lh3.googleusercontent.com/p/AF1QipNbEfJG1ZR_1QPDDtTgUNOqB0ivcPCc-J307zLb=w1200-h800-k-no",
    "https://lh3.googleusercontent.com/p/AF1QipMgsywC8a_dvG8URf20m2aJNBnTU9vTYOq17iYd=w1200-h800-k-no",
    "https://lh3.googleusercontent.com/p/AF1QipPWcM8gwcfI6F13ftwuSuGF4l6GBgvk1136oAsa=w1200-h800-k-no"
]

os.makedirs('images', exist_ok=True)

for i, url in enumerate(urls):
    try:
        urllib.request.urlretrieve(url, f"images/pg-photo-{i+1}.jpg")
        print(f"Downloaded pg-photo-{i+1}.jpg")
    except Exception as e:
        print(f"Failed to download {url}: {e}")
