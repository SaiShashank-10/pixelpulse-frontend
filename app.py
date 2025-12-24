# import streamlit as st
# import requests
# import pandas as pd
# import plotly.graph_objects as go
# from PIL import Image
# import time

# # --- 1. PAGE CONFIGURATION ---
# st.set_page_config(
#     page_title="PixelPulse | AI Soundscapes",
#     page_icon="🎵",
#     layout="wide",
#     initial_sidebar_state="collapsed"
# )

# # --- 2. BACKEND CONNECTION ---
# API_URL = "http://127.0.0.1:8000/recommend"

# # --- 3. ADVANCED STYLING & LAYOUT FIXES ---
# st.markdown("""
#     <style>
#     @import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300;400;500;600;700&display=swap');

#     /* GLOBAL THEME */
#     html, body, [class*="css"] {
#         font-family: 'Space Grotesk', sans-serif;
#     }
    
#     .stApp {
#         background-color: #050505;
#         background-image: 
#             radial-gradient(circle at 10% 20%, rgba(34, 197, 94, 0.1) 0%, transparent 20%),
#             radial-gradient(circle at 90% 80%, rgba(20, 184, 166, 0.1) 0%, transparent 20%);
#         color: #ffffff;
#     }

#     /* HIDE STREAMLIT CHROME */
#     #MainMenu, footer, header {visibility: hidden;}
#     .block-container {padding-top: 2rem; padding-bottom: 5rem;}

#     /* ALIGNMENT UTILS */
#     .center-content {
#         display: flex;
#         justify-content: center;
#         align-items: center;
#         flex-direction: column;
#         text-align: center;
#     }

#     /* GLASS CARDS */
#     .glass-panel {
#         background: rgba(255, 255, 255, 0.03);
#         backdrop-filter: blur(12px);
#         -webkit-backdrop-filter: blur(12px);
#         border: 1px solid rgba(255, 255, 255, 0.08);
#         border-radius: 24px;
#         padding: 24px;
#         margin-bottom: 20px;
#         box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.3);
#     }

#     /* MEDIA PREVIEW FIXES */
#     /* This forces images to be centered and not too tall */
#     .stImage > img {
#         max-height: 300px; 
#         object-fit: contain;
#         border-radius: 12px;
#         margin: 0 auto;
#         display: block;
#         box-shadow: 0 10px 30px rgba(0,0,0,0.5);
#     }
#     .stVideo > video {
#         border-radius: 12px;
#         box-shadow: 0 10px 30px rgba(0,0,0,0.5);
#     }

#     /* CUSTOM UPLOADER */
#     .stFileUploader {
#         border: 1px dashed rgba(255,255,255,0.2);
#         border-radius: 16px;
#         padding: 2rem 1rem;
#         background: rgba(255,255,255,0.02);
#         transition: all 0.3s;
#     }
#     .stFileUploader:hover {
#         border-color: #22c55e;
#         background: rgba(34, 197, 94, 0.05);
#     }

#     /* GRADIENT BUTTON */
#     .stButton > button {
#         background: linear-gradient(90deg, #22c55e, #14b8a6);
#         color: #000;
#         font-weight: 700;
#         border: none;
#         padding: 0.75rem 0;
#         border-radius: 12px;
#         width: 100%;
#         text-transform: uppercase;
#         letter-spacing: 1px;
#         transition: transform 0.2s, box-shadow 0.2s;
#     }
#     .stButton > button:hover {
#         transform: translateY(-2px);
#         box-shadow: 0 10px 25px -5px rgba(34, 197, 94, 0.5);
#         color: #000;
#     }

#     /* PLAYLIST ROW */
#     .playlist-row {
#         display: flex;
#         align-items: center;
#         background: rgba(255,255,255,0.02);
#         border-radius: 12px;
#         padding: 12px;
#         margin-bottom: 10px;
#         border: 1px solid transparent;
#         transition: all 0.2s;
#     }
#     .playlist-row:hover {
#         background: rgba(255,255,255,0.05);
#         border-color: rgba(34, 197, 94, 0.3);
#         transform: translateX(5px);
#     }
    
#     /* CUSTOM SCROLLBAR FOR METRICS */
#     .metric-container {
#         display: flex;
#         gap: 10px;
#         margin-top: 5px;
#         font-size: 0.75rem;
#         color: #888;
#     }
#     .metric-pill {
#         background: rgba(255,255,255,0.05);
#         padding: 2px 8px;
#         border-radius: 4px;
#         display: flex;
#         align-items: center;
#         gap: 4px;
#     }
#     </style>
# """, unsafe_allow_html=True)

# # --- 4. HELPER FUNCTIONS ---

# def create_radar_chart(mood_vector):
#     """Creates a sleek, dark-mode radar chart."""
#     categories = ['Valence (Happy)', 'Energy', 'Danceability', 'Tempo', 'Acousticness']
#     # Close the polygon
#     values = mood_vector + [mood_vector[0]]
#     categories = categories + [categories[0]]

#     fig = go.Figure()
#     fig.add_trace(go.Scatterpolar(
#         r=values,
#         theta=categories,
#         fill='toself',
#         fillcolor='rgba(34, 197, 94, 0.2)',
#         line=dict(color='#22c55e', width=2),
#         marker=dict(size=0)
#     ))

#     fig.update_layout(
#         polar=dict(
#             radialaxis=dict(visible=True, range=[0, 1], showticklabels=False, linecolor='rgba(255,255,255,0.1)', gridcolor='rgba(255,255,255,0.05)'),
#             angularaxis=dict(linecolor='rgba(255,255,255,0.0)', tickfont=dict(color='#666', size=10, family='Space Grotesk'))
#         ),
#         paper_bgcolor='rgba(0,0,0,0)',
#         plot_bgcolor='rgba(0,0,0,0)',
#         showlegend=False,
#         margin=dict(l=30, r=30, t=10, b=10),
#         height=250,
#         dragmode=False
#     )
#     return fig

# # --- 5. MAIN LAYOUT ---

# # Title Header
# col1, col2 = st.columns([0.8, 0.2])
# with col1:
#     st.markdown('<h1 style="font-size: 4rem; margin-bottom: 0; line-height: 1;">Pixel<span style="color:#22c55e">Pulse</span></h1>', unsafe_allow_html=True)
#     st.markdown('<p style="color: #666; font-size: 1.1rem; margin-top: -10px;">Advanced Multimodal Music Recommendation Engine</p>', unsafe_allow_html=True)

# st.markdown("---")

# # Main Content Grid: 40% Left (Input), 60% Right (Output)
# left_col, right_col = st.columns([4, 6], gap="medium")

# # --- LEFT COLUMN: CONTROL CENTER ---
# with left_col:
#     st.markdown('<div class="glass-panel">', unsafe_allow_html=True)
#     st.markdown("### 📤 Input Signal")
    
#     uploaded_file = st.file_uploader("Drop image or video file", type=["jpg", "png", "jpeg", "mp4"])

#     if uploaded_file:
#         st.success("File uploaded successfully")
        
#         # PREVIEW CONTAINER
#         # We use a container to apply the CSS fixes specifically here
#         with st.container():
#             st.markdown('<div style="text-align: center; margin: 20px 0;">', unsafe_allow_html=True)
#             if uploaded_file.type.startswith('image'):
#                 image = Image.open(uploaded_file)
#                 st.image(image, caption="Visual Input", use_column_width=False, width=None) # Width None allows CSS max-height to work
#             elif uploaded_file.type.startswith('video'):
#                 st.video(uploaded_file)
#             st.markdown('</div>', unsafe_allow_html=True)

#         if st.button("Generate Soundscape"):
#             with st.spinner("Analyzing Visual Features & Mapping Vectors..."):
#                 try:
#                     files = {"file": (uploaded_file.name, uploaded_file.getvalue(), uploaded_file.type)}
#                     response = requests.post(API_URL, files=files)
                    
#                     if response.status_code == 200:
#                         st.session_state['result'] = response.json()
#                     else:
#                         st.error(f"API Error: {response.text}")
#                 except Exception as e:
#                     st.error(f"Connection Failed. Ensure Backend is running. {e}")
#     else:
#         # Placeholder when no file
#         st.markdown("""
#             <div style="height: 200px; display: flex; align-items: center; justify-content: center; border: 2px dashed rgba(255,255,255,0.05); border-radius: 12px; color: #444;">
#                 Waiting for media...
#             </div>
#         """, unsafe_allow_html=True)
        
#     st.markdown('</div>', unsafe_allow_html=True)

#     # Resume-Ready Technical Details (Collapsible)
#     with st.expander("🛠️ Under the Hood (Tech Stack)"):
#         st.markdown("""
#         **Architecture:**
#         * **Vision Model:** ViT (Vision Transformer) / ResNet50
#         * **Feature Extraction:** High-dimensional vector mapping
#         * **Clustering:** K-Means on 100k+ Spotify tracks
#         * **Distance Metric:** Cosine Similarity
#         * **Backend:** FastAPI (Async Python)
#         """)

# # --- RIGHT COLUMN: INTELLIGENCE DISPLAY ---
# with right_col:
#     if 'result' in st.session_state:
#         data = st.session_state['result']
        
#         # Top Row: Tags & Radar Chart
#         row1_col1, row1_col2 = st.columns([1, 1])
        
#         with row1_col1:
#             st.markdown('<div class="glass-panel" style="height: 320px;">', unsafe_allow_html=True)
#             st.markdown("#### 👁️ Vision Tags")
#             st.write("The AI detected these visual concepts:")
            
#             # Tags as pills
#             tags_html = "".join([
#                 f'<span style="display:inline-block; background:rgba(255,255,255,0.1); padding:5px 12px; border-radius:20px; font-size:0.85rem; margin:0 5px 8px 0; border:1px solid rgba(255,255,255,0.05);">#{tag}</span>' 
#                 for tag in data.get('tags', [])
#             ])
#             st.markdown(tags_html, unsafe_allow_html=True)
#             st.markdown('</div>', unsafe_allow_html=True)

#         with row1_col2:
#             st.markdown('<div class="glass-panel" style="height: 320px; display: flex; flex-direction: column; justify-content: center;">', unsafe_allow_html=True)
#             st.markdown("#### 📊 Mood Vector")
#             mood_vector = data.get('mood_vector', [0,0,0,0,0])
#             fig = create_radar_chart(mood_vector)
#             st.plotly_chart(fig, use_container_width=True, config={'displayModeBar': False})
#             st.markdown('</div>', unsafe_allow_html=True)

#         # Bottom Row: Playlist
#         st.markdown('<div class="glass-panel">', unsafe_allow_html=True)
#         st.markdown("#### 🎧 Curated Playlist")
        
#         for song in data.get('recommendations', []):
#             st.markdown(f"""
#             <div class="playlist-row">
#                 <div style="width: 40px; height: 40px; background: #222; border-radius: 8px; display: flex; align-items: center; justify-content: center; margin-right: 15px; color: #555;">🎵</div>
#                 <div style="flex-grow: 1;">
#                     <div style="font-weight: 600; color: #fff;">{song['track_name']}</div>
#                     <div style="font-size: 0.85rem; color: #888;">{song['artists']}</div>
#                     <div class="metric-container">
#                         <span class="metric-pill">⚡ Energy: {song['energy']:.2f}</span>
#                         <span class="metric-pill">😊 Valence: {song['valence']:.2f}</span>
#                     </div>
#                 </div>
#                 <a href="{song.get('external_url', '#')}" target="_blank" style="text-decoration: none;">
#                     <div style="background: #22c55e; color: #000; padding: 8px 16px; border-radius: 20px; font-weight: 600; font-size: 0.8rem; box-shadow: 0 4px 12px rgba(34,197,94,0.3);">
#                         PLAY
#                     </div>
#                 </a>
#             </div>
#             """, unsafe_allow_html=True)
#         st.markdown('</div>', unsafe_allow_html=True)

#         # JSON Download
#         st.download_button(
#             label="Download JSON Data",
#             data=str(data),
#             file_name="pixelpulse_analysis.json",
#             mime="application/json"
#         )

#     else:
#         # Idle State (Futuristic Placeholder)
#         st.markdown("""
#         <div class="glass-panel" style="height: 100%; display: flex; flex-direction: column; align-items: center; justify-content: center; opacity: 0.5; min-height: 500px;">
#             <div style="font-size: 4rem; margin-bottom: 20px;">🧠</div>
#             <h3>System Idle</h3>
#             <p>Awaiting visual input to initiate neural processing...</p>
#         </div>
#         """, unsafe_allow_html=True)

### working version below
# import streamlit as st
# import requests
# import plotly.graph_objects as go
# from PIL import Image

# st.set_page_config(page_title="PixelPulse | CLIP AI", page_icon="🎵", layout="wide")

# API_URL = "http://127.0.0.1:8000/recommend"

# # --- MODERN CSS ---
# st.markdown("""
#     <style>
#     @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;500;700&display=swap');
    
#     .stApp {
#         background-color: #050505;
#         background-image: radial-gradient(circle at 50% 0%, #1e1e24 0%, #000000 100%);
#         font-family: 'Outfit', sans-serif;
#         color: white;
#     }
    
#     /* Clean Cards for Results */
#     div[data-testid="stMetricValue"] {
#         font-size: 1.2rem !important;
#         color: #4ade80;
#     }
    
#     /* Playlist Rows */
#     .song-row {
#         background: rgba(255,255,255,0.03);
#         border-radius: 12px;
#         padding: 15px;
#         margin-bottom: 10px;
#         border-left: 4px solid #4ade80;
#         transition: transform 0.2s;
#     }
#     .song-row:hover {
#         background: rgba(255,255,255,0.08);
#         transform: translateX(5px);
#     }
    
#     /* Remove standard headers */
#     header, footer {visibility: hidden;}
#     </style>
# """, unsafe_allow_html=True)

# # --- RADAR CHART FUNCTION ---
# def create_radar(mood_vec):
#     categories = ['Valence', 'Energy', 'Dance', 'Tempo', 'Acoustic']
#     values = mood_vec + [mood_vec[0]]
#     cats = categories + [categories[0]]
    
#     fig = go.Figure(go.Scatterpolar(
#         r=values, theta=cats, fill='toself',
#         line_color='#4ade80', fillcolor='rgba(74, 222, 128, 0.2)'
#     ))
#     fig.update_layout(
#         polar=dict(
#             radialaxis=dict(visible=True, range=[0, 1], showticklabels=False, linecolor='#333'),
#             angularaxis=dict(tickfont=dict(color='white', size=12))
#         ),
#         paper_bgcolor='rgba(0,0,0,0)',
#         plot_bgcolor='rgba(0,0,0,0)',
#         margin=dict(l=40, r=40, t=40, b=40),
#         height=300
#     )
#     return fig

# # --- MAIN UI ---
# st.title("PixelPulse 🎵")
# st.caption("Powered by OpenAI CLIP & Spotify API")

# col_left, col_right = st.columns([1, 1.5], gap="large")

# with col_left:
#     st.markdown("### 📤 Input Visual")
#     uploaded_file = st.file_uploader("Upload Image", type=["jpg", "png", "jpeg"])
    
#     if uploaded_file:
#         st.image(uploaded_file, caption="Input Media", use_column_width=True)
        
#         if st.button("Analyze Vibe", type="primary", use_container_width=True):
#             with st.spinner("CLIP Model is analyzing scene context..."):
#                 try:
#                     files = {"file": (uploaded_file.name, uploaded_file.getvalue(), uploaded_file.type)}
#                     response = requests.post(API_URL, files=files)
#                     if response.status_code == 200:
#                         st.session_state['data'] = response.json()
#                     else:
#                         st.error("Server Error. Check Backend Terminal.")
#                 except Exception as e:
#                     st.error(f"Connection Failed: {e}")

# with col_right:
#     if 'data' in st.session_state:
#         data = st.session_state['data']
#         tags = data.get('tags', ["Unknown"])
        
#         # 1. DISPLAY TAGS (Clean Layout)
#         st.markdown("### 👁️ AI Scene Detection")
#         st.info(f"**Identified Scene:** {tags[0].title()}")
        
#         # 2. DISPLAY CHART
#         st.markdown("### 📊 Audio DNA")
#         fig = create_radar(data.get('mood_vector', [0.5]*5))
#         st.plotly_chart(fig, use_container_width=True)
        
#         # 3. DISPLAY PLAYLIST
#         st.markdown("### 🎧 Curated Tracks")
#         for song in data.get('recommendations', []):
#             st.markdown(f"""
#             <div class="song-row">
#                 <div style="font-weight:bold; font-size:1.1rem;">{song['track_name']}</div>
#                 <div style="color:#aaa; font-size:0.9rem;">{song['artists']}</div>
#                 <div style="display:flex; gap:10px; margin-top:5px; font-size:0.8rem; color:#4ade80;">
#                     <span>⚡ Energy: {song['energy']:.2f}</span>
#                     <span>😊 Valence: {song['valence']:.2f}</span>
#                 </div>
#                 <div style="margin-top:8px;">
#                     <a href="{song['external_url']}" target="_blank" style="text-decoration:none; color:black; background:#4ade80; padding:4px 12px; border-radius:12px; font-weight:bold; font-size:0.8rem;">
#                         PLAY ON SPOTIFY
#                     </a>
#                 </div>
#             </div>
#             """, unsafe_allow_html=True)
            
#     else:
#         # Placeholder
#         st.markdown("""
#         <div style="height:400px; display:flex; align-items:center; justify-content:center; border:2px dashed #333; border-radius:15px; color:#555;">
#             <h3>Waiting for analysis...</h3>
#         </div>
#         """, unsafe_allow_html=True)


# import streamlit as st
# import requests
# import plotly.graph_objects as go
# from PIL import Image

# st.set_page_config(page_title="PixelPulse | CLIP AI", page_icon="🎵", layout="wide")

# API_URL = "http://127.0.0.1:8000/recommend"

# # --- MODERN CSS ---
# st.markdown("""
#     <style>
#     @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;500;700&display=swap');
    
#     .stApp {
#         background-color: #050505;
#         background-image: radial-gradient(circle at 50% 0%, #1e1e24 0%, #000000 100%);
#         font-family: 'Outfit', sans-serif;
#         color: white;
#     }
    
#     .accuracy-box {
#         background: rgba(74, 222, 128, 0.1); 
#         border: 1px solid #4ade80; 
#         color: #4ade80; 
#         padding: 8px 16px; 
#         border-radius: 12px;
#         font-weight: bold;
#         display: inline-block;
#         margin-top: 10px;
#     }

#     .song-row {
#         background: rgba(255,255,255,0.03);
#         border-radius: 12px;
#         padding: 15px;
#         margin-bottom: 10px;
#         border-left: 4px solid #4ade80;
#         transition: transform 0.2s;
#     }
#     .song-row:hover {
#         background: rgba(255,255,255,0.08);
#         transform: translateX(5px);
#     }
    
#     header, footer {visibility: hidden;}
#     </style>
# """, unsafe_allow_html=True)

# # --- RADAR CHART FUNCTION ---
# def create_radar(mood_vec):
#     categories = ['Valence', 'Energy', 'Dance', 'Tempo', 'Acoustic']
#     values = mood_vec + [mood_vec[0]]
#     cats = categories + [categories[0]]
    
#     fig = go.Figure(go.Scatterpolar(
#         r=values, theta=cats, fill='toself',
#         line_color='#4ade80', fillcolor='rgba(74, 222, 128, 0.2)'
#     ))
#     fig.update_layout(
#         polar=dict(
#             radialaxis=dict(visible=True, range=[0, 1], showticklabels=False, linecolor='#333'),
#             angularaxis=dict(tickfont=dict(color='white', size=12))
#         ),
#         paper_bgcolor='rgba(0,0,0,0)',
#         plot_bgcolor='rgba(0,0,0,0)',
#         margin=dict(l=40, r=40, t=40, b=40),
#         height=300
#     )
#     return fig

# # --- MAIN UI ---
# st.title("PixelPulse 🎵")
# st.caption("Powered by OpenAI CLIP & Spotify API")

# col_left, col_right = st.columns([1, 1.5], gap="large")

# with col_left:
#     st.markdown("### 📤 Input Visual")
#     uploaded_file = st.file_uploader("Upload Image", type=["jpg", "png", "jpeg"])
    
#     if uploaded_file:
#         st.image(uploaded_file, caption="Input Media", use_column_width=True)
        
#         if st.button("Analyze Vibe", type="primary", use_container_width=True):
#             with st.spinner("CLIP Model is calculating accuracy..."):
#                 try:
#                     files = {"file": (uploaded_file.name, uploaded_file.getvalue(), uploaded_file.type)}
#                     response = requests.post(API_URL, files=files)
#                     if response.status_code == 200:
#                         st.session_state['data'] = response.json()
#                     else:
#                         st.error("Server Error. Check Backend Terminal.")
#                 except Exception as e:
#                     st.error(f"Connection Failed: {e}")

# with col_right:
#     if 'data' in st.session_state:
#         data = st.session_state['data']
#         tags = data.get('tags', ["Unknown"])
#         accuracy = data.get('accuracy', 0)
        
#         # 1. DISPLAY TAGS & ACCURACY
#         st.markdown("### 👁️ AI Scene Detection")
#         st.write(f"**Identified Scene:** {tags[0].title()}")
        
#         # The Accuracy Badge
#         st.markdown(f'<div class="accuracy-box">🎯 AI Confidence Score: {accuracy}%</div>', unsafe_allow_html=True)
        
#         # 2. DISPLAY CHART
#         st.markdown("### 📊 Audio DNA")
#         fig = create_radar(data.get('mood_vector', [0.5]*5))
#         st.plotly_chart(fig, use_container_width=True)
        
#         # 3. DISPLAY PLAYLIST
#         st.markdown("### 🎧 Curated Tracks")
#         for song in data.get('recommendations', []):
#             st.markdown(f"""
#             <div class="song-row">
#                 <div style="font-weight:bold; font-size:1.1rem;">{song['track_name']}</div>
#                 <div style="color:#aaa; font-size:0.9rem;">{song['artists']}</div>
#                 <div style="display:flex; gap:10px; margin-top:5px; font-size:0.8rem; color:#4ade80;">
#                     <span>⚡ Energy: {song['energy']:.2f}</span>
#                     <span>😊 Valence: {song['valence']:.2f}</span>
#                 </div>
#                 <div style="margin-top:8px;">
#                     <a href="{song['external_url']}" target="_blank" style="text-decoration:none; color:black; background:#4ade80; padding:4px 12px; border-radius:12px; font-weight:bold; font-size:0.8rem;">
#                         PLAY ON SPOTIFY
#                     </a>
#                 </div>
#             </div>
#             """, unsafe_allow_html=True)
            
#     else:
#         st.markdown("""
#         <div style="height:400px; display:flex; align-items:center; justify-content:center; border:2px dashed #333; border-radius:15px; color:#555;">
#             <h3>Waiting for analysis...</h3>
#         </div>
#         """, unsafe_allow_html=True)


# latest after img scanner working code 

# import streamlit as st
# import requests
# import plotly.graph_objects as go
# import time
# import base64

# # --- CONFIG ---
# st.set_page_config(page_title="PixelPulse | Visual AI", page_icon="🎵", layout="wide")
# API_URL = "http://127.0.0.1:8000/recommend"

# # --- MODERN CSS & SCANNER ANIMATION ---
# st.markdown("""
#     <style>
#     @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;500;700&display=swap');
    
#     .stApp {
#         background-color: #050505;
#         background-image: radial-gradient(circle at 50% 0%, #1e1e24 0%, #000000 100%);
#         font-family: 'Outfit', sans-serif;
#         color: white;
#     }
    
#     /* --- THE CYBERPUNK SCANNER CSS --- */
#     .scan-container {
#         position: relative;
#         width: 100%;
#         max-width: 700px;
#         margin: auto;
#         border-radius: 12px;
#         overflow: hidden;
#         border: 1px solid #4ade8055;
#         box-shadow: 0 0 20px rgba(74, 222, 128, 0.2);
#     }
    
#     .scan-container img {
#         width: 100%;
#         display: block;
#     }

#     .scan-overlay {
#         position: absolute;
#         top: 0;
#         left: 0;
#         width: 100%;
#         height: 100%;
#         background: linear-gradient(to bottom, 
#             transparent 0%, 
#             rgba(74, 222, 128, 0.2) 50%, 
#             rgba(74, 222, 128, 0.8) 51%, 
#             rgba(74, 222, 128, 0.2) 52%, 
#             transparent 100%);
#         animation: scan 2s linear infinite;
#         z-index: 2;
#         pointer-events: none; /* let clicks pass through */
#     }

#     @keyframes scan {
#         0% { transform: translateY(-100%); }
#         100% { transform: translateY(100%); }
#     }
#     /* -------------------------------- */
    
#     .accuracy-box {
#         background: rgba(74, 222, 128, 0.1); 
#         border: 1px solid #4ade80; 
#         color: #4ade80; 
#         padding: 8px 16px; 
#         border-radius: 12px;
#         font-weight: bold;
#         display: inline-block;
#         margin-bottom: 15px;
#     }

#     .color-circle {
#         width: 40px;
#         height: 40px;
#         border-radius: 50%;
#         display: inline-block;
#         margin-right: 10px;
#         border: 2px solid rgba(255,255,255,0.2);
#         box-shadow: 0 0 10px rgba(0,0,0,0.5);
#     }

#     .song-row {
#         background: rgba(255,255,255,0.03);
#         border-radius: 12px;
#         padding: 15px;
#         margin-bottom: 10px;
#         border-left: 4px solid #4ade80;
#         transition: transform 0.2s;
#     }
#     .song-row:hover {
#         background: rgba(255,255,255,0.08);
#         transform: translateX(5px);
#     }
    
