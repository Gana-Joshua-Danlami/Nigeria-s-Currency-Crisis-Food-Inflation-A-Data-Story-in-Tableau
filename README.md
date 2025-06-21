# Nigeria's-Currency-Crisis-Food-Inflation-A-Data-Story-in-Tableau
> A visual deep-dive into how Nigeria’s weakening currency and rising food inflation affect everyday life, built as part of my beginner data journey using real-world data and Tableau.

## 📌 About the Project

This project started out of curiosity, a pain point, and ended as proof of growth.

At first, it was just me, a data analysis student at AltSchool Africa, trying to apply what I am learning into a real-life use case around what's going on in my immediate environment, out of wonder, i figured i could turn the chaos in Nigeria’s economy into a story I could understand with data.

This was my first time working on an independent project on my own, unlike the guided projects I am used to in school and on YouTube. I struggled for weeks. At one point, I wanted to give up, but my stubborn spirit couldn't relent until I finished what i started. I kept going back. Hooking. Resting. Vexing. Googling. Asking ChatGPT. Searching for resources on YouTube. Searching for help in the Tableau Public community. Failing. Trying again. Until I finally cracked it.

This project became a visual story of Nigeria’s **currency devaluation vs. food inflation**, built from scratch, no tutorial, no hand-holding. Just grit, curiosity, and a lot of grind to follow up till the end.

It wasn’t perfect. But it was real. And for me, that’s the win.

I didn't do this to impress anybody. I did it to *prove to myself* that I could apply the skills i am learning and use it to tell stories around my immediate environment. 

This goes to my fellow new migrants into the tech ecosystem. If you're just starting out, let this show you what’s possible when you stick with the process. You don't need permission to build. Just start.

## 🎯 Inspiration & Background

This project was inspired by the real-life struggles of the average Nigerian. you can feel the economy squeezing people daily especially around food prices and the value of our currency. I kept seeing the headlines and tweets, but I wanted to *understand* the patterns beneath the noise.

Rather than just complain, I asked myself: *What if I could explain this story with data? What if I could visualize what we're feeling?*

That’s what led me here, mixing my training as a data analyst with my storyteller’s heart to capture the economic tension every Nigerian can relate to.

It became more than a project. It became a way for me to find clarity in the chaos and show others what’s possible when you combine curiosity, storytelling, and the drive to grow.

## 🧠 Skills & Tools Used

This project wasn’t just about charts; it was about rolling up my sleeves, experimenting, failing forward, and turning theory into real-world storytelling.

Here’s a breakdown of the key tools and skills I leaned on:

- **🛠 Tools & Platforms:**
  - `Google Colab`: for data wrangling, cleanup, and exploratory analysis in Python
  - `Tableau Public`: for building the final dashboard and telling the visual story
  - `ChatGPT`: my debugging and ideation partner (it held my hand through some frustrating moments)
  - `Google Sheets`: quick data organization and version tracking
  - `YouTube & Tableau Community Forums`: self-learning on the go

- **📊 Core Skills Practiced:**
  - **Data Sourcing**: pulling raw, unstructured public datasets from multiple sources (CPI and exchange rate data)
  - **Data Cleaning**: merging, reshaping, and preparing messy data for analysis
  - **Exploratory Data Analysis** (EDA): using basic stats, trend analysis, and logic to uncover the story within the data
  - **Data Visualization**: transforming cleaned data into digestible visuals with a focus on clarity and emotional impact
  - **Problem Solving & Persistence**: When things broke, I didn’t quit. I found workarounds.

This wasn’t about being perfect. It was about being *resourceful*, taking limited tools and turning them into something amazing.

Every struggle sharpened a skill. Every error taught me something new. And every small win built my confidence.

## 📂 Data Sources

I didn’t want this project to rely on already-cleaned, “portfolio-perfect” datasets. I wanted the raw stuff, the kind that forces you to *actually think* and problem-solve.

I manually sourced the datasets from multiple public sites and institutional reports, each with its own formatting wahala:

- **[Nigeria Consumer Price Index (CPI)](https://nigerianstat.gov.ng)** : Monthly CPI records from the National Bureau of Statistics (NBS)
- **[Official Exchange Rate (₦ to $)](https://www.cbn.gov.ng/rates/exchratebycurrency.asp)** : Monthly exchange rates from the Central Bank of Nigeria (CBN)
- **[FMDQ Group](https://fmdqgroup.com/market-data/)** : Parallel/official rates from market data bulletins
- **[Trading Economics](https://tradingeconomics.com/nigeria/currency)** : Archival economic indicators for backup and validation
- **[Statista](https://www.statista.com/)** : For verifying yearly economic trends and food inflation figures
- **News Articles & Blogs** : Local economic commentary and timelines to add narrative context to the data

The datasets were *not* plug-and-play. I had to:

- Clean and merge them in **Google Colab**
- Reshape them to align with date values
- Manually extract data from PDFs, HTML tables, and inconsistent Excel files
- Deal with multiple currencies (parallel, official) and adjust for inflation gaps
- Fix data types, fill missing values, and create custom trend columns

At some point, I even thought of giving up. But the struggle itself became part of the value because real data work is messy, and this gave me a taste of that.

Everything I used is included in this repo, clean and documented, so you can trace the journey yourself or remix it into your own analysis.

## 📊 Analysis Journey & Visual Decisions

This wasn’t a straight line. It was a zigzag marathon of trial, error, rest, repeat.

I started with just one question:  
**“How bad has Nigeria’s food inflation become and is the currency crash the only driver?”**

From there, the real work began. No tutorial. No clean dataset. Just me, raw files, and vibes.

### 🧹 Cleaning & Exploration
- Merged CPI data and exchange rate data by month
- Dealt with missing rows, inconsistent date formats, and conflicting inflation categories
- Created custom fields like YoY (Year-on-Year) inflation, rolling trends, and parallel vs official exchange rate gaps
- Used **Python in Google Colab** to reshape and analyze the data
- Verified trends manually across multiple sources to avoid wrong narratives

### 🔍 Insights I Discovered
- Food inflation didn’t just spike randomly: it mirrored the timeline of ₦ devaluation almost exactly
- Parallel (black market) rates showed the earliest warning signs, months before official policy changes
- Government interventions barely made a dent: the data told a story of reactive, not proactive, decisions
- Inflation wasn’t only numbers; it had a human face: steep hikes in food basics like rice, bread, and yam

These insights became the backbone of my Tableau dashboard.

### 🎨 Visual Storytelling Decisions
I designed the visuals with one thing in mind:  
**“Can someone who knows nothing about economics understand this pain at a glance?”**

So I chose:
- **Line charts** for trends (to show inflation vs FX timeline side-by-side)
- **Dual-axis comparisons** to highlight correlation moments
- **Minimal text, strong color contrast**, and bold callouts to drive key points home
- **Hoverable tooltips** for clarity without clutter

The dashboard wasn’t about fancy aesthetics. It was about *truth*. I wanted the average Nigerian (and the curious outsider) to feel what we feel in a way that numbers alone don’t always show.

I tested, redesigned, and simplified until the message hit.






