#     header, footer {visibility: hidden;}
#     </style>
# """, unsafe_allow_html=True)

# # --- HELPER FUNCTIONS ---
# def create_radar(mood_vec):
#     categories = ['Valence', 'Energy', 'Dance', 'Tempo', 'Acoustic']
#     values = mood_vec + [mood_vec[0]]
#     cats = categories + [categories[0]]
    
#     fig = go.Figure(go.Scatterpolar(
#         r=values, theta=cats, fill='toself',
#         line_color='#4ade80', fillcolor='rgba(74, 222, 128, 0.2)'
#     ))
#     fig.update_layout(
#         polar=dict(
#             radialaxis=dict(visible=True, range=[0, 1], showticklabels=False, linecolor='#333'),
#             angularaxis=dict(tickfont=dict(color='white', size=12))
#         ),
#         paper_bgcolor='rgba(0,0,0,0)',
#         plot_bgcolor='rgba(0,0,0,0)',
#         margin=dict(l=40, r=40, t=40, b=40),
#         height=300
#     )
#     return fig

# # Helper to convert image to base64 for HTML injection
# def img_to_base64(img_file):
#     encoded_string = base64.b64encode(img_file.getvalue()).decode()
#     return f"data:image/{img_file.type.split('/')[-1]};base64,{encoded_string}"

# # --- MAIN UI ---
# st.title("PixelPulse 🎵")
# st.caption("Visual AI • Color Psychology • Audio Intelligence")

# col_left, col_right = st.columns([1, 1.5], gap="large")

# with col_left:
#     st.markdown("### 📤 Input Visual")
#     uploaded_file = st.file_uploader("Upload Image", type=["jpg", "png", "jpeg"])
    
#     if uploaded_file:
#         # Create placeholders for the image and the loading text
#         image_placeholder = st.empty()
#         progress_text = st.empty()

#         # Initially show normal image
#         image_placeholder.image(uploaded_file, caption="Input Media", use_column_width=True)
        
#         if st.button("Initiate Scan", type="primary", use_container_width=True):
            
#             # --- ACTIVATE SCANNER EFFECT ---
#             # Convert image to base64 so we can put it in HTML
#             img_base64 = img_to_base64(uploaded_file)
            
#             # Inject HTML with the image AND the scanner overlay div
#             scanner_html = f"""
#                 <div class="scan-container">
#                     <img src="{img_base64}">
#                     <div class="scan-overlay"></div>
#                 </div>
#             """
#             image_placeholder.markdown(scanner_html, unsafe_allow_html=True)

#             # Cyberpunk Status Updates
#             steps = [
#                 "📡 Establishing Neural Link...",
#                 "👁️ Analyzing Visual Cortex...",
#                 "🎨 Extracting Dominant Color Palette...",
#                 "🎵 Synthesizing Audio Vectors..."
#             ]
#             for step in steps:
#                 progress_text.markdown(f"**_{step}_**")
#                 time.sleep(0.7) # Let the scanner run for a bit
            
#             # Call Backend
#             try:
#                 files = {"file": (uploaded_file.name, uploaded_file.getvalue(), uploaded_file.type)}
#                 response = requests.post(API_URL, files=files)
                
#                 if response.status_code == 200:
#                     st.session_state['data'] = response.json()
#                     # Stop scanner, revert to normal image view
#                     progress_text.empty()
#                     image_placeholder.image(uploaded_file, caption="Scanned Input", use_column_width=True)
#                 else:
#                     st.error("Server Error.")
#                     image_placeholder.image(uploaded_file, caption="Input Media", use_column_width=True)
#             except Exception as e:
#                 st.error(f"Connection Failed: {e}")
#                 image_placeholder.image(uploaded_file, caption="Input Media", use_column_width=True)

# with col_right:
#     if 'data' in st.session_state:
#         data = st.session_state['data']
#         tags = data.get('tags', ["Unknown"])
#         accuracy = data.get('accuracy', 0)
#         palette = data.get('palette', [])
        
#         # 1. SCENE & ACCURACY
#         st.markdown("### 👁️ Intelligence Report")
#         st.markdown(f'<div class="accuracy-box">🎯 Confidence: {accuracy}%</div>', unsafe_allow_html=True)
#         st.write(f"**Detected Scene:** {tags[0].title()}")
        
#         # 2. COLOR PALETTE
#         st.write("**Dominant Palette:**")
#         cols_html = ""
#         for color in palette:
#             cols_html += f'<div class="color-circle" style="background-color: {color};"></div>'
#         st.markdown(f'<div>{cols_html}</div>', unsafe_allow_html=True)
        
#         # 3. CHART & PLAYLIST
#         st.markdown("---")
#         col_chart, col_list = st.columns([1, 1])
        
#         with col_chart:
#             st.markdown("#### 📊 Audio DNA")
#             fig = create_radar(data.get('mood_vector', [0.5]*5))
#             st.plotly_chart(fig, use_container_width=True)
            
#         with col_list:
#             st.markdown("#### 🎧 Recommendations")
#             for song in data.get('recommendations', [])[:4]:
#                 st.markdown(f"""
#                 <div class="song-row">
#                     <div style="font-weight:bold;">{song['track_name']}</div>
#                     <div style="font-size:0.8rem; color:#ccc;">{song['artists']}</div>
#                     <a href="{song['external_url']}" target="_blank" style="font-size:0.7rem; color:#4ade80;">▶ Play on Spotify</a>
#                 </div>
#                 """, unsafe_allow_html=True)
            
#     else:
#         st.info("Upload an image to start the neural engine.")

## working version with scanner effect along with cv 

# import streamlit as st
# import requests
# import plotly.graph_objects as go
# import time
# import base64

# # --- CONFIG ---
# st.set_page_config(page_title="PixelPulse | Visual AI", page_icon="🎵", layout="wide")
# API_URL = "http://127.0.0.1:8000/recommend"

# # --- CSS ---
# st.markdown("""
#     <style>
#     @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;500;700&display=swap');
    
#     .stApp {
#         background-color: #050505;
#         background-image: radial-gradient(circle at 50% 0%, #1e1e24 0%, #000000 100%);
#         font-family: 'Outfit', sans-serif;
#         color: white;
#     }
    
#     /* Scanner & Boxes */
#     .scan-container {
#         position: relative;
#         width: 100%;
#         max-width: 700px;
#         margin: auto;
#         border-radius: 12px;
#         overflow: hidden;
#         border: 1px solid #4ade8055;
#         box-shadow: 0 0 20px rgba(74, 222, 128, 0.2);
#     }
#     .scan-container img { width: 100%; display: block; }
#     .scan-overlay {
#         position: absolute; top: 0; left: 0; width: 100%; height: 100%;
#         background: linear-gradient(to bottom, transparent 0%, rgba(74, 222, 128, 0.2) 50%, rgba(74, 222, 128, 0.8) 51%, rgba(74, 222, 128, 0.2) 52%, transparent 100%);
#         animation: scan 2s linear infinite; z-index: 2; pointer-events: none;
#     }
#     @keyframes scan { 0% { transform: translateY(-100%); } 100% { transform: translateY(100%); } }
    
#     /* Info Pills */
#     .accuracy-box {
#         background: rgba(74, 222, 128, 0.1); border: 1px solid #4ade80; 
#         color: #4ade80; padding: 6px 12px; border-radius: 8px; 
#         font-weight: bold; display: inline-block; margin-right: 10px; font-size: 0.9rem;
#     }
#     .object-pill {
#         background: rgba(255, 255, 255, 0.1); border: 1px solid #555; 
#         color: #ddd; padding: 4px 10px; border-radius: 20px; 
#         font-size: 0.8rem; display: inline-block; margin: 3px;
#     }

#     /* Palette */
#     .color-circle {
#         width: 35px; height: 35px; border-radius: 50%; display: inline-block; 
#         margin-right: 8px; border: 2px solid rgba(255,255,255,0.2);
#     }

#     /* Songs */
#     .song-row {
#         background: rgba(255,255,255,0.03); border-radius: 12px; 
#         padding: 12px; margin-bottom: 8px; border-left: 4px solid #4ade80; 
#         transition: transform 0.2s;
#     }
#     .song-row:hover { background: rgba(255,255,255,0.08); transform: translateX(5px); }
    
#     header, footer {visibility: hidden;}
#     </style>
# """, unsafe_allow_html=True)

# # --- HELPERS ---
# def create_radar(mood_vec):
#     categories = ['Valence', 'Energy', 'Dance', 'Tempo', 'Acoustic']
#     values = mood_vec + [mood_vec[0]]
#     cats = categories + [categories[0]]
#     fig = go.Figure(go.Scatterpolar(r=values, theta=cats, fill='toself', line_color='#4ade80', fillcolor='rgba(74, 222, 128, 0.2)'))
#     fig.update_layout(polar=dict(radialaxis=dict(visible=True, range=[0, 1], showticklabels=False, linecolor='#333')), paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', height=300, margin=dict(l=40, r=40, t=20, b=20))
#     return fig

# def img_to_base64(img_file):
#     encoded_string = base64.b64encode(img_file.getvalue()).decode()
#     return f"data:image/{img_file.type.split('/')[-1]};base64,{encoded_string}"

# # --- MAIN UI ---
# st.title("PixelPulse 🎵")
# st.caption("Computer Vision • Object Detection • Audio Intelligence")

# col_left, col_right = st.columns([1, 1.4], gap="large")

# with col_left:
#     st.markdown("### 📤 Input Visual")
#     uploaded_file = st.file_uploader("Upload Image", type=["jpg", "png", "jpeg"])
    
#     if uploaded_file:
#         ph_img = st.empty()
#         ph_status = st.empty()
#         ph_img.image(uploaded_file, caption="Original Media", use_column_width=True)
        
#         if st.button("Initiate Neural Scan", type="primary", use_container_width=True):
#             # 1. Scanner Effect
#             img_b64 = img_to_base64(uploaded_file)
#             ph_img.markdown(f'<div class="scan-container"><img src="{img_b64}"><div class="scan-overlay"></div></div>', unsafe_allow_html=True)
            
#             steps = ["📡 Connecting to Neural Net...", "👁️ Identifying Objects (YOLO)...", "🎨 Analyzing Color Spectrum...", "🎵 Matching Audio DNA..."]
#             for s in steps:
#                 ph_status.markdown(f"**_{s}_**")
#                 time.sleep(0.6)
            
#             # 2. Backend Call
#             try:
#                 files = {"file": (uploaded_file.name, uploaded_file.getvalue(), uploaded_file.type)}
#                 response = requests.post(API_URL, files=files)
                
#                 if response.status_code == 200:
#                     data = st.session_state['data'] = response.json()
#                     ph_status.empty()
                    
#                     # 3. Show "Terminator View" (Image with Boxes)
#                     annotated_b64 = data.get('annotated_image')
#                     if annotated_b64:
#                         ph_img.image(base64.b64decode(annotated_b64), caption="Computer Vision Analysis", use_column_width=True)
#                 else:
#                     st.error("Server Error.")
#                     ph_img.image(uploaded_file)
#             except Exception as e:
#                 st.error(f"Error: {e}")
#                 ph_img.image(uploaded_file)

# with col_right:
#     if 'data' in st.session_state:
#         data = st.session_state['data']
#         tags = data.get('tags', ["Unknown"])
#         objects = data.get('detected_objects', [])
#         accuracy = data.get('accuracy', 0)
#         palette = data.get('palette', [])
        
#         # 1. REPORT HEADER
#         st.markdown("### 👁️ Intelligence Report")
#         st.markdown(f'<span class="accuracy-box">🎯 Confidence: {accuracy}%</span> <span class="accuracy-box">📦 Objects: {len(objects)}</span>', unsafe_allow_html=True)
#         st.write(f"**Scene Context:** {tags[0].title()}")
        
#         # 2. DETECTED OBJECTS & COLORS
#         st.write("**Detected Entities:**")
#         if objects:
#             obj_html = "".join([f'<span class="object-pill">{obj}</span>' for obj in objects])
#             st.markdown(obj_html, unsafe_allow_html=True)
#         else:
#             st.caption("No specific objects identified.")
            
#         st.write("**Dominant Palette:**")
#         cols_html = "".join([f'<div class="color-circle" style="background-color: {c};"></div>' for c in palette])
#         st.markdown(f'<div>{cols_html}</div>', unsafe_allow_html=True)
        
#         # 3. VISUALIZATIONS
#         st.markdown("---")
#         c1, c2 = st.columns([1, 1])
#         with c1:
#             st.markdown("#### 📊 Audio DNA")
#             st.plotly_chart(create_radar(data.get('mood_vector', [0.5]*5)), use_container_width=True)
#         with c2:
#             st.markdown("#### 🎧 Recommendations")
#             for song in data.get('recommendations', [])[:4]:
#                 st.markdown(f"""
#                 <div class="song-row">
#                     <div style="font-weight:bold;">{song['track_name']}</div>
#                     <div style="font-size:0.8rem; color:#aaa;">{song['artists']}</div>
#                     <a href="{song['external_url']}" target="_blank" style="font-size:0.7rem; color:#4ade80;">▶ Play on Spotify</a>
#                 </div>""", unsafe_allow_html=True)
#     else:
#         st.info("System Idle. Upload visuals to begin.")

# working version with scanner effect along with cv and plotly bg image

# import streamlit as st
# import requests
# import plotly.graph_objects as go
# import time
# import base64
# from PIL import Image
# import io

# # --- CONFIG ---
# st.set_page_config(page_title="PixelPulse | Visual AI", page_icon="🎵", layout="wide")
# API_URL = "http://127.0.0.1:8000/recommend"

# # --- CSS ---
# st.markdown("""
#     <style>
#     @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;500;700&display=swap');
    
#     .stApp {
#         background-color: #050505;
#         background-image: radial-gradient(circle at 50% 0%, #1e1e24 0%, #000000 100%);
#         font-family: 'Outfit', sans-serif;
#         color: white;
#     }
    
#     /* Scanner Effect */
#     .scan-container { position: relative; width: 100%; max-width: 700px; margin: auto; border-radius: 12px; overflow: hidden; border: 1px solid #4ade8055; box-shadow: 0 0 20px rgba(74, 222, 128, 0.2); }
#     .scan-container img { width: 100%; display: block; }
#     .scan-overlay { position: absolute; top: 0; left: 0; width: 100%; height: 100%; background: linear-gradient(to bottom, transparent 0%, rgba(74, 222, 128, 0.2) 50%, rgba(74, 222, 128, 0.8) 51%, rgba(74, 222, 128, 0.2) 52%, transparent 100%); animation: scan 2s linear infinite; z-index: 2; pointer-events: none; }
#     @keyframes scan { 0% { transform: translateY(-100%); } 100% { transform: translateY(100%); } }
    
#     /* Info Pills */
#     .accuracy-box { background: rgba(74, 222, 128, 0.1); border: 1px solid #4ade80; color: #4ade80; padding: 6px 12px; border-radius: 8px; font-weight: bold; display: inline-block; margin-right: 10px; font-size: 0.9rem; }
#     .object-pill { background: rgba(255, 255, 255, 0.1); border: 1px solid #555; color: #ddd; padding: 4px 10px; border-radius: 20px; font-size: 0.8rem; display: inline-block; margin: 3px; }
#     .color-circle { width: 35px; height: 35px; border-radius: 50%; display: inline-block; margin-right: 8px; border: 2px solid rgba(255,255,255,0.2); }
#     .song-row { background: rgba(255,255,255,0.03); border-radius: 12px; padding: 12px; margin-bottom: 8px; border-left: 4px solid #4ade80; transition: transform 0.2s; }
#     .song-row:hover { background: rgba(255,255,255,0.08); transform: translateX(5px); }
    
#     header, footer {visibility: hidden;}
#     </style>
# """, unsafe_allow_html=True)

# # --- HELPER FUNCTIONS ---

# def img_to_base64_str(img_file):
#     """Converts UploadedFile to base64 string for HTML display."""
#     encoded_string = base64.b64encode(img_file.getvalue()).decode()
#     return f"data:image/{img_file.type.split('/')[-1]};base64,{encoded_string}"

# def pil_to_base64(img_pil):
#     """Converts PIL Image to base64 string for Plotly background."""
#     buffer = io.BytesIO()
#     img_pil.save(buffer, format="PNG") # Save as PNG to ensure compatibility
#     encoded_string = base64.b64encode(buffer.getvalue()).decode()
#     return f"data:image/png;base64,{encoded_string}"

# def create_radar(mood_vec):
#     categories = ['Valence', 'Energy', 'Dance', 'Tempo', 'Acoustic']
#     values = mood_vec + [mood_vec[0]]
#     cats = categories + [categories[0]]
#     fig = go.Figure(go.Scatterpolar(r=values, theta=cats, fill='toself', line_color='#4ade80', fillcolor='rgba(74, 222, 128, 0.2)'))
#     fig.update_layout(polar=dict(radialaxis=dict(visible=True, range=[0, 1], showticklabels=False, linecolor='#333')), paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', height=300, margin=dict(l=40, r=40, t=20, b=20))
#     return fig

# def create_interactive_image(img_pil, detections):
#     """Uses Plotly to display image with invisible hover triggers."""
#     img_width, img_height = img_pil.size
    
#     # FIX: Convert PIL image to Base64 string so Plotly can read it
#     img_base64 = pil_to_base64(img_pil)

#     fig = go.Figure()

#     # 1. Add Image Background
#     fig.add_layout_image(
#         dict(
#             source=img_base64, # Using the base64 string here
#             xref="x", yref="y",
#             x=0, y=0,
#             sizex=img_width, sizey=img_height,
#             sizing="stretch",
#             layer="below"
#         )
#     )

#     # 2. Add Invisible Hover Markers
#     for det in detections:
#         x1, y1, x2, y2 = det['bbox']
#         label = det['label']
#         conf = det['confidence']
        
#         # Center of the box
#         center_x, center_y = (x1 + x2) / 2, (y1 + y2) / 2
        
#         fig.add_trace(go.Scatter(
#             x=[center_x], y=[center_y],
#             mode='markers',
#             marker=dict(color='#4ade80', size=20, opacity=0), # Invisible trigger
#             hoverinfo='text',
#             hovertext=f"<b>{label.upper()}</b><br>Confidence: {conf:.1%}",
#             showlegend=False
#         ))

#     # 3. Layout Setup (Remove axes, fit image)
#     fig.update_xaxes(showgrid=False, zeroline=False, range=[0, img_width], visible=False)
#     fig.update_yaxes(showgrid=False, zeroline=False, range=[img_height, 0], visible=False) # Reverse Y
    
#     fig.update_layout(
#         height=500,
#         margin=dict(l=0, r=0, t=0, b=0), # No margins
#         plot_bgcolor='rgba(0,0,0,0)',
#         paper_bgcolor='rgba(0,0,0,0)',
#         hovermode='closest',
#         dragmode=False 
#     )
#     return fig

# # --- MAIN UI ---
# st.title("PixelPulse 🎵")
# st.caption("Computer Vision • Interactive Detection • Audio Intelligence")

# col_left, col_right = st.columns([1, 1.4], gap="large")

# with col_left:
#     st.markdown("### 📤 Input Visual")
#     uploaded_file = st.file_uploader("Upload Image", type=["jpg", "png", "jpeg"])
    
#     if uploaded_file:
#         ph_img = st.empty()
#         ph_status = st.empty()
        
#         # Load PIL Image once
#         pil_image = Image.open(uploaded_file).convert("RGB")
#         ph_img.image(pil_image, caption="Original Media", use_column_width=True)
        
#         if st.button("Initiate Neural Scan", type="primary", use_container_width=True):
#             # 1. Scanner Effect
#             img_b64 = img_to_base64_str(uploaded_file)
#             ph_img.markdown(f'<div class="scan-container"><img src="{img_b64}"><div class="scan-overlay"></div></div>', unsafe_allow_html=True)
            
#             steps = ["📡 Connecting to Neural Net...", "👁️ Identifying Objects (YOLO)...", "🎨 Analyzing Color Spectrum...", "🎵 Matching Audio DNA..."]
#             for s in steps:
#                 ph_status.markdown(f"**_{s}_**")
#                 time.sleep(0.5)
            
#             # 2. Backend Call
#             try:
#                 files = {"file": (uploaded_file.name, uploaded_file.getvalue(), uploaded_file.type)}
#                 response = requests.post(API_URL, files=files)
                
#                 if response.status_code == 200:
#                     data = st.session_state['data'] = response.json()
#                     ph_status.empty()
                    
#                     # 3. INTERACTIVE DISPLAY
#                     detections = data.get('detections', [])
#                     if detections:
#                         fig = create_interactive_image(pil_image, detections)
#                         ph_img.plotly_chart(fig, use_container_width=True, config={'displayModeBar': False})
#                         st.caption("💡 Tip: Hover over objects (invisible targets) to reveal AI data.")
#                     else:
#                         ph_img.image(pil_image, caption="Analysis Complete (No specific objects)", use_column_width=True)
                        
#                 else:
#                     st.error("Server Error.")
#                     ph_img.image(pil_image)
#             except Exception as e:
#                 st.error(f"Error: {e}")
#                 ph_img.image(pil_image)

# with col_right:
#     if 'data' in st.session_state:
#         data = st.session_state['data']
#         tags = data.get('tags', ["Unknown"])
#         objects = data.get('detected_objects', [])
#         accuracy = data.get('accuracy', 0)
#         palette = data.get('palette', [])
        
#         # 1. REPORT HEADER
#         st.markdown("### 👁️ Intelligence Report")
#         st.markdown(f'<span class="accuracy-box">🎯 Confidence: {accuracy}%</span> <span class="accuracy-box">📦 Objects: {len(objects)}</span>', unsafe_allow_html=True)
#         st.write(f"**Scene Context:** {tags[0].title()}")
        
#         # 2. OBJECTS & COLORS
#         st.write("**Detected Entities:**")
#         if objects:
#             obj_html = "".join([f'<span class="object-pill">{obj}</span>' for obj in objects])
#             st.markdown(obj_html, unsafe_allow_html=True)
#         else:
#             st.caption("No specific objects identified.")
            
#         st.write("**Dominant Palette:**")
#         cols_html = "".join([f'<div class="color-circle" style="background-color: {c};"></div>' for c in palette])
#         st.markdown(f'<div>{cols_html}</div>', unsafe_allow_html=True)
        
#         # 3. VISUALIZATIONS
#         st.markdown("---")
#         c1, c2 = st.columns([1, 1])
#         with c1:
#             st.markdown("#### 📊 Audio DNA")
#             st.plotly_chart(create_radar(data.get('mood_vector', [0.5]*5)), use_container_width=True, config={'displayModeBar': False})
#         with c2:
#             st.markdown("#### 🎧 Recommendations")
#             for song in data.get('recommendations', [])[:4]:
#                 st.markdown(f"""
#                 <div class="song-row">
#                     <div style="font-weight:bold;">{song['track_name']}</div>
#                     <div style="font-size:0.8rem; color:#aaa;">{song['artists']}</div>
#                     <a href="{song['external_url']}" target="_blank" style="font-size:0.7rem; color:#4ade80;">▶ Play on Spotify</a>
#                 </div>""", unsafe_allow_html=True)
#     else:
#         st.info("System Idle. Upload visuals to begin.")


# latest working version with scanner effect along with cv and plotly bg image and improved css

# import streamlit as st
# import requests
# import plotly.graph_objects as go
# import time
# import base64
# from PIL import Image
# import io

# # --- CONFIG ---
# st.set_page_config(page_title="PixelPulse | Visual AI", page_icon="🎵", layout="wide")
# API_URL = "http://127.0.0.1:8000/recommend"

# # --- CSS IMPROVEMENTS ---
# st.markdown("""
#     <style>
#     @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;500;700&display=swap');
    
#     .stApp {
#         background-color: #050505;
#         background-image: radial-gradient(circle at 50% 0%, #1e1e24 0%, #000000 100%);
#         font-family: 'Outfit', sans-serif;
#         color: white;
#     }
    
#     /* Improved Electric Scanner Effect */
#     .scan-container { position: relative; width: 100%; border-radius: 12px; overflow: hidden; border: 1px solid #4ade8055; box-shadow: 0 0 25px rgba(74, 222, 128, 0.3); }
#     .scan-container img { width: 100%; display: block; }
#     .scan-overlay { 
#         position: absolute; top: 0; left: 0; width: 100%; height: 100%; 
#         background: linear-gradient(to bottom, transparent 0%, rgba(74, 222, 128, 0.1) 45%, rgba(100, 255, 150, 0.9) 50%, rgba(74, 222, 128, 0.1) 55%, transparent 100%); 
#         animation: scan 1.5s cubic-bezier(0.4, 0.0, 0.2, 1) infinite; /* More dynamic speed */
#         z-index: 2; pointer-events: none;
#         box-shadow: 0 0 15px rgba(74, 222, 128, 0.5); /* Glowing edge */
#     }
#     @keyframes scan { 0% { transform: translateY(-100%); } 100% { transform: translateY(100%); } }
    
#     /* UI Elements */
#     .accuracy-box { background: rgba(74, 222, 128, 0.15); border: 1px solid #4ade80; color: #4ade80; padding: 6px 12px; border-radius: 8px; font-weight: bold; display: inline-block; margin-right: 10px; font-size: 0.9rem; }
#     .object-pill { background: rgba(255, 255, 255, 0.1); border: 1px solid #4ade8088; color: #dfdfdf; padding: 4px 10px; border-radius: 20px; font-size: 0.8rem; display: inline-block; margin: 3px; }
#     .color-circle { width: 35px; height: 35px; border-radius: 50%; display: inline-block; margin-right: 8px; border: 2px solid rgba(255,255,255,0.2); box-shadow: 0 0 5px rgba(0,0,0,0.3); }
#     .song-row { background: rgba(255,255,255,0.03); border-radius: 12px; padding: 12px; margin-bottom: 8px; border-left: 4px solid #4ade80; transition: transform 0.2s; }
#     .song-row:hover { background: rgba(255,255,255,0.08); transform: translateX(5px); }
    
#     /* Fix Plotly modebar overlap */
#     .modebar { display: none !important; }
#     header, footer {visibility: hidden;}
#     </style>
# """, unsafe_allow_html=True)

# # --- HELPER FUNCTIONS ---

# def img_to_base64_str(img_file):
#     encoded_string = base64.b64encode(img_file.getvalue()).decode()
#     return f"data:image/{img_file.type.split('/')[-1]};base64,{encoded_string}"

# def pil_to_base64(img_pil):
#     buffer = io.BytesIO()
#     img_pil.save(buffer, format="PNG")
#     encoded_string = base64.b64encode(buffer.getvalue()).decode()
#     return f"data:image/png;base64,{encoded_string}"

# def create_radar(mood_vec):
#     categories = ['Valence', 'Energy', 'Dance', 'Tempo', 'Acoustic']
#     values = mood_vec + [mood_vec[0]]
#     cats = categories + [categories[0]]
#     fig = go.Figure(go.Scatterpolar(r=values, theta=cats, fill='toself', line_color='#4ade80', fillcolor='rgba(74, 222, 128, 0.2)'))
#     fig.update_layout(polar=dict(radialaxis=dict(visible=True, range=[0, 1], showticklabels=False, linecolor='#333')), paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', height=300, margin=dict(l=40, r=40, t=20, b=20))
#     return fig

# # --- IMPROVED INTERACTIVE IMAGE FUNCTION ---
# def create_interactive_image(img_pil, detections):
#     img_width, img_height = img_pil.size
#     img_base64 = pil_to_base64(img_pil)

#     fig = go.Figure()

#     # 1. Add Image Background
#     fig.add_layout_image(
#         dict(
#             source=img_base64,
#             xref="x", yref="y",
#             x=0, y=0, # Start from top-left
#             sizex=img_width, sizey=img_height,
#             sizing="stretch",
#             layer="below"
#         )
#     )

#     # 2. Add Subtle HUD Boxes & Hover Triggers
#     shapes = []
#     for det in detections:
#         x1, y1, x2, y2 = det['bbox']
#         label = det['label']
#         conf = det['confidence']
        
#         # A. Add subtle bounding box shape (HUD look)
#         shapes.append(dict(
#             type="rect",
#             x0=x1, y0=y1, x1=x2, y1=y2,
#             line=dict(color='rgba(74, 222, 128, 0.5)', width=1), # Faint green line
#             fillcolor='rgba(74, 222, 128, 0.05)' # Very faint green fill
#         ))

#         # B. Add central hover trigger marker
#         center_x, center_y = (x1 + x2) / 2, (y1 + y2) / 2
#         fig.add_trace(go.Scatter(
#             x=[center_x], y=[center_y],
#             mode='markers',
#             # Slightly visible center dot now
#             marker=dict(color='#4ade80', size=8, opacity=0.4, line=dict(width=1, color='white')), 
#             hoverinfo='text',
#             # Improved Tooltip HTML
#             hovertext=f"<span style='color:#4ade80; font-weight:bold;'>[ DETECTED OBJECT ]</span><br>TYPE: {label.upper()}<br>CONFIDENCE: {conf:.1%}",
#             showlegend=False
#         ))

#     # 3. Layout Setup (ASPECT RATIO LOCK & COORDINATE FIX)
#     fig.update_xaxes(showgrid=False, zeroline=False, range=[0, img_width], visible=False)
#     # IMPORTANT: yaxis matches image coordinates (0 at top) and locks aspect ratio to X axis
#     fig.update_yaxes(showgrid=False, zeroline=False, range=[img_height, 0], visible=False, scaleanchor="x", scaleratio=1)
    
#     fig.update_layout(
#         # Remove hardcoded height so Plotly calculates it based on width + aspect ratio
#         margin=dict(l=0, r=0, t=0, b=0),
#         plot_bgcolor='rgba(0,0,0,0)',
#         paper_bgcolor='rgba(0,0,0,0)',
#         hovermode='closest',
#         dragmode=False,
#         shapes=shapes # Add the HUD boxes
#     )
#     return fig

# # --- MAIN UI ---
# st.title("PixelPulse 🎵")
# st.caption("Computer Vision • Interactive Detection • Audio Intelligence")

# col_left, col_right = st.columns([1, 1.4], gap="large")

# with col_left:
#     st.markdown("### 📤 Input Visual")
#     uploaded_file = st.file_uploader("Upload Image", type=["jpg", "png", "jpeg"])
    
#     if uploaded_file:
#         ph_img = st.empty()
#         ph_status = st.empty()
        
#         pil_image = Image.open(uploaded_file).convert("RGB")
#         # Display initial image. 
#         ph_img.image(pil_image, caption="Original Media", use_column_width=True)
        
#         if st.button("Initiate Neural Scan", type="primary", use_container_width=True):
#             # 1. Improved Scanner Effect
#             img_b64 = img_to_base64_str(uploaded_file)
#             # Removed max-width constraint for better fit during scan
#             ph_img.markdown(f'<div class="scan-container" style="max-width: none;"><img src="{img_b64}"><div class="scan-overlay"></div></div>', unsafe_allow_html=True)
            
#             steps = ["📡 Establishing Neural Link...", "👁️ Processing Visual Cortex (YOLOv8)...", "🎨 Extracting Dominant Color Palette...", "🎵 Synthesizing Audio Vectors..."]
#             for s in steps:
#                 ph_status.markdown(f"**_{s}_**")
#                 time.sleep(0.6)
            
#             # 2. Backend Call
#             try:
#                 files = {"file": (uploaded_file.name, uploaded_file.getvalue(), uploaded_file.type)}
#                 response = requests.post(API_URL, files=files)
                
#                 if response.status_code == 200:
#                     data = st.session_state['data'] = response.json()
#                     ph_status.empty()
                    
#                     # 3. INTERACTIVE DISPLAY (Size Jump Fixed)
#                     detections = data.get('detections', [])
#                     if detections:
#                         fig = create_interactive_image(pil_image, detections)
#                         # use_column_width=True combined with aspect ratio lock fixes the size jump
#                         ph_img.plotly_chart(fig, use_container_width=True, config={'displayModeBar': False})
#                         st.caption("💡 HUD Active: Hover over detected regions for analysis data.")
#                     else:
#                         ph_img.image(pil_image, caption="Analysis Complete (No specific objects)", use_column_width=True)
                        
#                 else:
#                     st.error("Server Error.")
#                     ph_img.image(pil_image)
#             except Exception as e:
#                 st.error(f"Error: {e}")
#                 ph_img.image(pil_image)

# with col_right:
#     if 'data' in st.session_state:
#         data = st.session_state['data']
#         tags = data.get('tags', ["Unknown"])
#         objects = data.get('detected_objects', [])
#         accuracy = data.get('accuracy', 0)
#         palette = data.get('palette', [])
        
#         # 1. REPORT HEADER
#         st.markdown("### 👁️ Intelligence Report")
#         st.markdown(f'<span class="accuracy-box">🎯 Confidence: {accuracy}%</span> <span class="accuracy-box">📦 Objects: {len(objects)}</span>', unsafe_allow_html=True)
#         st.write(f"**Scene Context:** {tags[0].title()}")
        
#         # 2. OBJECTS & COLORS
#         st.write("**Detected Entities:**")
#         if objects:
#             obj_html = "".join([f'<span class="object-pill">{obj}</span>' for obj in objects])
#             st.markdown(obj_html, unsafe_allow_html=True)
#         else:
#             st.caption("No specific objects identified.")
            
#         st.write("**Dominant Palette:**")
#         cols_html = "".join([f'<div class="color-circle" style="background-color: {c};"></div>' for c in palette])
#         st.markdown(f'<div>{cols_html}</div>', unsafe_allow_html=True)
        
#         # 3. VISUALIZATIONS
#         st.markdown("---")
#         c1, c2 = st.columns([1, 1])
#         with c1:
#             st.markdown("#### 📊 Audio DNA")
#             st.plotly_chart(create_radar(data.get('mood_vector', [0.5]*5)), use_container_width=True, config={'displayModeBar': False})
#         with c2:
#             st.markdown("#### 🎧 Recommendations")
#             for song in data.get('recommendations', [])[:4]:
#                 st.markdown(f"""
#                 <div class="song-row">
#                     <div style="font-weight:bold;">{song['track_name']}</div>
#                     <div style="font-size:0.8rem; color:#aaa;">{song['artists']}</div>
#                     <a href="{song['external_url']}" target="_blank" style="font-size:0.7rem; color:#4ade80;">▶ Play on Spotify</a>
#                 </div>""", unsafe_allow_html=True)
#     else:
#         st.info("System Idle. Upload visuals to begin.")

# import streamlit as st
# import requests
# import plotly.graph_objects as go
# import time
# import base64
# from PIL import Image
# import io

# # --- CONFIG ---
# st.set_page_config(page_title="PixelPulse | Visual AI", page_icon="🎵", layout="wide")
# API_URL = "http://127.0.0.1:8000/recommend"

# # --- CSS ---
# st.markdown("""
#     <style>
#     @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;500;700&display=swap');
    
#     .stApp {
#         background-color: #050505;
#         background-image: radial-gradient(circle at 50% 0%, #1e1e24 0%, #000000 100%);
#         font-family: 'Outfit', sans-serif;
#         color: white;
#     }
    
#     /* Improved Electric Scanner Effect */
#     .scan-container { position: relative; width: 100%; border-radius: 12px; overflow: hidden; border: 1px solid #4ade8055; box-shadow: 0 0 25px rgba(74, 222, 128, 0.3); }
#     .scan-container img { width: 100%; display: block; }
#     .scan-overlay { 
#         position: absolute; top: 0; left: 0; width: 100%; height: 100%; 
#         background: linear-gradient(to bottom, transparent 0%, rgba(74, 222, 128, 0.1) 45%, rgba(100, 255, 150, 0.9) 50%, rgba(74, 222, 128, 0.1) 55%, transparent 100%); 
#         animation: scan 1.5s cubic-bezier(0.4, 0.0, 0.2, 1) infinite; 
#         z-index: 2; pointer-events: none;
#         box-shadow: 0 0 15px rgba(74, 222, 128, 0.5); 
#     }
#     @keyframes scan { 0% { transform: translateY(-100%); } 100% { transform: translateY(100%); } }
    
#     /* UI Elements */
#     .accuracy-box { background: rgba(74, 222, 128, 0.15); border: 1px solid #4ade80; color: #4ade80; padding: 6px 12px; border-radius: 8px; font-weight: bold; display: inline-block; margin-right: 10px; font-size: 0.9rem; }
#     .object-pill { background: rgba(255, 255, 255, 0.1); border: 1px solid #4ade8088; color: #dfdfdf; padding: 4px 10px; border-radius: 20px; font-size: 0.8rem; display: inline-block; margin: 3px; }
#     .color-circle { width: 35px; height: 35px; border-radius: 50%; display: inline-block; margin-right: 8px; border: 2px solid rgba(255,255,255,0.2); box-shadow: 0 0 5px rgba(0,0,0,0.3); }
    
#     /* Song Row with Audio Player support */
#     .song-row { background: rgba(255,255,255,0.03); border-radius: 12px; padding: 15px; margin-bottom: 12px; border-left: 4px solid #4ade80; transition: transform 0.2s; }
#     .song-row:hover { background: rgba(255,255,255,0.08); transform: translateX(5px); }
#     .stAudio { width: 100%; margin-top: 10px; }
    
#     .modebar { display: none !important; }
#     header, footer {visibility: hidden;}
#     </style>
# """, unsafe_allow_html=True)

# # --- HELPER FUNCTIONS ---
# def img_to_base64_str(img_file):
#     encoded_string = base64.b64encode(img_file.getvalue()).decode()
#     return f"data:image/{img_file.type.split('/')[-1]};base64,{encoded_string}"

# def pil_to_base64(img_pil):
#     buffer = io.BytesIO()
#     img_pil.save(buffer, format="PNG")
#     encoded_string = base64.b64encode(buffer.getvalue()).decode()
#     return f"data:image/png;base64,{encoded_string}"

# def create_radar(mood_vec):
#     categories = ['Valence', 'Energy', 'Dance', 'Tempo', 'Acoustic']
#     values = mood_vec + [mood_vec[0]]
#     cats = categories + [categories[0]]
#     fig = go.Figure(go.Scatterpolar(r=values, theta=cats, fill='toself', line_color='#4ade80', fillcolor='rgba(74, 222, 128, 0.2)'))
#     fig.update_layout(polar=dict(radialaxis=dict(visible=True, range=[0, 1], showticklabels=False, linecolor='#333')), paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', height=300, margin=dict(l=40, r=40, t=20, b=20))
#     return fig

# def create_interactive_image(img_pil, detections):
#     img_width, img_height = img_pil.size
#     img_base64 = pil_to_base64(img_pil)
#     fig = go.Figure()
#     fig.add_layout_image(dict(source=img_base64, xref="x", yref="y", x=0, y=0, sizex=img_width, sizey=img_height, sizing="stretch", layer="below"))

#     shapes = []
#     for det in detections:
#         x1, y1, x2, y2 = det['bbox']
#         label = det['label']
#         conf = det['confidence']
#         shapes.append(dict(type="rect", x0=x1, y0=y1, x1=x2, y1=y2, line=dict(color='rgba(74, 222, 128, 0.5)', width=1), fillcolor='rgba(74, 222, 128, 0.05)'))
#         center_x, center_y = (x1 + x2) / 2, (y1 + y2) / 2
#         fig.add_trace(go.Scatter(x=[center_x], y=[center_y], mode='markers', marker=dict(color='#4ade80', size=8, opacity=0.4, line=dict(width=1, color='white')), hoverinfo='text', hovertext=f"<span style='color:#4ade80; font-weight:bold;'>[ DETECTED OBJECT ]</span><br>TYPE: {label.upper()}<br>CONFIDENCE: {conf:.1%}", showlegend=False))

#     fig.update_xaxes(showgrid=False, zeroline=False, range=[0, img_width], visible=False)
#     fig.update_yaxes(showgrid=False, zeroline=False, range=[img_height, 0], visible=False, scaleanchor="x", scaleratio=1)
#     fig.update_layout(margin=dict(l=0, r=0, t=0, b=0), plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)', hovermode='closest', dragmode=False, shapes=shapes)
#     return fig

# # --- MAIN UI ---
# st.title("PixelPulse 🎵")
# st.caption("Computer Vision • Interactive Detection • Audio Intelligence")

# col_left, col_right = st.columns([1, 1.4], gap="large")

# with col_left:
#     st.markdown("### 📤 Input Visual")
#     uploaded_file = st.file_uploader("Upload Image", type=["jpg", "png", "jpeg"])
    
#     if uploaded_file:
#         ph_img = st.empty()
#         ph_status = st.empty()
#         pil_image = Image.open(uploaded_file).convert("RGB")
#         ph_img.image(pil_image, caption="Original Media", use_column_width=True)
        
#         if st.button("Initiate Neural Scan", type="primary", use_container_width=True):
#             img_b64 = img_to_base64_str(uploaded_file)
#             ph_img.markdown(f'<div class="scan-container" style="max-width: none;"><img src="{img_b64}"><div class="scan-overlay"></div></div>', unsafe_allow_html=True)
            
#             steps = ["📡 Connecting to Neural Net...", "👁️ Processing Visual Cortex (YOLOv8)...", "🎨 Extracting Dominant Color Palette...", "🎵 Synthesizing Audio Vectors..."]
#             for s in steps:
#                 ph_status.markdown(f"**_{s}_**")
#                 time.sleep(0.6)
            
#             try:
#                 files = {"file": (uploaded_file.name, uploaded_file.getvalue(), uploaded_file.type)}
#                 response = requests.post(API_URL, files=files)
                
#                 if response.status_code == 200:
#                     data = st.session_state['data'] = response.json()
#                     ph_status.empty()
#                     detections = data.get('detections', [])
#                     if detections:
#                         fig = create_interactive_image(pil_image, detections)
#                         ph_img.plotly_chart(fig, use_container_width=True, config={'displayModeBar': False})
#                         st.caption("💡 HUD Active: Hover over detected regions for analysis data.")
#                     else:
#                         ph_img.image(pil_image, caption="Analysis Complete", use_column_width=True)
#                 else:
#                     st.error("Server Error.")
#                     ph_img.image(pil_image)
#             except Exception as e:
#                 st.error(f"Error: {e}")
#                 ph_img.image(pil_image)

# with col_right:
#     if 'data' in st.session_state:
#         data = st.session_state['data']
#         tags = data.get('tags', ["Unknown"])
#         objects = data.get('detected_objects', [])
#         accuracy = data.get('accuracy', 0)
#         palette = data.get('palette', [])
#         recommendations = data.get('recommendations', [])
        
#         st.markdown("### 👁️ Intelligence Report")
#         st.markdown(f'<span class="accuracy-box">🎯 Confidence: {accuracy}%</span> <span class="accuracy-box">📦 Objects: {len(objects)}</span>', unsafe_allow_html=True)
#         st.write(f"**Scene Context:** {tags[0].title()}")
        
#         if objects:
#             obj_html = "".join([f'<span class="object-pill">{obj}</span>' for obj in objects])
#             st.markdown(obj_html, unsafe_allow_html=True)
            
#         st.write("**Dominant Palette:**")
#         cols_html = "".join([f'<div class="color-circle" style="background-color: {c};"></div>' for c in palette])
#         st.markdown(f'<div>{cols_html}</div>', unsafe_allow_html=True)
        
#         st.markdown("---")
#         st.markdown("#### 🎧 Recommendations")
        
#         # Limit to top 5 songs to keep it clean
#         for song in recommendations[:5]:
#             preview_url = song.get('preview_url')
            
#             # Song Info
#             st.markdown(f"""
#             <div class="song-row">
#                 <div style="font-weight:bold; font-size:1.1rem;">{song['track_name']}</div>
#                 <div style="font-size:0.9rem; color:#aaa;">{song['artists']}</div>
#                 <div style="margin-top:8px;">
#                     <a href="{song['external_url']}" target="_blank" style="text-decoration:none; color:black; background:#4ade80; padding:4px 10px; border-radius:10px; font-weight:bold; font-size:0.7rem;">
#                         OPEN SPOTIFY
#                     </a>
#                 </div>
#             </div>
#             """, unsafe_allow_html=True)

#             # Audio Player (Placed directly below card for cleanliness)
#             if preview_url:
#                 st.audio(preview_url, format="audio/mp3")
#             else:
#                 st.caption("⚠️ No Preview Available")
            
#             st.markdown("---")
#     else:
#         st.info("System Idle. Upload visuals to begin.")

## Latest

# import streamlit as st
# import requests
# import plotly.graph_objects as go
# import time
# import base64
# from PIL import Image
# import io

# # --- CONFIG ---
# st.set_page_config(page_title="PixelPulse | Visual AI", page_icon="🎵", layout="wide")
# API_URL = "http://127.0.0.1:8000/recommend"

# # --- CSS ---
# st.markdown("""
#     <style>
#     @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;500;700&display=swap');
    
#     .stApp {
#         background-color: #050505;
#         background-image: radial-gradient(circle at 50% 0%, #1e1e24 0%, #000000 100%);
#         font-family: 'Outfit', sans-serif;
#         color: white;
#     }
    
#     /* Scanner Effect */
#     .scan-container { position: relative; width: 100%; border-radius: 12px; overflow: hidden; border: 1px solid #4ade8055; box-shadow: 0 0 25px rgba(74, 222, 128, 0.3); }
#     .scan-container img { width: 100%; display: block; }
#     .scan-overlay { 
#         position: absolute; top: 0; left: 0; width: 100%; height: 100%; 
#         background: linear-gradient(to bottom, transparent 0%, rgba(74, 222, 128, 0.1) 45%, rgba(100, 255, 150, 0.9) 50%, rgba(74, 222, 128, 0.1) 55%, transparent 100%); 
#         animation: scan 1.5s cubic-bezier(0.4, 0.0, 0.2, 1) infinite; 
#         z-index: 2; pointer-events: none;
#     }
#     @keyframes scan { 0% { transform: translateY(-100%); } 100% { transform: translateY(100%); } }
    
#     /* UI Elements */
#     .accuracy-box { background: rgba(74, 222, 128, 0.15); border: 1px solid #4ade80; color: #4ade80; padding: 6px 12px; border-radius: 8px; font-weight: bold; display: inline-block; margin-right: 10px; font-size: 0.9rem; }
#     .object-pill { background: rgba(255, 255, 255, 0.1); border: 1px solid #4ade8088; color: #dfdfdf; padding: 4px 10px; border-radius: 20px; font-size: 0.8rem; display: inline-block; margin: 3px; }
#     .color-circle { width: 40px; height: 40px; border-radius: 50%; display: inline-block; margin-right: 10px; border: 2px solid rgba(255,255,255,0.2); box-shadow: 0 0 5px rgba(0,0,0,0.5); }
    
#     /* Song Row */
#     .song-row { background: rgba(255,255,255,0.03); border-radius: 12px; padding: 15px; margin-bottom: 12px; border-left: 4px solid #4ade80; transition: transform 0.2s; }
#     .song-row:hover { background: rgba(255,255,255,0.08); transform: translateX(5px); }
#     .stAudio { width: 100%; margin-top: 10px; }
    
#     .modebar { display: none !important; }
#     header, footer {visibility: hidden;}
#     </style>
# """, unsafe_allow_html=True)

# # --- HELPER FUNCTIONS ---
# def img_to_base64_str(img_file):
#     encoded_string = base64.b64encode(img_file.getvalue()).decode()
#     return f"data:image/{img_file.type.split('/')[-1]};base64,{encoded_string}"

# def pil_to_base64(img_pil):
#     buffer = io.BytesIO()
#     img_pil.save(buffer, format="PNG")
#     encoded_string = base64.b64encode(buffer.getvalue()).decode()
#     return f"data:image/png;base64,{encoded_string}"

# def create_radar(mood_vec):
#     categories = ['Valence', 'Energy', 'Dance', 'Tempo', 'Acoustic']
#     values = mood_vec + [mood_vec[0]]
#     cats = categories + [categories[0]]
#     fig = go.Figure(go.Scatterpolar(r=values, theta=cats, fill='toself', line_color='#4ade80', fillcolor='rgba(74, 222, 128, 0.2)'))
#     fig.update_layout(
#         polar=dict(radialaxis=dict(visible=True, range=[0, 1], showticklabels=False, linecolor='#333'), angularaxis=dict(tickfont=dict(color='white'))),
#         paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', 
#         height=350, margin=dict(l=50, r=50, t=30, b=30) # Adjusted margins to prevent cutoff
#     )
#     return fig

# def create_interactive_image(img_pil, detections):
#     img_width, img_height = img_pil.size
#     img_base64 = pil_to_base64(img_pil)
#     fig = go.Figure()
#     fig.add_layout_image(dict(source=img_base64, xref="x", yref="y", x=0, y=0, sizex=img_width, sizey=img_height, sizing="stretch", layer="below"))
#     shapes = []
#     for det in detections:
#         x1, y1, x2, y2 = det['bbox']
#         label = det['label']
#         conf = det['confidence']
#         shapes.append(dict(type="rect", x0=x1, y0=y1, x1=x2, y1=y2, line=dict(color='rgba(74, 222, 128, 0.5)', width=1), fillcolor='rgba(74, 222, 128, 0.05)'))
#         center_x, center_y = (x1 + x2) / 2, (y1 + y2) / 2
#         fig.add_trace(go.Scatter(x=[center_x], y=[center_y], mode='markers', marker=dict(color='#4ade80', size=8, opacity=0.4, line=dict(width=1, color='white')), hoverinfo='text', hovertext=f"<span style='color:#4ade80; font-weight:bold;'>[ DETECTED OBJECT ]</span><br>TYPE: {label.upper()}<br>CONFIDENCE: {conf:.1%}", showlegend=False))
#     fig.update_xaxes(showgrid=False, zeroline=False, range=[0, img_width], visible=False)
#     fig.update_yaxes(showgrid=False, zeroline=False, range=[img_height, 0], visible=False, scaleanchor="x", scaleratio=1)
#     fig.update_layout(margin=dict(l=0, r=0, t=0, b=0), plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)', hovermode='closest', dragmode=False, shapes=shapes)
#     return fig

# # --- MAIN UI ---
# st.title("PixelPulse 🎵")
# st.caption("Computer Vision • Interactive Detection • Audio Intelligence")

# col_left, col_right = st.columns([1, 1.4], gap="large")

# with col_left:
#     st.markdown("### 📤 Input Visual")
#     uploaded_file = st.file_uploader("Upload Image", type=["jpg", "png", "jpeg"])
    
#     if uploaded_file:
#         ph_img = st.empty()
#         ph_status = st.empty()
#         pil_image = Image.open(uploaded_file).convert("RGB")
#         ph_img.image(pil_image, caption="Original Media", use_column_width=True)
        
#         if st.button("Initiate Neural Scan", type="primary", use_container_width=True):
#             img_b64 = img_to_base64_str(uploaded_file)
#             ph_img.markdown(f'<div class="scan-container" style="max-width: none;"><img src="{img_b64}"><div class="scan-overlay"></div></div>', unsafe_allow_html=True)
            
#             steps = ["📡 Connecting to Neural Net...", "👁️ Processing Visual Cortex...", "🎨 Extracting Dominant Color Palette...", "🎵 Synthesizing Audio Vectors..."]
#             for s in steps:
#                 ph_status.markdown(f"**_{s}_**")
#                 time.sleep(0.6)
            
#             try:
#                 files = {"file": (uploaded_file.name, uploaded_file.getvalue(), uploaded_file.type)}
#                 response = requests.post(API_URL, files=files)
                
#                 if response.status_code == 200:
#                     data = st.session_state['data'] = response.json()
#                     ph_status.empty()
#                     detections = data.get('detections', [])
#                     if detections:
#                         fig = create_interactive_image(pil_image, detections)
#                         ph_img.plotly_chart(fig, use_container_width=True, config={'displayModeBar': False})
#                         st.caption("💡 HUD Active: Hover over detected regions for analysis data.")
#                     else:
#                         ph_img.image(pil_image, caption="Analysis Complete", use_column_width=True)
#                 else:
#                     st.error("Server Error.")
#                     ph_img.image(pil_image)
#             except Exception as e:
#                 st.error(f"Error: {e}")
#                 ph_img.image(pil_image)

# with col_right:
#     if 'data' in st.session_state:
#         data = st.session_state['data']
#         tags = data.get('tags', ["Unknown"])
#         objects = data.get('detected_objects', [])
#         accuracy = data.get('accuracy', 0)
#         palette = data.get('palette', [])
#         recommendations = data.get('recommendations', [])
        
#         # 1. SCENE CONTEXT
#         st.markdown("### 👁️ Intelligence Report")
#         st.markdown(f'<span class="accuracy-box">🎯 Confidence: {accuracy}%</span> <span class="accuracy-box">📦 Objects: {len(objects)}</span>', unsafe_allow_html=True)
#         st.write(f"**Scene Context:** {tags[0].title()}")
        
#         # 2. OBJECTS
#         if objects:
#             st.write("**Detected Entities:**")
#             obj_html = "".join([f'<span class="object-pill">{obj}</span>' for obj in objects])
#             st.markdown(obj_html, unsafe_allow_html=True)
        
#         st.markdown("---")

#         # 3. COLOR PALETTE
#         st.markdown("#### 🎨 Dominant Palette")
#         cols_html = "".join([f'<div class="color-circle" style="background-color: {c};"></div>' for c in palette])
#         st.markdown(f'<div>{cols_html}</div>', unsafe_allow_html=True)
        
#         # 4. AUDIO DNA (Radar Chart)
#         st.markdown("#### 📊 Audio DNA")
#         # Ensure this is called with the mood vector
#         radar_fig = create_radar(data.get('mood_vector', [0.5]*5))
#         st.plotly_chart(radar_fig, use_container_width=True, config={'displayModeBar': False})

#         st.markdown("---")
        
#         # 5. RECOMMENDATIONS
#         st.markdown("#### 🎧 Recommendations")
#         # Limit to top 5 playable songs
#         for song in recommendations[:5]:
#             preview_url = song.get('preview_url')
            
#             st.markdown(f"""
#             <div class="song-row">
#                 <div style="font-weight:bold; font-size:1.1rem;">{song['track_name']}</div>
#                 <div style="font-size:0.9rem; color:#aaa;">{song['artists']}</div>
#                 <div style="margin-top:8px;">
#                     <a href="{song['external_url']}" target="_blank" style="text-decoration:none; color:black; background:#4ade80; padding:4px 10px; border-radius:10px; font-weight:bold; font-size:0.7rem;">
#                         OPEN SPOTIFY
#                     </a>
#                 </div>
#             </div>
#             """, unsafe_allow_html=True)

#             if preview_url:
#                 st.audio(preview_url, format="audio/mp3")
#             else:
#                 st.caption("⚠️ No Preview Available (Regional Restriction)")
            
#             st.markdown("---")
#     else:
#         st.info("System Idle. Upload visuals to begin.")

## Latest with song previews 

# import streamlit as st
# import requests
# import plotly.graph_objects as go
# import time
# import base64
# from PIL import Image
# import io

# # --- CONFIG ---
# st.set_page_config(page_title="PixelPulse | Visual AI", page_icon="🎵", layout="wide")
# API_URL = "http://127.0.0.1:8000/recommend"

# # --- CSS ---
# st.markdown("""
#     <style>
#     @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;500;700&display=swap');
    
#     .stApp {
#         background-color: #050505;
#         background-image: radial-gradient(circle at 50% 0%, #1e1e24 0%, #000000 100%);
#         font-family: 'Outfit', sans-serif;
#         color: white;
#     }
    
#     /* Improved Electric Scanner Effect */
#     .scan-container { position: relative; width: 100%; border-radius: 12px; overflow: hidden; border: 1px solid #4ade8055; box-shadow: 0 0 25px rgba(74, 222, 128, 0.3); }
#     .scan-container img { width: 100%; display: block; }
#     .scan-overlay { 
#         position: absolute; top: 0; left: 0; width: 100%; height: 100%; 
#         background: linear-gradient(to bottom, transparent 0%, rgba(74, 222, 128, 0.1) 45%, rgba(100, 255, 150, 0.9) 50%, rgba(74, 222, 128, 0.1) 55%, transparent 100%); 
#         animation: scan 1.5s cubic-bezier(0.4, 0.0, 0.2, 1) infinite; 
#         z-index: 2; pointer-events: none;
#         box-shadow: 0 0 15px rgba(74, 222, 128, 0.5); 
#     }
#     @keyframes scan { 0% { transform: translateY(-100%); } 100% { transform: translateY(100%); } }
    
#     /* UI Elements */
#     .accuracy-box { background: rgba(74, 222, 128, 0.15); border: 1px solid #4ade80; color: #4ade80; padding: 6px 12px; border-radius: 8px; font-weight: bold; display: inline-block; margin-right: 10px; font-size: 0.9rem; }
#     .object-pill { background: rgba(255, 255, 255, 0.1); border: 1px solid #4ade8088; color: #dfdfdf; padding: 4px 10px; border-radius: 20px; font-size: 0.8rem; display: inline-block; margin: 3px; }
#     .color-circle { width: 40px; height: 40px; border-radius: 50%; display: inline-block; margin-right: 10px; border: 2px solid rgba(255,255,255,0.2); box-shadow: 0 0 5px rgba(0,0,0,0.5); }
    
#     .modebar { display: none !important; }
#     header, footer {visibility: hidden;}
#     </style>
# """, unsafe_allow_html=True)

# # --- HELPER FUNCTIONS ---
# def img_to_base64_str(img_file):
#     encoded_string = base64.b64encode(img_file.getvalue()).decode()
#     return f"data:image/{img_file.type.split('/')[-1]};base64,{encoded_string}"

# def pil_to_base64(img_pil):
#     buffer = io.BytesIO()
#     img_pil.save(buffer, format="PNG")
#     encoded_string = base64.b64encode(buffer.getvalue()).decode()
#     return f"data:image/png;base64,{encoded_string}"

# def create_radar(mood_vec):
#     categories = ['Valence', 'Energy', 'Dance', 'Tempo', 'Acoustic']
#     values = mood_vec + [mood_vec[0]]
#     cats = categories + [categories[0]]
#     fig = go.Figure(go.Scatterpolar(r=values, theta=cats, fill='toself', line_color='#4ade80', fillcolor='rgba(74, 222, 128, 0.2)'))
#     fig.update_layout(
#         polar=dict(radialaxis=dict(visible=True, range=[0, 1], showticklabels=False, linecolor='#333'), angularaxis=dict(tickfont=dict(color='white'))),
#         paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', 
#         height=350, margin=dict(l=50, r=50, t=30, b=30)
#     )
#     return fig

# def create_interactive_image(img_pil, detections):
#     img_width, img_height = img_pil.size
#     img_base64 = pil_to_base64(img_pil)
#     fig = go.Figure()
#     fig.add_layout_image(dict(source=img_base64, xref="x", yref="y", x=0, y=0, sizex=img_width, sizey=img_height, sizing="stretch", layer="below"))
#     shapes = []
#     for det in detections:
#         x1, y1, x2, y2 = det['bbox']
#         label = det['label']
#         conf = det['confidence']
#         shapes.append(dict(type="rect", x0=x1, y0=y1, x1=x2, y1=y2, line=dict(color='rgba(74, 222, 128, 0.5)', width=1), fillcolor='rgba(74, 222, 128, 0.05)'))
#         center_x, center_y = (x1 + x2) / 2, (y1 + y2) / 2
#         fig.add_trace(go.Scatter(x=[center_x], y=[center_y], mode='markers', marker=dict(color='#4ade80', size=8, opacity=0.4, line=dict(width=1, color='white')), hoverinfo='text', hovertext=f"<span style='color:#4ade80; font-weight:bold;'>[ DETECTED OBJECT ]</span><br>TYPE: {label.upper()}<br>CONFIDENCE: {conf:.1%}", showlegend=False))
#     fig.update_xaxes(showgrid=False, zeroline=False, range=[0, img_width], visible=False)
#     fig.update_yaxes(showgrid=False, zeroline=False, range=[img_height, 0], visible=False, scaleanchor="x", scaleratio=1)
#     fig.update_layout(margin=dict(l=0, r=0, t=0, b=0), plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)', hovermode='closest', dragmode=False, shapes=shapes)
#     return fig

# # --- MAIN UI ---
# st.title("PixelPulse 🎵")
# st.caption("Computer Vision • Interactive Detection • Audio Intelligence")

# col_left, col_right = st.columns([1, 1.4], gap="large")

# with col_left:
#     st.markdown("### 📤 Input Visual")
#     uploaded_file = st.file_uploader("Upload Image", type=["jpg", "png", "jpeg"])
    
#     if uploaded_file:
#         ph_img = st.empty()
#         ph_status = st.empty()
#         pil_image = Image.open(uploaded_file).convert("RGB")
#         ph_img.image(pil_image, caption="Original Media", use_column_width=True)
        
#         if st.button("Initiate Neural Scan", type="primary", use_container_width=True):
#             img_b64 = img_to_base64_str(uploaded_file)
#             ph_img.markdown(f'<div class="scan-container" style="max-width: none;"><img src="{img_b64}"><div class="scan-overlay"></div></div>', unsafe_allow_html=True)
            
#             steps = ["📡 Connecting to Neural Net...", "👁️ Processing Visual Cortex...", "🎨 Extracting Dominant Color Palette...", "🎵 Synthesizing Audio Vectors..."]
#             for s in steps:
#                 ph_status.markdown(f"**_{s}_**")
#                 time.sleep(0.6)
            
#             try:
#                 files = {"file": (uploaded_file.name, uploaded_file.getvalue(), uploaded_file.type)}
#                 response = requests.post(API_URL, files=files)
                
#                 if response.status_code == 200:
#                     data = st.session_state['data'] = response.json()
#                     ph_status.empty()
#                     detections = data.get('detections', [])
#                     if detections:
#                         fig = create_interactive_image(pil_image, detections)
#                         ph_img.plotly_chart(fig, use_container_width=True, config={'displayModeBar': False})
#                         st.caption("💡 HUD Active: Hover over detected regions for analysis data.")
#                     else:
#                         ph_img.image(pil_image, caption="Analysis Complete", use_column_width=True)
#                 else:
#                     st.error("Server Error.")
#                     ph_img.image(pil_image)
#             except Exception as e:
#                 st.error(f"Error: {e}")
#                 ph_img.image(pil_image)

# with col_right:
#     if 'data' in st.session_state:
#         data = st.session_state['data']
#         tags = data.get('tags', ["Unknown"])
#         objects = data.get('detected_objects', [])
#         accuracy = data.get('accuracy', 0)
#         palette = data.get('palette', [])
#         recommendations = data.get('recommendations', [])
        
#         # 1. SCENE CONTEXT
#         st.markdown("### 👁️ Intelligence Report")
#         st.markdown(f'<span class="accuracy-box">🎯 Confidence: {accuracy}%</span> <span class="accuracy-box">📦 Objects: {len(objects)}</span>', unsafe_allow_html=True)
#         st.write(f"**Scene Context:** {tags[0].title()}")
        
#         # 2. OBJECTS
#         if objects:
#             st.write("**Detected Entities:**")
#             obj_html = "".join([f'<span class="object-pill">{obj}</span>' for obj in objects])
#             st.markdown(obj_html, unsafe_allow_html=True)
        
#         st.markdown("---")

#         # 3. COLOR PALETTE
#         st.markdown("#### 🎨 Dominant Palette")
#         cols_html = "".join([f'<div class="color-circle" style="background-color: {c};"></div>' for c in palette])
#         st.markdown(f'<div>{cols_html}</div>', unsafe_allow_html=True)
        
#         # 4. AUDIO DNA
#         st.markdown("#### 📊 Audio DNA")
#         radar_fig = create_radar(data.get('mood_vector', [0.5]*5))
#         st.plotly_chart(radar_fig, use_container_width=True, config={'displayModeBar': False})

#         st.markdown("---")
        
#         # 5. RECOMMENDATIONS (Official Spotify Embed)
#         st.markdown("#### 🎧 Recommendations")
        
#         for song in recommendations[:6]:
#             track_id = song.get('id')
#             if track_id:
#                 # This iframe guarantees a player appears, regardless of 'preview_url'
#                 embed_url = f"https://open.spotify.com/embed/track/{track_id}?utm_source=generator"
#                 st.markdown(f"""
#                 <iframe style="border-radius:12px; margin-bottom: 10px;" 
#                 src="{embed_url}" 
#                 width="100%" height="80" frameBorder="0" 
#                 allowfullscreen="" 
#                 allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture" 
#                 loading="lazy"></iframe>
#                 """, unsafe_allow_html=True)
#             else:
#                 st.warning("Track ID missing.")

#     else:
#         st.info("System Idle. Upload visuals to begin.")


## Latest with working hover HUD and preview song with layout chnaged

# import streamlit as st
# import requests
# import plotly.graph_objects as go
# import time
# import base64
# from PIL import Image
# import io

# # --- CONFIG ---
# st.set_page_config(page_title="PixelPulse | Visual AI", page_icon="🎵", layout="wide")
# API_URL = "http://127.0.0.1:8000/recommend"

# # --- CSS ---
# st.markdown("""
#     <style>
#     @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;500;700&display=swap');
    
#     .stApp {
#         background-color: #050505;
#         background-image: radial-gradient(circle at 50% 0%, #1e1e24 0%, #000000 100%);
#         font-family: 'Outfit', sans-serif;
#         color: white;
#     }
    
#     /* Scanner Effect */
#     .scan-container { position: relative; width: 100%; border-radius: 12px; overflow: hidden; border: 1px solid #4ade8055; box-shadow: 0 0 25px rgba(74, 222, 128, 0.3); }
#     .scan-container img { width: 100%; display: block; }
#     .scan-overlay { 
#         position: absolute; top: 0; left: 0; width: 100%; height: 100%; 
#         background: linear-gradient(to bottom, transparent 0%, rgba(74, 222, 128, 0.1) 45%, rgba(100, 255, 150, 0.9) 50%, rgba(74, 222, 128, 0.1) 55%, transparent 100%); 
#         animation: scan 1.5s cubic-bezier(0.4, 0.0, 0.2, 1) infinite; 
#         z-index: 2; pointer-events: none;
#     }
#     @keyframes scan { 0% { transform: translateY(-100%); } 100% { transform: translateY(100%); } }
    
#     /* UI Elements */
#     .accuracy-box { background: rgba(74, 222, 128, 0.15); border: 1px solid #4ade80; color: #4ade80; padding: 6px 12px; border-radius: 8px; font-weight: bold; display: inline-block; margin-right: 10px; font-size: 0.9rem; }
#     .object-pill { background: rgba(255, 255, 255, 0.1); border: 1px solid #4ade8088; color: #dfdfdf; padding: 4px 10px; border-radius: 20px; font-size: 0.8rem; display: inline-block; margin: 3px; }
#     .color-circle { width: 40px; height: 40px; border-radius: 50%; display: inline-block; margin-right: 10px; border: 2px solid rgba(255,255,255,0.2); box-shadow: 0 0 5px rgba(0,0,0,0.5); }
    
#     .modebar { display: none !important; }
#     header, footer {visibility: hidden;}
#     </style>
# """, unsafe_allow_html=True)

# # --- HELPER FUNCTIONS ---
# def img_to_base64_str(img_file):
#     encoded_string = base64.b64encode(img_file.getvalue()).decode()
#     return f"data:image/{img_file.type.split('/')[-1]};base64,{encoded_string}"

# def pil_to_base64(img_pil):
#     buffer = io.BytesIO()
#     img_pil.save(buffer, format="PNG")
#     encoded_string = base64.b64encode(buffer.getvalue()).decode()
#     return f"data:image/png;base64,{encoded_string}"

# def create_radar(mood_vec):
#     categories = ['Valence', 'Energy', 'Dance', 'Tempo', 'Acoustic']
#     values = mood_vec + [mood_vec[0]]
#     cats = categories + [categories[0]]
#     fig = go.Figure(go.Scatterpolar(r=values, theta=cats, fill='toself', line_color='#4ade80', fillcolor='rgba(74, 222, 128, 0.2)'))
#     fig.update_layout(
#         polar=dict(radialaxis=dict(visible=True, range=[0, 1], showticklabels=False, linecolor='#333'), angularaxis=dict(tickfont=dict(color='white'))),
#         paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', 
#         height=350, margin=dict(l=40, r=40, t=20, b=20)
#     )
#     return fig

# def create_interactive_image(img_pil, detections):
#     img_width, img_height = img_pil.size
#     img_base64 = pil_to_base64(img_pil)
#     fig = go.Figure()
#     fig.add_layout_image(dict(source=img_base64, xref="x", yref="y", x=0, y=0, sizex=img_width, sizey=img_height, sizing="stretch", layer="below"))
#     shapes = []
#     for det in detections:
#         x1, y1, x2, y2 = det['bbox']
#         label = det['label']
#         conf = det['confidence']
#         shapes.append(dict(type="rect", x0=x1, y0=y1, x1=x2, y1=y2, line=dict(color='rgba(74, 222, 128, 0.5)', width=1), fillcolor='rgba(74, 222, 128, 0.05)'))
#         center_x, center_y = (x1 + x2) / 2, (y1 + y2) / 2
#         fig.add_trace(go.Scatter(x=[center_x], y=[center_y], mode='markers', marker=dict(color='#4ade80', size=8, opacity=0.4, line=dict(width=1, color='white')), hoverinfo='text', hovertext=f"<span style='color:#4ade80; font-weight:bold;'>[ DETECTED OBJECT ]</span><br>TYPE: {label.upper()}<br>CONFIDENCE: {conf:.1%}", showlegend=False))
#     fig.update_xaxes(showgrid=False, zeroline=False, range=[0, img_width], visible=False)
#     fig.update_yaxes(showgrid=False, zeroline=False, range=[img_height, 0], visible=False, scaleanchor="x", scaleratio=1)
#     fig.update_layout(margin=dict(l=0, r=0, t=0, b=0), plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)', hovermode='closest', dragmode=False, shapes=shapes)
#     return fig

# # --- MAIN UI ---
# st.title("PixelPulse 🎵")
# st.caption("Computer Vision • Interactive Detection • Audio Intelligence")

# col_left, col_right = st.columns([1, 1.4], gap="large")

# with col_left:
#     st.markdown("### 📤 Input Visual")
#     uploaded_file = st.file_uploader("Upload Image", type=["jpg", "png", "jpeg"])
    
#     if uploaded_file:
#         ph_img = st.empty()
#         ph_status = st.empty()
#         pil_image = Image.open(uploaded_file).convert("RGB")
#         ph_img.image(pil_image, caption="Original Media", use_column_width=True)
        
#         if st.button("Initiate Neural Scan", type="primary", use_container_width=True):
#             img_b64 = img_to_base64_str(uploaded_file)
#             ph_img.markdown(f'<div class="scan-container" style="max-width: none;"><img src="{img_b64}"><div class="scan-overlay"></div></div>', unsafe_allow_html=True)
            
#             steps = ["📡 Connecting to Neural Net...", "👁️ Processing Visual Cortex...", "🎨 Extracting Dominant Color Palette...", "🎵 Synthesizing Audio Vectors..."]
#             for s in steps:
#                 ph_status.markdown(f"**_{s}_**")
#                 time.sleep(0.6)
            
#             try:
#                 files = {"file": (uploaded_file.name, uploaded_file.getvalue(), uploaded_file.type)}
#                 response = requests.post(API_URL, files=files)
                
#                 if response.status_code == 200:
#                     data = st.session_state['data'] = response.json()
#                     ph_status.empty()
#                     detections = data.get('detections', [])
#                     if detections:
#                         fig = create_interactive_image(pil_image, detections)
#                         ph_img.plotly_chart(fig, use_container_width=True, config={'displayModeBar': False})
#                         st.caption("💡 HUD Active: Hover over detected regions for analysis data.")
#                     else:
#                         ph_img.image(pil_image, caption="Analysis Complete", use_column_width=True)
#                 else:
#                     st.error("Server Error.")
#                     ph_img.image(pil_image)
#             except Exception as e:
#                 st.error(f"Error: {e}")
#                 ph_img.image(pil_image)

# with col_right:
#     if 'data' in st.session_state:
#         data = st.session_state['data']
#         tags = data.get('tags', ["Unknown"])
#         objects = data.get('detected_objects', [])
#         accuracy = data.get('accuracy', 0)
#         palette = data.get('palette', [])
#         recommendations = data.get('recommendations', [])
        
#         # --- TOP SECTION: INFO & PALETTE ---
#         st.markdown("### 👁️ Intelligence Report")
#         st.markdown(f'<span class="accuracy-box">🎯 Confidence: {accuracy}%</span> <span class="accuracy-box">📦 Objects: {len(objects)}</span>', unsafe_allow_html=True)
#         st.write(f"**Scene Context:** {tags[0].title()}")
        
#         if objects:
#             obj_html = "".join([f'<span class="object-pill">{obj}</span>' for obj in objects])
#             st.markdown(obj_html, unsafe_allow_html=True)
        
#         st.write("**Dominant Palette:**")
#         cols_html = "".join([f'<div class="color-circle" style="background-color: {c};"></div>' for c in palette])
#         st.markdown(f'<div>{cols_html}</div>', unsafe_allow_html=True)
        
#         st.markdown("---")
        
#         # --- SPLIT LAYOUT: CHART (Left) | PLAYLIST (Right) ---
#         c1, c2 = st.columns([1, 1])
        
#         with c1:
#             st.markdown("#### 📊 Audio DNA")
#             radar_fig = create_radar(data.get('mood_vector', [0.5]*5))
#             st.plotly_chart(radar_fig, use_container_width=True, config={'displayModeBar': False})

#         with c2:
#             st.markdown("#### 🎧 Recommendations")
#             # Scrollable container concept or just standard list
#             for song in recommendations[:4]: # Top 4 to match height of chart
#                 track_id = song.get('id')
#                 if track_id:
#                     embed_url = f"https://open.spotify.com/embed/track/{track_id}?utm_source=generator"
#                     st.markdown(f"""
#                     <iframe style="border-radius:12px; margin-bottom: 10px;" 
#                     src="{embed_url}" 
#                     width="100%" height="80" frameBorder="0" 
#                     allowfullscreen="" 
#                     allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture" 
#                     loading="lazy"></iframe>
#                     """, unsafe_allow_html=True)
#                 else:
#                     st.caption("⚠️ Track unavailable")

#     else:
#         st.info("System Idle. Upload visuals to begin.")



## working code with all latest features but not accurate
# import streamlit as st
# import requests
# import plotly.graph_objects as go
# import time
# import base64
# from PIL import Image
# import io

# # --- CONFIG ---
# st.set_page_config(page_title="PixelPulse | Visual AI", page_icon="🎵", layout="wide")
# API_URL = "http://127.0.0.1:8000/recommend"

# # --- CSS ---
# st.markdown("""
#     <style>
#     @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;500;700&display=swap');
    
#     .stApp {
#         background-color: #050505;
#         background-image: radial-gradient(circle at 50% 0%, #1e1e24 0%, #000000 100%);
#         font-family: 'Outfit', sans-serif;
#         color: white;
#     }
    
#     /* DJ Message Box */
#     .dj-box {
#         background: rgba(255, 255, 255, 0.05);
#         border-left: 5px solid #a855f7; /* Purple accent */
#         padding: 15px;
#         border-radius: 8px;
#         margin-bottom: 20px;
#         font-style: italic;
#         color: #e9d5ff;
#         font-size: 1.05rem;
#     }

#     .scan-container { position: relative; width: 100%; border-radius: 12px; overflow: hidden; border: 1px solid #4ade8055; box-shadow: 0 0 25px rgba(74, 222, 128, 0.3); }
#     .scan-container img { width: 100%; display: block; }
#     .scan-overlay { 
#         position: absolute; top: 0; left: 0; width: 100%; height: 100%; 
#         background: linear-gradient(to bottom, transparent 0%, rgba(74, 222, 128, 0.1) 45%, rgba(100, 255, 150, 0.9) 50%, rgba(74, 222, 128, 0.1) 55%, transparent 100%); 
#         animation: scan 1.5s cubic-bezier(0.4, 0.0, 0.2, 1) infinite; 
#         z-index: 2; pointer-events: none;
#     }
#     @keyframes scan { 0% { transform: translateY(-100%); } 100% { transform: translateY(100%); } }
    
#     .accuracy-box { background: rgba(74, 222, 128, 0.15); border: 1px solid #4ade80; color: #4ade80; padding: 6px 12px; border-radius: 8px; font-weight: bold; display: inline-block; margin-right: 10px; font-size: 0.9rem; }
#     .object-pill { background: rgba(255, 255, 255, 0.1); border: 1px solid #4ade8088; color: #dfdfdf; padding: 4px 10px; border-radius: 20px; font-size: 0.8rem; display: inline-block; margin: 3px; }
#     .color-circle { width: 40px; height: 40px; border-radius: 50%; display: inline-block; margin-right: 10px; border: 2px solid rgba(255,255,255,0.2); box-shadow: 0 0 5px rgba(0,0,0,0.5); }
    
#     .modebar { display: none !important; }
#     header, footer {visibility: hidden;}
#     </style>
# """, unsafe_allow_html=True)

# # --- HELPER FUNCTIONS ---
# def img_to_base64_str(img_file):
#     encoded_string = base64.b64encode(img_file.getvalue()).decode()
#     return f"data:image/{img_file.type.split('/')[-1]};base64,{encoded_string}"

# def pil_to_base64(img_pil):
#     buffer = io.BytesIO()
#     img_pil.save(buffer, format="PNG")
#     encoded_string = base64.b64encode(buffer.getvalue()).decode()
#     return f"data:image/png;base64,{encoded_string}"

# def create_radar(mood_vec):
#     categories = ['Valence', 'Energy', 'Dance', 'Tempo', 'Acoustic']
#     values = mood_vec + [mood_vec[0]]
#     cats = categories + [categories[0]]
#     fig = go.Figure(go.Scatterpolar(r=values, theta=cats, fill='toself', line_color='#4ade80', fillcolor='rgba(74, 222, 128, 0.2)'))
#     fig.update_layout(
#         polar=dict(radialaxis=dict(visible=True, range=[0, 1], showticklabels=False, linecolor='#333'), angularaxis=dict(tickfont=dict(color='white'))),
#         paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', 
#         height=350, margin=dict(l=50, r=50, t=30, b=30)
#     )
#     return fig

# def create_interactive_image(img_pil, detections):
#     img_width, img_height = img_pil.size
#     img_base64 = pil_to_base64(img_pil)
#     fig = go.Figure()
#     fig.add_layout_image(dict(source=img_base64, xref="x", yref="y", x=0, y=0, sizex=img_width, sizey=img_height, sizing="stretch", layer="below"))
#     shapes = []
#     for det in detections:
#         x1, y1, x2, y2 = det['bbox']
#         label = det['label']
#         conf = det['confidence']
#         shapes.append(dict(type="rect", x0=x1, y0=y1, x1=x2, y1=y2, line=dict(color='rgba(74, 222, 128, 0.5)', width=1), fillcolor='rgba(74, 222, 128, 0.05)'))
#         center_x, center_y = (x1 + x2) / 2, (y1 + y2) / 2
#         fig.add_trace(go.Scatter(x=[center_x], y=[center_y], mode='markers', marker=dict(color='#4ade80', size=8, opacity=0.4, line=dict(width=1, color='white')), hoverinfo='text', hovertext=f"<span style='color:#4ade80; font-weight:bold;'>[ DETECTED OBJECT ]</span><br>TYPE: {label.upper()}<br>CONFIDENCE: {conf:.1%}", showlegend=False))
#     fig.update_xaxes(showgrid=False, zeroline=False, range=[0, img_width], visible=False)
#     fig.update_yaxes(showgrid=False, zeroline=False, range=[img_height, 0], visible=False, scaleanchor="x", scaleratio=1)
#     fig.update_layout(margin=dict(l=0, r=0, t=0, b=0), plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)', hovermode='closest', dragmode=False, shapes=shapes)
#     return fig

# def typewriter_effect(text, placeholder):
#     """Simulates a typewriter printing text."""
#     displayed_text = ""
#     for char in text:
#         displayed_text += char
#         placeholder.markdown(f'<div class="dj-box">{displayed_text}█</div>', unsafe_allow_html=True)
#         time.sleep(0.02) # Typing speed
#     placeholder.markdown(f'<div class="dj-box">{displayed_text}</div>', unsafe_allow_html=True)

# # --- MAIN UI ---
# st.title("PixelPulse 🎵")
# st.caption("Computer Vision • Interactive Detection • Audio Intelligence")

# col_left, col_right = st.columns([1, 1.4], gap="large")

# with col_left:
#     st.markdown("### 📤 Input Visual")
#     uploaded_file = st.file_uploader("Upload Image", type=["jpg", "png", "jpeg"])
    
#     if uploaded_file:
#         ph_img = st.empty()
#         ph_status = st.empty()
#         pil_image = Image.open(uploaded_file).convert("RGB")
#         ph_img.image(pil_image, caption="Original Media", use_column_width=True)
        
#         if st.button("Initiate Neural Scan", type="primary", use_container_width=True):
#             img_b64 = img_to_base64_str(uploaded_file)
#             ph_img.markdown(f'<div class="scan-container" style="max-width: none;"><img src="{img_b64}"><div class="scan-overlay"></div></div>', unsafe_allow_html=True)
            
#             steps = ["📡 Connecting to Neural Net...", "👁️ Processing Visual Cortex...", "🎨 Extracting Dominant Color Palette...", "🎵 Synthesizing Audio Vectors..."]
#             for s in steps:
#                 ph_status.markdown(f"**_{s}_**")
#                 time.sleep(0.6)
            
#             try:
#                 files = {"file": (uploaded_file.name, uploaded_file.getvalue(), uploaded_file.type)}
#                 response = requests.post(API_URL, files=files)
                
#                 if response.status_code == 200:
#                     data = st.session_state['data'] = response.json()
#                     ph_status.empty()
#                     detections = data.get('detections', [])
#                     if detections:
#                         fig = create_interactive_image(pil_image, detections)
#                         ph_img.plotly_chart(fig, use_container_width=True, config={'displayModeBar': False})
#                         st.caption("💡 HUD Active: Hover over detected regions for analysis data.")
#                     else:
#                         ph_img.image(pil_image, caption="Analysis Complete", use_column_width=True)
#                 else:
#                     st.error("Server Error.")
#                     ph_img.image(pil_image)
#             except Exception as e:
#                 st.error(f"Error: {e}")
#                 ph_img.image(pil_image)

# with col_right:
#     if 'data' in st.session_state:
#         data = st.session_state['data']
#         tags = data.get('tags', ["Unknown"])
#         objects = data.get('detected_objects', [])
#         accuracy = data.get('accuracy', 0)
#         palette = data.get('palette', [])
#         recommendations = data.get('recommendations', [])
#         dj_summary = data.get('dj_summary', "Analysis complete.")
        
#         # 1. DJ NARRATIVE (TYPEWRITER EFFECT)
#         st.markdown("### 👁️ Intelligence Report")
#         dj_placeholder = st.empty()
#         # Only type if it's the first time seeing this data to avoid re-typing on redraws
#         if 'last_dj_msg' not in st.session_state or st.session_state['last_dj_msg'] != dj_summary:
#             typewriter_effect(dj_summary, dj_placeholder)
#             st.session_state['last_dj_msg'] = dj_summary
#         else:
#              dj_placeholder.markdown(f'<div class="dj-box">{dj_summary}</div>', unsafe_allow_html=True)

#         st.markdown(f'<span class="accuracy-box">🎯 Confidence: {accuracy}%</span> <span class="accuracy-box">📦 Objects: {len(objects)}</span>', unsafe_allow_html=True)
#         st.write(f"**Scene Context:** {tags[0].title()}")
        
#         if objects:
#             obj_html = "".join([f'<span class="object-pill">{obj}</span>' for obj in objects])
#             st.markdown(obj_html, unsafe_allow_html=True)
        
#         st.write("**Dominant Palette:**")
#         cols_html = "".join([f'<div class="color-circle" style="background-color: {c};"></div>' for c in palette])
#         st.markdown(f'<div>{cols_html}</div>', unsafe_allow_html=True)
        
#         st.markdown("---")
        
#         c1, c2 = st.columns([1, 1])
        
#         with c1:
#             st.markdown("#### 📊 Audio DNA")
#             radar_fig = create_radar(data.get('mood_vector', [0.5]*5))
#             st.plotly_chart(radar_fig, use_container_width=True, config={'displayModeBar': False})

#         with c2:
#             st.markdown("#### 🎧 Recommendations")
#             for song in recommendations[:4]: 
#                 track_id = song.get('id')
#                 if track_id:
#                     embed_url = f"https://open.spotify.com/embed/track/{track_id}?utm_source=generator"
#                     st.markdown(f"""
#                     <iframe style="border-radius:12px; margin-bottom: 10px;" 
#                     src="{embed_url}" 
#                     width="100%" height="80" frameBorder="0" 
#                     allowfullscreen="" 
#                     allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture" 
#                     loading="lazy"></iframe>
#                     """, unsafe_allow_html=True)
#                 else:
#                     st.caption("⚠️ Track unavailable")

#     else:
#         st.info("System Idle. Upload visuals to begin.")


## Basic latest code without typewriter and hover HUD
# import streamlit as st
# import requests
# import plotly.graph_objects as go
# import time
# import base64
# from PIL import Image
# import io

# # --- CONFIG ---
# st.set_page_config(page_title="PixelPulse | Visual AI", page_icon="🎵", layout="wide")
# API_URL = "http://127.0.0.1:8000/recommend"

# # --- CSS ---
# st.markdown("""
#     <style>
#     @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;500;700&display=swap');
    
#     .stApp {
#         background-color: #050505;
#         background-image: radial-gradient(circle at 50% 0%, #1e1e24 0%, #000000 100%);
#         font-family: 'Outfit', sans-serif;
#         color: white;
#     }
    
#     /* DJ Message Box */
#     .dj-box {
#         background: rgba(255, 255, 255, 0.05);
#         border-left: 5px solid #a855f7;
#         padding: 15px;
#         border-radius: 8px;
#         margin-bottom: 20px;
#         font-style: italic;
#         color: #e9d5ff;
#         font-size: 1.05rem;
#         line-height: 1.5;
#     }

#     /* Scanner Effect */
#     .scan-container { position: relative; width: 100%; border-radius: 12px; overflow: hidden; border: 1px solid #4ade8055; box-shadow: 0 0 25px rgba(74, 222, 128, 0.3); }
#     .scan-container img { width: 100%; display: block; }
#     .scan-overlay { 
#         position: absolute; top: 0; left: 0; width: 100%; height: 100%; 
#         background: linear-gradient(to bottom, transparent 0%, rgba(74, 222, 128, 0.1) 45%, rgba(100, 255, 150, 0.9) 50%, rgba(74, 222, 128, 0.1) 55%, transparent 100%); 
#         animation: scan 1.5s cubic-bezier(0.4, 0.0, 0.2, 1) infinite; 
#         z-index: 2; pointer-events: none;
#     }
#     @keyframes scan { 0% { transform: translateY(-100%); } 100% { transform: translateY(100%); } }
    
#     /* UI Elements */
#     .accuracy-box { background: rgba(74, 222, 128, 0.15); border: 1px solid #4ade80; color: #4ade80; padding: 6px 12px; border-radius: 8px; font-weight: bold; display: inline-block; margin-right: 10px; font-size: 0.9rem; }
#     .object-pill { background: rgba(255, 255, 255, 0.1); border: 1px solid #4ade8088; color: #dfdfdf; padding: 4px 10px; border-radius: 20px; font-size: 0.8rem; display: inline-block; margin: 3px; }
#     .color-circle { width: 40px; height: 40px; border-radius: 50%; display: inline-block; margin-right: 10px; border: 2px solid rgba(255,255,255,0.2); box-shadow: 0 0 5px rgba(0,0,0,0.5); }
    
#     .modebar { display: none !important; }
#     header, footer {visibility: hidden;}
#     </style>
# """, unsafe_allow_html=True)

# # --- HELPER FUNCTIONS ---
# def img_to_base64_str(img_file):
#     encoded_string = base64.b64encode(img_file.getvalue()).decode()
#     return f"data:image/{img_file.type.split('/')[-1]};base64,{encoded_string}"

# def pil_to_base64(img_pil):
#     buffer = io.BytesIO()
#     img_pil.save(buffer, format="PNG")
#     encoded_string = base64.b64encode(buffer.getvalue()).decode()
#     return f"data:image/png;base64,{encoded_string}"

# def create_radar(mood_vec):
#     # Updated to match backend 5-point vector
#     categories = ['Valence (Mood)', 'Energy', 'Danceability', 'Tempo', 'Acoustic']
#     values = mood_vec + [mood_vec[0]]
#     cats = categories + [categories[0]]
#     fig = go.Figure(go.Scatterpolar(r=values, theta=cats, fill='toself', line_color='#4ade80', fillcolor='rgba(74, 222, 128, 0.2)'))
#     fig.update_layout(
#         polar=dict(radialaxis=dict(visible=True, range=[0, 1], showticklabels=False, linecolor='#333'), angularaxis=dict(tickfont=dict(color='white', size=11))),
#         paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', 
#         height=350, margin=dict(l=50, r=50, t=30, b=30)
#     )
#     return fig

# def create_interactive_image(img_pil, detections):
#     img_width, img_height = img_pil.size
#     img_base64 = pil_to_base64(img_pil)
#     fig = go.Figure()
#     fig.add_layout_image(dict(source=img_base64, xref="x", yref="y", x=0, y=0, sizex=img_width, sizey=img_height, sizing="stretch", layer="below"))
#     shapes = []
#     for det in detections:
#         x1, y1, x2, y2 = det['bbox']
#         label = det['label']
#         conf = det['confidence']
#         shapes.append(dict(type="rect", x0=x1, y0=y1, x1=x2, y1=y2, line=dict(color='rgba(74, 222, 128, 0.5)', width=1), fillcolor='rgba(74, 222, 128, 0.05)'))
#         center_x, center_y = (x1 + x2) / 2, (y1 + y2) / 2
#         fig.add_trace(go.Scatter(x=[center_x], y=[center_y], mode='markers', marker=dict(color='#4ade80', size=8, opacity=0.4, line=dict(width=1, color='white')), hoverinfo='text', hovertext=f"<span style='color:#4ade80; font-weight:bold;'>[ DETECTED OBJECT ]</span><br>TYPE: {label.upper()}<br>CONFIDENCE: {conf:.1%}", showlegend=False))
#     fig.update_xaxes(showgrid=False, zeroline=False, range=[0, img_width], visible=False)
#     fig.update_yaxes(showgrid=False, zeroline=False, range=[img_height, 0], visible=False, scaleanchor="x", scaleratio=1)
#     fig.update_layout(margin=dict(l=0, r=0, t=0, b=0), plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)', hovermode='closest', dragmode=False, shapes=shapes)
#     return fig

# def typewriter_effect(text, placeholder):
#     displayed_text = ""
#     for char in text:
#         displayed_text += char
#         placeholder.markdown(f'<div class="dj-box">{displayed_text}█</div>', unsafe_allow_html=True)
#         time.sleep(0.015) 
#     placeholder.markdown(f'<div class="dj-box">{displayed_text}</div>', unsafe_allow_html=True)

# # --- MAIN UI ---
# st.title("PixelPulse 🎵")
# st.caption("Computer Vision • Interactive Detection • Audio Intelligence")

# col_left, col_right = st.columns([1, 1.4], gap="large")

# with col_left:
#     st.markdown("### 📤 Input Visual")
#     uploaded_file = st.file_uploader("Upload Image", type=["jpg", "png", "jpeg"])
    
#     if uploaded_file:
#         ph_img = st.empty()
#         ph_status = st.empty()
#         pil_image = Image.open(uploaded_file).convert("RGB")
#         ph_img.image(pil_image, caption="Original Media", use_column_width=True)
        
#         if st.button("Initiate Neural Scan", type="primary", use_container_width=True):
#             img_b64 = img_to_base64_str(uploaded_file)
#             ph_img.markdown(f'<div class="scan-container" style="max-width: none;"><img src="{img_b64}"><div class="scan-overlay"></div></div>', unsafe_allow_html=True)
            
#             steps = ["📡 Establishing Vibe Vector...", "👁️ Analyzing Visual Harmony...", "🎨 Calculating Audio Targets...", "🎵 Curating Spotify Sequence..."]
#             for s in steps:
#                 ph_status.markdown(f"**_{s}_**")
#                 time.sleep(0.5)
            
#             try:
#                 files = {"file": (uploaded_file.name, uploaded_file.getvalue(), uploaded_file.type)}
#                 response = requests.post(API_URL, files=files)
                
#                 if response.status_code == 200:
#                     data = st.session_state['data'] = response.json()
#                     ph_status.empty()
#                     detections = data.get('detections', [])
#                     if detections:
#                         fig = create_interactive_image(pil_image, detections)
#                         ph_img.plotly_chart(fig, use_container_width=True, config={'displayModeBar': False})
#                         st.caption("💡 HUD Active: Hover over detected regions for analysis data.")
#                     else:
#                         ph_img.image(pil_image, caption="Analysis Complete", use_column_width=True)
#                 else:
#                     st.error("Server Error.")
#                     ph_img.image(pil_image)
#             except Exception as e:
#                 st.error(f"Error: {e}")
#                 ph_img.image(pil_image)

# with col_right:
#     if 'data' in st.session_state:
#         data = st.session_state['data']
#         tags = data.get('tags', ["Unknown Vibe"])
#         objects = data.get('detected_objects', [])
#         accuracy = data.get('accuracy', 0)
#         palette = data.get('palette', [])
#         recommendations = data.get('recommendations', [])
#         dj_summary = data.get('dj_summary', "Analysis complete.")
        
#         # 1. DJ NARRATIVE
#         st.markdown("### 👁️ Intelligence Report")
#         dj_placeholder = st.empty()
#         # Prevent re-typing on refresh if data is same
#         if 'last_dj_msg' not in st.session_state or st.session_state['last_dj_msg'] != dj_summary:
#             typewriter_effect(dj_summary, dj_placeholder)
#             st.session_state['last_dj_msg'] = dj_summary
#         else:
#              dj_placeholder.markdown(f'<div class="dj-box">{dj_summary}</div>', unsafe_allow_html=True)

#         st.markdown(f'<span class="accuracy-box">🎯 Vibe Match: {accuracy}%</span> <span class="accuracy-box">📦 Entities: {len(objects)}</span>', unsafe_allow_html=True)
#         st.write(f"**Musical Vibe:** {tags[0]}")
        
#         if objects:
#             obj_html = "".join([f'<span class="object-pill">{obj}</span>' for obj in objects])
#             st.markdown(obj_html, unsafe_allow_html=True)
        
#         st.write("**Dominant Palette:**")
#         cols_html = "".join([f'<div class="color-circle" style="background-color: {c};"></div>' for c in palette])
#         st.markdown(f'<div>{cols_html}</div>', unsafe_allow_html=True)
        
#         st.markdown("---")
        
#         # --- SPLIT LAYOUT ---
#         c1, c2 = st.columns([1, 1])
        
#         with c1:
#             st.markdown("#### 📊 Audio DNA Target")
#             radar_fig = create_radar(data.get('mood_vector', [0.5]*5))
#             st.plotly_chart(radar_fig, use_container_width=True, config={'displayModeBar': False})

#         with c2:
#             st.markdown("#### 🎧 Curated Tracks")
#             for song in recommendations[:4]: 
#                 track_id = song.get('id')
#                 if track_id:
#                     # OFFICIAL EMBED URL - THIS ALWAYS WORKS
#                     embed_url = f"https://open.spotify.com/embed/track/{track_id}?utm_source=generator&theme=0"
#                     st.markdown(f"""
#                     <iframe style="border-radius:12px; margin-bottom: 10px;" 
#                     src="{embed_url}" 
#                     width="100%" height="80" frameBorder="0" 
#                     allowfullscreen="" 
#                     allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture" 
#                     loading="lazy"></iframe>
#                     """, unsafe_allow_html=True)
#                 else:
#                     st.caption("⚠️ Track unavailable")

#     else:
#         st.info("System Idle. Upload visuals to begin.")



## Latest working code with all features
# import streamlit as st
# import requests
# import plotly.graph_objects as go
# import time
# import base64
# from PIL import Image
# import io

# # --- CONFIG ---
# st.set_page_config(page_title="PixelPulse | Visual AI", page_icon="🎵", layout="wide")
# API_URL = "http://127.0.0.1:8000/recommend"

# # --- CSS ---
# st.markdown("""
#     <style>
#     @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;500;700&display=swap');
    
#     .stApp {
#         background-color: #050505;
#         background-image: radial-gradient(circle at 50% 0%, #1e1e24 0%, #000000 100%);
#         font-family: 'Outfit', sans-serif;
#         color: white;
#     }
    
#     /* DJ Message Box */
#     .dj-box {
#         background: rgba(255, 255, 255, 0.05);
#         border-left: 5px solid #a855f7;
#         padding: 15px;
#         border-radius: 8px;
#         margin-bottom: 20px;
#         font-style: italic;
#         color: #e9d5ff;
#         font-size: 1.05rem;
#         line-height: 1.5;
#     }

#     /* Scanner Effect */
#     .scan-container { position: relative; width: 100%; border-radius: 12px; overflow: hidden; border: 1px solid #4ade8055; box-shadow: 0 0 25px rgba(74, 222, 128, 0.3); }
#     .scan-container img { width: 100%; display: block; }
#     .scan-overlay { 
#         position: absolute; top: 0; left: 0; width: 100%; height: 100%; 
#         background: linear-gradient(to bottom, transparent 0%, rgba(74, 222, 128, 0.1) 45%, rgba(100, 255, 150, 0.9) 50%, rgba(74, 222, 128, 0.1) 55%, transparent 100%); 
#         animation: scan 1.5s cubic-bezier(0.4, 0.0, 0.2, 1) infinite; 
#         z-index: 2; pointer-events: none;
#     }
#     @keyframes scan { 0% { transform: translateY(-100%); } 100% { transform: translateY(100%); } }
    
#     /* UI Elements */
#     .accuracy-box { background: rgba(74, 222, 128, 0.15); border: 1px solid #4ade80; color: #4ade80; padding: 6px 12px; border-radius: 8px; font-weight: bold; display: inline-block; margin-right: 10px; font-size: 0.9rem; }
#     .object-pill { background: rgba(255, 255, 255, 0.1); border: 1px solid #4ade8088; color: #dfdfdf; padding: 4px 10px; border-radius: 20px; font-size: 0.8rem; display: inline-block; margin: 3px; }
#     .color-circle { width: 40px; height: 40px; border-radius: 50%; display: inline-block; margin-right: 10px; border: 2px solid rgba(255,255,255,0.2); box-shadow: 0 0 5px rgba(0,0,0,0.5); }
    
#     .modebar { display: none !important; }
#     header, footer {visibility: hidden;}
#     </style>
# """, unsafe_allow_html=True)

# # --- HELPER FUNCTIONS ---
# def img_to_base64_str(img_file):
#     encoded_string = base64.b64encode(img_file.getvalue()).decode()
#     return f"data:image/{img_file.type.split('/')[-1]};base64,{encoded_string}"

# def pil_to_base64(img_pil):
#     buffer = io.BytesIO()
#     img_pil.save(buffer, format="PNG")
#     encoded_string = base64.b64encode(buffer.getvalue()).decode()
#     return f"data:image/png;base64,{encoded_string}"

# def create_radar(mood_vec):
#     categories = ['Valence (Mood)', 'Energy', 'Danceability', 'Tempo', 'Acoustic']
#     values = mood_vec + [mood_vec[0]]
#     cats = categories + [categories[0]]
#     fig = go.Figure(go.Scatterpolar(r=values, theta=cats, fill='toself', line_color='#4ade80', fillcolor='rgba(74, 222, 128, 0.2)'))
#     fig.update_layout(
#         polar=dict(radialaxis=dict(visible=True, range=[0, 1], showticklabels=False, linecolor='#333'), angularaxis=dict(tickfont=dict(color='white', size=11))),
#         paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', 
#         height=380, margin=dict(l=60, r=60, t=30, b=30)
#     )
#     return fig

# def create_interactive_image(img_pil, detections):
#     img_width, img_height = img_pil.size
#     img_base64 = pil_to_base64(img_pil)
#     fig = go.Figure()
#     fig.add_layout_image(dict(source=img_base64, xref="x", yref="y", x=0, y=0, sizex=img_width, sizey=img_height, sizing="stretch", layer="below"))
#     shapes = []
#     for det in detections:
#         x1, y1, x2, y2 = det['bbox']
#         label = det['label']
#         conf = det['confidence']
#         shapes.append(dict(type="rect", x0=x1, y0=y1, x1=x2, y1=y2, line=dict(color='rgba(74, 222, 128, 0.5)', width=1), fillcolor='rgba(74, 222, 128, 0.05)'))
#         center_x, center_y = (x1 + x2) / 2, (y1 + y2) / 2
#         fig.add_trace(go.Scatter(x=[center_x], y=[center_y], mode='markers', marker=dict(color='#4ade80', size=8, opacity=0.4, line=dict(width=1, color='white')), hoverinfo='text', hovertext=f"<span style='color:#4ade80; font-weight:bold;'>[ DETECTED OBJECT ]</span><br>TYPE: {label.upper()}<br>CONFIDENCE: {conf:.1%}", showlegend=False))
#     fig.update_xaxes(showgrid=False, zeroline=False, range=[0, img_width], visible=False)
#     fig.update_yaxes(showgrid=False, zeroline=False, range=[img_height, 0], visible=False, scaleanchor="x", scaleratio=1)
#     fig.update_layout(margin=dict(l=0, r=0, t=0, b=0), plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)', hovermode='closest', dragmode=False, shapes=shapes)
#     return fig

# def typewriter_effect(text, placeholder):
#     displayed_text = ""
#     for char in text:
#         displayed_text += char
#         placeholder.markdown(f'<div class="dj-box">{displayed_text}█</div>', unsafe_allow_html=True)
#         time.sleep(0.015) 
#     placeholder.markdown(f'<div class="dj-box">{displayed_text}</div>', unsafe_allow_html=True)

# # --- MAIN UI ---
# st.title("PixelPulse 🎵")
# st.caption("Computer Vision • Interactive Detection • Audio Intelligence")

# col_left, col_right = st.columns([1, 1.4], gap="large")

# with col_left:
#     st.markdown("### 📤 Input Visual")
#     uploaded_file = st.file_uploader("Upload Image", type=["jpg", "png", "jpeg"])
    
#     if uploaded_file:
#         ph_img = st.empty()
#         ph_status = st.empty()
#         pil_image = Image.open(uploaded_file).convert("RGB")
#         ph_img.image(pil_image, caption="Original Media", use_column_width=True)
        
#         if st.button("Initiate Neural Scan", type="primary", use_container_width=True):
#             img_b64 = img_to_base64_str(uploaded_file)
#             ph_img.markdown(f'<div class="scan-container" style="max-width: none;"><img src="{img_b64}"><div class="scan-overlay"></div></div>', unsafe_allow_html=True)
            
#             steps = ["📡 Establishing Vibe Vector...", "👁️ Analyzing Visual Harmony...", "🎨 Calculating Audio Targets...", "🎵 Curating Spotify Sequence..."]
#             for s in steps:
#                 ph_status.markdown(f"**_{s}_**")
#                 time.sleep(0.5)
            
#             try:
#                 files = {"file": (uploaded_file.name, uploaded_file.getvalue(), uploaded_file.type)}
#                 response = requests.post(API_URL, files=files)
                
#                 if response.status_code == 200:
#                     data = st.session_state['data'] = response.json()
#                     ph_status.empty()
#                     detections = data.get('detections', [])
#                     if detections:
#                         fig = create_interactive_image(pil_image, detections)
#                         ph_img.plotly_chart(fig, use_container_width=True, config={'displayModeBar': False})
#                         st.caption("💡 HUD Active: Hover over detected regions for analysis data.")
#                     else:
#                         ph_img.image(pil_image, caption="Analysis Complete", use_column_width=True)
#                 else:
#                     st.error("Server Error.")
#                     ph_img.image(pil_image)
#             except Exception as e:
#                 st.error(f"Error: {e}")
#                 ph_img.image(pil_image)

# with col_right:
#     if 'data' in st.session_state:
#         data = st.session_state['data']
#         tags = data.get('tags', ["Unknown Vibe"])
#         objects = data.get('detected_objects', [])
#         accuracy = data.get('accuracy', 0)
#         palette = data.get('palette', [])
#         recommendations = data.get('recommendations', [])
#         dj_summary = data.get('dj_summary', "Analysis complete.")
        
#         # 1. DJ NARRATIVE
#         st.markdown("### 👁️ Intelligence Report")
#         dj_placeholder = st.empty()
#         if 'last_dj_msg' not in st.session_state or st.session_state['last_dj_msg'] != dj_summary:
#             typewriter_effect(dj_summary, dj_placeholder)
#             st.session_state['last_dj_msg'] = dj_summary
#         else:
#              dj_placeholder.markdown(f'<div class="dj-box">{dj_summary}</div>', unsafe_allow_html=True)

#         st.markdown(f'<span class="accuracy-box">🎯 Vibe Match: {accuracy}%</span> <span class="accuracy-box">📦 Entities: {len(objects)}</span>', unsafe_allow_html=True)
#         st.write(f"**Musical Vibe:** {tags[0]}")
        
#         if objects:
#             obj_html = "".join([f'<span class="object-pill">{obj}</span>' for obj in objects])
#             st.markdown(obj_html, unsafe_allow_html=True)
        
#         st.write("**Dominant Palette:**")
#         cols_html = "".join([f'<div class="color-circle" style="background-color: {c};"></div>' for c in palette])
#         st.markdown(f'<div>{cols_html}</div>', unsafe_allow_html=True)
        
#         st.markdown("---")
        
#         # --- SPLIT LAYOUT ---
#         c1, c2 = st.columns([1, 1])
        
#         with c1:
#             st.markdown("#### 📊 Audio DNA Target")
#             radar_fig = create_radar(data.get('mood_vector', [0.5]*5))
#             st.plotly_chart(radar_fig, use_container_width=True, config={'displayModeBar': False})

#         with c2:
#             st.markdown("#### 🎧 Curated Tracks")
#             for song in recommendations[:4]: 
#                 track_id = song.get('id')
#                 if track_id:
#                     # OFFICIAL EMBED URL - SAFE AND RELIABLE
#                     embed_url = f"https://open.spotify.com/embed/track/{track_id}?utm_source=generator&theme=0"
#                     st.markdown(f"""
#                     <iframe style="border-radius:12px; margin-bottom: 10px;" 
#                     src="{embed_url}" 
#                     width="100%" height="80" frameBorder="0" 
#                     allowfullscreen="" 
#                     allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture" 
#                     loading="lazy"></iframe>
#                     """, unsafe_allow_html=True)
#                 else:
#                     st.caption("⚠️ Track unavailable")

#     else:
#         st.info("System Idle. Upload visuals to begin.")




# added top 5 songs latest as of now code ----------
# import streamlit as st
# import requests
# import plotly.graph_objects as go
# import time
# import base64
# from PIL import Image
# import io

# # --- CONFIG ---
# st.set_page_config(page_title="PixelPulse | Visual AI", page_icon="🎵", layout="wide")
# API_URL = "http://127.0.0.1:8000/recommend"

# # --- CSS ---
# st.markdown("""
#     <style>
#     @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;500;700&display=swap');
    
#     .stApp {
#         background-color: #050505;
#         background-image: radial-gradient(circle at 50% 0%, #1e1e24 0%, #000000 100%);
#         font-family: 'Outfit', sans-serif;
#         color: white;
#     }
    
#     .dj-box { background: rgba(255, 255, 255, 0.05); border-left: 5px solid #a855f7; padding: 15px; border-radius: 8px; margin-bottom: 20px; font-style: italic; color: #e9d5ff; font-size: 1.05rem; line-height: 1.5; }
#     .scan-container { position: relative; width: 100%; border-radius: 12px; overflow: hidden; border: 1px solid #4ade8055; box-shadow: 0 0 25px rgba(74, 222, 128, 0.3); }
#     .scan-container img { width: 100%; display: block; }
#     .scan-overlay { position: absolute; top: 0; left: 0; width: 100%; height: 100%; background: linear-gradient(to bottom, transparent 0%, rgba(74, 222, 128, 0.1) 45%, rgba(100, 255, 150, 0.9) 50%, rgba(74, 222, 128, 0.1) 55%, transparent 100%); animation: scan 1.5s cubic-bezier(0.4, 0.0, 0.2, 1) infinite; z-index: 2; pointer-events: none; }
#     @keyframes scan { 0% { transform: translateY(-100%); } 100% { transform: translateY(100%); } }
#     .accuracy-box { background: rgba(74, 222, 128, 0.15); border: 1px solid #4ade80; color: #4ade80; padding: 6px 12px; border-radius: 8px; font-weight: bold; display: inline-block; margin-right: 10px; font-size: 0.9rem; }
#     .object-pill { background: rgba(255, 255, 255, 0.1); border: 1px solid #4ade8088; color: #dfdfdf; padding: 4px 10px; border-radius: 20px; font-size: 0.8rem; display: inline-block; margin: 3px; }
#     .color-circle { width: 40px; height: 40px; border-radius: 50%; display: inline-block; margin-right: 10px; border: 2px solid rgba(255,255,255,0.2); box-shadow: 0 0 5px rgba(0,0,0,0.5); }
#     .modebar { display: none !important; }
#     header, footer {visibility: hidden;}
#     </style>
# """, unsafe_allow_html=True)

# # --- HELPERS ---
# def img_to_base64_str(img_file):
#     encoded_string = base64.b64encode(img_file.getvalue()).decode()
#     return f"data:image/{img_file.type.split('/')[-1]};base64,{encoded_string}"

# def pil_to_base64(img_pil):
#     buffer = io.BytesIO()
#     img_pil.save(buffer, format="PNG")
#     encoded_string = base64.b64encode(buffer.getvalue()).decode()
#     return f"data:image/png;base64,{encoded_string}"

# def create_radar(mood_vec):
#     categories = ['Valence (Mood)', 'Energy', 'Danceability', 'Tempo', 'Acoustic']
#     values = mood_vec + [mood_vec[0]]
#     cats = categories + [categories[0]]
#     fig = go.Figure(go.Scatterpolar(r=values, theta=cats, fill='toself', line_color='#4ade80', fillcolor='rgba(74, 222, 128, 0.2)'))
#     fig.update_layout(polar=dict(radialaxis=dict(visible=True, range=[0, 1], showticklabels=False, linecolor='#333'), angularaxis=dict(tickfont=dict(color='white', size=11))), paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', height=380, margin=dict(l=60, r=60, t=30, b=30))
#     return fig

# def create_interactive_image(img_pil, detections):
#     img_width, img_height = img_pil.size
#     img_base64 = pil_to_base64(img_pil)
#     fig = go.Figure()
#     fig.add_layout_image(dict(source=img_base64, xref="x", yref="y", x=0, y=0, sizex=img_width, sizey=img_height, sizing="stretch", layer="below"))
#     shapes = []
#     for det in detections:
#         x1, y1, x2, y2 = det['bbox']
#         label = det['label']
#         conf = det['confidence']
#         shapes.append(dict(type="rect", x0=x1, y0=y1, x1=x2, y1=y2, line=dict(color='rgba(74, 222, 128, 0.5)', width=1), fillcolor='rgba(74, 222, 128, 0.05)'))
#         center_x, center_y = (x1 + x2) / 2, (y1 + y2) / 2
#         fig.add_trace(go.Scatter(x=[center_x], y=[center_y], mode='markers', marker=dict(color='#4ade80', size=8, opacity=0.4, line=dict(width=1, color='white')), hoverinfo='text', hovertext=f"<span style='color:#4ade80; font-weight:bold;'>[ DETECTED OBJECT ]</span><br>TYPE: {label.upper()}<br>CONFIDENCE: {conf:.1%}", showlegend=False))
#     fig.update_xaxes(showgrid=False, zeroline=False, range=[0, img_width], visible=False)
#     fig.update_yaxes(showgrid=False, zeroline=False, range=[img_height, 0], visible=False, scaleanchor="x", scaleratio=1)
#     fig.update_layout(margin=dict(l=0, r=0, t=0, b=0), plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)', hovermode='closest', dragmode=False, shapes=shapes)
#     return fig

# def typewriter_effect(text, placeholder):
#     displayed_text = ""
#     for char in text:
#         displayed_text += char
#         placeholder.markdown(f'<div class="dj-box">{displayed_text}█</div>', unsafe_allow_html=True)
#         time.sleep(0.015) 
#     placeholder.markdown(f'<div class="dj-box">{displayed_text}</div>', unsafe_allow_html=True)

# # --- MAIN UI ---
# st.title("PixelPulse 🎵")
# st.caption("Computer Vision • Interactive Detection • Audio Intelligence")

# col_left, col_right = st.columns([1, 1.4], gap="large")

# with col_left:
#     st.markdown("### 📤 Input Visual")
#     uploaded_file = st.file_uploader("Upload Image", type=["jpg", "png", "jpeg"])
    
#     if uploaded_file:
#         ph_img = st.empty()
#         ph_status = st.empty()
#         pil_image = Image.open(uploaded_file).convert("RGB")
#         ph_img.image(pil_image, caption="Original Media", use_column_width=True)
        
#         if st.button("Initiate Neural Scan", type="primary", use_container_width=True):
#             img_b64 = img_to_base64_str(uploaded_file)
#             ph_img.markdown(f'<div class="scan-container" style="max-width: none;"><img src="{img_b64}"><div class="scan-overlay"></div></div>', unsafe_allow_html=True)
            
#             steps = ["📡 Establishing Vibe Vector...", "👁️ Analyzing Visual Harmony...", "🎨 Calculating Audio Targets...", "🎵 Curating Spotify Sequence..."]
#             for s in steps:
#                 ph_status.markdown(f"**_{s}_**")
#                 time.sleep(0.5)
            
#             try:
#                 files = {"file": (uploaded_file.name, uploaded_file.getvalue(), uploaded_file.type)}
#                 response = requests.post(API_URL, files=files)
                
#                 if response.status_code == 200:
#                     data = st.session_state['data'] = response.json()
#                     ph_status.empty()
#                     detections = data.get('detections', [])
#                     if detections:
#                         fig = create_interactive_image(pil_image, detections)
#                         ph_img.plotly_chart(fig, use_container_width=True, config={'displayModeBar': False})
#                         st.caption("💡 HUD Active: Hover over detected regions for analysis data.")
#                     else:
#                         ph_img.image(pil_image, caption="Analysis Complete", use_column_width=True)
#                 else:
#                     st.error("Server Error.")
#                     ph_img.image(pil_image)
#             except Exception as e:
#                 st.error(f"Error: {e}")
#                 ph_img.image(pil_image)

# with col_right:
#     if 'data' in st.session_state:
#         data = st.session_state['data']
#         tags = data.get('tags', ["Unknown Vibe"])
#         objects = data.get('detected_objects', [])
#         accuracy = data.get('accuracy', 0)
#         palette = data.get('palette', [])
#         recommendations = data.get('recommendations', [])
#         dj_summary = data.get('dj_summary', "Analysis complete.")
        
#         st.markdown("### 👁️ Intelligence Report")
#         dj_placeholder = st.empty()
#         if 'last_dj_msg' not in st.session_state or st.session_state['last_dj_msg'] != dj_summary:
#             typewriter_effect(dj_summary, dj_placeholder)
#             st.session_state['last_dj_msg'] = dj_summary
#         else:
#              dj_placeholder.markdown(f'<div class="dj-box">{dj_summary}</div>', unsafe_allow_html=True)

#         st.markdown(f'<span class="accuracy-box">🎯 Vibe Match: {accuracy}%</span> <span class="accuracy-box">📦 Entities: {len(objects)}</span>', unsafe_allow_html=True)
#         st.write(f"**Musical Vibe:** {tags[0]}")
        
#         if objects:
#             obj_html = "".join([f'<span class="object-pill">{obj}</span>' for obj in objects])
#             st.markdown(obj_html, unsafe_allow_html=True)
        
#         st.write("**Dominant Palette:**")
#         cols_html = "".join([f'<div class="color-circle" style="background-color: {c};"></div>' for c in palette])
#         st.markdown(f'<div>{cols_html}</div>', unsafe_allow_html=True)
        
#         st.markdown("---")
        
#         c1, c2 = st.columns([1, 1])
#         with c1:
#             st.markdown("#### 📊 Audio DNA Target")
#             radar_fig = create_radar(data.get('mood_vector', [0.5]*5))
#             st.plotly_chart(radar_fig, use_container_width=True, config={'displayModeBar': False})
#         with c2:
#             st.markdown("#### 🎧 Curated Tracks (Top 5 Mix)")
#             # Display TOP 5 songs (Mixed Languages)
#             for song in recommendations[:5]: 
#                 track_id = song.get('id')
#                 if track_id:
#                     embed_url = f"https://open.spotify.com/embed/track/{track_id}?utm_source=generator&theme=0"
#                     st.markdown(f"""
#                     <iframe style="border-radius:12px; margin-bottom: 10px;" 
#                     src="{embed_url}" 
#                     width="100%" height="80" frameBorder="0" 
#                     allowfullscreen="" 
#                     allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture" 
#                     loading="lazy"></iframe>
#                     """, unsafe_allow_html=True)
#                 else:
#                     st.caption("⚠️ Track unavailable")

#     else:
#         st.info("System Idle. Upload visuals to begin.")




## Badge not properly placed
# import streamlit as st
# import requests
# import plotly.graph_objects as go
# import time
# import base64
# from PIL import Image
# import io

# # --- CONFIG ---
# st.set_page_config(page_title="PixelPulse | Visual AI", page_icon="🎵", layout="wide")
# API_URL = "http://127.0.0.1:8000/recommend"

# # --- CSS ---
# st.markdown("""
#     <style>
#     @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;500;700&display=swap');
    
#     .stApp {
#         background-color: #050505;
#         background-image: radial-gradient(circle at 50% 0%, #1e1e24 0%, #000000 100%);
#         font-family: 'Outfit', sans-serif;
#         color: white;
#     }
    
#     .dj-box { background: rgba(255, 255, 255, 0.05); border-left: 5px solid #a855f7; padding: 15px; border-radius: 8px; margin-bottom: 20px; font-style: italic; color: #e9d5ff; font-size: 1.05rem; line-height: 1.5; }
#     .scan-container { position: relative; width: 100%; border-radius: 12px; overflow: hidden; border: 1px solid #4ade8055; box-shadow: 0 0 25px rgba(74, 222, 128, 0.3); }
#     .scan-container img { width: 100%; display: block; }
#     .scan-overlay { position: absolute; top: 0; left: 0; width: 100%; height: 100%; background: linear-gradient(to bottom, transparent 0%, rgba(74, 222, 128, 0.1) 45%, rgba(100, 255, 150, 0.9) 50%, rgba(74, 222, 128, 0.1) 55%, transparent 100%); animation: scan 1.5s cubic-bezier(0.4, 0.0, 0.2, 1) infinite; z-index: 2; pointer-events: none; }
#     @keyframes scan { 0% { transform: translateY(-100%); } 100% { transform: translateY(100%); } }
#     .accuracy-box { background: rgba(74, 222, 128, 0.15); border: 1px solid #4ade80; color: #4ade80; padding: 6px 12px; border-radius: 8px; font-weight: bold; display: inline-block; margin-right: 10px; font-size: 0.9rem; }
#     .object-pill { background: rgba(255, 255, 255, 0.1); border: 1px solid #4ade8088; color: #dfdfdf; padding: 4px 10px; border-radius: 20px; font-size: 0.8rem; display: inline-block; margin: 3px; }
#     .color-circle { width: 40px; height: 40px; border-radius: 50%; display: inline-block; margin-right: 10px; border: 2px solid rgba(255,255,255,0.2); box-shadow: 0 0 5px rgba(0,0,0,0.5); }
    
#     /* New Match Badge Style */
#     .match-badge {
#         background-color: #4ade80;
#         color: #000;
#         padding: 4px 10px;
#         border-radius: 6px;
#         font-weight: 700;
#         font-size: 0.8rem;
#         margin-bottom: 8px;
#         display: inline-block;
#         box-shadow: 0 0 10px rgba(74, 222, 128, 0.3);
#     }

#     .modebar { display: none !important; }
#     header, footer {visibility: hidden;}
#     </style>
# """, unsafe_allow_html=True)

# # --- HELPERS ---
# def img_to_base64_str(img_file):
#     encoded_string = base64.b64encode(img_file.getvalue()).decode()
#     return f"data:image/{img_file.type.split('/')[-1]};base64,{encoded_string}"

# def pil_to_base64(img_pil):
#     buffer = io.BytesIO()
#     img_pil.save(buffer, format="PNG")
#     encoded_string = base64.b64encode(buffer.getvalue()).decode()
#     return f"data:image/png;base64,{encoded_string}"

# def create_radar(mood_vec):
#     categories = ['Valence (Mood)', 'Energy', 'Danceability', 'Tempo', 'Acoustic']
#     values = mood_vec + [mood_vec[0]]
#     cats = categories + [categories[0]]
#     fig = go.Figure(go.Scatterpolar(r=values, theta=cats, fill='toself', line_color='#4ade80', fillcolor='rgba(74, 222, 128, 0.2)'))
#     fig.update_layout(polar=dict(radialaxis=dict(visible=True, range=[0, 1], showticklabels=False, linecolor='#333'), angularaxis=dict(tickfont=dict(color='white', size=11))), paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', height=380, margin=dict(l=60, r=60, t=30, b=30))
#     return fig

# def create_interactive_image(img_pil, detections):
#     img_width, img_height = img_pil.size
#     img_base64 = pil_to_base64(img_pil)
#     fig = go.Figure()
#     fig.add_layout_image(dict(source=img_base64, xref="x", yref="y", x=0, y=0, sizex=img_width, sizey=img_height, sizing="stretch", layer="below"))
#     shapes = []
#     for det in detections:
#         x1, y1, x2, y2 = det['bbox']
#         label = det['label']
#         conf = det['confidence']
#         shapes.append(dict(type="rect", x0=x1, y0=y1, x1=x2, y1=y2, line=dict(color='rgba(74, 222, 128, 0.5)', width=1), fillcolor='rgba(74, 222, 128, 0.05)'))
#         center_x, center_y = (x1 + x2) / 2, (y1 + y2) / 2
#         fig.add_trace(go.Scatter(x=[center_x], y=[center_y], mode='markers', marker=dict(color='#4ade80', size=8, opacity=0.4, line=dict(width=1, color='white')), hoverinfo='text', hovertext=f"<span style='color:#4ade80; font-weight:bold;'>[ DETECTED OBJECT ]</span><br>TYPE: {label.upper()}<br>CONFIDENCE: {conf:.1%}", showlegend=False))
#     fig.update_xaxes(showgrid=False, zeroline=False, range=[0, img_width], visible=False)
#     fig.update_yaxes(showgrid=False, zeroline=False, range=[img_height, 0], visible=False, scaleanchor="x", scaleratio=1)
#     fig.update_layout(margin=dict(l=0, r=0, t=0, b=0), plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)', hovermode='closest', dragmode=False, shapes=shapes)
#     return fig

# def typewriter_effect(text, placeholder):
#     displayed_text = ""
#     for char in text:
#         displayed_text += char
#         placeholder.markdown(f'<div class="dj-box">{displayed_text}█</div>', unsafe_allow_html=True)
#         time.sleep(0.015) 
#     placeholder.markdown(f'<div class="dj-box">{displayed_text}</div>', unsafe_allow_html=True)

# # --- MAIN UI ---
# st.title("PixelPulse 🎵")
# st.caption("Computer Vision • Interactive Detection • Audio Intelligence")

# col_left, col_right = st.columns([1, 1.4], gap="large")

# with col_left:
#     st.markdown("### 📤 Input Visual")
#     uploaded_file = st.file_uploader("Upload Image", type=["jpg", "png", "jpeg"])
    
#     if uploaded_file:
#         ph_img = st.empty()
#         ph_status = st.empty()
#         pil_image = Image.open(uploaded_file).convert("RGB")
#         ph_img.image(pil_image, caption="Original Media", use_column_width=True)
        
#         if st.button("Initiate Neural Scan", type="primary", use_container_width=True):
#             img_b64 = img_to_base64_str(uploaded_file)
#             ph_img.markdown(f'<div class="scan-container" style="max-width: none;"><img src="{img_b64}"><div class="scan-overlay"></div></div>', unsafe_allow_html=True)
            
#             steps = ["📡 Establishing Vibe Vector...", "👁️ Analyzing Visual Harmony...", "🎨 Calculating Audio Targets...", "🎵 Curating Spotify Sequence..."]
#             for s in steps:
#                 ph_status.markdown(f"**_{s}_**")
#                 time.sleep(0.5)
            
#             try:
#                 files = {"file": (uploaded_file.name, uploaded_file.getvalue(), uploaded_file.type)}
#                 response = requests.post(API_URL, files=files)
                
#                 if response.status_code == 200:
#                     data = st.session_state['data'] = response.json()
#                     ph_status.empty()
#                     detections = data.get('detections', [])
#                     if detections:
#                         fig = create_interactive_image(pil_image, detections)
#                         ph_img.plotly_chart(fig, use_container_width=True, config={'displayModeBar': False})
#                         st.caption("💡 HUD Active: Hover over detected regions for analysis data.")
#                     else:
#                         ph_img.image(pil_image, caption="Analysis Complete", use_column_width=True)
#                 else:
#                     st.error("Server Error.")
#                     ph_img.image(pil_image)
#             except Exception as e:
#                 st.error(f"Error: {e}")
#                 ph_img.image(pil_image)

# with col_right:
#     if 'data' in st.session_state:
#         data = st.session_state['data']
#         tags = data.get('tags', ["Unknown Vibe"])
#         objects = data.get('detected_objects', [])
#         accuracy = data.get('accuracy', 0)
#         palette = data.get('palette', [])
#         recommendations = data.get('recommendations', [])
#         dj_summary = data.get('dj_summary', "Analysis complete.")
        
#         st.markdown("### 👁️ Intelligence Report")
#         dj_placeholder = st.empty()
#         if 'last_dj_msg' not in st.session_state or st.session_state['last_dj_msg'] != dj_summary:
#             typewriter_effect(dj_summary, dj_placeholder)
#             st.session_state['last_dj_msg'] = dj_summary
#         else:
#              dj_placeholder.markdown(f'<div class="dj-box">{dj_summary}</div>', unsafe_allow_html=True)

#         st.markdown(f'<span class="accuracy-box">🎯 Vibe Match: {accuracy}%</span> <span class="accuracy-box">📦 Entities: {len(objects)}</span>', unsafe_allow_html=True)
#         st.write(f"**Musical Vibe:** {tags[0]}")
        
#         if objects:
#             obj_html = "".join([f'<span class="object-pill">{obj}</span>' for obj in objects])
#             st.markdown(obj_html, unsafe_allow_html=True)
        
#         st.write("**Dominant Palette:**")
#         cols_html = "".join([f'<div class="color-circle" style="background-color: {c};"></div>' for c in palette])
#         st.markdown(f'<div>{cols_html}</div>', unsafe_allow_html=True)
        
#         st.markdown("---")
        
#         c1, c2 = st.columns([1, 1])
#         with c1:
#             st.markdown("#### 📊 Audio DNA Target")
#             radar_fig = create_radar(data.get('mood_vector', [0.5]*5))
#             st.plotly_chart(radar_fig, use_container_width=True, config={'displayModeBar': False})
#         with c2:
#             st.markdown("#### 🎧 Curated Tracks")
            
#             for song in recommendations[:5]:
#                 match_score = song.get('match_score', 85) # Default match score if calculations fail
                
#                 # Dynamic Badge Color
#                 badge_color = "#4ade80" # Green for > 80%
#                 if match_score < 80: badge_color = "#facc15" # Yellow
#                 if match_score < 60: badge_color = "#f87171" # Red
                
#                 st.markdown(f'<div class="match-badge" style="background-color: {badge_color};">⚡ {match_score}% MATCH</div>', unsafe_allow_html=True)
                
#                 track_id = song.get('id')
#                 if track_id:
#                     embed_url = f"https://open.spotify.com/embed/track/{track_id}?utm_source=generator&theme=0"
#                     st.markdown(f"""
#                     <iframe style="border-radius:12px; margin-bottom: 5px;" 
#                     src="{embed_url}" 
#                     width="100%" height="80" frameBorder="0" 
#                     allowfullscreen="" 
#                     allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture" 
#                     loading="lazy"></iframe>
#                     """, unsafe_allow_html=True)
#                 else:
#                     st.caption("⚠️ Track unavailable")

#     else:
#         st.info("System Idle. Upload visuals to begin.")



## Badge not properly placed 
# import streamlit as st
# import requests
# import plotly.graph_objects as go
# import time
# import base64
# from PIL import Image
# import io

# # --- CONFIG ---
# st.set_page_config(page_title="PixelPulse | Visual AI", page_icon="🎵", layout="wide")
# API_URL = "http://127.0.0.1:8000/recommend"

# # --- CSS ---
# st.markdown("""
#     <style>
#     @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;500;700&display=swap');
    
#     .stApp {
#         background-color: #050505;
#         background-image: radial-gradient(circle at 50% 0%, #1e1e24 0%, #000000 100%);
#         font-family: 'Outfit', sans-serif;
#         color: white;
#     }
    
#     .dj-box { background: rgba(255, 255, 255, 0.05); border-left: 5px solid #a855f7; padding: 15px; border-radius: 8px; margin-bottom: 20px; font-style: italic; color: #e9d5ff; font-size: 1.05rem; line-height: 1.5; }
#     .scan-container { position: relative; width: 100%; border-radius: 12px; overflow: hidden; border: 1px solid #4ade8055; box-shadow: 0 0 25px rgba(74, 222, 128, 0.3); }
#     .scan-container img { width: 100%; display: block; }
#     .scan-overlay { position: absolute; top: 0; left: 0; width: 100%; height: 100%; background: linear-gradient(to bottom, transparent 0%, rgba(74, 222, 128, 0.1) 45%, rgba(100, 255, 150, 0.9) 50%, rgba(74, 222, 128, 0.1) 55%, transparent 100%); animation: scan 1.5s cubic-bezier(0.4, 0.0, 0.2, 1) infinite; z-index: 2; pointer-events: none; }
#     @keyframes scan { 0% { transform: translateY(-100%); } 100% { transform: translateY(100%); } }
#     .accuracy-box { background: rgba(74, 222, 128, 0.15); border: 1px solid #4ade80; color: #4ade80; padding: 6px 12px; border-radius: 8px; font-weight: bold; display: inline-block; margin-right: 10px; font-size: 0.9rem; }
#     .object-pill { background: rgba(255, 255, 255, 0.1); border: 1px solid #4ade8088; color: #dfdfdf; padding: 4px 10px; border-radius: 20px; font-size: 0.8rem; display: inline-block; margin: 3px; }
#     .color-circle { width: 40px; height: 40px; border-radius: 50%; display: inline-block; margin-right: 10px; border: 2px solid rgba(255,255,255,0.2); box-shadow: 0 0 5px rgba(0,0,0,0.5); }
    
#     /* --- NEW BADGE STYLING --- */
#     .player-wrapper {
#         position: relative; /* Anchor for the absolute badge */
#         margin-bottom: 15px;
#         transition: transform 0.2s;
#     }
#     .player-wrapper:hover {
#         transform: scale(1.01);
#     }
    
#     .match-badge {
#         position: absolute;
#         top: 12px;     /* Position from top */
#         right: 60px;   /* Position from right (Left of Spotify Icon) */
#         background-color: #4ade80;
#         color: #000;
#         padding: 3px 8px;
#         border-radius: 4px;
#         font-weight: 800;
#         font-size: 0.7rem;
#         z-index: 10;   /* Ensure it sits ON TOP of the iframe */
#         pointer-events: none; /* Allows clicks to pass through to the player if needed */
#         box-shadow: 0 2px 5px rgba(0,0,0,0.5);
#         letter-spacing: 0.5px;
#     }

#     .modebar { display: none !important; }
#     header, footer {visibility: hidden;}
#     </style>
# """, unsafe_allow_html=True)

# # --- HELPERS ---
# def img_to_base64_str(img_file):
#     encoded_string = base64.b64encode(img_file.getvalue()).decode()
#     return f"data:image/{img_file.type.split('/')[-1]};base64,{encoded_string}"

# def pil_to_base64(img_pil):
#     buffer = io.BytesIO()
#     img_pil.save(buffer, format="PNG")
#     encoded_string = base64.b64encode(buffer.getvalue()).decode()
#     return f"data:image/png;base64,{encoded_string}"

# def create_radar(mood_vec):
#     categories = ['Valence (Mood)', 'Energy', 'Danceability', 'Tempo', 'Acoustic']
#     values = mood_vec + [mood_vec[0]]
#     cats = categories + [categories[0]]
#     fig = go.Figure(go.Scatterpolar(r=values, theta=cats, fill='toself', line_color='#4ade80', fillcolor='rgba(74, 222, 128, 0.2)'))
#     fig.update_layout(polar=dict(radialaxis=dict(visible=True, range=[0, 1], showticklabels=False, linecolor='#333'), angularaxis=dict(tickfont=dict(color='white', size=11))), paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', height=380, margin=dict(l=60, r=60, t=30, b=30))
#     return fig

# def create_interactive_image(img_pil, detections):
#     img_width, img_height = img_pil.size
#     img_base64 = pil_to_base64(img_pil)
#     fig = go.Figure()
#     fig.add_layout_image(dict(source=img_base64, xref="x", yref="y", x=0, y=0, sizex=img_width, sizey=img_height, sizing="stretch", layer="below"))
#     shapes = []
#     for det in detections:
#         x1, y1, x2, y2 = det['bbox']
#         label = det['label']
#         conf = det['confidence']
#         shapes.append(dict(type="rect", x0=x1, y0=y1, x1=x2, y1=y2, line=dict(color='rgba(74, 222, 128, 0.5)', width=1), fillcolor='rgba(74, 222, 128, 0.05)'))
#         center_x, center_y = (x1 + x2) / 2, (y1 + y2) / 2
#         fig.add_trace(go.Scatter(x=[center_x], y=[center_y], mode='markers', marker=dict(color='#4ade80', size=8, opacity=0.4, line=dict(width=1, color='white')), hoverinfo='text', hovertext=f"<span style='color:#4ade80; font-weight:bold;'>[ DETECTED OBJECT ]</span><br>TYPE: {label.upper()}<br>CONFIDENCE: {conf:.1%}", showlegend=False))
#     fig.update_xaxes(showgrid=False, zeroline=False, range=[0, img_width], visible=False)
#     fig.update_yaxes(showgrid=False, zeroline=False, range=[img_height, 0], visible=False, scaleanchor="x", scaleratio=1)
#     fig.update_layout(margin=dict(l=0, r=0, t=0, b=0), plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)', hovermode='closest', dragmode=False, shapes=shapes)
#     return fig

# def typewriter_effect(text, placeholder):
#     displayed_text = ""
#     for char in text:
#         displayed_text += char
#         placeholder.markdown(f'<div class="dj-box">{displayed_text}█</div>', unsafe_allow_html=True)
#         time.sleep(0.015) 
#     placeholder.markdown(f'<div class="dj-box">{displayed_text}</div>', unsafe_allow_html=True)

# # --- MAIN UI ---
# st.title("PixelPulse 🎵")
# st.caption("Computer Vision • Interactive Detection • Audio Intelligence")

# col_left, col_right = st.columns([1, 1.4], gap="large")

# with col_left:
#     st.markdown("### 📤 Input Visual")
#     uploaded_file = st.file_uploader("Upload Image", type=["jpg", "png", "jpeg"])
    
#     if uploaded_file:
#         ph_img = st.empty()
#         ph_status = st.empty()
#         pil_image = Image.open(uploaded_file).convert("RGB")
#         ph_img.image(pil_image, caption="Original Media", use_column_width=True)
        
#         if st.button("Initiate Neural Scan", type="primary", use_container_width=True):
#             img_b64 = img_to_base64_str(uploaded_file)
#             ph_img.markdown(f'<div class="scan-container" style="max-width: none;"><img src="{img_b64}"><div class="scan-overlay"></div></div>', unsafe_allow_html=True)
            
#             steps = ["📡 Establishing Vibe Vector...", "👁️ Analyzing Visual Harmony...", "🎨 Calculating Audio Targets...", "🎵 Curating Spotify Sequence..."]
#             for s in steps:
#                 ph_status.markdown(f"**_{s}_**")
#                 time.sleep(0.5)
            
#             try:
#                 files = {"file": (uploaded_file.name, uploaded_file.getvalue(), uploaded_file.type)}
#                 response = requests.post(API_URL, files=files)
                
#                 if response.status_code == 200:
#                     data = st.session_state['data'] = response.json()
#                     ph_status.empty()
#                     detections = data.get('detections', [])
#                     if detections:
#                         fig = create_interactive_image(pil_image, detections)
#                         ph_img.plotly_chart(fig, use_container_width=True, config={'displayModeBar': False})
#                         st.caption("💡 HUD Active: Hover over detected regions for analysis data.")
#                     else:
#                         ph_img.image(pil_image, caption="Analysis Complete", use_column_width=True)
#                 else:
#                     st.error("Server Error.")
#                     ph_img.image(pil_image)
#             except Exception as e:
#                 st.error(f"Error: {e}")
#                 ph_img.image(pil_image)

# with col_right:
#     if 'data' in st.session_state:
#         data = st.session_state['data']
#         tags = data.get('tags', ["Unknown Vibe"])
#         objects = data.get('detected_objects', [])
#         accuracy = data.get('accuracy', 0)
#         palette = data.get('palette', [])
#         recommendations = data.get('recommendations', [])
#         dj_summary = data.get('dj_summary', "Analysis complete.")
        
#         st.markdown("### 👁️ Intelligence Report")
#         dj_placeholder = st.empty()
#         if 'last_dj_msg' not in st.session_state or st.session_state['last_dj_msg'] != dj_summary:
#             typewriter_effect(dj_summary, dj_placeholder)
#             st.session_state['last_dj_msg'] = dj_summary
#         else:
#              dj_placeholder.markdown(f'<div class="dj-box">{dj_summary}</div>', unsafe_allow_html=True)

#         st.markdown(f'<span class="accuracy-box">🎯 Vibe Match: {accuracy}%</span> <span class="accuracy-box">📦 Entities: {len(objects)}</span>', unsafe_allow_html=True)
#         st.write(f"**Musical Vibe:** {tags[0]}")
        
#         if objects:
#             obj_html = "".join([f'<span class="object-pill">{obj}</span>' for obj in objects])
#             st.markdown(obj_html, unsafe_allow_html=True)
        
#         st.write("**Dominant Palette:**")
#         cols_html = "".join([f'<div class="color-circle" style="background-color: {c};"></div>' for c in palette])
#         st.markdown(f'<div>{cols_html}</div>', unsafe_allow_html=True)
        
#         st.markdown("---")
        
#         c1, c2 = st.columns([1, 1])
#         with c1:
#             st.markdown("#### 📊 Audio DNA Target")
#             radar_fig = create_radar(data.get('mood_vector', [0.5]*5))
#             st.plotly_chart(radar_fig, use_container_width=True, config={'displayModeBar': False})
#         with c2:
#             st.markdown("#### 🎧 Curated Tracks")
            
#             for song in recommendations[:5]:
#                 match_score = song.get('match_score', 85)
                
#                 # Dynamic Badge Color
#                 badge_color = "#4ade80" # Green
#                 if match_score < 80: badge_color = "#facc15" # Yellow
#                 if match_score < 60: badge_color = "#f87171" # Red
                
#                 track_id = song.get('id')
#                 if track_id:
#                     embed_url = f"https://open.spotify.com/embed/track/{track_id}?utm_source=generator&theme=0"
                    
#                     # SINGLE BLOCK containing Wrapper + Badge + Iframe
#                     st.markdown(f"""
#                     <div class="player-wrapper">
#                         <div class="match-badge" style="background-color: {badge_color};">⚡ {match_score}% MATCH</div>
#                         <iframe style="border-radius:12px;" 
#                         src="{embed_url}" 
#                         width="100%" height="80" frameBorder="0" 
#                         allowfullscreen="" 
#                         allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture" 
#                         loading="lazy"></iframe>
#                     </div>
#                     """, unsafe_allow_html=True)
#                 else:
#                     st.caption("⚠️ Track unavailable")

#     else:
#         st.info("System Idle. Upload visuals to begin.")




## latest v 
# import streamlit as st
# import requests
# import plotly.graph_objects as go
# import time
# import base64
# from PIL import Image
# import io

# # --- CONFIG ---
# st.set_page_config(page_title="PixelPulse | Visual AI", page_icon="🎵", layout="wide")
# API_URL = "http://127.0.0.1:8000/recommend"

# # --- CSS ---
# st.markdown("""
#     <style>
#     @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;500;700&display=swap');
    
#     .stApp {
#         background-color: #050505;
#         background-image: radial-gradient(circle at 50% 0%, #1e1e24 0%, #000000 100%);
#         font-family: 'Outfit', sans-serif;
#         color: white;
#     }
    
#     .dj-box { background: rgba(255, 255, 255, 0.05); border-left: 5px solid #a855f7; padding: 15px; border-radius: 8px; margin-bottom: 20px; font-style: italic; color: #e9d5ff; font-size: 1.05rem; line-height: 1.5; }
#     .scan-container { position: relative; width: 100%; border-radius: 12px; overflow: hidden; border: 1px solid #4ade8055; box-shadow: 0 0 25px rgba(74, 222, 128, 0.3); }
#     .scan-container img { width: 100%; display: block; }
#     .scan-overlay { position: absolute; top: 0; left: 0; width: 100%; height: 100%; background: linear-gradient(to bottom, transparent 0%, rgba(74, 222, 128, 0.1) 45%, rgba(100, 255, 150, 0.9) 50%, rgba(74, 222, 128, 0.1) 55%, transparent 100%); animation: scan 1.5s cubic-bezier(0.4, 0.0, 0.2, 1) infinite; z-index: 2; pointer-events: none; }
#     @keyframes scan { 0% { transform: translateY(-100%); } 100% { transform: translateY(100%); } }
#     .accuracy-box { background: rgba(74, 222, 128, 0.15); border: 1px solid #4ade80; color: #4ade80; padding: 6px 12px; border-radius: 8px; font-weight: bold; display: inline-block; margin-right: 10px; font-size: 0.9rem; }
#     .object-pill { background: rgba(255, 255, 255, 0.1); border: 1px solid #4ade8088; color: #dfdfdf; padding: 4px 10px; border-radius: 20px; font-size: 0.8rem; display: inline-block; margin: 3px; }
#     .color-circle { width: 40px; height: 40px; border-radius: 50%; display: inline-block; margin-right: 10px; border: 2px solid rgba(255,255,255,0.2); box-shadow: 0 0 5px rgba(0,0,0,0.5); }
    
#     /* --- NEW PREMIUM BADGE --- */
#     .player-wrapper {
#         position: relative;
#         margin-bottom: 12px;
#         transition: transform 0.2s;
#     }
#     .player-wrapper:hover {
#         transform: scale(1.02);
#     }
    
#     .match-badge {
#         position: absolute;
#         top: 8px;     
#         right: 50px;   
#         background: rgba(0, 0, 0, 0.6); /* Glass effect */
#         backdrop-filter: blur(4px);
#         color: #4ade80;
#         border: 1px solid #4ade80;
#         padding: 2px 8px;
#         border-radius: 12px;
#         font-weight: 600;
#         font-size: 0.75rem;
#         z-index: 10;
#         pointer-events: none;
#         box-shadow: 0 4px 6px rgba(0,0,0,0.3);
#         letter-spacing: 0.5px;
#     }

#     .modebar { display: none !important; }
#     header, footer {visibility: hidden;}
#     </style>
# """, unsafe_allow_html=True)

# # --- HELPERS ---
# def img_to_base64_str(img_file):
#     encoded_string = base64.b64encode(img_file.getvalue()).decode()
#     return f"data:image/{img_file.type.split('/')[-1]};base64,{encoded_string}"

# def pil_to_base64(img_pil):
#     buffer = io.BytesIO()
#     img_pil.save(buffer, format="PNG")
#     encoded_string = base64.b64encode(buffer.getvalue()).decode()
#     return f"data:image/png;base64,{encoded_string}"

# def create_radar(mood_vec):
#     categories = ['Valence (Mood)', 'Energy', 'Danceability', 'Tempo', 'Acoustic']
#     values = mood_vec + [mood_vec[0]]
#     cats = categories + [categories[0]]
#     fig = go.Figure(go.Scatterpolar(r=values, theta=cats, fill='toself', line_color='#4ade80', fillcolor='rgba(74, 222, 128, 0.2)'))
#     fig.update_layout(polar=dict(radialaxis=dict(visible=True, range=[0, 1], showticklabels=False, linecolor='#333'), angularaxis=dict(tickfont=dict(color='white', size=11))), paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', height=380, margin=dict(l=60, r=60, t=30, b=30))
#     return fig

# def create_interactive_image(img_pil, detections):
#     img_width, img_height = img_pil.size
#     img_base64 = pil_to_base64(img_pil)
#     fig = go.Figure()
#     fig.add_layout_image(dict(source=img_base64, xref="x", yref="y", x=0, y=0, sizex=img_width, sizey=img_height, sizing="stretch", layer="below"))
#     shapes = []
#     for det in detections:
#         x1, y1, x2, y2 = det['bbox']
#         label = det['label']
#         conf = det['confidence']
#         shapes.append(dict(type="rect", x0=x1, y0=y1, x1=x2, y1=y2, line=dict(color='rgba(74, 222, 128, 0.5)', width=1), fillcolor='rgba(74, 222, 128, 0.05)'))
#         center_x, center_y = (x1 + x2) / 2, (y1 + y2) / 2
#         fig.add_trace(go.Scatter(x=[center_x], y=[center_y], mode='markers', marker=dict(color='#4ade80', size=8, opacity=0.4, line=dict(width=1, color='white')), hoverinfo='text', hovertext=f"<span style='color:#4ade80; font-weight:bold;'>[ DETECTED OBJECT ]</span><br>TYPE: {label.upper()}<br>CONFIDENCE: {conf:.1%}", showlegend=False))
#     fig.update_xaxes(showgrid=False, zeroline=False, range=[0, img_width], visible=False)
#     fig.update_yaxes(showgrid=False, zeroline=False, range=[img_height, 0], visible=False, scaleanchor="x", scaleratio=1)
#     fig.update_layout(margin=dict(l=0, r=0, t=0, b=0), plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)', hovermode='closest', dragmode=False, shapes=shapes)
#     return fig

# def typewriter_effect(text, placeholder):
#     displayed_text = ""
#     for char in text:
#         displayed_text += char
#         placeholder.markdown(f'<div class="dj-box">{displayed_text}█</div>', unsafe_allow_html=True)
#         time.sleep(0.015) 
#     placeholder.markdown(f'<div class="dj-box">{displayed_text}</div>', unsafe_allow_html=True)

# # --- MAIN UI ---
# st.title("PixelPulse 🎵")
# st.caption("Computer Vision • Interactive Detection • Audio Intelligence")

# col_left, col_right = st.columns([1, 1.4], gap="large")

# with col_left:
#     st.markdown("### 📤 Input Visual")
#     uploaded_file = st.file_uploader("Upload Image", type=["jpg", "png", "jpeg"])
    
#     if uploaded_file:
#         ph_img = st.empty()
#         ph_status = st.empty()
#         pil_image = Image.open(uploaded_file).convert("RGB")
#         ph_img.image(pil_image, caption="Original Media", use_column_width=True)
        
#         if st.button("Initiate Neural Scan", type="primary", use_container_width=True):
#             img_b64 = img_to_base64_str(uploaded_file)
#             ph_img.markdown(f'<div class="scan-container" style="max-width: none;"><img src="{img_b64}"><div class="scan-overlay"></div></div>', unsafe_allow_html=True)
            
#             steps = ["📡 Establishing Vibe Vector...", "👁️ Analyzing Visual Harmony...", "🎨 Calculating Audio Targets...", "🎵 Curating Spotify Sequence..."]
#             for s in steps:
#                 ph_status.markdown(f"**_{s}_**")
#                 time.sleep(0.5)
            
#             try:
#                 files = {"file": (uploaded_file.name, uploaded_file.getvalue(), uploaded_file.type)}
#                 response = requests.post(API_URL, files=files)
                
#                 if response.status_code == 200:
#                     data = st.session_state['data'] = response.json()
#                     ph_status.empty()
#                     detections = data.get('detections', [])
#                     if detections:
#                         fig = create_interactive_image(pil_image, detections)
#                         ph_img.plotly_chart(fig, use_container_width=True, config={'displayModeBar': False})
#                         st.caption("💡 HUD Active: Hover over detected regions for analysis data.")
#                     else:
#                         ph_img.image(pil_image, caption="Analysis Complete", use_column_width=True)
#                 else:
#                     st.error("Server Error.")
#                     ph_img.image(pil_image)
#             except Exception as e:
#                 st.error(f"Error: {e}")
#                 ph_img.image(pil_image)

# with col_right:
#     if 'data' in st.session_state:
#         data = st.session_state['data']
#         tags = data.get('tags', ["Unknown Vibe"])
#         objects = data.get('detected_objects', [])
#         accuracy = data.get('accuracy', 0)
#         palette = data.get('palette', [])
#         recommendations = data.get('recommendations', [])
#         dj_summary = data.get('dj_summary', "Analysis complete.")
        
#         st.markdown("### 👁️ Intelligence Report")
#         dj_placeholder = st.empty()
#         if 'last_dj_msg' not in st.session_state or st.session_state['last_dj_msg'] != dj_summary:
#             typewriter_effect(dj_summary, dj_placeholder)
#             st.session_state['last_dj_msg'] = dj_summary
#         else:
#              dj_placeholder.markdown(f'<div class="dj-box">{dj_summary}</div>', unsafe_allow_html=True)

#         st.markdown(f'<span class="accuracy-box">🎯 Vibe Match: {accuracy}%</span> <span class="accuracy-box">📦 Entities: {len(objects)}</span>', unsafe_allow_html=True)
#         st.write(f"**Musical Vibe:** {tags[0]}")
        
#         if objects:
#             obj_html = "".join([f'<span class="object-pill">{obj}</span>' for obj in objects])
#             st.markdown(obj_html, unsafe_allow_html=True)
        
#         st.write("**Dominant Palette:**")
#         cols_html = "".join([f'<div class="color-circle" style="background-color: {c};"></div>' for c in palette])
#         st.markdown(f'<div>{cols_html}</div>', unsafe_allow_html=True)
        
#         st.markdown("---")
        
#         c1, c2 = st.columns([1, 1])
#         with c1:
#             st.markdown("#### 📊 Audio DNA Target")
#             radar_fig = create_radar(data.get('mood_vector', [0.5]*5))
#             st.plotly_chart(radar_fig, use_container_width=True, config={'displayModeBar': False})
#         with c2:
#             st.markdown("#### 🎧 Curated Tracks")
            
#             for song in recommendations[:5]:
#                 match_score = song.get('match_score', 85)
                
#                 # Dynamic Color: Green for high, Yellow for medium
#                 badge_color = "#4ade80" 
#                 if match_score < 80: badge_color = "#facc15"
#                 if match_score < 60: badge_color = "#f87171"
                
#                 track_id = song.get('id')
#                 if track_id:
#                     embed_url = f"https://open.spotify.com/embed/track/{track_id}?utm_source=generator&theme=0"
                    
#                     st.markdown(f"""
#                     <div class="player-wrapper">
#                         <div class="match-badge" style="border-color: {badge_color}; color: {badge_color};">
#                            {match_score}% Match
#                         </div>
#                         <iframe style="border-radius:12px;" 
#                         src="{embed_url}" 
#                         width="100%" height="80" frameBorder="0" 
#                         allowfullscreen="" 
#                         allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture" 
#                         loading="lazy"></iframe>
#                     </div>
#                     """, unsafe_allow_html=True)
#                 else:
#                     st.caption("⚠️ Track unavailable")

#     else:
#         st.info("System Idle. Upload visuals to begin.")




### latest code wwith all features woking chnaged badge pos correctly ----------
# import streamlit as st
# import requests
# import plotly.graph_objects as go
# import time
# import base64
# from PIL import Image
# import io

# # --- CONFIG ---
# st.set_page_config(page_title="PixelPulse | Visual AI", page_icon="🎵", layout="wide")
# API_URL = "http://127.0.0.1:8000/recommend"

# # --- CSS ---
# st.markdown("""
#     <style>
#     @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;500;700&display=swap');
    
#     .stApp {
#         background-color: #050505;
#         background-image: radial-gradient(circle at 50% 0%, #1e1e24 0%, #000000 100%);
#         font-family: 'Outfit', sans-serif;
#         color: white;
#     }
    
#     .dj-box { background: rgba(255, 255, 255, 0.05); border-left: 5px solid #a855f7; padding: 15px; border-radius: 8px; margin-bottom: 20px; font-style: italic; color: #e9d5ff; font-size: 1.05rem; line-height: 1.5; }
#     .scan-container { position: relative; width: 100%; border-radius: 12px; overflow: hidden; border: 1px solid #4ade8055; box-shadow: 0 0 25px rgba(74, 222, 128, 0.3); }
#     .scan-container img { width: 100%; display: block; }
#     .scan-overlay { position: absolute; top: 0; left: 0; width: 100%; height: 100%; background: linear-gradient(to bottom, transparent 0%, rgba(74, 222, 128, 0.1) 45%, rgba(100, 255, 150, 0.9) 50%, rgba(74, 222, 128, 0.1) 55%, transparent 100%); animation: scan 1.5s cubic-bezier(0.4, 0.0, 0.2, 1) infinite; z-index: 2; pointer-events: none; }
#     @keyframes scan { 0% { transform: translateY(-100%); } 100% { transform: translateY(100%); } }
#     .accuracy-box { background: rgba(74, 222, 128, 0.15); border: 1px solid #4ade80; color: #4ade80; padding: 6px 12px; border-radius: 8px; font-weight: bold; display: inline-block; margin-right: 10px; font-size: 0.9rem; }
#     .object-pill { background: rgba(255, 255, 255, 0.1); border: 1px solid #4ade8088; color: #dfdfdf; padding: 4px 10px; border-radius: 20px; font-size: 0.8rem; display: inline-block; margin: 3px; }
#     .color-circle { width: 40px; height: 40px; border-radius: 50%; display: inline-block; margin-right: 10px; border: 2px solid rgba(255,255,255,0.2); box-shadow: 0 0 5px rgba(0,0,0,0.5); }
    
#     /* --- NEW PREMIUM BADGE --- */
#     .player-wrapper {
#         position: relative;
#         margin-bottom: 12px;
#         transition: transform 0.2s;
#     }
#     .player-wrapper:hover {
#         transform: scale(1.02);
#     }
    
#     .match-badge {
#         position: absolute;
#         top: 8px;     
#         right: 40px;   
#         background: rgba(0, 0, 0, 0.6); /* Glass effect */
#         backdrop-filter: blur(4px);
#         padding: 2px 8px;
#         border-radius: 12px;
#         font-weight: 700;
#         font-size: 0.65rem;
#         z-index: 12;
#         pointer-events: none;
#         box-shadow: 0 4px 6px rgba(0,0,0,0.3);
#         letter-spacing: 0.5px;
#     }

#     .modebar { display: none !important; }
#     header, footer {visibility: hidden;}
#     </style>
# """, unsafe_allow_html=True)

# # --- HELPERS ---
# def img_to_base64_str(img_file):
#     encoded_string = base64.b64encode(img_file.getvalue()).decode()
#     return f"data:image/{img_file.type.split('/')[-1]};base64,{encoded_string}"

# def pil_to_base64(img_pil):
#     buffer = io.BytesIO()
#     img_pil.save(buffer, format="PNG")
#     encoded_string = base64.b64encode(buffer.getvalue()).decode()
#     return f"data:image/png;base64,{encoded_string}"

# def create_radar(mood_vec):
#     categories = ['Valence (Mood)', 'Energy', 'Danceability', 'Tempo', 'Acoustic']
#     values = mood_vec + [mood_vec[0]]
#     cats = categories + [categories[0]]
#     fig = go.Figure(go.Scatterpolar(r=values, theta=cats, fill='toself', line_color='#4ade80', fillcolor='rgba(74, 222, 128, 0.2)'))
#     fig.update_layout(polar=dict(radialaxis=dict(visible=True, range=[0, 1], showticklabels=False, linecolor='#333'), angularaxis=dict(tickfont=dict(color='white', size=11))), paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', height=380, margin=dict(l=60, r=60, t=30, b=30))
#     return fig

# def create_interactive_image(img_pil, detections):
#     img_width, img_height = img_pil.size
#     img_base64 = pil_to_base64(img_pil)
#     fig = go.Figure()
#     fig.add_layout_image(dict(source=img_base64, xref="x", yref="y", x=0, y=0, sizex=img_width, sizey=img_height, sizing="stretch", layer="below"))
#     shapes = []
#     for det in detections:
#         x1, y1, x2, y2 = det['bbox']
#         label = det['label']
#         conf = det['confidence']
#         shapes.append(dict(type="rect", x0=x1, y0=y1, x1=x2, y1=y2, line=dict(color='rgba(74, 222, 128, 0.5)', width=1), fillcolor='rgba(74, 222, 128, 0.05)'))
#         center_x, center_y = (x1 + x2) / 2, (y1 + y2) / 2
#         fig.add_trace(go.Scatter(x=[center_x], y=[center_y], mode='markers', marker=dict(color='#4ade80', size=8, opacity=0.4, line=dict(width=1, color='white')), hoverinfo='text', hovertext=f"<span style='color:#4ade80; font-weight:bold;'>[ DETECTED OBJECT ]</span><br>TYPE: {label.upper()}<br>CONFIDENCE: {conf:.1%}", showlegend=False))
#     fig.update_xaxes(showgrid=False, zeroline=False, range=[0, img_width], visible=False)
#     fig.update_yaxes(showgrid=False, zeroline=False, range=[img_height, 0], visible=False, scaleanchor="x", scaleratio=1)
#     fig.update_layout(margin=dict(l=0, r=0, t=0, b=0), plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)', hovermode='closest', dragmode=False, shapes=shapes)
#     return fig

# def typewriter_effect(text, placeholder):
#     displayed_text = ""
#     for char in text:
#         displayed_text += char
#         placeholder.markdown(f'<div class="dj-box">{displayed_text}█</div>', unsafe_allow_html=True)
#         time.sleep(0.015) 
#     placeholder.markdown(f'<div class="dj-box">{displayed_text}</div>', unsafe_allow_html=True)

# # --- MAIN UI ---
# st.title("PixelPulse 🎵")
# st.caption("Computer Vision • Interactive Detection • Audio Intelligence")

# col_left, col_right = st.columns([1, 1.4], gap="large")

# with col_left:
#     st.markdown("### 📤 Input Visual")
#     uploaded_file = st.file_uploader("Upload Image", type=["jpg", "png", "jpeg"])
    
#     if uploaded_file:
#         ph_img = st.empty()
#         ph_status = st.empty()
#         pil_image = Image.open(uploaded_file).convert("RGB")
#         ph_img.image(pil_image, caption="Original Media", use_column_width=True)
        
#         if st.button("Initiate Neural Scan", type="primary", use_container_width=True):
#             img_b64 = img_to_base64_str(uploaded_file)
#             ph_img.markdown(f'<div class="scan-container" style="max-width: none;"><img src="{img_b64}"><div class="scan-overlay"></div></div>', unsafe_allow_html=True)
            
#             steps = ["📡 Establishing Vibe Vector...", "👁️ Analyzing Visual Harmony...", "🎨 Calculating Audio Targets...", "🎵 Curating Spotify Sequence..."]
#             for s in steps:
#                 ph_status.markdown(f"**_{s}_**")
#                 time.sleep(0.5)
            
#             try:
#                 files = {"file": (uploaded_file.name, uploaded_file.getvalue(), uploaded_file.type)}
#                 response = requests.post(API_URL, files=files)
                
#                 if response.status_code == 200:
#                     data = st.session_state['data'] = response.json()
#                     ph_status.empty()
#                     detections = data.get('detections', [])
#                     if detections:
#                         fig = create_interactive_image(pil_image, detections)
#                         ph_img.plotly_chart(fig, use_container_width=True, config={'displayModeBar': False})
#                         st.caption("💡 HUD Active: Hover over detected regions for analysis data.")
#                     else:
#                         ph_img.image(pil_image, caption="Analysis Complete", use_column_width=True)
#                 else:
#                     st.error("Server Error.")
#                     ph_img.image(pil_image)
#             except Exception as e:
#                 st.error(f"Error: {e}")
#                 ph_img.image(pil_image)

# with col_right:
#     if 'data' in st.session_state:
#         data = st.session_state['data']
#         tags = data.get('tags', ["Unknown Vibe"])
#         objects = data.get('detected_objects', [])
#         accuracy = data.get('accuracy', 0)
#         palette = data.get('palette', [])
#         recommendations = data.get('recommendations', [])
#         dj_summary = data.get('dj_summary', "Analysis complete.")
        
#         st.markdown("### 👁️ Intelligence Report")
#         dj_placeholder = st.empty()
#         if 'last_dj_msg' not in st.session_state or st.session_state['last_dj_msg'] != dj_summary:
#             typewriter_effect(dj_summary, dj_placeholder)
#             st.session_state['last_dj_msg'] = dj_summary
#         else:
#              dj_placeholder.markdown(f'<div class="dj-box">{dj_summary}</div>', unsafe_allow_html=True)

#         st.markdown(f'<span class="accuracy-box">🎯 Vibe Match: {accuracy}%</span> <span class="accuracy-box">📦 Entities: {len(objects)}</span>', unsafe_allow_html=True)
#         st.write(f"**Musical Vibe:** {tags[0]}")
        
#         if objects:
#             obj_html = "".join([f'<span class="object-pill">{obj}</span>' for obj in objects])
#             st.markdown(obj_html, unsafe_allow_html=True)
        
#         st.write("**Dominant Palette:**")
#         cols_html = "".join([f'<div class="color-circle" style="background-color: {c};"></div>' for c in palette])
#         st.markdown(f'<div>{cols_html}</div>', unsafe_allow_html=True)
        
#         st.markdown("---")
        
#         c1, c2 = st.columns([1, 1])
#         with c1:
#             st.markdown("#### 📊 Audio DNA Target")
#             radar_fig = create_radar(data.get('mood_vector', [0.5]*5))
#             st.plotly_chart(radar_fig, use_container_width=True, config={'displayModeBar': False})
#         with c2:
#             st.markdown("#### 🎧 Curated Tracks")
            
#             for song in recommendations[:5]:
#                 match_score = song.get('match_score', 85)
                
#                 # Dynamic Color
#                 badge_color = "#4ade80" 
#                 if match_score < 80: badge_color = "#facc15"
#                 if match_score < 60: badge_color = "#f87171"
                
#                 track_id = song.get('id')
#                 if track_id:
#                     embed_url = f"https://open.spotify.com/embed/track/{track_id}?utm_source=generator&theme=0"
                    
#                     st.markdown(f"""
#                     <div class="player-wrapper">
#                         <div class="match-badge" style="border-color: {badge_color}; color: {badge_color};">
#                            ⚡ {match_score}%
#                         </div>
#                         <iframe style="border-radius:12px;" 
#                         src="{embed_url}" 
#                         width="100%" height="80" frameBorder="0" 
#                         allowfullscreen="" 
#                         allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture" 
#                         loading="lazy"></iframe>
#                     </div>
#                     """, unsafe_allow_html=True)
#                 else:
#                     st.caption("⚠️ Track unavailable")

#     else:
#         st.info("System Idle. Upload visuals to begin.")


import streamlit as st
import requests
import plotly.graph_objects as go
import time
import base64
from PIL import Image
import io

# --- CONFIG: FORCE SIDEBAR OPEN ---
st.set_page_config(
    page_title="PixelPulse | Visual AI", 
    page_icon="🎵", 
    layout="wide", 
    initial_sidebar_state="expanded" # <--- Forces sidebar to open on load
)

BACKEND_URL = "https://saishashankv10-pixelpulse.hf.space"
API_URL = f"{BACKEND_URL}/recommend"


# --- CSS ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;500;700&display=swap');
    
    .stApp {
        background-color: #050505;
        background-image: radial-gradient(circle at 50% 0%, #1e1e24 0%, #000000 100%);
        font-family: 'Outfit', sans-serif;
        color: white;
    }
    
    /* --- FIX: FORCE SIDEBAR ICON VISIBILITY --- */
    [data-testid="stSidebarCollapsedControl"] {
        display: block !important;
        visibility: visible !important;
        color: #4ade80 !important; /* Bright Green */
        background-color: rgba(255, 255, 255, 0.1);
        border-radius: 50%;
        padding: 5px;
        z-index: 9999;
    }
    
    section[data-testid="stSidebar"] {
        background-color: #0e0e10;
        border-right: 1px solid #333;
    }

    /* DJ Box & UI Elements */
    .dj-box { background: rgba(255, 255, 255, 0.05); border-left: 5px solid #a855f7; padding: 15px; border-radius: 8px; margin-bottom: 20px; font-style: italic; color: #e9d5ff; font-size: 1.05rem; line-height: 1.5; }
    .scan-container { position: relative; width: 100%; border-radius: 12px; overflow: hidden; border: 1px solid #4ade8055; box-shadow: 0 0 25px rgba(74, 222, 128, 0.3); }
    .scan-container img { width: 100%; display: block; }
    .scan-overlay { position: absolute; top: 0; left: 0; width: 100%; height: 100%; background: linear-gradient(to bottom, transparent 0%, rgba(74, 222, 128, 0.1) 45%, rgba(100, 255, 150, 0.9) 50%, rgba(74, 222, 128, 0.1) 55%, transparent 100%); animation: scan 1.5s cubic-bezier(0.4, 0.0, 0.2, 1) infinite; z-index: 2; pointer-events: none; }
    @keyframes scan { 0% { transform: translateY(-100%); } 100% { transform: translateY(100%); } }
    .accuracy-box { background: rgba(74, 222, 128, 0.15); border: 1px solid #4ade80; color: #4ade80; padding: 6px 12px; border-radius: 8px; font-weight: bold; display: inline-block; margin-right: 10px; font-size: 0.9rem; }
    .object-pill { background: rgba(255, 255, 255, 0.1); border: 1px solid #4ade8088; color: #dfdfdf; padding: 4px 10px; border-radius: 20px; font-size: 0.8rem; display: inline-block; margin: 3px; }
    .color-circle { width: 40px; height: 40px; border-radius: 50%; display: inline-block; margin-right: 10px; border: 2px solid rgba(255,255,255,0.2); box-shadow: 0 0 5px rgba(0,0,0,0.5); }
    
    .player-wrapper { position: relative; margin-bottom: 12px; transition: transform 0.2s; }
    .player-wrapper:hover { transform: scale(1.02); }
    
    .match-badge {
        position: absolute;
        top: 8px;     
        right: 50px;   
        background: rgba(0, 0, 0, 0.6); 
        backdrop-filter: blur(4px);
        padding: 2px 8px;
        border-radius: 12px;
        font-weight: 700;
        font-size: 0.75rem;
        z-index: 10;
        pointer-events: none;
        box-shadow: 0 4px 6px rgba(0,0,0,0.3);
        letter-spacing: 0.5px;
    }

    .modebar { display: none !important; }
    header, footer {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

# --- HELPERS ---
def img_to_base64_str(img_file):
    encoded_string = base64.b64encode(img_file.getvalue()).decode()
    return f"data:image/{img_file.type.split('/')[-1]};base64,{encoded_string}"

def pil_to_base64(img_pil):
    buffer = io.BytesIO()
    img_pil.save(buffer, format="PNG")
    encoded_string = base64.b64encode(buffer.getvalue()).decode()
    return f"data:image/png;base64,{encoded_string}"

def create_radar(mood_vec):
    categories = ['Valence (Mood)', 'Energy', 'Danceability', 'Tempo', 'Acoustic']
    values = mood_vec + [mood_vec[0]]
    cats = categories + [categories[0]]
    fig = go.Figure(go.Scatterpolar(r=values, theta=cats, fill='toself', line_color='#4ade80', fillcolor='rgba(74, 222, 128, 0.2)'))
    fig.update_layout(polar=dict(radialaxis=dict(visible=True, range=[0, 1], showticklabels=False, linecolor='#333'), angularaxis=dict(tickfont=dict(color='white', size=11))), paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', height=380, margin=dict(l=60, r=60, t=30, b=30))
    return fig

def create_interactive_image(img_pil, detections):
    img_width, img_height = img_pil.size
    img_base64 = pil_to_base64(img_pil)
    fig = go.Figure()
    fig.add_layout_image(dict(source=img_base64, xref="x", yref="y", x=0, y=0, sizex=img_width, sizey=img_height, sizing="stretch", layer="below"))
    shapes = []
    for det in detections:
        x1, y1, x2, y2 = det['bbox']
        label = det['label']
        conf = det['confidence']
        shapes.append(dict(type="rect", x0=x1, y0=y1, x1=x2, y1=y2, line=dict(color='rgba(74, 222, 128, 0.5)', width=1), fillcolor='rgba(74, 222, 128, 0.05)'))
        center_x, center_y = (x1 + x2) / 2, (y1 + y2) / 2
        fig.add_trace(go.Scatter(x=[center_x], y=[center_y], mode='markers', marker=dict(color='#4ade80', size=8, opacity=0.4, line=dict(width=1, color='white')), hoverinfo='text', hovertext=f"<span style='color:#4ade80; font-weight:bold;'>[ DETECTED OBJECT ]</span><br>TYPE: {label.upper()}<br>CONFIDENCE: {conf:.1%}", showlegend=False))
    fig.update_xaxes(showgrid=False, zeroline=False, range=[0, img_width], visible=False)
    fig.update_yaxes(showgrid=False, zeroline=False, range=[img_height, 0], visible=False, scaleanchor="x", scaleratio=1)
    fig.update_layout(margin=dict(l=0, r=0, t=0, b=0), plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)', hovermode='closest', dragmode=False, shapes=shapes)
    return fig

def typewriter_effect(text, placeholder):
    displayed_text = ""
    for char in text:
        displayed_text += char
        placeholder.markdown(f'<div class="dj-box">{displayed_text}█</div>', unsafe_allow_html=True)
        time.sleep(0.015) 
    placeholder.markdown(f'<div class="dj-box">{displayed_text}</div>', unsafe_allow_html=True)

# --- AUTH CHECK ---
if 'is_logged_in' not in st.session_state:
    try:
        res = requests.get(f"{BACKEND_URL}/check_auth")
        if res.status_code == 200:
            st.session_state['is_logged_in'] = res.json().get('is_logged_in', False)
        else:
            st.session_state['is_logged_in'] = False
    except:
        st.session_state['is_logged_in'] = False

# --- SIDEBAR LOGIN ---
with st.sidebar:
    st.header("🔑 Account")
    if st.session_state['is_logged_in']:
        st.success("Connected to Spotify")
    else:
        st.info("Log in to save playlists!")
        st.link_button("Connect Spotify Account", f"{BACKEND_URL}/login")

# --- MAIN UI ---
st.title("PixelPulse 🎵")
st.caption("Computer Vision • Interactive Detection • Audio Intelligence")

# --- BACKUP LOGIN BUTTON (Main Page) ---
# If user is NOT logged in, show a login button right here on the main page too
if not st.session_state['is_logged_in']:
    col_login_a, col_login_b = st.columns([3, 1])
    with col_login_b:
        st.link_button("🔓 Login to Spotify", f"{BACKEND_URL}/login", type="secondary")

col_left, col_right = st.columns([1, 1.4], gap="large")

with col_left:
    st.markdown("### 📤 Input Visual")
    uploaded_file = st.file_uploader("Upload Image", type=["jpg", "png", "jpeg"])
    
    if uploaded_file:
        ph_img = st.empty()
        ph_status = st.empty()
        pil_image = Image.open(uploaded_file).convert("RGB")
        ph_img.image(pil_image, caption="Original Media", use_column_width=True)
        
        if st.button("Initiate Neural Scan", type="primary", use_container_width=True):
            img_b64 = img_to_base64_str(uploaded_file)
            ph_img.markdown(f'<div class="scan-container" style="max-width: none;"><img src="{img_b64}"><div class="scan-overlay"></div></div>', unsafe_allow_html=True)
            
            steps = ["📡 Establishing Vibe Vector...", "👁️ Analyzing Visual Harmony...", "🎨 Calculating Audio Targets...", "🎵 Curating Spotify Sequence..."]
            for s in steps:
                ph_status.markdown(f"**_{s}_**")
                time.sleep(0.5)
            
            try:
                files = {"file": (uploaded_file.name, uploaded_file.getvalue(), uploaded_file.type)}
                response = requests.post(API_URL, files=files)
                
                if response.status_code == 200:
                    data = st.session_state['data'] = response.json()
                    ph_status.empty()
                    detections = data.get('detections', [])
                    if detections:
                        fig = create_interactive_image(pil_image, detections)
                        ph_img.plotly_chart(fig, use_container_width=True, config={'displayModeBar': False})
                        st.caption("💡 HUD Active: Hover over detected regions for analysis data.")
                    else:
                        ph_img.image(pil_image, caption="Analysis Complete", use_column_width=True)
                else:
                    st.error("Server Error.")
                    ph_img.image(pil_image)
            except Exception as e:
                st.error(f"Error: {e}")
                ph_img.image(pil_image)

with col_right:
    if 'data' in st.session_state:
        data = st.session_state['data']
        tags = data.get('tags', ["Unknown Vibe"])
        objects = data.get('detected_objects', [])
        accuracy = data.get('accuracy', 0)
        palette = data.get('palette', [])
        recommendations = data.get('recommendations', [])
        dj_summary = data.get('dj_summary', "Analysis complete.")
        
        st.markdown("### 👁️ Intelligence Report")
        dj_placeholder = st.empty()
        if 'last_dj_msg' not in st.session_state or st.session_state['last_dj_msg'] != dj_summary:
            typewriter_effect(dj_summary, dj_placeholder)
            st.session_state['last_dj_msg'] = dj_summary
        else:
             dj_placeholder.markdown(f'<div class="dj-box">{dj_summary}</div>', unsafe_allow_html=True)

        st.markdown(f'<span class="accuracy-box">🎯 Vibe Match: {accuracy}%</span> <span class="accuracy-box">📦 Entities: {len(objects)}</span>', unsafe_allow_html=True)
        st.write(f"**Musical Vibe:** {tags[0]}")
        
        if objects:
            obj_html = "".join([f'<span class="object-pill">{obj}</span>' for obj in objects])
            st.markdown(obj_html, unsafe_allow_html=True)
        
        st.write("**Dominant Palette:**")
        cols_html = "".join([f'<div class="color-circle" style="background-color: {c};"></div>' for c in palette])
        st.markdown(f'<div>{cols_html}</div>', unsafe_allow_html=True)
        
        st.markdown("---")
        
        c1, c2 = st.columns([1, 1])
        with c1:
            st.markdown("#### 📊 Audio DNA Target")
            radar_fig = create_radar(data.get('mood_vector', [0.5]*5))
            st.plotly_chart(radar_fig, use_container_width=True, config={'displayModeBar': False})
        with c2:
            st.markdown("#### 🎧 Curated Tracks")
            
            for song in recommendations[:5]:
                match_score = song.get('match_score', 85)
                
                # Dynamic Color
                badge_color = "#4ade80" 
                if match_score < 80: badge_color = "#facc15"
                if match_score < 60: badge_color = "#f87171"
                
                track_id = song.get('id')
                if track_id:
                    embed_url = f"https://open.spotify.com/embed/track/{track_id}?utm_source=generator&theme=0"
                    
                    st.markdown(f"""
                    <div class="player-wrapper">
                        <div class="match-badge" style="border-color: {badge_color}; color: {badge_color};">
                           ⚡ {match_score}%
                        </div>
                        <iframe style="border-radius:12px;" 
                        src="{embed_url}" 
                        width="100%" height="80" frameBorder="0" 
                        allowfullscreen="" 
                        allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture" 
                        loading="lazy"></iframe>
                    </div>
                    """, unsafe_allow_html=True)
                else:
                    st.caption("⚠️ Track unavailable")
            
            # --- SAVE PLAYLIST BUTTON ---
            if st.session_state['is_logged_in']:
                if st.button("💾 Save Playlist to Library", use_container_width=True):
                    track_ids = [s['id'] for s in recommendations if s.get('id')]
                    playlist_name = f"PixelPulse: {tags[0]}"
                    
                    try:
                        res = requests.post(f"{BACKEND_URL}/save_playlist", json={"track_ids": track_ids, "name": playlist_name})
                        if res.status_code == 200 and res.json().get("status") == "success":
                            st.success(f"Playlist Created! [Open in Spotify]({res.json().get('url')})")
                        else:
                            st.error("Failed to save playlist.")
                    except Exception as e:
                        st.error(f"Error: {e}")
            else:
                st.caption("Login to save this playlist (Check Sidebar or Top Right)")

    else:
        st.info("System Idle. Upload visuals to begin.")